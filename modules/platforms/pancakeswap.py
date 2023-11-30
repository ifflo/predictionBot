# pancakeswap.py
from modules.common.prediction_platform import PredictionPlatform
from config import (PANCAKESWAP_PREDICTION_BNB_ADDRESS, PANCAKESWAP_PREDICTION_CAKE_ADDRESS,
                    PANCAKESWAP_PREDICTION_CHOICE)


class PancakeSwap(PredictionPlatform):
    def __init__(self, web3_instance, contract_address, abi_file):
        super().__init__(web3_instance, contract_address, abi_file)

    def get_round_details(self, epoch):
        """
        Fetches details about a specific round in PancakeSwap prediction.

        :param epoch: The epoch (round number) to get details for.
        :return: The round details.
        """
        return self.contract.functions.rounds(epoch).call()

    # Add more PancakeSwap-specific methods if needed
