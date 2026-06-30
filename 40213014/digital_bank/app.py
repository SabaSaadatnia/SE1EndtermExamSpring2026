from datetime import date

from digital_bank.application.average_balance_calculator import AverageBalanceCalculator
from digital_bank.application.loan_facade import LoanFacade
from digital_bank.application.loan_service import LoanApplicationService, LoanEligibilityService
from digital_bank.application.loan_strategy import AverageBalanceLoanStrategy
from digital_bank.domain.models import Account, Customer, Transaction, TransactionType
from digital_bank.infrastructure.repositories import (
    AccountRepository,
    CustomerRepository,
    LoanApplicationRepository,
    TransactionRepository,
)


def build_demo_facade() -> LoanFacade:
    customer_repo = CustomerRepository()
    account_repo = AccountRepository()
    transaction_repo = TransactionRepository()
    application_repo = LoanApplicationRepository()

    customer_repo.save(Customer(1, "Ali Ahmadi", "1234567890", "09120000000"))
    account_repo.save(Account(1, 1, "100-200-300", 3_000_000, date(2026, 1, 1)))

    transaction_repo.save(Transaction(1, 1, 2_000_000, TransactionType.DEPOSIT, date(2026, 1, 5)))
    transaction_repo.save(Transaction(2, 1, 500_000, TransactionType.WITHDRAWAL, date(2026, 1, 10)))

    eligibility_service = LoanEligibilityService(
        account_repository=account_repo,
        transaction_repository=transaction_repo,
        calculator=AverageBalanceCalculator(),
        strategy=AverageBalanceLoanStrategy(),
    )

    application_service = LoanApplicationService(eligibility_service, application_repo)
    return LoanFacade(application_service)


if __name__ == "__main__":
    facade = build_demo_facade()
    result = facade.apply_for_loan(customer_id=1, account_id=1, amount=4_000_000)
    print(result)
