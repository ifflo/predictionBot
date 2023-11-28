from utils.log_utils import setup_logger

logger = setup_logger('prediction_logger', 'prediction.log')


def make_prediction(current_price):
    # Implement your prediction logic here
    # This could be based on historical data, machine learning models, etc.
    # Ensure to place bets within the rounds' time limits
    logger.info(current_price)
    pass
