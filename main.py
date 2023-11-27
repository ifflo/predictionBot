import sys
from web3 import Web3
from config import PLATFORM
from modules.platforms import pancakeswap, dogebets
from modules.prediction import make_prediction


def main():
    # Create a Web3 instance
    BSC_HTTP = "https://bsc-dataseed.binance.org/"  # Or use an appropriate provider
    web3_instance = Web3(Web3.HTTPProvider(BSC_HTTP))

    # Check if the connection is successful
    if not web3_instance.is_connected():
        print("Failed to connect to Binance Smart Chain")
        return

    # Select the platform module based on configuration
    if PLATFORM == 'PancakeSwap':
        platform_module = pancakeswap
    elif PLATFORM == 'Dogebets':
        platform_module = dogebets
    else:
        sys.exit("Unsupported platform")

    # Call the get_current_price function with the web3_instance
    price = platform_module.get_current_price(web3_instance)
    make_prediction(price)


if __name__ == "__main__":
    main()
