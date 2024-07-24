# WhatShouldIBuildNext discord bot
Simple discord bot which suggests what you can build next

### Adding to your server
You can add my instance of the bot to your discord server via the link below
https://discord.com/oauth2/authorize?client_id=1265128137696739480&permissions=2048&integration_type=0&scope=bot

### Wanna get support, give ideas or request a feature?
Join my [discord server](https://discord.gg/3HQKbwFzpR)!!

## Running your own instance of the bot

### Docker (Recommended)
#### Using Docker CLI (Getting the project from docker hub)
```shell
docker run -d \
  --name wsibn \
  -e TOKEN=your_discord_token \
  -e InstanceRanBy=your_nickname \
  --restart unless-stopped \
  9783e6/wsibn
```
#### Building from Dockerfile
```shell
git clone https://github.com/9783e6/WhatShouldIBuildNext_DiscordBot
cd ./WhatShouldIBuildNext_DiscordBot
docker build -t wsibn .
docker run --name wsibn -e "TOKEN=your_discord_bot_token InstanceRanBy=your_nickname" wsibn
```
### Running via native python
```shell
git clone https://github.com/9783e6/WhatShouldIBuildNext_DiscordBot
cd ./WhatShouldIBuildNext_DiscordBot
pip3 install -r requirements.txt
TOKEN="your_discord_token" InstanceRanBy="your_nickname" python3 ./main.py
```