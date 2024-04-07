# This module contains relevant Address, token Contract and abi

SyUSD_ADDRESS = '0xDE30D6edD20c573746758E817782e43E747d56CC' 
SyBNB_ADDRESS = '0x0F5E421700C56ebdC456EeC66C5dB431C31A2139'
SyAVAX = '0x3028D24aF28d7103db6f5754a1663611f6eF683E'
SyMATIC = '0x9Ef14c18f2Fd7235b902Bc5f2B88d5c754A0128A'

SWAP_ROUTER_ADRESS = '0xe0875cbd144fe66c015a95e5b2d2c15c3b612179'
BRIDGE_ROUTER_ADDRESS = '0x2f1673bed3e85219e2b01bc988abcc482261c38c'

SWAP_ROUTER_ABI = [{"inputs":[{"internalType":"contract ExternWrappedStateToken","name":"_extTokenState","type":"address"},{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_resolver","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"uint256","name":"synthRedeemed","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"amountLiquidated","type":"uint256"},{"indexed":False,"internalType":"address","name":"liquidator","type":"address"}],"name":"AccountLiquidated","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"bytes32","name":"name","type":"bytes32"},{"indexed":False,"internalType":"address","name":"destination","type":"address"}],"name":"CacheUpdated","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"indexed":False,"internalType":"uint256","name":"synthAmount","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"debtShare","type":"uint256"}],"name":"DestBurn","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"string","name":"message","type":"string"}],"name":"DestBurnFailed","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":True,"internalType":"bytes32","name":"marketKey","type":"bytes32"},{"indexed":False,"internalType":"uint256","name":"marginDelta","type":"uint256"}],"name":"DestTransferMargin","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"string","name":"message","type":"string"}],"name":"DestTransferMarginFailed","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"oldOwner","type":"address"},{"indexed":False,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerNominated","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"bytes32","name":"collateralKey","type":"bytes32"},{"indexed":False,"internalType":"uint256","name":"collateralAmount","type":"uint256"}],"name":"StakeCollateral","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"from","type":"address"},{"indexed":False,"internalType":"bytes32","name":"collateralKey","type":"bytes32"},{"indexed":False,"internalType":"address","name":"collateralCurrency","type":"address"},{"indexed":False,"internalType":"uint256","name":"collateralAmount","type":"uint256"},{"indexed":False,"internalType":"uint16","name":"destChainId","type":"uint16"}],"name":"WithdrawCollateral","type":"event"},{"inputs":[],"name":"CONTRACT_NAME","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"acceptOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes32","name":"synthKey","type":"bytes32"},{"internalType":"bytes32","name":"bridgeName","type":"bytes32"}],"name":"burnSynths","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"synthKey","type":"bytes32"},{"internalType":"bytes32","name":"bridgeName","type":"bytes32"}],"name":"burnSynthsToTarget","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"uint16","name":"_destChainId","type":"uint16"}],"name":"chainBalanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_collateralKey","type":"bytes32"},{"internalType":"uint16","name":"_destChainId","type":"uint16"}],"name":"chainBalanceOfPerKey","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_collateralKey","type":"bytes32"}],"name":"collateralCurrency","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_synthKey","type":"bytes32"},{"internalType":"uint256","name":"_synthAmount","type":"uint256"}],"name":"destBurn","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"uint256","name":"_marginDelta","type":"uint256"},{"internalType":"bytes32","name":"_marketKey","type":"bytes32"}],"name":"destTransferMargin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"sourceCurrencyKey","type":"bytes32"},{"internalType":"uint256","name":"sourceAmount","type":"uint256"},{"internalType":"bytes32","name":"destinationCurrencyKey","type":"bytes32"},{"internalType":"bytes32","name":"bridgeName","type":"bytes32"},{"internalType":"uint16","name":"destChainId","type":"uint16"},{"internalType":"bool","name":"erc20Payment","type":"bool"}],"name":"exchange","outputs":[{"internalType":"uint256","name":"amountReceived","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"sourceCurrencyKey","type":"bytes32"},{"internalType":"uint256","name":"sourceAmount","type":"uint256"},{"internalType":"bytes32","name":"destinationCurrencyKey","type":"bytes32"},{"internalType":"uint256","name":"minAmount","type":"uint256"},{"internalType":"bytes32","name":"bridgeName","type":"bytes32"},{"internalType":"uint16","name":"destChainId","type":"uint16"},{"internalType":"bool","name":"erc20Payment","type":"bool"}],"name":"exchangeAtomically","outputs":[{"internalType":"uint256","name":"amountReceived","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"getAvailableCollaterals","outputs":[{"internalType":"bytes32[]","name":"","type":"bytes32[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_collateralKey","type":"bytes32"},{"internalType":"uint256","name":"_collateralAmount","type":"uint256"},{"internalType":"bytes32","name":"_bridgeName","type":"bytes32"},{"internalType":"uint16","name":"_destChainId","type":"uint16"}],"name":"getSendWithdrawGasFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"initializeLiquidatorRewardsRestitution","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"isResolverCached","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"isWaitingPeriod","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_bridgeName","type":"bytes32"},{"internalType":"uint16","name":"_destChainId","type":"uint16"},{"internalType":"bool","name":"erc20Payment","type":"bool"}],"name":"issueMaxSynths","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_collateralKey","type":"bytes32"},{"internalType":"uint256","name":"_collateralAmount","type":"uint256"},{"internalType":"uint256","name":"_synthToMint","type":"uint256"},{"internalType":"bytes32","name":"_bridgeName","type":"bytes32"},{"internalType":"uint16","name":"_destChainId","type":"uint16"},{"internalType":"bool","name":"erc20Payment","type":"bool"}],"name":"issueSynths","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"bytes32","name":"collateralKey","type":"bytes32"},{"internalType":"bytes32","name":"bridgeName","type":"bytes32"},{"internalType":"uint16","name":"destChainId","type":"uint16"},{"internalType":"bool","name":"erc20Payment","type":"bool"}],"name":"liquidateDelinquentAccount","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"collateralKey","type":"bytes32"},{"internalType":"bytes32","name":"bridgeName","type":"bytes32"},{"internalType":"uint16","name":"destChainId","type":"uint16"},{"internalType":"bool","name":"erc20Payment","type":"bool"}],"name":"liquidateSelf","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"nominateNewOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"nominatedOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"sourceCurrencyKey","type":"bytes32"},{"internalType":"uint256","name":"sourceAmount","type":"uint256"},{"internalType":"bytes32","name":"destinationCurrencyKey","type":"bytes32"},{"internalType":"bytes32","name":"bridgeName","type":"bytes32"},{"internalType":"bytes[]","name":"priceUpdateData","type":"bytes[]"},{"internalType":"uint16","name":"destChainId","type":"uint16"},{"internalType":"bool","name":"erc20Payment","type":"bool"}],"name":"offChainExchange","outputs":[{"internalType":"uint256","name":"amountReceived","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rebuildCache","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"resolver","outputs":[{"internalType":"contract AddressResolver","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"resolverAddressesRequired","outputs":[{"internalType":"bytes32[]","name":"addresses","type":"bytes32[]"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"restituted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"sUSD","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"settle","outputs":[{"internalType":"uint256","name":"reclaimed","type":"uint256"},{"internalType":"uint256","name":"refunded","type":"uint256"},{"internalType":"uint256","name":"numEntriesSettled","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_collateralKey","type":"bytes32"},{"internalType":"uint256","name":"_collateralAmount","type":"uint256"},{"internalType":"bytes32","name":"_bridgeName","type":"bytes32"},{"internalType":"uint16","name":"_destChainId","type":"uint16"},{"internalType":"bool","name":"_erc20Payment","type":"bool"}],"name":"withdrawCollateral","outputs":[],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]

BRIDGE_ROUTER_ABI = [{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_resolver","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"indexed":False,"internalType":"uint256","name":"synthAmount","type":"uint256"}],"name":"BurnSynthForBridge","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"bytes32","name":"name","type":"bytes32"},{"indexed":False,"internalType":"address","name":"destination","type":"address"}],"name":"CacheUpdated","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"indexed":False,"internalType":"uint256","name":"synthAmount","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"debtShare","type":"uint256"}],"name":"DestBurn","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"indexed":False,"internalType":"uint256","name":"synthAmount","type":"uint256"}],"name":"DestIssue","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"oldOwner","type":"address"},{"indexed":False,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerNominated","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"indexed":False,"internalType":"address","name":"synth","type":"address"}],"name":"SynthAdded","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":False,"internalType":"bytes32","name":"synthKey","type":"bytes32"},{"indexed":False,"internalType":"uint256","name":"synthAmount","type":"uint256"}],"name":"SynthIssueFromSynthrSwap","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"indexed":False,"internalType":"address","name":"synth","type":"address"}],"name":"SynthRemoved","type":"event"},{"inputs":[],"name":"CIRCUIT_BREAKER_SUSPENSION_REASON","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"CONTRACT_NAME","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"acceptOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract ISynth","name":"synth","type":"address"}],"name":"addSynth","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"allNetworksDebtInfo","outputs":[{"internalType":"uint256","name":"debt","type":"uint256"},{"internalType":"uint256","name":"sharesSupply","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"availableCurrencyKeys","outputs":[{"internalType":"bytes32[]","name":"","type":"bytes32[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"availableSynthCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"availableSynths","outputs":[{"internalType":"contract ISynth","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_synthKey","type":"bytes32"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes32","name":"_bridgeName","type":"bytes32"},{"internalType":"uint16","name":"_destChainId","type":"uint16"},{"internalType":"bool","name":"_erc20Payment","type":"bool"}],"name":"bridgeSynth","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"deprecatedSynth","type":"address"},{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"balance","type":"uint256"}],"name":"burnForRedemption","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"bytes32","name":"synthKey","type":"bytes32"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnSynths","outputs":[{"internalType":"uint256","name":"synthAmount","type":"uint256"},{"internalType":"uint256","name":"debtShare","type":"uint256"},{"internalType":"uint256","name":"reclaimed","type":"uint256"},{"internalType":"uint256","name":"refunded","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"bytes32","name":"synthKey","type":"bytes32"}],"name":"burnSynthsToTarget","outputs":[{"internalType":"uint256","name":"synthAmount","type":"uint256"},{"internalType":"uint256","name":"debtShare","type":"uint256"},{"internalType":"uint256","name":"reclaimed","type":"uint256"},{"internalType":"uint256","name":"refunded","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"},{"internalType":"address","name":"from","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnSynthsWithoutDebt","outputs":[{"internalType":"uint256","name":"burnAmount","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"canBurnSynths","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_issuer","type":"address"},{"internalType":"bytes32","name":"_collateralKey","type":"bytes32"},{"internalType":"uint16","name":"_chainId","type":"uint16"}],"name":"checkFreeCollateral","outputs":[{"internalType":"uint256","name":"withdrawableSynthr","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"collateral","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_issuer","type":"address"}],"name":"collateralisationRatio","outputs":[{"internalType":"uint256","name":"cratio","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_issuer","type":"address"}],"name":"collateralisationRatioAndAnyRatesInvalid","outputs":[{"internalType":"uint256","name":"cratio","type":"uint256"},{"internalType":"bool","name":"anyRateIsInvalid","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_issuer","type":"address"}],"name":"debtBalanceOf","outputs":[{"internalType":"uint256","name":"debtBalance","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_synthKey","type":"bytes32"},{"internalType":"uint256","name":"_synthAmount","type":"uint256"}],"name":"destBurn","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_synthKey","type":"bytes32"},{"internalType":"uint256","name":"_synthAmount","type":"uint256"}],"name":"destIssue","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_synthKey","type":"bytes32"},{"internalType":"uint256","name":"_synthAmount","type":"uint256"},{"internalType":"bytes32","name":"_bridgeName","type":"bytes32"},{"internalType":"uint16","name":"_destChainId","type":"uint16"}],"name":"getSendBridgeSynthGasFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_collateralKey","type":"bytes32"},{"internalType":"bytes32","name":"_bridgeName","type":"bytes32"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"bool","name":"_isSelf","type":"bool"}],"name":"getSendLiquidateGasFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"uint256","name":"_synthToMint","type":"uint256"},{"internalType":"bytes32","name":"_bridgeName","type":"bytes32"},{"internalType":"uint16","name":"_destChainId","type":"uint16"},{"internalType":"bool","name":"_issueMax","type":"bool"}],"name":"getSendMintGasFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32[]","name":"currencyKeys","type":"bytes32[]"}],"name":"getSynths","outputs":[{"internalType":"contract ISynth[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isResolverCached","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_issuer","type":"address"},{"internalType":"bytes32","name":"_collateralKey","type":"bytes32"},{"internalType":"uint256","name":"_collateralAmount","type":"uint256"},{"internalType":"uint256","name":"_cRatio","type":"uint256"}],"name":"issuableSynthExpected","outputs":[{"internalType":"uint256","name":"maxIssuable","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"issuanceRatio","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"uint256","name":"destChainId","type":"uint256"}],"name":"issueMaxSynths","outputs":[{"internalType":"uint256","name":"synthAmount","type":"uint256"},{"internalType":"uint256","name":"debtShare","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"destChainId","type":"uint256"}],"name":"issueSynths","outputs":[{"internalType":"uint256","name":"synthAmount","type":"uint256"},{"internalType":"uint256","name":"debtShare","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"lastDebtRatio","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"lastIssueEvent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"bytes32","name":"_collateralKey","type":"bytes32"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"bool","name":"isSelfLiquidation","type":"bool"}],"name":"liquidateAccount","outputs":[{"internalType":"uint256","name":"totalRedeemed","type":"uint256"},{"internalType":"uint256","name":"amountToLiquidate","type":"uint256"},{"internalType":"uint256","name":"sharesToRemove","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_collateralKey","type":"bytes32"},{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"bool","name":"_isSelfLiquidation","type":"bool"}],"name":"liquidateAmount","outputs":[{"internalType":"uint256","name":"totalRedeemed","type":"uint256"},{"internalType":"uint256","name":"amountToLiquidate","type":"uint256"},{"internalType":"bool","name":"removeFlag","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_issuer","type":"address"}],"name":"maxIssuableSynths","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minimumStakeTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"nominateNewOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"nominatedOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rebuildCache","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_issuer","type":"address"}],"name":"remainingIssuableSynths","outputs":[{"internalType":"uint256","name":"maxIssuable","type":"uint256"},{"internalType":"uint256","name":"alreadyIssued","type":"uint256"},{"internalType":"uint256","name":"totalSystemDebt","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"removeSynth","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"resolver","outputs":[{"internalType":"contract AddressResolver","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"resolverAddressesRequired","outputs":[{"internalType":"bytes32[]","name":"addresses","type":"bytes32[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint128","name":"periodId","type":"uint128"}],"name":"setCurrentPeriodId","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"ratio","type":"uint256"}],"name":"setLastDebtRatio","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"bytes32","name":"_synthKey","type":"bytes32"},{"internalType":"uint256","name":"_synthAmount","type":"uint256"}],"name":"synthIssueFromSynthrSwap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"synths","outputs":[{"internalType":"contract ISynth","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"synthsByAddress","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"currencyKey","type":"bytes32"}],"name":"totalIssuedSynths","outputs":[{"internalType":"uint256","name":"totalIssued","type":"uint256"}],"stateMutability":"view","type":"function"}]

BASIC_TOKEN_ABI = [ { "constant": True, "inputs": [], "name": "name", "outputs": [ { "name": "", "type": "string" } ], "payable": False, "stateMutability": "view", "type": "function" }, { "constant": True, "inputs": [], "name": "symbol", "outputs": [ { "name": "", "type": "string" } ], "payable": False, "stateMutability": "view", "type": "function" }, { "constant": True, "inputs": [], "name": "decimals", "outputs": [ { "name": "", "type": "uint8" } ], "payable": False, "stateMutability": "view", "type": "function" }, { "constant": True, "inputs": [ { "name": "", "type": "address" } ], "name": "balanceOf", "outputs": [ { "name": "", "type": "uint256" } ], "payable": False, "stateMutability": "view", "type": "function" }, { "constant": True, "inputs": [ { "name": "", "type": "address" }, { "name": "", "type": "address" } ], "name": "allowance", "outputs": [ { "name": "", "type": "uint256" } ], "payable": False, "stateMutability": "view", "type": "function" }, { "inputs": [ { "name": "_spender", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "approve", "outputs": [ { "name": "", "type": "bool" } ], "payable": False, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "name": "_to", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "transfer", "outputs": [ { "name": "", "type": "bool" } ], "payable": False, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "name": "_from", "type": "address" }, { "name": "_to", "type": "address" }, { "name": "_value", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "name": "", "type": "bool" } ], "payable": False, "stateMutability": "nonpayable", "type": "function" }, { "anonymous": False, "inputs": [ { "indexed": True, "name": "_from", "type": "address" }, { "indexed": True, "name": "_to", "type": "address" }, { "indexed": False, "name": "_value", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "anonymous": False, "inputs": [ { "indexed": True, "name": "_owner", "type": "address" }, { "indexed": True, "name": "_spender", "type": "address" }, { "indexed": False, "name": "_value", "type": "uint256" } ], "name": "Approval", "type": "event" }]