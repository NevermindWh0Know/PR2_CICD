Python Calculator

Простой калькулятор на Python с поддержкой базовых арифметических операций и тестированием через pytest.

Возможности:
 - Сложение (add(a, b))
 - Вычитание (subtract(a, b))
 - Умножение (multiply(a, b))
 - Деление (divide(a, b))
 - Возведение в степень (power(a, b))

Структура проекта:

PR2_CICD/    
  │── .github/workflows/   # Настройки CI/CD (GitHub Actions)   
  │── tests/test_calc.py   # Unit-тесты для pytest  
  │── .gitignore  
  │── calculator.py        # Основные функции калькулятора  
  │── requirements.txt     # Зависимости проекта  
  │── README.md            # Документация

CI/CD:
Автоматические тесты запускаются при каждом push и pull_request в ветки:
main
development

Версии:
v1.0.0 – первая версия, добавлены основные функции калькулятора.
