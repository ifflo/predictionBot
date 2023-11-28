from datetime import datetime
import time
from utils.log_utils import setup_logger

logger = setup_logger('round_monitor_logger', 'round_monitor.log')


def get_round_info(contract, round_info_function_name):
    """
    Fetches round information from a given smart contract.

    :param contract: The smart contract instance.
    :param round_info_function_name: The name of the function in the contract to fetch round info.
    :return: Round information or None if an error occurs.
    """
    try:
        round_info_func = getattr(contract.functions, round_info_function_name)
        round_info = round_info_func().call()
        return round_info
    except Exception as e:
        print(f"Error fetching round info: {e}")
        return None


def is_round_active(round_info):
    """
    Determines if the current round is active.
    """
    now = datetime.now()
    # Implement logic based on round_info structure
    # Example:
    # start_time = round_info['start_time']
    # end_time = round_info['end_time']
    # active = start_time <= now <= end_time
    # print(f"Round active: {active} (from {start_time} to {end_time})")
    # return active
    pass


def wait_for_next_round(round_info):
    """
    Waits until the next round starts.
    """
    logger.info("Waiting for the next round to start...")
    # Implement logic to wait for the next round
    # Example:
    # next_round_start_time = round_info['next_round_start_time']
    # current_time = datetime.now()
    # wait_time = (next_round_start_time - current_time).total_seconds()
    # print(f"Waiting for {wait_time} seconds until the next round starts.")
    # time.sleep(wait_time)
    pass
