# Канивец Евгения, 15-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests

# Функция для создания заказа и сохранения трек-номера заказа
def post_create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order_body)

# Функция для получения заказа по трек-номеру
def get_order_by_number(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH + str(track_number))
