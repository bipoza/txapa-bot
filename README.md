#  TxapaBot 🤖 📻


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


## Baina... Nola funtzionatzen du honek?
Bueno ba, bot honek hiru funtzionalitate nagusitan banatzen da:
1. Informazioa lortu:
   
   Teknologia libreak erabiltzeak onura zoragarriak ditu.
   Honi esker, TxapaBot-ek behar duen informazio guztia [txapairratia.org-eko](http://txapairratia.org) RSStik lortzen du. http://www.txapairratia.org/rss/

2. Audioa + thumb irudia konprimitu:
   
   Telegrameko botek aukera asko izan arren, aukera batzuk mugatuta daude.
   Adibidez, bot batek **50 MB-tik beherako fitxategiak** bakarrik bidal ditzake. https://core.telegram.org/bots/faq#how-do-i-upload-a-large-file

   Beraz, arazo honi aurre egiteko, audio fitxategiak deskargatu eta konprimitu behar dira, 50 MB baino gutxiagoko fitxategiak sortuz.

   Prozesu hau egiteko, **pydub** izeneko liburutegia erabiltzen dugu. Tresna honek **ffmpeg**-eko interfaze bat eskaintzen digu (ffmpeg sisteman instalatu behar da ere). Kalitate tabla: https://trac.ffmpeg.org/wiki/Encode/MP3

   Irudiari dagokionez, 200kb-eko muga dauka. Kalitatea txikitzeko Pillow liburutegia erabili da.

   Bestalde, honi alde ona ikus diezaiokegu. Irratsaio bat mugikorrera deskargatzean, gutxiago okupatuko digu ;)

3. Audioa bidali:
   
   Bukatzeko, fitxategia txat batera bidaltzen da, **python-telegram-bot** liburutegia erabiliz.

   Gure kasuan, edonork parte har dezan, telegrameko @txapagram kanal publikora bidaltzen dugu.




## Erabilitako python liburutegiak
* python-telegram-bot
* pydub
* Pillow
* feedparser
* beautifulsoup4
* schedule