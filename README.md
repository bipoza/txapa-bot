# TxapaBot


## Instalazioa
### 1. Virtual environment bat sortu 
##### *virtualenv instalatuta baldin badaukazu ez egin pauso hau
1. Instalatu virtualenv
   ```$ pip3 install virtualenv```
   
2. Sortu zure ingurune birtuala
   ```$ virtualenv -p venv .```

### 2. Dependentziak instalatu
```
$ pip install -r requirements.txt
```

## Konfigurazioa
1. TELEGRAM_BOT_API_KEY: Token-a lortzeko, lehenengo bot bat sortu behar da.
   [BotFather](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
2. TELEGRAM_CHAT_ID: CHAT_ID-a lortzeko, jarraitu gida hau: https://github.com/GabrielRF/telegram-id#web-channel-id