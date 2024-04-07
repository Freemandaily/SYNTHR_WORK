## SYNTHR_WORK
This is an experimental program for interacting with Synthr testnet project. Treat this script as an educational work rather than any other thing

## Requrements
- web3 ( pip install web3)
- telegram ( pip install python-telegram-bot)

## Note:
- You have to get your telegram bot token and your infura api key ready ( getting this two is simple, just google search them for guide)

## CONFIGURATION
### FOR SCRIPT IN Swap_Cross_swwap folder
- Inside `classSynth` module, Paste in your infura key in  variable ( INFURA_KEY = 'YOUR_INFURA_KEY' ), In `Alert and failedTrade` function , paste your Telegram bot token and the chat id into the variable (bot_token and CHAT_ID) respectively <br>

- Inside `mainSynth` module, Paste in your infura key in  variable ( INFURA_KEY = 'YOUR_INFURA_KEY' )

## ACCOUNT SETUPS
Setting your private key as environment variable:
- Linux : export arbitrumBot_1='YOUR_PRIVATE_KEY'
- Window: setx arbitrumBot_1='YOUR_PRIVATE_KEY'

  ## WANT MANY ACCOUTS
  Currently the the bot is set to only one account but you can modify to accomdate max of 4 accounts,  inside inside `synth_divider.py` module uncomment thoose #subprocess.Popen(['python3','mainSynth.py','arbitrumBot_..']) as per your numer of account you want, but remeber to set the environment variable as per the account.<br>

  for seconnd
