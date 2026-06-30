from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import List, Optional


class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


class LoanApplicationStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class LoanStatus(str, Enum):
    ACTIVE = "active"
    CLOSED = "closed"


@dataclass
class Customer:
    customer_id: int
    full_name: str
    national_id: str
    phone_number: str


@dataclass
class Transaction:
    transaction_id: int
    account_id: int
    amount: float
    transaction_type: TransactionType
    transaction_date: date


@dataclass
class Account:
    account_id: int
    customer_id: int
    account_number: str
    balance: float
    open_date: date
    transactions: List[Transaction] = field(default_factory=list)


@dataclass
class LoanApplication:
    application_id: int
    customer_id: int
    account_id: int
    requested_amount: float
    average_balance: float
    status: LoanApplicationStatus
    request_date: date


@dataclass
class Loan:
    loan_id: int
    application_id: int
    amount: float
    interest_rate: float
    start_date: date
    status: LoanStatus


@dataclass
class Repayment:
    repayment_id: int
    loan_id: int
    amount: float
    due_date: date
    paid_date: Optional[date]
    status: str
