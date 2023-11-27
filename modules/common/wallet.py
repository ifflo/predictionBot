from web3 import Web3


def check_balance(wallet_address, web3_instance):
    try:
        balance = web3_instance.eth.get_balance(wallet_address)
        # Convert Wei to Ether (or relevant cryptocurrency unit)
        return Web3.fromWei(balance, 'ether')
    except Exception as e:
        print(f"Error checking wallet balance: {e}")
        return None

# Additional wallet interaction functions can be added here, such as sending transactions.
