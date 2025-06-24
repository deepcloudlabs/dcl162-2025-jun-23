"""
CUT: Class Under Test -> Account
MUT: Method Under Test -> deposit, withdraw, getter/setter, __str__, ...

Unit Test Phases:
1. Test Fixture/Setup
2. Call Exercise Method
3. Verification: Assert Exercise Method Result
4. Cleanup/Teardown
"""
import pytest

from banking.account import Account, AccountStatus

deposit_failure_values = [0, -0.1, -1, -10]
deposit_success_values = [(0.1, 1_000.1), (1, 1_001), (10, 1_010), (100, 1_100)]


@pytest.fixture
def an_active_account():
    return Account("TR1", 1_000, AccountStatus.ACTIVE)


@pytest.fixture
def a_closed_account():
    return Account("TR2", 0, AccountStatus.CLOSED)


@pytest.mark.parametrize("amount", deposit_failure_values)
def test_deposit_with_negative_amount_should_raise_exception(an_active_account: Account, amount: float):
    with pytest.raises(ValueError):  # 3. Verification: Assert Exercise Method Result
        # 2. Call Exercise Method
        an_active_account.deposit(amount)
    # 4. Cleanup/Teardown


@pytest.mark.parametrize("test_value", deposit_success_values)
def test_deposit_with_positive_amount_should_success(an_active_account: Account, test_value):
    amount, expected_balance = test_value
    # 2. Call Exercise Method
    an_active_account.deposit(amount)
    # 3. Verification: Assert Exercise Method Result
    assert an_active_account.balance == expected_balance
    assert an_active_account.status == AccountStatus.ACTIVE
    # 4. Cleanup/Teardown


def test_deposit_to_closed_account_should_raise_exception(a_closed_account: Account):
    with pytest.raises(ValueError):  # 3. Verification: Assert Exercise Method Result
        # 2. Call Exercise Method
        a_closed_account.deposit(1)
    # 4. Cleanup/Teardown
