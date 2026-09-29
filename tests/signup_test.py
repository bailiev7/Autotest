import pytest

TIMEOUT = 10
OK = (200, 201)
ERR = (400, 409, 422)


def assert_error(response):
    assert response.status_code in ERR, response.text
    assert response.json()


class TestAuthSignup:

    def test_signup_success(self, session, signup_url, new_user):
        payload = new_user
        response = session.post(signup_url, json=payload, timeout=TIMEOUT)
        assert response.status_code in OK, response.text
        body = response.json()
        assert any("token" in key.lower() for key in body)
        assert new_user["password"] not in response.text

    @pytest.mark.parametrize("email", [
        "plainaddress", "@example.com", "user@", "user@@example.com",
        "user name@example.com", "",
    ])
    def test_invalid_email(self, session, signup_url, new_user, email):
        payload = {**new_user, "email": email}
        response = session.post(signup_url, json=payload, timeout=TIMEOUT)
        assert_error(response)

    @pytest.mark.parametrize("password", [
        "1", "123", "password", "12345678", "abcdefgh", "",
    ])
    def test_weak_password(self, session, signup_url, new_user, password):
        payload = {**new_user, "password": password}
        response = session.post(signup_url, json=payload, timeout=TIMEOUT)
        assert_error(response)

    def test_empty_body(self, session, signup_url):
        response = session.post(signup_url, json={}, timeout=TIMEOUT)
        assert_error(response)

    @pytest.mark.parametrize("field", ["email", "username", "password"])
    def test_missing_field(self, session, signup_url, new_user, field):
        payload = {k: v for k, v in new_user.items() if k != field}
        response = session.post(signup_url, json=payload, timeout=TIMEOUT)
        assert_error(response)

    def test_duplicate_email(self, session, signup_url, new_user):
        first = session.post(signup_url, json=new_user, timeout=TIMEOUT)
        assert first.status_code in OK, first.text
        repeat = {**new_user, "username": new_user["username"] + "_2"}
        second = session.post(signup_url, json=repeat, timeout=TIMEOUT)
        assert_error(second)