from typing import Dict, List, Optional
from digital_bank.domain.models import Account, Customer, LoanApplication, Transaction


class CustomerRepository:
    def __init__(self):
        self._customers: Dict[int, Customer] = {}

    def save(self, customer: Customer) -> None:
        self._customers[customer.customer_id] = customer

    def find_by_id(self, customer_id: int) -> Optional[Customer]:
        return self._customers.get(customer_id)


class AccountRepository:
    def __init__(self):
        self._accounts: Dict[int, Account] = {}

    def save(self, account: Account) -> None:
        self._accounts[account.account_id] = account

    def find_by_id(self, account_id: int) -> Optional[Account]:
        return self._accounts.get(account_id)


class TransactionRepository:
    def __init__(self):
        self._transactions: List[Transaction] = []

    def save(self, transaction: Transaction) -> None:
        self._transactions.append(transaction)

    def find_by_account_id(self, account_id: int) -> List[Transaction]:
        return [t for t in self._transactions if t.account_id == account_id]


class LoanApplicationRepository:
    def __init__(self):
        self._applications: Dict[int, LoanApplication] = {}

    def save(self, application: LoanApplication) -> None:
        self._applications[application.application_id] = application

    def find_by_id(self, application_id: int) -> Optional[LoanApplication]:
        return self._applications.get(application_id)
