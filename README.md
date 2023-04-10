## Deploy

### .env schema
```docker
QBIT_HOST="XXX.XXX.X.XXX"
QBIT_PORT="XXXX"
QBIT_USERAME="username"
QBIT_PASS="password"
TELEGRAM_TOKEN="XXXXX:XXXXX-XXXXXXXXXXX"
ADMINS='["usernam_admin1", "usernam_admin2"]'
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
 - [X] List all categories.
 - [X] Add torrent via magnet with a category.
 - [X] View all torrents
 - [X] View all downloading torrents
 - [ ] Add a category.
 - [ ] Delete a torrent.
  