# Rawana - UserBot
# Copyright (C) 2021-2022 TeamRawana
#This file is a part of < https://github.com/Rawana-Developers/Rawana-User-Bot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Rawana-Developers/Rawana-User-Bot/blob/main/LICENSE/>.

FROM theteamRawana/Rawana:main

# set timezone
ENV TZ=Asia/SriLanka

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    # cloning the repo and installing requirements.
    && git clone https://github.com/TeamUltroid/Ultroid.git /root/TeamRawana/ \
    && pip3 install --no-cache-dir -r root/TeamRawana/requirements.txt \
    && pip3 install av --no-binary av

# Railway's banned dependency
RUN if [ ! $RAILWAY_STATIC_URL ]; then pip3 install --no-cache-dir yt-dlp; fi

# changing workdir
WORKDIR /root/TeamRawana/

# start the bot
CMD ["bash", "startup"]
