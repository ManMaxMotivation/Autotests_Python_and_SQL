# Александр Самсонов, 24-я когорта — Финальный проект. Инженер по тестированию плюс

# Импорт модуля requests для отправки HTTP-запросов
import requests
# Импорт конфигурационного файла, который содержит настройки URL
import configuration
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
from data import order_body  # Импортируем данные из data.py

# Запрос на создание заказа.
# Определение функции create_order для отправки POST-запроса на создание нового заказа
def create_order(order_data):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREAT_ORDERS объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=order_data)
    return response

# Выполняет запрос на получение заказа по трек-номеру.
# Определение функции для отправки GET-запроса получение номера заказа. С параметром track_number.
def get_order_by_track(track_number):
    get_order_url = f"{configuration.URL_SERVICE}{configuration.GET_ORDER_BY_TRACK}"
    # Вызов функции requests.get с телом запроса для создания нового заказа из модуля data
    response = requests.get(get_order_url, params={"t": track_number})
    return response