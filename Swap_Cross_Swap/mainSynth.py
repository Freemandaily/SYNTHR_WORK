# This program is for synth testnet

from web3 import *
import time,os,sys,random
import synth_Abi
from classSynth import SyTHNR

INFURA_KEY = 'YOUR_INFURA_KEY'
connect = Web3(Web3.HTTPProvider(f'https://arbitrum-sepolia.infura.io/v3/{INFURA_KEY}'))
print(connect.is_connected())

# TOKEN AND CONTRACTS USED 
SWAP_ROUTER = connect.eth.contract(address=connect.to_checksum_address(synth_Abi.SWAP_ROUTER_ADRESS),abi=synth_Abi.SWAP_ROUTER_ABI)
BRIGDE_ROUTER = connect.eth.contract(address=connect.to_checksum_address(synth_Abi.BRIDGE_ROUTER_ADDRESS),abi=synth_Abi.BRIDGE_ROUTER_ABI)

SyUSD_sourceCurrencyKey = '0x7355534400000000000000000000000000000000000000000000000000000000'
SyBNB_destinationCurrencyKey = '0x73424e4200000000000000000000000000000000000000000000000000000000'
SyAVAX_destinationCurrencyKey = '0x7341564158000000000000000000000000000000000000000000000000000000'
SyMATIC_destinationCurrencyKey = '0x734d617469630000000000000000000000000000000000000000000000000000'

amount_In_list = [10,9,5,7]
destination_list = [ SyBNB_destinationCurrencyKey,SyAVAX_destinationCurrencyKey ]     #,SyMATIC_destinationCurrencyKey]

hashes = [ ]
def Action(priv,wallet_number):
    number_of_swap = random.choice([2,2])
    destination = random.sample(destination_list,number_of_swap)
    amountIn = random.choice(amount_In_list)
    processor = SyTHNR(priv,amountIn) 

    # For same Chain Swap
    def SwapSameChain():
        for chain in destination:
            try:
                hash = processor.SameChainSwap(connect,SWAP_ROUTER,chain)
                print('Waiting for 10 before swapping another')
                hashes.append(hash)
                time.sleep(5)
            except Exception as e:
                print(f'The issue is from {e}')
            

    # For Cross Chain Swapping
    def CrossChain():
        for chain in destination_list :
            try:
                if chain == SyBNB_destinationCurrencyKey:
                    chainId = 10102
                    hash = processor.CrossChainSwap(connect,SWAP_ROUTER,chain,chainId)
                    hashes.append(hash)
                elif chain == SyAVAX_destinationCurrencyKey:
                    chainId = 10106
                    hash = processor.CrossChainSwap(connect,SWAP_ROUTER,chain,chainId)
                    hashes.append(hash)
                elif chain == SyMATIC_destinationCurrencyKey:
                    chainId = 10109
                    hash = processor.CrossChainSwap(connect,SWAP_ROUTER,chain,chainId)
                    hashes.append(hash)
                print('Waiting for 15 seconds before swapping another')
                time.sleep(5)
            except:
                pass
            #return hash
    
    # Bridging
    def Bridge():
        for chain in destination_list:
            amount_in_list = [7,8,9,5]
            try:
                amount_in = random.choice(amount_in_list)
                if chain == SyBNB_destinationCurrencyKey:
                    chainId = 10102
                    hash = processor.BridgeSwap(connect,BRIGDE_ROUTER,chainId,amount_in)
                    hashes.append(hash)
                elif chain == SyAVAX_destinationCurrencyKey:
                    chainId = 10106
                    hash = processor.BridgeSwap(connect,BRIGDE_ROUTER,chainId,amount_in)
                    hashes.append(hash)
                elif chain == SyMATIC_destinationCurrencyKey:
                    chainId = 10109
                    hash = processor.BridgeSwap(connect,BRIGDE_ROUTER,chainId,amount_in)
                    hashes.append(hash)
                print('Waiting for 10 seconds before swapping another')
                time.sleep(5)
            except:
                pass
            #return hash

    # This is where to chooose which one action to take
    action_initials =  [0,1,2]
    random_initials = random.sample(action_initials,3)
    for initial in random_initials:
        if initial == 0 :
            SwapSameChain()
        elif initial == 1 :
            CrossChain()
        elif initial == 2 :
            Bridge()

    hash = random.choice(hashes)    
    processor.Alert(hash,wallet_number)
 

# Taking Command From The Subprocess
wallet_command = sys.argv[1] 
if wallet_command == 'arbitrumBot_1':
    priv = os.environ.get('arbitrumBot_1')
    wallet_number = 1
    Action(priv,wallet_number)
elif wallet_command == 'arbitrumBot_2':
    priv = os.environ.get('arbitrumBot_2')
    wallet_number = 2
    Action(priv,wallet_number)
elif wallet_command == 'arbitrumBot_3':
    priv = os.environ.get('arbitrumBot_3')
    wallet_number = 3
    Action(priv,wallet_number)
elif wallet_command == 'arbitrumBot_4':
    priv = os.environ.get('arbitrumBot_4')
    wallet_number = 4
    Action(priv,wallet_number)




