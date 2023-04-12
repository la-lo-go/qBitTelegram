<div align="center" >
<img src="./docs/logo-long.svg" align="center" width="60%"/>
</div>
<h2 align="center" >
Manage your torrent server from anywhere via Telegram.
</h2>

## Features
- Torrents:
   - [X] Add torrent via magnet with a category.
   - [ ] Delete a torrent.
   - [ ] Resume.
- Categories
   - [X] List all categories.
   - [X] View all torrents.
   - [X] View all downloading torrents.
   - [ ] Add a category.
   - [ ] Edit a category.
- Search:
   - [ ] Search torrents with search plugings.
   - [ ] Download from search.

## Prerequisites
1. The telegram bot token ([here](https://core.telegram.org/bots#how-do-i-create-a-bot) is a tutorial)
2. [Docker](https://www.docker.com/) installed and running on the server.

## Deploy
### Clone the repository
```bash
git clone https://github.com/la-lo-go/qBitTelegram
cd ./qBitTelegram/
```

### Change the environment variables in the Dockerfile (Optional)
You can change the env variables values now on the [Dockerfile](./Dockerfile) or change ir later when you run the container. 

### Build the image
```
docker build -t qbittelegram .
```

### Run the container
#### If you did not change the environment variables:
```bash
docker run --name qBitTelegram -e QBIT_HOST="XXX.XXX.X.XXX" -e QBIT_PORT="XXXX" -e QBIT_USERAME="admin" -e QBIT_PASS="admin" -e TELEGRAM_TOKEN="XXXXX:XXXXX-XXXXXXXXXXX" -e ADMINS="username_admin1,username_admin2" qbittelegram
```
#### If you changed the environment variables:
```bash
docker run --name qBitTelegram qbittelegram
```

### Add the commands to menu
1. Go to the [_BotFather_](https://t.me/botfather) chat.
2. Send the command `/setcommands`.
3. Choose the bot.
4. Write:
   ```
    torrents - All torrents
    torrents_downloading - Downloading torrents 
    categories - List of categories
   ```