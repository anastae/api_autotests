import pytest
from pydantic import BaseModel
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from clients.courses.courses_client import CoursesClient, get_courses_client
from fixtures.files import FileFixture
from fixtures.users import UserFixture

class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

#создает клиент CoursesClient, который используется для взаимодействия с API курсов
@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user())

#создает тестовый курс перед выполнением теста и возвращает объект с данными созданного курса.
@pytest.fixture
def function_course(
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture
) -> CourseFixture:
    request = CreateCourseRequestSchema(
        preview_file_id=function_file.response.file.id,
        created_by_user_id=function_user.response.user.id
    )
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)