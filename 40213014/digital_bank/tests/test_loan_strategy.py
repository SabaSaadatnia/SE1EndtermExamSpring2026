from digital_bank.application.loan_strategy import AverageBalanceLoanStrategy


def test_average_balance_strategy_approves_valid_loan():
    strategy = AverageBalanceLoanStrategy(multiplier=2, minimum_average_balance=1_000_000)

    assert strategy.is_eligible(requested_amount=2_000_000, average_balance=1_500_000)


def test_average_balance_strategy_rejects_large_loan():
    strategy = AverageBalanceLoanStrategy(multiplier=2, minimum_average_balance=1_000_000)

    assert not strategy.is_eligible(requested_amount=4_000_000, average_balance=1_500_000)
