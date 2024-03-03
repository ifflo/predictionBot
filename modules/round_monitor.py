from datetime import datetime
import time
from utils.log_utils import setup_logger

logger = setup_logger('round_monitor_logger', 'round_monitor.log')

def get_round_info(platform):
    """
    Fetches round information using the provided platform instance.

    :param platform: The instance of the prediction platform (PancakeSwap or Dogebets).
    :return: Round information or None if an error occurs.
    """
    try:
        current_epoch = platform.get_current_epoch()
        round_info = platform.get_round_details(current_epoch)
        logger.info(f"Fetched round info for epoch {current_epoch}: {round_info}")
        return round_info, current_epoch
    except Exception as e:
        logger.error(f"Error fetching round info: {e}")
        return None, None

def is_round_active(round_info):
    """
    Determines if the current round is active based on the round information.

    :param round_info: The information about the round fetched from the platform.
    :return: Boolean indicating if the round is active.
    """
    logger.info(f"Received round_info: {round_info}")
    if round_info:
        # Assuming round_info[0] contains the actual round details dictionary
        # Adjust these indices based on the structure of round_details
        round_details = round_info[0]  # Adjust this based on actual data structure
        now = datetime.now().timestamp()
        if isinstance(round_info, dict):
            start_time = round_details['startTimestamp'] / 1000  # Adjust if timestamps are in milliseconds
            lock_time = round_details['lockTimestamp'] / 1000
            active = start_time <= now <= lock_time
            logger.info(f"Round active: {active} (from {datetime.fromtimestamp(start_time)} to {datetime.fromtimestamp(lock_time)})")
            return active
    else:
        logger.error(f"Unexpected round_info type: {type(round_info)}")
        return False
    return False

def wait_for_next_round(round_info):
    """
    Waits until the next round starts based on the round information.

    :param round_info: The information about the round fetched from the platform.
    """
    if round_info:
        now = datetime.now().timestamp()
        # Assuming round_info should be a dictionary containing 'closeTimestamp'
        # We need to ensure round_info is properly structured as a dictionary
        if isinstance(round_info, dict) and 'closeTimestamp' in round_info:
            # Convert timestamp to seconds if it's in milliseconds
            next_round_start_time = round_info['closeTimestamp'] / 1000
            wait_time = max(next_round_start_time - now, 0)  # Ensure wait_time is not negative
            logger.info(f"Waiting for {wait_time} seconds until the next round starts.")
            time.sleep(wait_time)
        else:
            logger.error("Invalid round_info format.")