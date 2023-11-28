from web3 import Web3
from config import PLATFORM, BSC_HTTP
from modules.common import price, wallet
from modules.platforms import pancakeswap, dogebets
import time
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
        try:
            # Fetch round information using the selected platform module
            round_info = platform_module.get_round_info(web3_instance)
            print(f"{PLATFORM} Round Info:", round_info)

            # Add any additional logic you want to perform based on the round info

            time.sleep(60)  # Wait for 60 seconds before checking again
        except KeyboardInterrupt:
            print("Exiting...")
            break
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(60)  # Wait before retrying in case of an error


if __name__ == "__main__":
    main()
