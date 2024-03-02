# main.py
import time
from web3 import Web3
from config import (WEB3_PROVIDER_URL, PANCAKESWAP_PREDICTION_BNB_ADDRESS,
                    PANCAKESWAP_PREDICTION_CAKE_ADDRESS, PANCAKESWAP_PREDICTION_CHOICE,
                    DOGEBETS_ADDRESS, PLATFORM_CHOICE, BET_AMOUNT, MIN_PROFIT)
from modules.platforms.pancakeswap import PancakeSwap
from modules.platforms.dogebets import Dogebets
from modules.prediction import make_prediction  # Assuming this function exists and is implemented properly
from modules.common.wallet import get_wallet_balance, send_transaction  # Adjust based on actual wallet handling


def main():
    web3_instance = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))

    # Initialize the chosen platform contract instance
    if PLATFORM_CHOICE == 'PancakeSwap':
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
            current_round = platform.get_round_details(current_epoch)
            print("Round Details:", current_round)

            # Example of custom betting logic
            prediction = make_prediction(current_round, 0)  # Custom function based on prediction algorithm
            if prediction and get_wallet_balance('', web3_instance) >= BET_AMOUNT:
                tx_hash = platform.place_bet(prediction, BET_AMOUNT)
                print(f"Placed a {prediction} bet for epoch {current_epoch} with transaction hash {tx_hash}")

            # Example of claiming rewards logic
            if platform.can_claim(current_epoch):
                claim_tx_hash = platform.claim_rewards(current_epoch)
                print(f"Claimed rewards for epoch {current_epoch} with transaction hash {claim_tx_hash}")

            # Implement your logic for reinvestment, withdrawal, or other strategies
            # For example, check if the profit exceeds a certain threshold before reinvesting or withdrawing

            time.sleep(60)  # Wait for 60 seconds before the next check
        except KeyboardInterrupt:
            print("Exiting...")
            break
        except Exception as e:
            print(f"Error occurred: {e}")
            # Implement logging or error handling as needed
            time.sleep(60)  # Wait before retrying in case of an error


if __name__ == "__main__":
    main()