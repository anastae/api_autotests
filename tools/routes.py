from enum import Enum


class APIRoutes(str, Enum):
    USERS = "/api/v1/users"
    FILES = "/api/v1/files"
    COURSES = "/api/v1/courses"
    EXERCISES = "/api/v1/exercises"
    AUTHENTICATION = "/api/v1/authentication"

    def __str__(self):
        """
        при преобразовании элементов Enum в строку
        (например, при конкатенации с другими строками или выводе в логах)
        возвращалась не сама переменная типа Enum,
        а именно её значение. Это позволяет избежать вывода лишней информации
        типа <APIRoutes.USERS: '/api/v1/users'>,
         а вместо этого получать только строковое представление пути /api/v1/users.
        :return:
        """
        return self.value