# main.py
import time
from web3 import Web3
from config import (WEB3_PROVIDER_URL, PANCAKESWAP_PREDICTION_BNB_ADDRESS,
                    PANCAKESWAP_PREDICTION_CAKE_ADDRESS, PANCAKESWAP_PREDICTION_CHOICE,
                    DOGEBETS_ADDRESS)
from modules.platforms.pancakeswap import PancakeSwap
from modules.platforms.dogebets import Dogebets


def main():
    web3_instance = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))

    # Select the appropriate PancakeSwap contract address based on the choice in config.py
    pancakeswap_address = (PANCAKESWAP_PREDICTION_BNB_ADDRESS if PANCAKESWAP_PREDICTION_CHOICE == 'BNB'
                           else PANCAKESWAP_PREDICTION_CAKE_ADDRESS)

    # PancakeSwap instance for the chosen contract
    pancakeswap = PancakeSwap(web3_instance, pancakeswap_address, 'pancakeswap_prediction_abi.json')

    # Dogebets instance
    dogebets = Dogebets(web3_instance, DOGEBETS_ADDRESS, 'dogebets_abi.json')

    while True:
        try:
            current_epoch_pancakeswap = pancakeswap.get_current_epoch()
            current_epoch_dogebets = dogebets.get_current_epoch()

            # Example usage of PancakeSwap and Dogebets classes
            current_round_pancake = pancakeswap.get_round_details(current_epoch_pancakeswap)
            print("PancakeSwap Round Details:", current_round_pancake)

            current_round_dogebet = dogebets.get_round_details(current_epoch_dogebets)
            print("Dogebets Round Details:", current_round_dogebet)

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
