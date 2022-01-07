#!/usr/bin/python3

import pytest


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="module")
def kornGold(KornGold, accounts):
    return KornGold.deploy({'from': accounts[0]})

@pytest.fixture(scope="module")
def kornToken(KornToken, kornGold, accounts):
    return KornToken.deploy("KornToken", "KTN", kornGold.address, {'from': accounts[0]})
