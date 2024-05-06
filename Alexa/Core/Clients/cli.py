from pyrogram import Client

from config import (
    API_HASH,
    API_ID,
    BOT_TOKEN,
    LOG_SESSION,
    STRING1,
    STRING2,
    STRING3,
    STRING4,
    STRING5,
)

app = Client(
    "AlexaMusicBot",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)


if not STRING1:
    ASS_CLI_1 = None
else:
    ASS_CLI_1 = Client(
        'ASS_CLI_1',
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING1,
        plugins=dict(root="Alexa.Plugins.Multi-Assistant"),
    )


if not STRING2:
    ASS_CLI_2 = None
else:
    ASS_CLI_2 = Client(
        'ASS_CLI_2',
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING2,
        plugins=dict(root="Alexa.Plugins.Multi-Assistant"),
    )


if not STRING3:
    ASS_CLI_3 = None
else:
    ASS_CLI_3 = Client(
        'ASS_CLI_3',
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING3,
        plugins=dict(root="Alexa.Plugins.Multi-Assistant"),
    )


if not STRING4:
    ASS_CLI_4 = None
else:
    ASS_CLI_4 = Client(
        'ASS_CLI_4',
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING4,
        plugins=dict(root="Alexa.Plugins.Multi-Assistant"),
    )


if not STRING5:
    ASS_CLI_5 = None
else:
    ASS_CLI_5 = Client(
        'ASS_CLI_5',
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING5,
        plugins=dict(root="Alexa.Plugins.Multi-Assistant"),
    )


if not LOG_SESSION:
    LOG_CLIENT = None
else:
    LOG_CLIENT = Client('LOG_SESSION', session_string=LOG_SESSION, api_id=API_ID, api_hash=API_HASH)
