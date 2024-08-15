from markdown import markdown
from fasthtml.common import (
    Div,
    Button,
    NotStr,
    H1,
    Span,
    Input,
    Form,
    P,
    Dialog,
    Label,
    Img,
)


def TextCard(
    pair_id,
    text_id,
    chosen,
    text,
    cls="flex-1 prose cursor-pointer border-2 h-full max-h-full overflow-auto w-2/5 max-w-3xl bg-base-300 p-4 rounded-box text-xl",
    **kwargs,
):
    card_cls = cls
    card_cls_chosen = f"{card_cls} border-green-500"
    card_cls_not_chosen = f"{card_cls} border-transparent"
    md_exts = [
        "codehilite",
        "smarty",
        "extra",
        "sane_lists",
    ]

    return Div(
        NotStr(markdown(text, extensions=md_exts)),
        cls=(card_cls_not_chosen if not chosen else card_cls_chosen),
        hx_on="click",
        hx_post=f"/update-choice/{pair_id}/{text_id}",
        hx_swap="outerHTML",
        hx_target="#text-comparison",
        **kwargs,
    )


def NavigationButtons(text_id: int, text_pairs_count: int):
    is_last_text = text_id >= text_pairs_count
    is_first_text = text_id == 1

    return Div(
        Button(
            "Previous",
            cls="btn btn-primary btn-sm md:btn-md",
            disabled=is_first_text,
            hx_target="body",
            hx_get=f"/{text_id - 1}",
        ),
        Button(
            "Next",
            cls="btn btn-primary btn-sm md:btn-md",
            disabled=is_last_text,
            hx_target="body",
            hx_get=f"/{text_id + 1}",
        ),
        cls="flex flex-row gap-3 fixed bottom-6 md:bottom-4 width-full justify-center",
    )


def TextComparison(
    pair,
    chosen_text,
    checked_text=None,
    is_mobile: bool = False,
    cls="flex flex-row flex-grow mt-6 gap-3 max-h-[85%] h-4/5 w-full justify-center",
):
    if is_mobile:
        tab_cls = "tab-content border-base-300 bg-base-300 p-4 rounded-box h-fit max-h-full overflow-auto"
        card_cls = "prose max-w-full"
        checked_text = checked_text if checked_text else "text1"
        return Div(
            Input(
                type="radio",
                name="tabs",
                role="tab",
                cls=(
                    "tab !w-max text-green-300 font-semibold"
                    if chosen_text == "text1"
                    else "tab !w-max"
                ),
                aria_label="Text 1",
                checked=(checked_text == "text1"),
            ),
            Div(
                TextCard(
                    pair.id,
                    "text1",
                    chosen_text == "text1",
                    pair.text1,
                    cls=card_cls,
                ),
                role="tabpanel",
                cls=tab_cls,
            ),
            Input(
                type="radio",
                name="tabs",
                role="tab",
                cls=(
                    "tab !w-max text-green-300 font-semibold"
                    if chosen_text == "text2"
                    else "tab !w-max"
                ),
                aria_label="Text 2",
                checked=(checked_text == "text2"),
            ),
            Div(
                TextCard(
                    pair.id,
                    "text2",
                    chosen_text == "text2",
                    pair.text2,
                    cls=card_cls,
                ),
                role="tabpanel",
                cls=tab_cls,
            ),
            cls="tabs tabs-lifted w-full content-start max-h-[80%] items-start",
            role="tablist",
            id="text-comparison",
        )
    else:
        return Div(
            TextCard(pair.id, "text1", chosen_text == "text1", pair.text1),
            TextCard(pair.id, "text2", chosen_text == "text2", pair.text2),
            cls=cls,
            id="text-comparison",
        )


def ResetModal():
    return (
        Button(
            Img(
                src="./icons/trash.svg",
                cls="w-6 h-6 fill-white",
            ),
            cls="btn btn-sm md:btn-md btn-error",
            onclick="my_modal_2.showModal()",
        ),
        Dialog(
            Div(
                P(
                    "Are you sure you want to reset your answers?",
                    cls="text-xl font-semibold",
                ),
                Div(
                    Button(
                        "Yes",
                        cls="btn btn-error",
                        onclick="my_modal_2.close()",
                        hx_post="/reset",
                    ),
                    Button(
                        "No",
                        cls="btn",
                        type="button",
                        onclick="my_modal_2.close()",
                    ),
                    cls="w-full flex flex-row gap-4 justify-center",
                ),
                cls="modal-box flex flex-col gap-4",
            ),
            id="my_modal_2",
            cls="modal",
        ),
    )


def InfoModal():
    return (
        Button(
            Img(
                src="./icons/info.svg",
                cls="w-6 h-6 fill-white",
            ),
            cls="btn btn-sm md:btn-md",
            onclick="my_modal_3.showModal()",
        ),
        Dialog(
            Div(
                P(
                    "This is a simple text comparison tool. You will be presented with two texts, and you will have to choose which one you prefer.",
                    cls="text-xl font-semibold",
                ),
                P(
                    "You can navigate through the texts using the 'Previous' and 'Next' buttons. You can also reset your answers using the 'Reset' button.",
                    cls="text-xl font-semibold",
                ),
                P(
                    "To track your answers, please provide your email. This will also be used to contact you in case you win a prize for participating.",
                    cls="text-xl font-semibold",
                ),
                Div(
                    Form(
                        Button(
                            "Close",
                            cls="btn",
                            type="button",
                            onclick="my_modal_3.close()",
                        ),
                        method="dialog",
                    ),
                    cls="modal-action",
                ),
                cls="modal-box flex flex-col gap-4 md:w-1/4 md:max-w-full",
            ),
            id="my_modal_3",
            cls="modal",
        ),
    )


def EmailModalDialogContent(email, error=None):
    return (
        Div(
            P(
                "To track your answers, please provide your email. This will also be used to contact you in case you win a prize for participating.",
                cls="text-xl font-semibold",
            ),
            Form(
                Label(
                    Img(
                        src="./icons/email.svg",
                        cls="w-8 h-8 fill-white",
                    ),
                    Input(
                        type="email",
                        name="email",
                        placeholder="Email",
                        value=email,
                        cls="grow",
                    ),
                    cls="input input-bordered flex items-center gap-2 !mb-0"
                    + (" input-error" if error else ""),
                ),
                P(
                    error,
                    hidden=(error is None),
                    cls="text-red-500",
                ),
                Div(
                    Div(
                        Button(
                            "Save",
                            cls="btn btn-primary",
                        ),
                        Button(
                            "Close",
                            cls="btn",
                            type="button",
                            onclick="my_modal_1.close()",
                        ),
                        cls="w-full flex flex-row gap-4 justify-center",
                    ),
                ),
                cls="modal-action w-full flex flex-col gap-4",
                method="dialog",
                hx_post="/update-email",
                hx_swap="outerHTML",
                hx_target="#modal-dialog-content",
            ),
            cls="modal-box flex flex-col gap-4",
            id="modal-dialog-content",
        ),
    )


def EmailModal(email, error=None):
    return (
        Button(
            Img(
                src="./icons/email.svg",
                cls="w-6 h-6 fill-white",
            ),
            cls="btn btn-sm md:btn-md",
            onclick="my_modal_1.showModal()",
        ),
        Dialog(
            EmailModalDialogContent(email, error),
            id="my_modal_1",
            cls="modal",
        ),
    )


def Toast(message, show=False, cls="toast z-50"):
    return (
        Div(
            Div(
                Span(message),
                Div(
                    Button(
                        "Close",
                        cls="btn btn-sm",
                        onclick="document.getElementById('toast').classList.toggle('hidden')",
                    ),
                ),
                cls="alert alert-success",
                role="alert",
                hidden=(not show),
            ),
            cls=cls,
            id="toast",
        ),
    )


def Header(email, session_id):
    return Div(
        H1(
            "Which text is more likely to have been written by a human?",
            cls="text-xl md:text-2xl font-semibold text-white",
        ),
        Div(
            Div(
                session_id,
                cls="badge badge-neutral md:badge-lg",
                hidden=(session_id is None),
            ),
            InfoModal(),
            EmailModal(email),
            ResetModal(),
            cls="flex flex-row gap-4 justify-between md:justify-end mt-4 md:mt-0 w-full md:w-auto items-center",
        ),
        cls="w-full flex flex-col md:flex-row justify-between items-center mb-3 md:mb-0",
    )
