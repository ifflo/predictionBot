# web3_utils.py

from web3 import Web3

def init_web3(web3_provider_url):
    """
    Initialize a Web3 instance with the given provider URL.
    :param web3_provider_url: URL of the Web3 provider
    :return: Web3 instance
    """
    return Web3(Web3.HTTPProvider(web3_provider_url))

def check_connection(w3):
    """
    Check if the connection to the blockchain is successful.
    :param w3: Web3 instance
    :return: True if connected, False otherwise
    """
    return w3.isConnected()

def get_current_block_number(w3):
    """
    Get the current block number of the blockchain.
    :param w3: Web3 instance
    :return: Current block number
    """
    return w3.eth.blockNumber

def get_transaction_receipt(w3, tx_hash):
    """
    Retrieve the receipt of a transaction by its hash.
    :param w3: Web3 instance
    :param tx_hash: Transaction hash
    :return: Transaction receipt object
    """
    return w3.eth.getTransactionReceipt(tx_hash)
