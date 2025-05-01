from engine import price_product
import matplotlib.pyplot as plt

product_type = "vanilla"

if product_type == "vanilla":
    product_params = {
        "option_type": "call",
        "s": 100,
        "k": 100,
        "r": 0.05,
        "q": 0.0,
        "sigma": 0.2,
        "t": 1,
    }

    sim_params = {
        "S0": 100,
        "sigma": 0.2,
        "q": 0.0,
        "N": 252,
        "n_paths": 2,
        "T": 1,
    }

    market_params = {}

    price_dict, all_prices, paths = price_product(
        product_type, product_params, market_params, sim_params
    )

    print(f"\n▶ Prix Black-Scholes : {price_dict['bs']:.4f} €")
    print(f"▶ Prix Monte Carlo   : {price_dict['mc']:.4f} €")
    

    plt.figure(figsize=(20,10))
    for path in paths:
        plt.plot(path)
    plt.title("Simulation de trajectoires de prix")
    plt.xlabel("Temps (jours)")
    plt.ylabel("Prix")
    plt.grid(True)
    plt.show()

    error = abs(price_dict["mc"] - price_dict["bs"]) / price_dict["bs"] * 100
    print(f"▶ Erreur relative Monte Carlo vs BS : {error:.2f} %")

elif product_type == "autocall":
    product_params = {
        "notional": 1000,
        "coupon_rate": 0.01,
        "coupon_barrier": 70,
        "autocall_barrier": 100,
        "protection_barrier": 60,
        "obs_dates": list(range(21, 253, 21)),
    }

    sim_params = {
        "T": 1,
        "N": 252,
        "n_paths": 10_000,
    }

    market_params = {
        "S0": 100,
        "sigma": 0.25,
        "r": 0.015,
        "q": 0.03,
    }

    price, all_prices = price_product(
        product_type, product_params, market_params, sim_params
    )

    print(f"\n▶ Prix estimé du produit [{product_type}] : {price:.2f} €")

# === Affichage histogramme si Monte Carlo ===
if all_prices and isinstance(all_prices, list):
    plt.hist(all_prices, bins=50, color="skyblue", edgecolor="black")
    plt.title(f"Distribution des payoffs du {product_type}")
    plt.xlabel("Payoff actualisé (€)")
    plt.ylabel("Fréquence")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
