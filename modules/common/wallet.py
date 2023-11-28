# wallet.py
from web3 import Web3


def get_wallet_balance(address, web3_instance):
    """
    Retrieves the balance of a given wallet address.

    :param address: The wallet address to check.
    :param web3_instance: An instance of Web3.
    :return: The balance of the address in Ether (or the native cryptocurrency).
    """
    try:
        balance_wei = web3_instance.eth.get_balance(address)
        return web3_instance.fromWei(balance_wei, 'ether')
    except Exception as e:
        print(f"Error fetching wallet balance: {e}")
        return None


def send_transaction(from_address, to_address, amount, web3_instance, private_key):
    """
    Sends a transaction from one address to another.

    :param from_address: The sending wallet address.
    :param to_address: The receiving wallet address.
    :param amount: The amount to send.
    :param web3_instance: An instance of Web3.
    :param private_key: The private key of the sending address.
    :return: Transaction hash if successful, None otherwise.
    """
    try:
        nonce = web3_instance.eth.get_transaction_count(from_address)
        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': web3_instance.toWei(amount, 'ether'),
            'gas': 21000,
            'gasPrice': web3_instance.eth.gas_price
        }
        signed_tx = web3_instance.eth.account.sign_transaction(tx, private_key)
        tx_hash = web3_instance.eth.send_raw_transaction(signed_tx.rawTransaction)
        return web3_instance.toHex(tx_hash)
    except Exception as e:
        print(f"Error sending transaction: {e}")
        return None
