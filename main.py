import time
from web3 import Web3
from config import (WEB3_PROVIDER_URL, PANCAKESWAP_PREDICTION_BNB_ADDRESS,
                    PANCAKESWAP_PREDICTION_CAKE_ADDRESS, PANCAKESWAP_PREDICTION_CHOICE,
                    DOGEBETS_ADDRESS, PLATFORM_CHOICE, BET_AMOUNT)
from modules.platforms.pancakeswap import PancakeSwap
from modules.platforms.dogebets import Dogebets
from modules.round_monitor import get_round_info, is_round_active, wait_for_next_round
# Assuming make_prediction, get_wallet_balance, and send_transaction are properly implemented
from modules.prediction import make_prediction
from modules.common.wallet import get_wallet_balance

def main():
    web3_instance = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))

    # Initialize the chosen platform contract instance
    platform = None
    if PLATFORM_CHOICE == 'PancakeSwap':
        pancakeswap_address = (PANCAKESWAP_PREDICTION_BNB_ADDRESS if PANCAKESWAP_PREDICTION_CHOICE == 'BNB'
                               else PANCAKESWAP_PREDICTION_CAKE_ADDRESS)
        platform = PancakeSwap(web3_instance, pancakeswap_address, 'pancakeswap_abi.json')
    elif PLATFORM_CHOICE == 'Dogebets':
        platform = Dogebets(web3_instance, DOGEBETS_ADDRESS, 'dogebets_abi.json')
    else:
        print("Unsupported platform selected")
        return  # Exit if platform is not supported

    while True:
        try:
            # Assuming 'platform' is an instance of PancakeSwap or Dogebets
            round_info, current_epoch = get_round_info(platform)
            if round_info:
                if is_round_active(round_info):
                    # If round is active, execute strategy
                    print(f"Round {current_epoch} is active.")
                    # Implement betting logic here based on the strategy
                else:
                    # If round is not active, wait for the next one
                    print(f"Round {current_epoch} is not active, waiting for the next round.")
                    wait_for_next_round(round_info)
            else:
                print("Failed to fetch round details, will retry.")

            time.sleep(60)  # Wait for 60 seconds before the next check
        except KeyboardInterrupt:
            print("Exiting...")
            break
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(60)  # Wait before retrying in case of an error

if __name__ == "__main__":
    main()
