# Test Booster Bot

> Telegram bot for making online testing


## Running

To start the server, type in terminal:

```bash
python3 -m src.main
```


## Environment

All local environment is keeping in `.env` file. There are follow variables:

### Telegram:
- `TELEGRAM_TOKEN` - Token of the bot, taken from BotFather

### Gigachat:
- `GIGACHAT_CLIENT_ID` - Client ID of `SBER.ID`
- `GIGACHAT_AUTH_KEY` - Authentication key of API
- `GIGACHAT_SCOPE` - Mode of a model

### Posgresql database:
- `POSTGRESQL_USER` - username
- `POSTGRESQL_PASS` - password
- `POSTGRESQL_HOST` - host (*ex. `localhost`*)
- `POSTGRESQL_PORT` - port for connection
- `POSTGRESQL_DATABASE` - name of the created database
