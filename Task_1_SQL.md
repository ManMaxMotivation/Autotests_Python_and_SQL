# Александр Самсонов, 24-я когорта — Финальный проект. Инженер по тестированию плюс

# Подключение к серверу:
var = ssh - rsa
AAAAB3NzaC1yc2EAAAADAQABAAABgQDfBwQK2yfu1iZvOvHdp6S32MIMs0LostJovFNvbsRSdG10lOw8I / UlN9DtCmMLKcQA5BBbKyuTEGLxvdiy5QzWwVEvj / u7tRlde7LKdUMpIYK / zU6GKqxgPAs4P4Z27y6wQhq + IomVxs2KA4xMSF49just5PuOwIBpbhWLtl3E1OK412QNYIyd21cHkEvIZcSpao1jMVyeN1A0EdR8EdQI0Vb / GjoUTR7QRRzSf98bFtnoh0ukbHuLClmxXg3NwylYFT65wY8Jp8mFrU9W1Z4vue3X / 4
XwXIu6sy5XzonSZQAWmuhK3fsza / Tja / Zn3SHCgyZzpmLSwlsgOyIf41o3EqQXUBxS / 4
PzdTO8Y2UuM7o5mHrK2Z2AbbVwskvl5CHLVd2O + GaSXPN25gq2uKV4 + StoOfPeuNXlaiqhposYFGe7532lEs9n9 / q8w + W + XvYDR5tSLusyW27bfJ7ErJAI0D3DPNjsmzd0yYplTw9uBOoVmLcQ2iLNF5mckS5Kr7E = 79528 @ xaMep

ssh <имя пользователя>@<хост> -p <порт>
ssh bef65cda-5bcd-449f-98f7-ce552302c095@serverhub.praktikum-services.ru -p 4554
# Доступ к базе осуществляется с помощью команды psql -U morty -d scooter_rent, пароль: smith.

## Задание 1
# Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
# Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).
# Для проверки создам 2 курьера в Postman {{stend}}/api/v1/courier:
{
    "login": "barack",
    "password": "4444",
    "firstName": "abama"
}
#Создаём 3 заказа (в теле меняем дату, метро чтобы не перепутать) {{stend}}/api/v1/orders:
var = {
    "firstName": "Абдурахмангаджи",
    "lastName": "Убдурахмангаджи",
    "address": "Центральный проезд Хорошёвского Серебряного Бора 2",
    "metroStation": 3,
    "phone": "+34916123451",
    "rentTime": 1,
    "deliveryDate": "2024-12-04",
    "comment": "Привет, Абдурахмангаджи!",
    "color": [
        "BLACK"
    ]
}

# SQL запрос
SELECT c.login, COUNT(o.id) AS "deliveryCount"
   FROM "Couriers" AS c
   LEFT JOIN "Orders" AS o ON c.id = o."courierId"
   WHERE o."inDelivery" = true
   GROUP BY c.login;

# Работа запроса:
# SELECT c.login, COUNT(o.id) AS "deliveryCount": Извлекает логин курьера и количество заказов, связанных с этим курьером.
# FROM "Couriers" AS c: Работает с таблицей курьеров (сокращение AS c используется для удобства).
# LEFT JOIN "Orders" AS o ON c.id = o."courierId": Соединяет таблицы Couriers и Orders по идентификатору курьера.
# LEFT JOIN обеспечивает, что даже если у курьера нет заказов, он всё равно будет присутствовать в результате.
# WHERE o."inDelivery" = true: Фильтрует заказы, которые находятся в статусе "в доставке" (inDelivery = true).
# Это условие применяется только к заказам, которые соответствуют LEFT JOIN.
# GROUP BY c.login: Группирует результаты по логинам курьеров, чтобы подсчитать количество доставляемых заказов для каждого из них.

# Замечание: Если у курьера нет заказов, то с использованием текущего WHERE условие полностью исключит этого курьера из результата.
# Чтобы отобразить курьеров с нулевым количеством заказов, условие o."inDelivery" = true лучше перенести в часть ON:

SELECT c.login, COUNT(o.id) AS "deliveryCount"
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o ON c.id = o."courierId" AND o."inDelivery" = true
GROUP BY c.login;

# Чтобы увидеть количеством их заказов в статусе «В доставке», нужно "Принять" заказ Курьерами. Захожу в
# Android Studio и на эмуляторы принимаю 1 заказ первым курером и 2 заказа втормы курьером.
# Заказов в 2 раза больше у каждого курьера чем мы приняли в работу так как есть БАГ, ранее его фиксировали.