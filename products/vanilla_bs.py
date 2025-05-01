import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def d1(s, k, r, q, sigma, t):
    return (np.log(s / k) + (r - q + sigma**2 / 2) * t) / (sigma * np.sqrt(t))


def d2(s, k, r, q, sigma, t):
    return d1(s, k, r, q, sigma, t) - (sigma * np.sqrt(t))


def price(
    option_type,
    s,
    k,
    r,
    q,
    sigma,
    t,
):
    """
    _summary_

    Args:
        option_type (_type_): call ou put
        s (_type_): prix spot
        k (_type_): prix strike
        r (_type_): taux d'interet domestique
        d (_type_): taux de dividende
        sigma (_type_): volatilité
        t (_type_): maturité en années
    """
    if option_type == "call":
        phi_d1 = norm.cdf(d1(s, k, r, q, sigma, t))
        phi_d2 = norm.cdf(d2(s, k, r, q, sigma, t))
        price = s * np.exp(-q * t) * phi_d1 - k * np.exp(-r * t) * phi_d2
    elif option_type == "put":
        phi_d1 = norm.cdf(-d1(s, k, r, q, sigma, t))
        phi_d2 = norm.cdf(-d2(s, k, r, q, sigma, t))
        price = k * np.exp(-r * t) * phi_d2 - s * np.exp(-q * t) * phi_d1
    else:
        raise ValueError("option type should be call or put")
    return price, None
