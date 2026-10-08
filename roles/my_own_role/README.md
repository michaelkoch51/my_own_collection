# my_own_role

Single-task роль, использующая модуль my_own_module.

## Default-параметры

| Переменная              | По умолчанию                                  |
|-------------------------|-----------------------------------------------|
| my_own_module_path      | /tmp/my_own_file.txt                          |
| my_own_module_content   | "Default content from my_own_role"            |

## Пример использования

    - hosts: localhost
      roles:
        - my_own_namespace.yandex_cloud_elk.my_own_role
      vars:
        my_own_module_path: /tmp/custom.txt
        my_own_module_content: "Custom content"
