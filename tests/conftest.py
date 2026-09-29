import uuid

import pytest
import requests
from faker import Faker

BASE_URL = "https://automation.tivaliclub.com/fcle"
fake = Faker()


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def session():
    with requests.Session() as s:
        s.headers.update({"Accept": "application/json"})
        yield s


@pytest.fixture
def signup_url(base_url):
    return f"{base_url}/api/Auth/signup"


@pytest.fixture
def new_user():
    suffix = uuid.uuid4().hex[:10]
    return {
        "email": f"autotest_{suffix}@example.com",
        "username": f"autotest_{suffix}",
        "password": fake.password(length=12),
    }