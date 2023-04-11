## Deploy
### Docker
#### Build the image
```
docker build -t qbittelegram .
```

#### Run the container
Change the enviorement variables values here
``` arduino
docker run --name qBitTelegramContainer -e QBIT_HOST="XXX.XXX.X.XXX" -e QBIT_PORT="XXXX" -e QBIT_USERAME="username" -e QBIT_PASS="password" -e TELEGRAM_TOKEN="XXXXX:XXXXX-XXXXXXXXXXX" -e ADMINS="usernam_admin1,usernam_admin2" qbittelegram
```

### Add the commands to menu
1. Go to the _BotFather_ chat 
2. Send the command `/setcommands`
3. Choose the bot 
4. Write 
   ```
    torrents - list of all torrents
    torrents_downloading - list of all downloading torrents 
    categories - list of categories with their paths
   ```

## Roadmap
 - [X] Dockerize the bot
 - [X] List all categories.
 - [X] Add torrent via magnet with a category.
 - [X] View all torrents
 - [X] View all downloading torrents
 - [ ] Add a category.
 - [ ] Delete a torrent.
  