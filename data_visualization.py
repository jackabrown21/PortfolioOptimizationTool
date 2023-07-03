import matplotlib.pyplot as plt

def plot_weights(tickers, weights):
    plt.figure(figsize=(10, 6))
    plt.bar(tickers, weights)
    plt.xlabel('Selected Stocks')
    plt.ylabel('Portfolio Weights')
    plt.title('Portfolio Weights of Stocks')
    plt.show()