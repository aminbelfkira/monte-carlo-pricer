import numpy as np
from simu.simulate_path import simulate_paths


def price_vanilla(option_type, k, r, T, path):
    if option_type == "call":
        return np.maximum((path[-1] - k) * np.exp(-r * T), 0)
    elif option_type == "put":
        return np.maximum((k - path[-1]) * np.exp(-r * T), 0)


def price(
    option_type,
    k,
    r,
    T,
    paths=None,
    S0=None,
    sigma=None,
    q=None,
    N=None,
    n_paths=None,
):
    if paths is None:
        if None in [S0, sigma, q, N, n_paths]:
            raise ValueError(
                "Les paramètres de simulation sont requis si paths n'est pas fourni."
            )
        paths = simulate_paths(S0, r, sigma, T, N, q, n_paths)

    prices = [price_vanilla(option_type, k, r, T, path) for path in paths]

    return np.mean(prices), prices, paths
