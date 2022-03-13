# Rawana - UserBot
# Copyright (C) 2021-2022 TeamRawana
#
# This file is a part of < https://github.com/Rawana-Developers/Rawana-User-Bot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Rawana-Developers/Rawana-User-Bot/blob/main/LICENSE/>.

from pyRawana import *
from pyRawana import _ult_cache
from pyRawana.functions.helper import *
from pyRawana.functions.tools import get_stored_file
from pyRawana.misc import owner_and_sudos
from pyRawana.misc._assistant import asst_cmd, callback, in_pattern
from telethon import Button, custom

from plugins import ATRA_COL
from strings import get_languages, get_string, language

OWNER_NAME = ultroid_bot.full_name
OWNER_ID = ultroid_bot.uid

AST_PLUGINS = {}


async def setit(event, name, value):
    try:
        udB.set_key(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    return [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
