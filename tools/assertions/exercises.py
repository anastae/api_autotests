from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import ExerciseSchema, CreateExerciseRequestSchema, \
    CreateExerciseResponseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_internal_error_response


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
       Проверяет, что фактические данные упражнения соответствуют ожидаемым.
       выполняет поэлементное сравнение всех ключевых полей модели курса
       :param actual: Фактические данные курса.
       :param expected: Ожидаемые данные курса.
       :raises AssertionError: Если хотя бы одно поле не совпадает.
       """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

def assert_create_exercise_response(request: CreateExerciseRequestSchema, response: CreateExerciseResponseSchema):
    """
       Проверяет, что ответ на создание упражнения соответствует запросу
       :param request: Исходный запрос на создание упражнения.
       :param response: Ответ API с данными упражнения.
       :raises AssertionError: Если хотя бы одно поле не совпадает.
       """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")

def assert_get_exercise_by_id_response(get_exercise_response: GetExerciseResponseSchema,
                                       create_exercise_response: CreateExerciseResponseSchema):
    """
            Проверяет, что ответ на получение упражнения соответствует ответу на его создание.

            :param get_exercise_response: Ответ API при запросе данных упражнения.
            :param create_exercise_response: Ответ API при создании упражнения.
            :raises AssertionError: Если данные файла не совпадают.
            """
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)

def assert_update_exercise_response(request: UpdateExerciseRequestSchema,
                                    response: UpdateExerciseResponseSchema):
    assert_equal(request.title, response.title, "title")
    assert_equal(request.max_score, response.max_score, "max_score")
    assert_equal(request.min_score, response.min_score, "min_score")
    assert_equal(request.order_index, response.order_index, "order_index")
    assert_equal(request.description, response.description, "description")
    assert_equal(request.estimated_time, response.estimated_time, "estimated_time")

def assert_exercise_not_found(actual: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)