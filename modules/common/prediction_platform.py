# common/prediction_platform.py
from utils.abi_utils import load_abi_from_file
from web3 import Web3


class PredictionPlatform:
    def __init__(self, web3_instance, contract_address, abi_file):
        self.web3 = web3_instance
        self.contract = web3_instance.eth.contract(
            address=web3_instance.to_checksum_address(contract_address),
            abi=load_abi_from_file(abi_file)
        )

    def bet_bear(self, epoch, amount, from_address, private_key):
        """
        Places a bear bet for the specified epoch and amount.

        :param epoch: The epoch (round number) to bet on.
        :param amount: The amount to bet.
        :param from_address: The address placing the bet.
        :param private_key: The private key for signing the transaction.
        :return: Transaction hash.
        """
        # Implement the betBear function
        # ...

    def bet_bull(self, epoch, amount, from_address, private_key):
        """
        Places a bull bet for the specified epoch and amount.

        :param epoch: The epoch (round number) to bet on.
        :param amount: The amount to bet.
        :param from_address: The address placing the bet.
        :param private_key: The private key for signing the transaction.
        :return: Transaction hash.
        """
        # Implement the betBull function
        # ...

    def claim_rewards(self, epochs, from_address, private_key):
        """
        Claims rewards for specified epochs.

        :param epochs: List of epochs to claim rewards for.
        :param from_address: The address claiming the rewards.
        :param private_key: The private key for signing the transaction.
        :return: Transaction hash.
        """
        # Implement the claim function
        # ...

    def get_current_epoch(self):
        """
        Fetches the current epoch number from the prediction contract.
        """
        return self.contract.functions.currentEpoch().call()

    # ... Other shared functions ...

# Add more common functionalities as needed
