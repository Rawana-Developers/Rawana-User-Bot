#!/usr/bin/env bash
# Rawana - UserBot
# Copyright (C) 2021-2022 TeamRawana
#
# This file is a part of < https://github.com/Rawana-Developers/Rawana-User-Bot/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/Rawana-Developers/Rawana-User-Bot/blob/main/LICENSE/>.
clear
echo -e "\e[1m"
echo    "       ΞΞΞΞΞΞΞΞΞΞΞ         ΞΞΞΞΞΞ       ΞΞ             ΞΞ            ΞΞ     ΞΞΞΞΞΞ       ΞΞΞΞ       ΞΞ     ΞΞΞΞΞ     "
echo    "       ΞΞ       ΞΞ        ΞΞ    ΞΞ       ΞΞ           ΞΞΞΞ          ΞΞ     ΞΞ    ΞΞ      ΞΞ ΞΞ      ΞΞ    ΞΞ   ΞΞ    "
echo    "       ΞΞ       ΞΞ       ΞΞ      ΞΞ       ΞΞ         ΞΞ  ΞΞ        ΞΞ     ΞΞ      ΞΞ     ΞΞ  ΞΞ     ΞΞ   ΞΞ     ΞΞ   "
echo    "       ΞΞΞΞΞΞΞΞΞΞΞ      ΞΞ        ΞΞ       ΞΞ       ΞΞ    ΞΞ      ΞΞ     ΞΞ        ΞΞ    ΞΞ   ΞΞ    ΞΞ  ΞΞΞΞΞΞΞΞΞΞΞ  " 
echo    "       ΞΞ  ΞΞ           ΞΞ ΞΞΞΞΞΞ ΞΞ        ΞΞ     ΞΞ      ΞΞ    ΞΞ      ΞΞ ΞΞΞΞΞΞ ΞΞ    ΞΞ    ΞΞ   ΞΞ  ΞΞ       ΞΞ  "
echo    "       ΞΞ   ΞΞ          ΞΞ        ΞΞ         ΞΞ  ΞΞ         ΞΞ  ΞΞ       ΞΞ        ΞΞ    ΞΞ     ΞΞ  ΞΞ  ΞΞ       ΞΞ  " 
echo    "       ΞΞ    ΞΞ         ΞΞ        ΞΞ          ΞΞΞΞ           ΞΞΞΞ        ΞΞ        ΞΞ    ΞΞ      ΞΞ ΞΞ  ΞΞ       ΞΞ  "
echo    "       ΞΞ     ΞΞ        ΞΞ        ΞΞ           ΞΞ             ΞΞ         ΞΞ        ΞΞ    ΞΞ       ΞΞΞΞ  ΞΞ       ΞΞ  "
echo -e "\e[0m"
sec=5
spinner=(⣻ ⢿ ⡿ ⣟ ⣯ ⣷)
while [ $sec -gt 0 ]; do
    echo -ne "\e[33m ${spinner[sec]} Starting dependency installation in $sec seconds...\r"
    sleep 1
    sec=$(($sec - 1))
done
echo -e "\e[1;32mInstalling Dependencies ---------------------------\e[0m\n" # Don't Remove Dashes / Fix it
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/Rawana-Developers/Rawana-User-Bot/main/resources/session/ssgen.py
pip uninstall telethon -y && install telethon
clear
python3 ssgen.py
