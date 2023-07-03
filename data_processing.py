def calculate_returns(data):
    prices = data['Adj Close']
    returns = prices.pct_change()
    returns = returns.dropna()
    return returns

def calculate_mean_and_covariance(returns):
    mean_returns = returns.mean()
    covariance_matrix = returns.cov()
    return mean_returns, covariance_matrix
    