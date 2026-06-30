from abc import ABC, abstractmethod


class LoanStrategy(ABC):
    @abstractmethod
    def calculate_limit(self, average_balance: float) -> float:
        pass

    @abstractmethod
    def is_eligible(self, requested_amount: float, average_balance: float) -> bool:
        pass


class AverageBalanceLoanStrategy(LoanStrategy):
    def __init__(self, multiplier: float = 2.0, minimum_average_balance: float = 1_000_000):
        self.multiplier = multiplier
        self.minimum_average_balance = minimum_average_balance

    def calculate_limit(self, average_balance: float) -> float:
        if average_balance < self.minimum_average_balance:
            return 0
        return average_balance * self.multiplier

    def is_eligible(self, requested_amount: float, average_balance: float) -> bool:
        return requested_amount <= self.calculate_limit(average_balance)
