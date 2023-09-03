"""Lesson_22 Hometask_01."""

import pytest
from hometask_22_hillel_api import auth, cars, s, users


def test_signup_positive():
    """Create a new user."""
    user_data = {
        'name': 'Johnny',
        'lastName': 'Tonny',
        'email': 'qal2808@2022test.com',
        'password': 'Qal2608venv',
        'repeatPassword': 'Qal2608venv',
    }
    r = auth.signup(s, user_data)
    r_json = r.json()
    assert r.status_code == 201, f'Wrong status code:\n{r_json}'
    assert r_json.get('status', False) == 'ok', "Key 'status' is not ok"


def test_signin_positive():
    """Login with user."""
    user_data = {
        'email': 'qal2808@2022test.com',
        'password': 'Qal2608venv',
        'remember': False,
    }
    r = auth.signin(s, user_data)
    r_json = r.json()
    assert r.status_code == 200, f'Wrong status code:\n{r_json}'
    assert r_json.get('status', False) == 'ok', "Key 'status' is not ok"


def get_a(a):
    """Nazva testu."""
    return int(a)


def test_error():
    """Nazva testu."""
    with pytest.raises(ValueError):
        a = 'dsdsd'
        get_a(a)


def get_error():
    """Nazva testu."""
    raise AttributeError('character name empty')


def test_error_message():
    """Nazva testu."""
    with pytest.raises(AttributeError, match='character name empty'):
        get_error()

# Homework


"""
https://qauto.forstudy.space/api-docs/
Написати п'ять тестів що проходять через пункти
1. Реєстрація користувача
2. Створення машини POST cars
3. редагування машини
4. отримання даних через GET в Cars або Expenses
5. Видалення користувача
"""


def test_send_reset_pass():
    """Sends_reset_password_instruction_to_email."""
    user_email = {
        'email': 'qal2808@2022test.com',
    }
    r = auth.resetpassword(s, user_email)
    r_json = r.json()
    assert r.status_code == 200, f'Wrong status code:\n{r_json}'
    assert r_json.get('status', False) == 'ok', "Key 'status' is not ok"


def test_create_car_positive():
    """Creates new car."""
    car_data = {
        'carBrandId': 1,
        'carModelId': 1,
        'mileage': 1012,
    }
    r = cars.cars_post(s, car_data)
    r_json = r.json()
    assert r.status_code == 201, f'Wrong status code: \n{r_json}'
    assert r_json.get('status', False) == 'ok', "Key 'status' is not ok"


def test_edits_car_positive():
    """Edits existing car."""
    r = cars.cars_get(s)
    r_json = r.json()

    new_car_data = {
        'carBrandId': 1,
        'carModelId': 1,
        'mileage': 1013,
        'id': r_json['data'][0]['id'],
    }
    r = cars.cars_id_put(s, new_car_data)
    r_json = r.json()
    assert r.status_code == 200, f'Wrong status code:\n{r_json}'
    assert r_json.get('status', False) == 'ok', "Key 'status' is not ok"


def test_remove_car():
    """Remove car."""
    r = cars.cars_get(s)
    r_json = r.json()

    car_data_remove = {
        'id': r_json['data'][0]['id'],
    }
    r = cars.cars_id_delete(s, car_data_remove)
    r_json = r.json()
    assert r.status_code == 200, f'Wrong status code:\n{r_json}'
    assert r_json.get('status', False) == 'ok', "Key 'status' is not ok"


def test_remove_user():
    """Remove user."""
    r = users.users(s)
    r_json = r.json()
    assert r.status_code == 200, f'Wrong status code:\n{r_json}'
    assert r_json.get('status', False) == 'ok', "Key 'status' is not ok"
