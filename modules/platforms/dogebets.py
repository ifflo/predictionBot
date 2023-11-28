from config import DOGEBETS_CONTRACT_ADDRESS
from utils.abi_utils import load_abi_from_file
from utils.log_utils import setup_logger

logger = setup_logger('dogebets_logger', 'dogebets.log')


def get_contract(web3_instance):
    abi = load_abi_from_file('dogebets_abi.json')
    if abi is None:
        raise ValueError("Failed to load Dogebets ABI")

    return web3_instance.eth.contract(address=DOGEBETS_CONTRACT_ADDRESS, abi=abi)


def get_current_price(web3_instance):
    contract = get_contract(web3_instance)
    # Implement the specific interaction with Dogebets contract here
    pass

# Additional Dogebets-specific functionalities can be added as needed
