import numpy as np


def next_spot(S, r, sigma, deltaT, q):
    return S * np.exp(
        (r - q - (sigma**2) / 2) * deltaT
        + sigma * np.sqrt(deltaT) * np.random.normal(0, 1)
    )


def simulate_path(S0, r, sigma, T, N, q):
    S = S0
    spots = [S0]
    deltaT = T / N
    for i in range(N):
        S = next_spot(S, r, sigma, deltaT, q)
        spots.append(S)
    return np.array(spots)


def simulate_paths(S0, r, sigma, T, N, q, n_paths):
    return np.array([simulate_path(S0, r, sigma, T, N, q) for _ in range(n_paths)])
