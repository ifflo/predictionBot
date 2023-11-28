from config import DOGEBETS_CONTRACT_ADDRESS
from utils.abi_utils import load_abi_from_file
from utils.log_utils import setup_logger
from modules import round_monitor

logger = setup_logger('dogebets_logger', 'dogebets.log')

# dogebets_round_info = get_round_info(dogebets_contract, 'getLatestRoundInfo')


def get_contract(web3_instance):
    abi = load_abi_from_file('dogebets_abi.json')
    if abi is None:
        raise ValueError("Failed to load Dogebets ABI")

    return web3_instance.eth.contract(address=DOGEBETS_CONTRACT_ADDRESS, abi=abi)


def get_round_info(web3_instance):
    contract = get_contract(web3_instance)
    # Replace 'getLatestRoundInfo' with the actual function name in the Dogebets contract
    return round_monitor.get_round_info(contract, 'getLatestRoundInfo')

# Additional Dogebets-specific functionalities can be added as needed
