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
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    # Вызов функции requests.get с телом запроса для создания нового заказа из модуля data
    response = requests.get(get_order_url)
    return response

def test_order_creation_and_tracking():

    # Создание заказа
    create_response = create_order(order_body)  # Используем import из data.py
    assert create_response.status_code == 201, "Не удалось создать заказ"

    # Сохранение трек-номера
    track_number = create_response.json().get("track")
    print("Заказ создан. Номер трека:", track_number)
    assert track_number, "Трек-номер не получен"

    # Получение заказа по трек-номеру
    get_response = get_order_by_track(track_number)

    # Проверка статуса ответа
    assert get_response.status_code == 200, "Заказ не найден"
    print("Тест успешно пройден. Код 200.")

# Без блока if __name__ == "__main__": код может неконтролируемо выполняться при импорте.
if __name__ == "__main__":
    test_order_creation_and_tracking()