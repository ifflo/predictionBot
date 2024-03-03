from abc import ABC, abstractmethod
from utils.abi_utils import load_abi_from_file

class PredictionPlatform(ABC):
    def __init__(self, web3_instance, contract_address, abi):
        self.web3 = web3_instance
        self.contract = web3_instance.eth.contract(
            address=web3_instance.to_checksum_address(contract_address),
            abi=load_abi_from_file(abi)
        )
    
    @abstractmethod
    def get_current_epoch(self):
        pass

    @abstractmethod
    def place_bet(self, prediction, amount, from_address):
        pass

    @abstractmethod
    def can_claim(self, epoch):
        pass

    @abstractmethod
    def claim_rewards(self, epoch, from_address):
        pass

    @abstractmethod
    def get_round_details(self, epoch):
        pass