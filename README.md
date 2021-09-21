# Emph_test

1. Создать пустой проект и настроить виртуальное окружение
2. Загрузить код, написав:
 `git clone git@github.com:Ririgirl/Emph_test.git`
3. Установить зависимости, прописав в консоли 
`pip install -r requirements.txt` 
4. Сделать миграции
`python manage.py makemigrations`
`python manage.py migrate`
5. Запустить сервер
`python manage.py runserver`

## Инструкция по работе в swagger

Шаги:
1) зарегистрироваться по  /register /
2) залогиниться по /login_token/  - получить токен и скопировать его
3) авторизоваться по кнопке authorize 
4) в открвшемся окне ввести в поле Bearer [ВАШ ТОКЕН]

или использовать готовые учетные данные:

 "username": "string",
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com",
  "password": "string12345"
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InN0cmluZyJ9.EfIZBXeRvSoH5Tyr2KQOcGNHez_2wLyBYdKzY5Sqo5k"
}

в кнопке авторизация ввести: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InN0cmluZyJ9.EfIZBXeRvSoH5Tyr2KQOcGNHez_2wLyBYdKzY5Sqo5k

после авторизации можно проверить всю работоспособность апишек в блоке user

