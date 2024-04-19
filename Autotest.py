# Канивец Евгения, 15-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request

# Тест для получения заказа по трек-номеру
def test_get_order_by_number():
    order_body = {"item": "test_item", "quantity": 1}  # Пример данных заказа
    track_number = sender_stand_request.post_create_order(order_body).json()["track"]

    data_order = sender_stand_request.get_order_by_number(track_number)

    # Проверка, что код ответа равен 200
    assert data_order.status_code == 200


if __name__ == "__main__":
    test_get_order_by_number()
