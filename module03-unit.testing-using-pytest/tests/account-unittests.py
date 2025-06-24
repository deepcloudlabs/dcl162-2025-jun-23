import unittest
from banking.account import Account, AccountStatus

class TestAccount(unittest.TestCase):
    def setUp(self):
        # 1. Test Fixture/Setup
        self.active_account = Account("TR1", 1_000, AccountStatus.ACTIVE)
        self.closed_account = Account("TR2", 0, AccountStatus.CLOSED)

    def test_deposit_with_negative_or_zero_amount_should_raise_exception(self):
        deposit_failure_values = [0, -0.1, -1, -10]
        for amount in deposit_failure_values:
            with self.assertRaises(ValueError):
                # 2. Call Exercise Method
                self.active_account.deposit(amount)
            # 3. Verification is done by assertRaises

    def test_deposit_with_positive_amount_should_succeed(self):
        deposit_success_values = [(0.1, 1_000.1), (1, 1_001), (10, 1_010), (100, 1_100)]
        for amount, expected_balance in deposit_success_values:
            # Reset account for each case
            account = Account("TR1", 1_000, AccountStatus.ACTIVE)
            # 2. Call Exercise Method
            account.deposit(amount)
            # 3. Verification
            self.assertEqual(account.balance, expected_balance)
            self.assertEqual(account.status, AccountStatus.ACTIVE)

    def test_deposit_to_closed_account_should_raise_exception(self):
        # 2. Call Exercise Method
        with self.assertRaises(ValueError):
            self.closed_account.deposit(1)
        # 3. Verification is done by assertRaises

if __name__ == '__main__':
    unittest.main()
