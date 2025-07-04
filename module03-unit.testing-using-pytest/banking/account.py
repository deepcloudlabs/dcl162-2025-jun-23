from enum import Enum


class InsufficientBalanceException(Exception):
    def __init__(self, message, deficit):
        super().__init__()
        self.message = message
        self.deficit = deficit


class AccountStatus(Enum):
    ACTIVE = 100
    CLOSED = 200
    BLOCKED = 300


class Account:
    def __init__(self, iban, balance=5_000, status=AccountStatus.ACTIVE):
        # attributes/state/data: iban, balance
        self.__iban = iban
        # constraint: self.balance must be always positive or zero
        self._balance = balance
        self.__status = status

    def deposit(self, amount):
        # business rule
        if self.__status != AccountStatus.ACTIVE:
            raise ValueError('Account is not active')
        # validation rule
        if amount <= 0.0:
            raise ValueError('Amount must be positive')
        self._balance = self._balance + amount
        return self._balance

    # business method
    def withdraw(self, amount):
        # business rule
        if self.__status != AccountStatus.ACTIVE:
            raise ValueError('Account is not active')
        # validation rule
        if amount <= 0.0:
            raise ValueError('Amount must be positive')
        # business rule
        if amount > self._balance:
            deficit = amount - self._balance
            # business exception
            raise InsufficientBalanceException("Your balance does not cover your expenses", deficit)
        self._balance = self._balance - amount
        return self._balance

    @property
    def balance(self):
        return self._balance

    @property
    def iban(self):
        return self.__iban

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if status is None:
            raise ValueError('Status cannot be None')
        if status not in [AccountStatus.ACTIVE, AccountStatus.CLOSED, AccountStatus.BLOCKED]:
            raise ValueError('Status must be either "Active", "Closed", "Blocked"')
        self.__status = status

    def __str__(self):
        return f"Account: iban: {self.__iban}, balance: {self._balance}, status: {self.__status}"


"""
CheckingAccount: sub class,derived class
Account        : super class, base class
"""


class CheckingAccount(Account):
    def __init__(self, iban, balance=5_000, status=AccountStatus.ACTIVE, overdraft_amount=1_000):
        super().__init__(iban, balance, status)
        self.__overdraftAmount = overdraft_amount

    # overriding
    def withdraw(self, amount):
        if self.__status != AccountStatus.ACTIVE:
            raise ValueError('Account is not active')
        # validation rule
        if amount <= 0.0:
            raise ValueError('Amount must be positive')
        # business rule
        if amount > (self._balance + self.__overdraftAmount):
            deficit = amount - self._balance - self.__overdraftAmount
            # business exception
            raise InsufficientBalanceException("Your balance does not cover your expenses", deficit)
        self._balance = self._balance - amount
        return self._balance

    @property
    def overdraft_balance(self):
        return self.__overdraftAmount

    @overdraft_balance.setter
    def overdraft_balance(self, overdraft_amount):
        if overdraft_amount <= 0.0:
            raise ValueError('Overdraft amount must be positive')
        self.__overdraftAmount = overdraft_amount

    def __str__(self):
        return f"CheckingAccount: iban: {self.iban}, balance: {self.balance}, status: {self.status}, overdraftAmount: {self.__overdraftAmount}"