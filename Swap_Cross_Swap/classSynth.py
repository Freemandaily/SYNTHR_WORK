from web3 import *
import time,sys,os
import telegram,asyncio
from telegram.constants import ParseMode
import synth_Abi

INFURA_KEY = 'YOUR_INFURA_KEY'
connect = Web3(Web3.HTTPProvider(f'https://arbitrum-sepolia.infura.io/v3/{INFURA_KEY}'))

SyUSD_CONTRACT = connect.eth.contract(address=connect.to_checksum_address(synth_Abi.SyUSD_ADDRESS),abi=synth_Abi.BASIC_TOKEN_ABI)



class SyTHNR:
    def __init__(self,priv,amountIn) -> None:
        self.priv = priv
        self.account = Account.from_key(self.priv)
        self.SyUSD_sourceCurrencyKey = '0x7355534400000000000000000000000000000000000000000000000000000000'
        self.amountIn = int(amountIn*10**18)
        self.additionalGas = connect.to_wei('0.0003','gwei')
        self.amountOut = 0
        self.bridgeName = '0x4c617965725a65726f0000000000000000000000000000000000000000000000'
        self.chainId = 0
        self.erc20Payment = False


    # Same Chain Swapping
    def SameChainSwap(self,connect,Router,destinationCurrencyKey):
        user_balance = SyUSD_CONTRACT.functions.balanceOf(self.account.address).call()
        
        if user_balance >= self.amountIn :
            try:
                gasPrice = connect.eth.get_block('latest')['baseFeePerGas']
                transaction = Router.functions.exchangeAtomically(
                    self.SyUSD_sourceCurrencyKey,
                    self.amountIn,
                    destinationCurrencyKey,
                    self.amountOut,
                    self.bridgeName,
                    self.chainId,
                    self.erc20Payment
                ).build_transaction({
                    'from': self.account.address,
                    'gas': 2000000,
                    'gasPrice': connect.t0_wei('5','gwei'),
                    'nonce': connect.eth.get_transaction_count(self.account.address)
                })

                sign_trx = connect.eth.account.sign_transaction(transaction,self.priv)
                send = connect.eth.send_raw_transaction(sign_trx.rawTransaction)
                print(f'The transaction hash for Same ChainSwap is: {send.hex()}')
                return send
            except Exception as e:
                #Alert
                action = 'SameChainSwap'
                self.failedTrade(e,action)
                print(f'The problem is from {e}')
        else :
            # Alert
            error = 'YOU DONT HAS ENOUGH SyUSD BALANCE'
            action = 'SameChainSwap'
            self.failedTrade(error,action)

    # For Cross Chain Swapping
    def CrossChainSwap(self,connect,Router,destinationCurrencyKey,chainId):
        user_balance = SyUSD_CONTRACT.functions.balanceOf(self.account.address).call()

        if user_balance >= self.amountIn :
            try:
                gasPrice = connect.eth.get_block('latest')['baseFeePerGas']
                transaction = Router.functions.exchangeAtomically(
                        self.SyUSD_sourceCurrencyKey,
                        self.amountIn,
                        destinationCurrencyKey,
                        self.amountOut,
                        self.bridgeName,
                        chainId,
                        self.erc20Payment
                    ).build_transaction({
                        'from': self.account.address,
                        'value': connect.to_wei('0.00125','ether'),
                        'gas': 2000000,
                        'gasPrice':'gasPrice': connect.t0_wei('5','gwei'),
                        'nonce': connect.eth.get_transaction_count(self.account.address)
                    })
                
                sign_trx = connect.eth.account.sign_transaction(transaction,self.priv)
                send = connect.eth.send_raw_transaction(sign_trx.rawTransaction)
                print(f'The transaction hash for CrossChainSwap is: {send.hex()}')
                return send
            except  Exception as e:
                # Alert
                action = 'CrossChainSwap'
                self.failedTrade(e,action)
                print(f'The issue is from {e}')
        else :
             # Alert
            error = 'YOU DONT HAS ENOUGH SyUSD BALANCE'
            action = 'CrossChainSwap'
            self.failedTrade(error,action)

    # For Bridging
    def BridgeSwap(self,connect,Router,chainId,amount_In):
        amountIn = int(amount_In*10**18)
        user_balance = SyUSD_CONTRACT.functions.balanceOf(self.account.address).call()

        if user_balance >= amountIn:
            try:
                gasPrice = connect.eth.get_block('latest')['baseFeePerGas']
                transaction = Router.functions.bridgeSynth(
                    self.account.address,
                    self.SyUSD_sourceCurrencyKey,
                    amountIn,
                    self.bridgeName,
                    chainId,
                    self.erc20Payment
                ).build_transaction({
                    'from': self.account.address,
                    'value': connect.to_wei('0.00125','ether'),
                    'gas': 2000000,
                    'gasPrice': 'gasPrice': connect.t0_wei('5','gwei'),
                    'nonce': connect.eth.get_transaction_count(self.account.address)

                })

                sign_trx = connect.eth.account.sign_transaction(transaction,self.priv)
                send = connect.eth.send_raw_transaction(sign_trx.rawTransaction)
                print(f'The Transaction hash for Bridging is {send.hex()}')
                return send
            except Exception as e:
                # Alert
                action = 'bridge'
                self.failedTrade(e,action)
                print(f'The issue is from {e}')
        else:
              # Alert
            error = 'YOU DONT HAS ENOUGH SyUSD BALANCE'
            action = 'Bridge'
            self.failedTrade(error,action)

    
    # Alert
    def Alert(self,hash,walletNumber):
        bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'
        CHAT_ID = 'YOUR TELEGRAM CHAT_ID'
        hash_link = f'https://sepolia.arbiscan.io/tx/{hash.hex()}'
        trade_info =  f' ALL SYNTHR TRANSCTIONS SUCCESFULLY POSTED \n\n'\
                      f'WALLET: {walletNumber}\n\n'\
                      f'CLICK <a href="{hash_link}">HASH </a> TO VIEW TRANSACTION\n\n'
        async def main():
            try:
                bot = telegram.Bot(bot_token)
            except:
                bot = telegram.Bot(bot_token)
            async with bot:
                await bot.send_message(text=trade_info,parse_mode=ParseMode.HTML,chat_id=CHAT_ID)
        if __name__!='__main__':
            asyncio.run(main())
      
   # For failed Trade
    def failedTrade(self,e,action):
        bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'
        CHAT_ID = 'YOUR TELEGRAM CHAT_ID'
        async def main():
            try:
                bot = telegram.Bot(bot_token)
            except:
                bot = telegram.Bot(bot_token)
            async with bot:
                await bot.send_message(text=f'UNABLE TO POST TRANSACTION\n\nActiom:{action}\n\nERROR: {e}',chat_id=CHAT_ID)
        if __name__!='__main__':
            asyncio.run(main())

