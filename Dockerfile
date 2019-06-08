FROM python:3.6-stretch

# replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

WORKDIR /code

RUN apt update
RUN apt install -y postgresql postgresql-contrib

# Install deps needed to run headless chrome
# TODO: We don't need all of these... check which come by default and remove
RUN apt install -y gconf-service libasound2 libatk1.0-0 libatk-bridge2.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget

COPY . /code

# TODO: Use nvm
RUN curl -sL https://deb.nodesource.com/setup_10.x  | bash -
RUN apt-get -y install nodejs
RUN npm install

RUN pip3 install -r requirements.txt
RUN pip3 install ipython

ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

COPY ./docker-entrypoint.sh /code/
ENTRYPOINT ["/code/docker-entrypoint.sh"]

EXPOSE 7667
