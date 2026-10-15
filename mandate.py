"""Evaluate candidate portfolios for the Meridian Foundation Reserve mandate."""

# Editable mandate inputs
RESERVE_SIZE = 100.0  # USD millions
QUARTERLY_DISTRIBUTION = 0.75  # USD millions
QUARTERS_TO_COVER = 4
LIQUIDITY_WINDOW = 5  # business days
MINIMUM_LIQUID_SHARE = 90.0  # percent
ISSUER_CONCENTRATION_LIMIT = 8.0  # percent

# Editable holding information
# Each value contains: issuer, days to redeem, reserve eligible, issuer exempt.
HOLDINGS = {
    "Cash": ("none", 0, True, True),
    "Treasury bills": ("U.S. Treasury", 1, True, True),
    "Treasury 10-year note": ("U.S. Treasury", 1, True, True),
    "Global equity index fund": ("diversified fund", 2, False, True),
    "Investment-grade bond fund": ("diversified fund", 3, False, True),
    "Private real estate fund": ("diversified fund", 90, False, True),
    "Acme Corp bonds": ("Acme Corp", 4, False, False),
    "Acme Corp stock": ("Acme Corp", 1, False, False),
}

# Editable portfolio weights (percent)
PORTFOLIOS = {
    "A": {
        "Cash": 2.0,
        "Treasury bills": 2.0,
        "Treasury 10-year note": 10.0,
        "Global equity index fund": 60.0,
        "Investment-grade bond fund": 26.0,
        "Private real estate fund": 0.0,
        "Acme Corp bonds": 0.0,
        "Acme Corp stock": 0.0,
    },
    "B": {
        "Cash": 1.0,
        "Treasury bills": 0.0,
        "Treasury 10-year note": 0.0,
        "Global equity index fund": 55.0,
        "Investment-grade bond fund": 20.0,
        "Private real estate fund": 15.0,
        "Acme Corp bonds": 5.0,
        "Acme Corp stock": 4.0,
    },
    "C": {
        "Cash": 1.0,
        "Treasury bills": 1.0,
        "Treasury 10-year note": 0.0,
        "Global equity index fund": 70.0,
        "Investment-grade bond fund": 20.0,
        "Private real estate fund": 0.0,
        "Acme Corp bonds": 0.0,
        "Acme Corp stock": 8.0,
    },
    "D": {
        "Cash": 100.0,
        "Treasury bills": 0.0,
        "Treasury 10-year note": 0.0,
        "Global equity index fund": 0.0,
        "Investment-grade bond fund": 0.0,
        "Private real estate fund": 0.0,
        "Acme Corp bonds": 0.0,
        "Acme Corp stock": 0.0,
    },
}


def status(condition):
    """Return the required label for a check result."""
    return "pass" if condition else "FAIL"


def evaluate_portfolio(name, weights, reserve_minimum):
    """Calculate and print the five checkable mandate rules."""
    total_weight = sum(weights.values())
    lowest_weight = min(weights.values())

    reserve_weight = sum(
        weight
        for holding, weight in weights.items()
        if HOLDINGS[holding][2]
    )

    liquid_weight = sum(
        weight
        for holding, weight in weights.items()
        if HOLDINGS[holding][1] <= LIQUIDITY_WINDOW
    )

    company_totals = {}
    for holding, weight in weights.items():
        issuer, _, _, issuer_exempt = HOLDINGS[holding]
        if not issuer_exempt:
            company_totals[issuer] = company_totals.get(issuer, 0.0) + weight
    largest_company = max(company_totals.values(), default=0.0)

    checks = [
        total_weight == 100.0,
        lowest_weight >= 0.0,
        reserve_weight >= reserve_minimum,
        liquid_weight >= MINIMUM_LIQUID_SHARE,
        largest_company <= ISSUER_CONCENTRATION_LIMIT,
    ]

    print(f"\nPortfolio {name}:")
    print(f"Weights = {total_weight:.1f} {status(checks[0])}")
    print(f"Lowest weight = {lowest_weight:.1f} {status(checks[1])}")
    print(f"Reserve = {reserve_weight:.1f} {status(checks[2])}")
    print(f"Liquidity = {liquid_weight:.1f} {status(checks[3])}")
    print(f"Largest single company = {largest_company:.1f} {status(checks[4])}")
    print("Calendar-year loss = requires CIO clarification")

    failed_checks = checks.count(False)
    if failed_checks == 0:
        print("Verdict = passes every checkable rule")
    else:
        print(f"Verdict = fails {failed_checks} rule(s)")


def main():
    reserve_minimum = (
        QUARTERS_TO_COVER * QUARTERLY_DISTRIBUTION / RESERVE_SIZE
    ) * 100
    print(f"Reserve minimum = {reserve_minimum:.1f}%")

    for name, weights in PORTFOLIOS.items():
        evaluate_portfolio(name, weights, reserve_minimum)


if __name__ == "__main__":
    main()
