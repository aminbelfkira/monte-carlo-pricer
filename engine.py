def price_product(
    product_type, product_params, market_params, sim_params=None, paths=None
):
    from products import autocall, vanilla_bs, vanilla_mc

    if product_type == "vanilla":

        bs_price, _ = vanilla_bs.price(**product_params, **market_params)

        mc_price, mc_prices, paths = vanilla_mc.price(
            option_type=product_params["option_type"],
            k=product_params["k"],
            r=product_params["r"],
            T=product_params["t"],
            S0=sim_params["S0"],
            sigma=sim_params["sigma"],
            q=sim_params["q"],
            N=sim_params["N"],
            n_paths=sim_params["n_paths"],
        )

        return {"bs": bs_price, "mc": mc_price}, mc_prices, paths

    if product_type == "autocall":
        return autocall.price(**product_params, **market_params)

    else:
        raise ValueError("Produit non reconnu")
