import cvxpy as cp

def optimize_portfolio(mean_returns, covariance_matrix, target_return):
    num_assets = len(mean_returns)
    weights = cp.Variable(num_assets)
    portfolio_return = mean_returns.T @ weights
    portfolio_variance = cp.quad_form(weights, covariance_matrix)
    objective = cp.Minimize(portfolio_variance)
    constraints = [
        portfolio_return >= target_return,
        cp.sum(weights) == 1,
        weights >= 0
    ]
    prob = cp.Problem(objective, constraints)
    prob.solve()
    print(f"Problem status: {prob.status}")
    if prob.status == "optimal":
        print(f"Optimal value: {prob.value}")
    return weights.value if prob.status == "optimal" else None
