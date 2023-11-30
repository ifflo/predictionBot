# main.py
import time
from web3 import Web3
from config import (WEB3_PROVIDER_URL, PANCAKESWAP_PREDICTION_BNB_ADDRESS,
                    PANCAKESWAP_PREDICTION_CAKE_ADDRESS, PANCAKESWAP_PREDICTION_CHOICE,
                    DOGEBETS_ADDRESS, PLATFORM_CHOICE)
from modules.platforms.pancakeswap import PancakeSwap
from modules.platforms.dogebets import Dogebets


def main():
    web3_instance = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))

    # Instance for the chosen platform contract
    if PLATFORM_CHOICE == 'PancakeSwap':
        # Select the appropriate PancakeSwap contract address based on the choice in config.py
        pancakeswap_address = (PANCAKESWAP_PREDICTION_BNB_ADDRESS if PANCAKESWAP_PREDICTION_CHOICE == 'BNB'
                               else PANCAKESWAP_PREDICTION_CAKE_ADDRESS)
        platform = PancakeSwap(web3_instance, pancakeswap_address, 'pancakeswap_abi.json')
    elif PLATFORM_CHOICE == 'Dogebets':
        platform = Dogebets(web3_instance, DOGEBETS_ADDRESS, 'dogebets_abi.json')
    else:
        raise ValueError("Unsupported platform selected")

    while True:
        try:
            current_epoch = platform.get_current_epoch()

            # Example usage of PancakeSwap and Dogebets classes
            current_round = platform.get_round_details(current_epoch)
            print("Round Details:", current_round)

            # Additional logic for betting, claiming, etc. can be added here

            time.sleep(60)  # Wait for 60 seconds before the next check
        except KeyboardInterrupt:
            print("Exiting...")
            break
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(60)  # Wait before retrying in case of an error


if __name__ == "__main__":
    main()
