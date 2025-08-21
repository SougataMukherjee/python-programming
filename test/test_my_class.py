import pytest
from python.my_class import Account

def test_account_debit_credit():
    acc = Account(10000, 12000)

    acc.debit(5000)
    assert acc.get_balance() == 5000

    acc.credit(20000)
    assert acc.get_balance() == 25000

def test_multiple_accounts():
    acc1 = Account(5000, 111)
    acc2 = Account(1000, 222)

    acc1.credit(500)
    acc2.debit(200)

    assert acc1.get_balance() == 5500
    assert acc2.get_balance() == 800
