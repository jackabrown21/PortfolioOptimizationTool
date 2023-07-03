from data_gathering import get_price_data
from data_processing import calculate_returns, calculate_mean_and_covariance
from portfolio_optimizer import optimize_portfolio
from data_visualization import plot_weights

def main():
    while True:
        try:
            tickers = input("Enter the tickers of the stocks, separated by commas (e.g., AAPL,GOOG,MSFT): ").split(',')
            start_date = input("Enter the start date for the price data in YYYY-MM-DD format (e.g., 2020-01-01): ")
            end_date = input("Enter the end date for the price data in YYYY-MM-DD format (e.g., 2020-12-31): ")
            data = get_price_data(tickers, start_date, end_date)
            if data.empty:
                print("Unable to get data, please enter the details again.")
                continue
            returns = calculate_returns(data)
            mean_returns, covariance_matrix = calculate_mean_and_covariance(returns)
            target_return = float(input("Enter the target annual return as a decimal (e.g., for a 10% return, enter 0.10): "))
            if target_return <= 0:
                print("Target return must be positive. Please enter again.")
                continue
            target_return = (1 + target_return)**(1/252) - 1
            weights = optimize_portfolio(mean_returns.to_numpy(), covariance_matrix.to_numpy(), target_return)
            if weights is None:
                print("Unable to optimize portfolio with the given target return. Please enter again.")
                continue
            for ticker, weight in zip(tickers, weights):
                weight = max(0, weight)
                print(f"{ticker}: {weight}")
            plot_weights(tickers, weights)
            break
        except Exception as e:
            print("An error occurred: ", str(e))
            print("Please enter the details again.")
if __name__ == "__main__":
    main()
