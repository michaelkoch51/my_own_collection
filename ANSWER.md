# Домашнее задание к занятию 6 «Создание собственных модулей»

## Ссылки

- Collection (GitHub): https://github.com/michaelkoch51/my_own_collection
- Тег: 1.0.0
- Архив (tar.gz): https://github.com/michaelkoch51/my_own_collection/blob/main/my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz

## Что сделано

### 1. Модуль my_own_module

Написан собственный модуль, который создаёт текстовый файл на удалённом
хосте по указанному пути с указанным содержимым.

Параметры:
- path (обязательный, str) — абсолютный путь к файлу
- content (обязательный, str) — содержимое файла

Возможности:
- Идемпотентность: если файл уже существует с тем же содержимым,
  модуль не вносит изменений (changed: false)
- Поддержка check mode: в тестовом режиме файл не создаётся
- Создание родительских директорий, если их нет
- Документация (DOCUMENTATION, EXAMPLES, RETURN) по стандартам Ansible

### 2. Локальное тестирование

Модуль проверен локально:
- Первый запуск -> changed: true, файл создан
- Повторный запуск -> changed: false (идемпотентность)
- Check mode -> changed: true, но файл не создан

### 3. Single-task playbook

Написан простой playbook, использующий модуль. Проверен на идемпотентность:
- Первый запуск -> changed=1
- Второй запуск -> changed=0

### 4. Collection

Создана collection my_own_namespace.yandex_cloud_elk:
- plugins/modules/my_own_module.py — наш модуль
- roles/my_own_role/ — роль с default-параметрами:
  - my_own_module_path: /tmp/my_own_file.txt
  - my_own_module_content: "Default content from my_own_role"
- galaxy.yml, README.md — метаданные и документация

### 5. Сборка и установка

- Collection собран в .tar.gz через ansible-galaxy collection build
- Установлен из архива через ansible-galaxy collection install
- Playbook, использующий роль из collection, отработал:
  - Первый запуск -> changed=1, файл создан
  - Второй запуск -> changed=0 (идемпотентность)

## Технологии

- Ansible Core 2.15.12
- Python 3.11
- macOS (Apple Silicon)

## Структура collection

    my_own_namespace/yandex_cloud_elk/
    ├── galaxy.yml
    ├── README.md
    ├── meta/runtime.yml
    ├── plugins/
    │   └── modules/
    │       └── my_own_module.py
    └── roles/
        └── my_own_role/
            ├── defaults/main.yml
            ├── tasks/main.yml
            └── ...

## Скриншоты

- [Шаг 4 — локальная проверка модуля](screenshots/04-module-local-check.png)
- [Шаг 6 — идемпотентность через playbook](screenshots/06-playbook-idempotency.png)
- [Шаг 15 — установка collection из архива](screenshots/15-collection-install.png)
- [Шаг 16 — запуск playbook через collection](screenshots/16-playbook-collection.png)
