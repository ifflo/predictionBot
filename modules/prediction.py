# prediction.py

def make_prediction(price_data, threshold):
    """
    Make a prediction based on price data and a set threshold.
    :param price_data: Historical price data of the cryptocurrency
    :param threshold: Threshold value to decide whether to bet up or down
    :return: 'up' if prediction is above the threshold, 'down' otherwise
    """
    average_price = sum(price_data) / len(price_data)
    return 'up' if average_price > threshold else 'down'
