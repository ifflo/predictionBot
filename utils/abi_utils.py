import json
from utils.log_utils import setup_logger
from web3 import Web3
from config import PANCAKESWAP_CONTRACT_ADDRESS, DOGEBETS_CONTRACT_ADDRESS


def load_abi_from_file(file_name, abis_dir='abis'):
    try:
        with open(f"{abis_dir}/{file_name}", 'r') as file:
            data = json.load(file)
            # Check if the 'result' key exists and return its value
            if 'result' in data:
                return data['result']
            else:
                print(f"'result' key not found in the ABI file: {file_name}")
                return None
    except FileNotFoundError:
        print(f"ABI file not found: {abis_dir}/{file_name}")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON in ABI file: {abis_dir}/{file_name}")
        return None
