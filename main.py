import random, uuid, json
from fasthtml.common import *
from db import init_database
from consts import debug, tailwind, daisyui, hide_scrollbar
from components import (
    TextComparison,
    NavigationButtons,
    Toast,
    Header,
    EmailModalDialogContent,
)
from utils import detect_mobile, parse_args, invalid_api_token

TextPair, UserChoice, EmailTokens, text_pairs, user_choices, email_tokens = (
    init_database()
)
app, rt = fast_app(
    pico=False,
    live=debug,
    hdrs=(tailwind, daisyui, hide_scrollbar),
)
args = parse_args()


@rt("/api/user-choices")
def get(request):
    if invalid_api_token(request, args.api_token):
        return Response(status_code=401, content="Unauthorized")

    # get all user choices
    choices = user_choices()
    json_choices = json.dumps(
        [
            {
                "pair_id": choice.pair_id,
                "choice": choice.choice,
                "session_id": choice.session_id,
                "email": choice.email,
            }
            for choice in choices
        ]
    )
    # return the choices as a list of dictionaries
    return Response(json_choices, media_type="application/json", status_code=200)


@rt("/api/text-pairs")
def get(request):
    if invalid_api_token(request, args.api_token):
        return Response(status_code=401, content="Unauthorized")

    # get all text pairs
    pairs = text_pairs()
    json_pairs = json.dumps(
        [
            {
                "id": pair.id,
                "model": pair.model,
                "text1": pair.text1,
                "text2": pair.text2,
                "natural": pair.natural,
            }
            for pair in pairs
        ]
    )
    # return the pairs as a list of dictionaries
    return Response(json_pairs, media_type="application/json", status_code=200)


@rt("/api/email-tokens")
def get(request):
    if invalid_api_token(request, args.api_token):
        return Response(status_code=401, content="Unauthorized")

    # get all email tokens
    tokens = email_tokens()
    json_tokens = json.dumps(
        [
            {
                "id": token.id,
                "token": token.token,
                "email": token.email,
            }
            for token in tokens
        ]
    )
    # return the tokens as a list of dictionaries
    return Response(json_tokens, media_type="application/json", status_code=200)


@rt("/api/reset")
def post(request):
    if invalid_api_token(request, args.api_token):
        return Response(status_code=401, content="Unauthorized")

    # delete all user choices
    user_choices.delete_where()
    # delete all email tokens
    email_tokens.delete_where()
    # delete all text pairs
    # text_pairs.delete_where()
    return Response(status_code=200, content="Reset successful.")


@rt("/reset")
def post(session):
    # delete all user choices associated with the session id
    # if email is present, delete all user choices associated with the email and delete the email token
    if "email" in session:
        user_choices.delete_where(f"email = '{session['email']}'")
        email_tokens.delete_where(f"email = '{session['email']}'")
    else:
        user_choices.delete_where(f"session_id = '{session['session_id']}'")

    # reset the session id
    del session["session_id"]
    # reset the email
    if "email_local" in session:
        del session["email_local"]
    return Response(status_code=303, headers={"HX-Refresh": "true"})


@rt("/update-choice/{id}/{text}")
def post(id: int, text: str, session, request):
    is_mobile = detect_mobile(request)

    if "session_id" not in session:
        return Response(
            status_code=400, content="Session ID not found. Please refresh the page."
        )

    email = session["email_local"] if "email_local" in session else None

    choice = user_choices(
        where=f"pair_id = {id} AND session_id = '{session['session_id']}'"
    )
    choice = choice[0] if len(choice) > 0 else None

    if choice is None:
        choice = user_choices.insert(
            UserChoice(
                pair_id=id,
                choice="",
                session_id=session["session_id"],
                email=email,
            )
        )

    if choice.choice == text:
        chosen_text = ""
        user_choices.delete(choice.id)
    else:
        chosen_text = text
        choice.choice = text
        user_choices.update(choice)

    return TextComparison(text_pairs.get(id), chosen_text, text, is_mobile=is_mobile)


def not_found_page():
    return Body(
        H1("Not Found", cls="justify-start text-3xl font-bold"),
        Button(
            "Go Home",
            cls="btn btn-primary",
            hx_target="body",
            hx_get="/",
        ),
        cls="w-full h-screen flex flex-col items-center p-6 gap-4",
    )


@rt("/update-email")
def post(email: str, session, token: str = ""):
    if email == "":
        return EmailModalDialogContent(email, "Email cannot be empty.")

    current_emails = email_tokens(where=f"email = '{email}'")

    if len(current_emails) == 0:
        email_tokens.insert(
            EmailTokens(token=str(random.randint(1000, 9999)), email=email)
        )
    elif token == "":
        return EmailModalDialogContent(email, "Email already in use.")
    elif token != current_emails[0].token:
        return Response(status_code=400, content="Invalid token provided.")

    session["email_local"] = email
    if "session_id" in session:
        choices = user_choices(where=f"session_id = '{session['session_id']}'")
        for choice in choices:
            choice.email = email
            user_choices.update(choice)

    session["show_toast"] = "true"

    return Response(status_code=303, headers={"HX-Refresh": "true"})


@rt("/{id}")
def get(id: int, session, request):
    pair = None
    is_mobile = detect_mobile(request)

    try:
        pair = text_pairs.get(id)
    except Exception:
        return not_found_page()

    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
    email = session["email_local"] if "email_local" in session else None

    if email:
        user_choice = user_choices(where=f"pair_id = {id} AND email = '{email}'")
    else:
        user_choice = user_choices(
            where=f"pair_id = {id} AND session_id = '{session['session_id']}'"
        )

    user_choice = user_choice[0] if len(user_choice) > 0 else None

    chosen_text = user_choice.choice if user_choice is not None else ""
    show_toast = False
    if "show_toast" in session:
        show_toast = session["show_toast"].lower() == "true"
        del session["show_toast"]

    return (
        Body(
            Header(email, (session["session_id"] if debug and not is_mobile else None)),
            TextComparison(
                pair,
                chosen_text,
                chosen_text,
                is_mobile=is_mobile,
            ),
            Toast(message="Email updated successfully.", show=show_toast),
            NavigationButtons(id, text_pairs.count),
            cls="w-full h-screen flex flex-col items-center p-6",
        ),
    )


@rt("/")
def get():
    text_id = random.randint(1, text_pairs.count - 1)

    # redirect to the text comparison page
    return RedirectResponse(f"/{text_id}")


if __name__ == "__main__":
    serve(port=args.port)
