import numpy as np
from simu.simulate_path import simulate_paths


def price_autocall(
    path,
    notional,
    coupon_rate,
    coupon_barrier,
    autocall_barrier,
    protection_barrier,
    obs_dates,
    r,
    T,
    N,
):
    price = 0
    autocall = False
    delta_t = T / N
    for t in obs_dates:
        if path[t] >= autocall_barrier:
            price += notional * (1 + coupon_rate) * np.exp(-r * t * delta_t)
            autocall = True
            break
        elif path[t] >= coupon_barrier:
            price += notional * coupon_rate * np.exp(-r * t * delta_t)
    if not autocall:
        if path[obs_dates[-1]] >= protection_barrier:
            price += notional * np.exp(-r * T)
        else:
            price += (
                notional * (path[obs_dates[-1]] / path[obs_dates[0]]) * np.exp(-r * T)
            )
    return price


def price(
    notional,
    coupon_rate,
    coupon_barrier,
    autocall_barrier,
    protection_barrier,
    obs_dates,
    r,
    T,
    N,
    S0,
    sigma,
    q,
    n_paths,
    paths=None,
):
    if paths is None:
        paths = simulate_paths(S0, r, sigma, T, N, q, n_paths)
    prices = [
        price_autocall(
            path,
            notional,
            coupon_rate,
            coupon_barrier,
            autocall_barrier,
            protection_barrier,
            obs_dates,
            r,
            T,
            N,
        )
        for path in paths
    ]
    return np.mean(prices), prices
