from web3 import Web3
from config import PLATFORM, BSC_HTTP
from modules.common import price, wallet
from modules.platforms import pancakeswap, dogebets
from modules.prediction import make_prediction
from modules.round_monitor import get_round_info, is_round_active, wait_for_next_round
from utils.log_utils import setup_logger


def main():
    # Create a Web3 instance
    web3_instance = Web3(Web3.HTTPProvider(BSC_HTTP))

    # Check if the connection is successful
    if not web3_instance.is_connected():
        print("Failed to connect to Binance Smart Chain")
        return

    # Select the platform module based on configuration
    platform_module = None
    if PLATFORM == 'PancakeSwap':
        platform_module = pancakeswap
    elif PLATFORM == 'Dogebets':
        platform_module = dogebets
    else:
        print("Unsupported platform")
        return

    # Main loop
    while True:
        contract = platform_module.get_contract(web3_instance)

        round_info = get_round_info(contract)
        if is_round_active(round_info):
            current_price = platform_module.get_current_price(web3_instance)
            prediction = make_prediction(current_price)
            # Implement the logic for placing a bet based on the prediction
            pass
        else:
            wait_for_next_round(round_info)

        # Additional logic can be added here
        # ...


if __name__ == "__main__":
    main()
