from modules.common.prediction_platform import PredictionPlatform

class Dogebets(PredictionPlatform):
    def get_current_epoch(self):
        return self.contract.functions.currentEpoch().call()

    def place_bet(self, prediction, amount, from_address):
        if prediction == 'bull':
            return self.contract.functions.user_BetBull(self.get_current_epoch()).transact({'from': from_address, 'value': amount})
        elif prediction == 'bear':
            return self.contract.functions.user_BetBear(self.get_current_epoch()).transact({'from': from_address, 'value': amount})

    def can_claim(self, epoch):
        user_address = self.web3.eth.defaultAccount  # Replace with actual user address
        return self.contract.functions.Claimable(epoch, user_address).call()

    def claim_rewards(self, epoch, from_address):
        return self.contract.functions.user_Claim([epoch]).transact({'from': from_address})

    def get_round_details(self, epoch):
        # Implement based on how Dogebets contract stores round details
        return self.contract.functions.rounds(epoch).call()
