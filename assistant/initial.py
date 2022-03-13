# Rawana - UserBot
# Copyright (C) 2021-2022 TeamRawana
#
# This file is a part of < https://github.com/Rawana-Developers/Rawana-User-Bot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Rawana-Developers/Rawana-User-Bot/blob/main/LICENSE/>.

import re

from . import *

STRINGS = {
    1: """🎇 **Thanks for Deploying Rawana Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage.""",
    2: """🎉** About Rawana**

🧿 Rawana Is is Pluggable and powerful Telethon Userbot, made in Python from Scratch. It is Aimed to Increase Security along with Addition of Other Useful Features.

❣ Made by **@Rawana_Developers**""",
    3: """**💡• FAQs •**

-> [Username Tracker](https://t.me/Rawana_Bot_Developers/35)
-> [Keeping Custom Addons Repo](https://t.me/Rawana_Bot_Developers/37)
-> [Disabling Deploy message](https://t.me/Rawana_Bot_Developers/38)
-> [Setting up TimeZone](https://t.me/Rawana_Bot_Developers/39)
-> [About Inline PmPermit](https://t.me/Rawana_Bot_Developers/40)
-> [About Dual Mode](https://t.me/Rawana_Bot_Developers/41)
-> [Custom Thumbnail](https://t.me/Rawana_Bot_Developers/42)
-> [About FullSudo](https://t.me/Rawana_Bot_Developers/43)
-> [Setting Up PmBot](https://t.me/Rawana_Bot_Developers/44)
-> [Also Check](https://t.me/Rawana_Bot_Developers/45)

**• To Know About Updates**
  - Join @Rawana_Developers.""",
    4: f"""• `To Know All Available Commands`

  - `{HNDLR}help`
  - `{HNDLR}cmds`""",
    5: """• **For Any Other Query or Suggestion**
  - Move to **@Rawana_Bot_Developers**.

• Thanks for Reaching till END.""",
}


@callback(re.compile("initft_(\\d+)"))
async def init_depl(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 5:
        return await e.edit(
            STRINGS[5],
            buttons=Button.inline("<< Back", "initbk_" + str(4)),
            link_preview=False,
        )
    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", "initbk_" + str(CURRENT - 1)),
            Button.inline(">>", "initft_" + str(CURRENT + 1)),
        ],
        link_preview=False,
    )


@callback(re.compile("initbk_(\\d+)"))
async def ineiq(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 1:
        return await e.edit(
            STRINGS[1],
            buttons=Button.inline("Start Back >>", "initft_" + str(2)),
            link_preview=False,
        )
    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", "initbk_" + str(CURRENT - 1)),
            Button.inline(">>", "initft_" + str(CURRENT + 1)),
        ],
        link_preview=False,
    )
