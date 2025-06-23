from enum import Enum


class AccountStatus(Enum):
    ACTIVE = 100
    CLOSED = 200
    BLOCKED = 300


class Account:
    def __init__(self, iban: str, balance: float = 0, status: AccountStatus = AccountStatus.ACTIVE):
        self.__iban = iban
        self.__balance = balance
        self.__status = status

    @property
    def iban(self) -> str:
        return self.__iban

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def status(self) -> AccountStatus:
        return self.__status

    @status.setter
    def status(self, new_status: AccountStatus) -> None:
        self.__status = new_status

    def deposit(self, amount: float) -> bool:
        if self.__status == AccountStatus.CLOSED:
            raise ValueError(
                "deposit is not allowed for closed accounts"
            )
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.__balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        if self.__status == AccountStatus.CLOSED or self.__status == AccountStatus.BLOCKED:
            raise ValueError(
                "deposit is not allowed for closed accounts"
            )
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self.__balance:
            raise ValueError("amount must be less than or equal to balance")
        self.__balance -= amount
        return True

    def __str__(self) -> str:
        return f"Account: {self.__iban}, {self.__balance}, {self.__status}"


try:
    account1 = Account("DE89370400440532013000", 1000)
    account2 = Account("TR1", 2000, AccountStatus.CLOSED)
    account3 = Account("BE2", 3000, AccountStatus.BLOCKED)
    account1.deposit(100)
    account1.withdraw(1000)
    account2.deposit(100)
    account2.withdraw(1000)
    account3.deposit(100)
    account3.withdraw(1000)
    account1.withdraw(1000)
    account1.status = AccountStatus.CLOSED
    account2.status = AccountStatus.BLOCKED
except ValueError as ve:
    print(ve)
finally:
    print(account1)
    print(account2)
    print(account3)

"""
CheckingAccount: i. sub class   ii. derived class
Account        : i. super class ii. base class
"""


class CheckingAccount(Account):

    def __init__(self, iban: str, balance: float = 0, status: AccountStatus = AccountStatus.ACTIVE,
                 overdraft_amount: float = 1_000.0):
        super().__init__(iban, balance, status)
        self.__overdraft_amount = overdraft_amount

    @property
    def overdraft_amount(self) -> float:
        return self.__overdraft_amount

    def withdraw(self, amount: float) -> bool:
        if self.__status == AccountStatus.CLOSED or self.__status == AccountStatus.BLOCKED:
            raise ValueError(
                "deposit is not allowed for closed accounts"
            )
        if amount <= 0:
            raise ValueError("amount must be positive")

        if amount > self.__balance + self.__overdraft_amount:
            raise ValueError("amount must be less than or equal to balance + overdraft amount")
        self.__balance -= amount
        return True

    def __str__(self) -> str:
        return super().__str__()
