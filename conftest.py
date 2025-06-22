import pytest
import requests
from driver_factory import DriverFactory
from data import Data
from urls import Urls



@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = DriverFactory.get_driver(request.param)
    driver.set_window_position(0, 0)
    driver.set_window_size(1280, 800)
    yield driver
    driver.quit()


@pytest.fixture()
def register_new_user_and_return_credentials():
    payload = Data.USER_CREDENTIALS
    email = payload.get('email')
    password = payload.get('password')
    response = requests.post(Urls.create_user, json=payload)
    if response.status_code == 200:
        access_token = response.json()["accessToken"]
        refresh_token = response.json()["refreshToken"]
        yield email, password, access_token, refresh_token
        headers = {"Authorization": access_token}
        requests.delete(Urls.user_data_management_url, headers=headers)
    else:
        pytest.fail(f"Не удалось зарегистрировать пользователя: {response.status_code}, {response.text}")


@pytest.fixture()
def login_user_via_localstorage(register_new_user_and_return_credentials, driver):
    """
    Установка токенов в localStorage браузера и обновление страницы.
    Возвращает email и password.
    """
    email, password, access_token, refresh_token = register_new_user_and_return_credentials
    driver.get(Urls.BASE_URL)
    script_set_tokens = (
        "window.localStorage.setItem('accessToken', '{}');"
        "window.localStorage.setItem('refreshToken', '{}');"
    ).format(access_token, refresh_token)
    driver.execute_script(script_set_tokens)
    driver.refresh()
    return email, password