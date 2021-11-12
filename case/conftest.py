import time
import pytest
from faker import Faker

@pytest.fixture()
def getid():
    return int(time.time())

@pytest.fixture()
def getname():
    fake = Faker(locale='zh_TW')
    return fake.name()
@pytest.fixture()
def geteamil():
    fake = Faker()
    return fake.email()
@pytest.fixture()
def getinfo():
    fake = Faker(locale='zh_TW')
    return fake.city()