# Quake 3 status bot

Quake 3 status bot is [Telegram](https://telegram.org/) bot, based on [telepot](https://github.com/nickoala/telepot) framework, which sends notification to group/user once someone connects to Quake 3 game server and when all players are gone.

Please note that the bot will not work with servers where `g_humanplayers` parameter is disabled.

### Installation

Donwload and unpack the bot (or simply `git clone` it)

Install packages from requirements.txt file.
```
$ cd q3
$ pip install -r requirements.txt
```

Modify `config/bot.conf` file and enter bot token, ID of your user or group, address and port of the server.
Information on how to create new bot and obtain token is described [here](https://core.telegram.org/bots).

### Usage

Simply run `bot.py` file by python.
```
$ cd <project path>
$ python bot.py
```