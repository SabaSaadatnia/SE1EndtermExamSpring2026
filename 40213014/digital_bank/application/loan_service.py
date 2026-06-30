from datetime import date
from itertools import count

from digital_bank.application.average_balance_calculator import AverageBalanceCalculator
from digital_bank.application.loan_strategy import LoanStrategy
from digital_bank.domain.models import LoanApplication, LoanApplicationStatus
from digital_bank.infrastructure.repositories import (
    AccountRepository,
    TransactionRepository,
    LoanApplicationRepository,
)


class LoanEligibilityService:
    def __init__(
        self,
        account_repository: AccountRepository,
        transaction_repository: TransactionRepository,
        calculator: AverageBalanceCalculator,
        strategy: LoanStrategy,
    ):
        self.account_repository = account_repository
        self.transaction_repository = transaction_repository
        self.calculator = calculator
        self.strategy = strategy

    def check_eligibility(self, account_id: int, requested_amount: float) -> tuple[bool, float]:
        account = self.account_repository.find_by_id(account_id)
        if account is None:
            raise ValueError("Account not found")

        transactions = self.transaction_repository.find_by_account_id(account_id)
        average_balance = self.calculator.calculate_average_balance(account.balance, transactions)
        eligible = self.strategy.is_eligible(requested_amount, average_balance)
        return eligible, average_balance


class LoanApplicationService:
    _ids = count(1)

    def __init__(
        self,
        eligibility_service: LoanEligibilityService,
        application_repository: LoanApplicationRepository,
    ):
        self.eligibility_service = eligibility_service
        self.application_repository = application_repository

    def create_application(self, customer_id: int, account_id: int, requested_amount: float) -> LoanApplication:
        eligible, average_balance = self.eligibility_service.check_eligibility(account_id, requested_amount)

        application = LoanApplication(
            application_id=next(self._ids),
            customer_id=customer_id,
            account_id=account_id,
            requested_amount=requested_amount,
            average_balance=average_balance,
            status=LoanApplicationStatus.APPROVED if eligible else LoanApplicationStatus.REJECTED,
            request_date=date.today(),
        )

        self.application_repository.save(application)
        return application
