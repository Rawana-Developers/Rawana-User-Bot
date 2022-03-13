#!/usr/bin/python3
# Rawana - UserBot
# Copyright (C) 2021-2022 TeamRawana
#
# This file is a part of < https://github.com/Rawana-Developers/Rawana-User-Bot/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/Rawana-Developers/Rawana-User-Bot/blob/main/LICENSE/>.

import os
from time import sleep

RAWANA = r"""
           ΞΞΞΞΞΞΞΞΞΞΞ         ΞΞΞΞΞΞ       ΞΞ             ΞΞ            ΞΞ     ΞΞΞΞΞΞ       ΞΞΞΞ       ΞΞ     ΞΞΞΞΞ
           ΞΞ       ΞΞ        ΞΞ    ΞΞ       ΞΞ           ΞΞΞΞ          ΞΞ     ΞΞ    ΞΞ      ΞΞ ΞΞ      ΞΞ    ΞΞ   ΞΞ
           ΞΞ       ΞΞ       ΞΞ      ΞΞ       ΞΞ         ΞΞ  ΞΞ        ΞΞ     ΞΞ      ΞΞ     ΞΞ  ΞΞ     ΞΞ   ΞΞ     ΞΞ
           ΞΞΞΞΞΞΞΞΞΞΞ      ΞΞ        ΞΞ       ΞΞ       ΞΞ    ΞΞ      ΞΞ     ΞΞ        ΞΞ    ΞΞ   ΞΞ    ΞΞ  ΞΞΞΞΞΞΞΞΞΞΞ 
           ΞΞ  ΞΞ           ΞΞ ΞΞΞΞΞΞ ΞΞ        ΞΞ     ΞΞ      ΞΞ    ΞΞ      ΞΞ ΞΞΞΞΞΞ ΞΞ    ΞΞ    ΞΞ   ΞΞ  ΞΞ       ΞΞ
           ΞΞ   ΞΞ          ΞΞ        ΞΞ         ΞΞ  ΞΞ         ΞΞ  ΞΞ       ΞΞ        ΞΞ    ΞΞ     ΞΞ  ΞΞ  ΞΞ       ΞΞ 
           ΞΞ    ΞΞ         ΞΞ        ΞΞ          ΞΞΞΞ           ΞΞΞΞ        ΞΞ        ΞΞ    ΞΞ      ΞΞ ΞΞ  ΞΞ       ΞΞ 
           ΞΞ     ΞΞ        ΞΞ        ΞΞ           ΞΞ             ΞΞ         ΞΞ        ΞΞ    ΞΞ       ΞΞΞΞ  ΞΞ       ΞΞ
"""


def spinner():
    print("Checking if Telethon is installed...")
    for _ in range(3):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.1)


def clear_screen():
    # https://www.tutorialspoint.com/how-to-clear-screen-in-python#:~:text=In%20Python%20sometimes%20we%20have,screen%20by%20pressing%20Control%20%2B%20l%20.
    if os.name == "posix":
        os.system("clear")
    else:
        # for windows platfrom
        os.system("cls")


def get_api_id_and_hash():
    print(
        "Get your API ID and API HASH from my.telegram.org or @ScrapperRoBot to proceed.\n\n",
    )
    try:
        API_ID = int(input("Please enter your API ID: "))
    except ValueError:
        print("APP ID must be an integer.\nQuitting...")
        exit(0)
    API_HASH = input("Please enter your API HASH: ")
    return API_ID, API_HASH


def telethon_session():
    try:
        spinner()
        import telethon # ignore: pylint
        text = "\bFound an existing installation of Telethon...\nSuccessfully Imported.\n\n"
    except ImportError:
        print("Installing Telethon...")
        os.system("pip uninstall telethon -y && pip install -U telethon")

        text = "\bDone. Installed and imported Telethon."
    clear_screen()
    print(RAWANA)
    print(text)

    # the imports

    from telethon.errors.rpcerrorlist import (
        ApiIdInvalidError,
        PhoneNumberInvalidError,
        UserIsBotError,
    )
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient

    API_ID, API_HASH = get_api_id_and_hash()

    # logging in
    try:
        with TelegramClient(StringSession(), API_ID, API_HASH) as Rawana:
            print("Generating a string session for •Rawana•")
            try:
                ult = ultroid.send_message(
                    "me",
                    f"**Rawana** `SESSION`:\n\n`{Rawana.session.save()}`\n\n**Do not share this anywhere!**",
                )
                print(
                    "Your SESSION has been generated. Check your Telegram saved messages!"
                )
                return
            except UserIsBotError:
                print("You are trying to Generate Session for your Bot's Account?")
                print("Here is That!\n{Rawana.session.save()}\n\n")
                print("NOTE: You can't use that as User Session..")
    except ApiIdInvalidError:
        print(
            "Your API ID/API HASH combination is invalid. Kindly recheck.\nQuitting..."
        )
        exit(0)
    except ValueError:
        print("API HASH must not be empty!\nQuitting...")
        exit(0)
    except PhoneNumberInvalidError:
        print("The phone number is invalid!\nQuitting...")
        exit(0)
    except Exception as er:
        print("Unexpected Error Occurred while Creating Session")
        print(er)
        print("If you think It as a Bug, Report to @Rawana_Developers.\n\n")


def main():
    clear_screen()
    print(Rawana)
    telethon_session()
    x = input("Run again? (y/n)")
    if x.lower() in ["y", "yes"]:
        main()
    else:
        exit(0)


main()
