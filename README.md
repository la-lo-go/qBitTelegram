<div align="center" >
<img src="./docs/logo-long.svg" align="center" width="60%"/>

</br>
</br>
<strong> Manage your torrent server from anywhere via Telegram </strong>
</div>


## Features
- Torrents:
   - [X] Add torrent via magnet with a category.
   - [ ] Send a notification when a torrent is added/downloaded.
   - [ ] Delete a torrent.
   - [ ] Resume.
- Categories
   - [X] List all categories.
   - [ ] Add a category.
   - [ ] Edit a category.
- View:
   - [X] View all torrents.
   - [X] View all downloading torrents.
   - [X] View all torrents with a full description of status, size, etc.
- Search:
   - [ ] Search torrents with search plugings.
   - [ ] Download from search.

## Prerequisites
1. The telegram bot token ([here](https://core.telegram.org/bots#how-do-i-create-a-bot) is a tutorial)
2. [Docker](https://www.docker.com/) and [Docker compose](https://docs.docker.com/compose/install/) installed and running on the server.
   
## Run the container with docker-compose

| Variable Name    | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| `QBIT_HOST`      | The host (IP) of the qBitTorrent server.                    |
| `QBIT_PORT`      | The port of the qBitTorrent server.                         |
| `QBIT_USERAME`   | The username of the qBitTorrent server.                     |
| `QBIT_PASS`      | The password of the qBitTorrent server.                     |
| `TELEGRAM_TOKEN` | The token of the telegram bot.                              |
| `ADMINS`         | The telegram usernames of the admins (separeted by commas). |

### Using DockerHub image (recommended)
```bash
version: '3.8'
services:
  qbittelegram:
    container_name: qBitTelegram
    image: lalogo/qbittelegram:latest 
    environment:
      - QBIT_HOST=127.0.0.1
      - QBIT_PORT=8080
      - QBIT_USERAME=admin
      - QBIT_PASS=admin
      - TELEGRAM_TOKEN=XXXXXXXXX:XXXXXXXXXXXXXX
      - ADMINS=admin1,admin2
    restart: unless-stopped
```

### Cloning the repository
```bash
git clone
cd qBitTelegram
docker-compose up -d
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
