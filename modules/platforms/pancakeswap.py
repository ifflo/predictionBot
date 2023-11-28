from web3 import Web3
from config import PANCAKESWAP_CONTRACT_ADDRESS
from utils.abi_utils import load_abi_from_file
from utils.log_utils import setup_logger
from modules import round_monitor

logger = setup_logger('pancakeswap_logger', 'pancakeswap.log')

# pancakeswap_round_info = get_round_info(pancakeswap_contract, 'getCurrentRoundInfo')


def get_contract(web3_instance):
    abi = load_abi_from_file('pancakeswap_abi.json')
    if abi is None:
        raise ValueError("Failed to load PancakeSwap ABI")
    return web3_instance.eth.contract(address=PANCAKESWAP_CONTRACT_ADDRESS, abi=abi)


def get_round_info(web3_instance):
    contract = get_contract(web3_instance)
    # Replace 'getCurrentRoundInfo' with the actual function name in the PancakeSwap contract
    return round_monitor.get_round_info(contract, 'getCurrentRoundInfo')

# You can add more functions specific to PancakeSwap's operations
