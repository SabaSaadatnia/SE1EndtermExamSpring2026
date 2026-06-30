from datetime import date

from digital_bank.application.average_balance_calculator import AverageBalanceCalculator
from digital_bank.domain.models import Transaction, TransactionType


def test_average_balance_calculator():
    transactions = [
        Transaction(1, 1, 1_000_000, TransactionType.DEPOSIT, date(2026, 1, 1)),
        Transaction(2, 1, 500_000, TransactionType.WITHDRAWAL, date(2026, 1, 2)),
    ]

    calculator = AverageBalanceCalculator()
    result = calculator.calculate_average_balance(2_000_000, transactions)

    assert result == 2_250_000
