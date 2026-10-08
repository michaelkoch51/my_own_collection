# my_own_namespace.yandex_cloud_elk

Custom Ansible collection с собственным модулем и ролью.

## Модуль my_own_module

Создаёт текстовый файл на удалённом хосте по указанному пути
с указанным содержимым.

Параметры:
- path (обязательный, str) — абсолютный путь к файлу
- content (обязательный, str) — содержимое файла

Пример:

    - name: Create a file
      my_own_namespace.yandex_cloud_elk.my_own_module:
        path: /tmp/test.txt
        content: "hello world"

Идемпотентность: если файл существует и содержимое совпадает,
изменений не вносится (changed: false).

## Роль my_own_role

Single-task роль, использующая my_own_module.

Default-параметры:
- my_own_module_path: /tmp/my_own_file.txt
- my_own_module_content: "Default content from my_own_role"

Пример:

    - hosts: localhost
      roles:
        - my_own_namespace.yandex_cloud_elk.my_own_role

## Лицензия

GPL-2.0-or-later
