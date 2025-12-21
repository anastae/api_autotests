from typing import TypedDict
from httpx import Response
from clients.api_client import ApiClient

from clients.private_http_builder import get_private_http_client, AuthenticationUserDict

class GetExercisesQueryDict(TypedDict):
    """
        Описание структуры запроса на получение списка упражнений.
        """
    courseId: str

class CreateExerciseRequestDict(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class Exercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]


class ExercisesClient(ApiClient):
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
               Метод получения списка всех упражнений.
               :param query: Словарь с courseId.
               :return: Ответ от сервера в виде объекта httpx.Response
               """
        return self.get('/api/v1/exercises', params=query)

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
               Метод создания упражнения.
               :param request: словарь из CreateExerciseRequestDict.
               :return: Ответ от сервера в виде объекта httpx.Response
               """
        return self.post('/api/v1/exercises', json=request)

    def create_exercise(self, request: CreateExerciseRequestDict) -> GetExercisesResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
               Метод получения упражнения по id.

               :param exercise_id: Идентификатор упражнения.
               :return: Ответ от сервера в виде объекта httpx.Response
               """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> Exercise:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
                       Метод удаления упражнения по id.

                       :param exercise_id: Идентификатор упражнения.
                       :return: Ответ от сервера в виде объекта httpx.Response
                       """
        return self.delete(f'/api/v1/exercises/{exercise_id}')

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
                       Метод обновления упражнения.
                       :param exercise_id: Идентификатор упражнения.
                       :param request: словарь из UpdateExerciseRequestDict.
                       :return: Ответ от сервера в виде объекта httpx.Response
                       """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseRequestDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

def get_exercises_client(user:AuthenticationUserDict) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))
