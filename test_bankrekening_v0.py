# Tests for the 'bankrekening.py' source code
# CopyLeft 2022: Hossein Chamani, Jan Kroon, Rotterdam University of Applied Sciences
# Inspired by: Semaphore tutorial by Kevin Ndung'u Gathuku

import pytest
from bankrekening_v0 import Bankrekening, OnvoldoendeSaldoMelding

def test_default_balance():
    bankrekening = Bankrekening()
    assert bankrekening.saldo == 0

def test_setting_balance():
    bankrekening = Bankrekening(100)
    assert bankrekening.saldo == 100

def test_deposit():
    bankrekening = Bankrekening(10)
    bankrekening.storting(90)
    assert bankrekening.saldo == 100

def test_withdraw():
    bankrekening = Bankrekening(20)
    bankrekening.opname(10)
    assert bankrekening.saldo == 10

def test_bankrekening_foutmelding():
    bankrekening = Bankrekening()
    with pytest.raises(OnvoldoendeSaldoMelding):
        bankrekening.opname(50)
