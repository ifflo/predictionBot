# dogebets.py
from modules.common.prediction_platform import PredictionPlatform


class Dogebets(PredictionPlatform):
    def __init__(self, web3_instance, contract_address, abi_file):
        super().__init__(web3_instance, contract_address, abi_file)

    def get_round_details(self, epoch):
        """
        Fetches details about a specific round in PancakeSwap prediction.

        :param epoch: The epoch (round number) to get details for.
        :return: The round details.
        """
        return self.contract.functions.Rounds(epoch).call()

    # Add more Dogebets-specific methods if needed
