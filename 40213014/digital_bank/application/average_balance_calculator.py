from typing import List
from digital_bank.domain.models import Transaction, TransactionType


class AverageBalanceCalculator:
    def calculate_average_balance(self, opening_balance: float, transactions: List[Transaction]) -> float:
        if not transactions:
            return opening_balance

        running_balance = opening_balance
        balances = []

        for transaction in sorted(transactions, key=lambda t: t.transaction_date):
            if transaction.transaction_type == TransactionType.DEPOSIT:
                running_balance += transaction.amount
            else:
                running_balance -= transaction.amount
            balances.append(running_balance)

        return sum(balances) / len(balances)
