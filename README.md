# Autotest

Тестовое задание: автотесты на Python (pytest + requests) для регистрации
нового аккаунта. Тесты написаны по паттерну AAA (Arrange/Act/Assert).

Базовый URL: https://automation.tivaliclub.com/fcle
Swagger: https://automation.tivaliclub.com/fcle/swagger/index.html

## Установка

Нужен Python 3.9+.

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск

```bash
pytest tests/ -v
```

Один тест или один класс:

```bash
pytest tests/test_signup.py::TestAuthSignup::test_signup_success -v
```

## Структура проекта

```
project/
├── tests/
│   ├── __init__.py
│   ├── test_signup.py    
│   └── conftest.py       
├── requirements.txt      
├── README.md
└── .gitignore
```

- `conftest.py` - фикстуры. `session` создаётся один раз на весь прогон и
  закрывается в конце. `new_user` на каждый тест отдаёт свежие email и
  username, поэтому тесты можно запускать повторно и в любом порядке.
- `test_signup.py` - сами тесты в классе `TestAuthSignup`.

## Что проверяется

- успешная регистрация: код ответа, токен в ответе, пароль не возвращается;
- невалидные email;
- слабые пароли;
- пустое тело запроса;
- отсутствие обязательного поля (email/username/password);
- регистрация с уже существующим email.

Всего тестов было 18: 8 положительные, 10 отрицательные 

## Пример вывода

<img width="976" height="355" alt="image" src="https://github.com/user-attachments/assets/0d38799a-e7e1-4fbe-909e-b5e74bc663bf" />
<img width="959" height="268" alt="image" src="https://github.com/user-attachments/assets/3f9d7722-7c90-49df-bc7f-b1f785a494ef" />
<img width="977" height="23" alt="image" src="https://github.com/user-attachments/assets/a6dfab4c-658a-4ac1-9d2c-5f7f7b8f4f0e" />





