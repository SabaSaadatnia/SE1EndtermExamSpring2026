from digital_bank.application.loan_service import LoanApplicationService
from digital_bank.domain.models import LoanApplication


class LoanFacade:
    def __init__(self, loan_application_service: LoanApplicationService):
        self.loan_application_service = loan_application_service

    def apply_for_loan(self, customer_id: int, account_id: int, amount: float) -> LoanApplication:
        return self.loan_application_service.create_application(customer_id, account_id, amount)
