from fasthtml.common import database
from consts import texts, texts2


def init_database():
    db = database("data/database.db")
    tables = db.t
    text_pairs, user_choices, email_tokens = (
        tables.text_pair,
        tables.user_choice,
        tables.email_token,
    )

    if text_pairs not in tables:
        text_pairs.create(
            dict(id=int, model=str, text1=str, text2=str, natural=str),
            pk="id",
        )
        user_choices.create(
            dict(id=int, pair_id=int, choice=str, session_id=str, email=str),
            pk="id",
        )
        email_tokens.create(
            dict(id=int, token=str, email=str),
            pk="id",
        )
        TextPair, UserChoice, EmailTokens = (
            text_pairs.dataclass(),
            user_choices.dataclass(),
            email_tokens.dataclass(),
        )

        text_pairs.insert(
            TextPair(
                model="apollo11",
                text1=texts[0],
                text2=texts[1],
                natural="text1",
            )
        )
        text_pairs.insert(
            TextPair(
                model="apollo13",
                text1=texts2[0],
                text2=texts2[1],
                natural="text2",
            )
        )
    else:
        TextPair, UserChoice, EmailTokens = (
            text_pairs.dataclass(),
            user_choices.dataclass(),
            email_tokens.dataclass(),
        )

    return TextPair, UserChoice, EmailTokens, text_pairs, user_choices, email_tokens
