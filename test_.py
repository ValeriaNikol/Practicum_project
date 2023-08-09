# Валерия Николаева, 7-я когорта — Финальный проект. Инженер по тестированию плюс

import request


def possitive_assert():
    response_get = request.get_order_info()
    assert response_get.status_code == 200


def test_success_get_order_info():
    possitive_assert()