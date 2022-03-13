# Rawana - UserBot
# Copyright (C) 2021-2022 TeamRawana
#
# This file is a part of < https://github.com/Rawana-Developers/Rawana-User-Bot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Rawana-Developers/Rawana-User-Bot/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, ultroid_cmd

REPOMSG = """
• **RAWANA USERBOT** •\n
• Repo - [Click Here](https://github.com/Rawana-Developers/Rawana-User-Bot/)
• Addons - [Click Here](https://t.me/Rawana_Bot_Developers)
• Support - @Rawana_Developers
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/Rawana-Developers/Rawana-User-Bot/"),
        Button.url("Addons", "https://github.com/TeamUltroid/UltroidAddons"),
    ],
    [Button.url("Support Group", "t.me/ultroidsupport")],
]

ULTSTRING = """🎇 **Thanks for Deploying Ultroid Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@Rawana_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info("Error while repo command : " + str(er))
    await e.eor(REPOMSG)


@Rawana_cmd(pattern="ultroid$")
async def useUltroid(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://te.legra.ph/file/00f7f36f128e9366ec578.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
