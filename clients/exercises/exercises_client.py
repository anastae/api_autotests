from httpx import Response
from clients.api_client import ApiClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.exercises.exercises_schema import ExerciseSchema, CreateExerciseRequestSchema, CreateExerciseResponseSchema, GetExercisesQuerySchema, GetExercisesResponseSchema, UpdateExerciseRequestSchema
from tools.routes import APIRoutes


class ExercisesClient(ApiClient):
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
               Метод получения списка всех упражнений.
               :return: Ответ от сервера в виде объекта httpx.Response
               """
        return self.get(APIRoutes.EXERCISES, params=query.model_dump(by_alias=True)) #сериализация

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
               Метод создания упражнения.
               :param request: словарь из CreateExerciseRequestDict.
               :return: Ответ от сервера в виде объекта httpx.Response
               """
        return self.post(APIRoutes.EXERCISES, json=request.model_dump(by_alias=True))

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
               Метод получения упражнения по id.

               :param exercise_id: Идентификатор упражнения.
               :return: Ответ от сервера в виде объекта httpx.Response
               """
        return self.get(f'{APIRoutes.EXERCISES}/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> ExerciseSchema:
        response = self.get_exercise_api(exercise_id)
        return ExerciseSchema.model_validate_json(response.text)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
                       Метод удаления упражнения по id.

                       :param exercise_id: Идентификатор упражнения.
                       :return: Ответ от сервера в виде объекта httpx.Response
                       """
        return self.delete(f'{APIRoutes.EXERCISES}/{exercise_id}')

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
                       Метод обновления упражнения.
                       :param exercise_id: Идентификатор упражнения.
                       :param request: словарь из UpdateExerciseRequestDict.
                       :return: Ответ от сервера в виде объекта httpx.Response
                       """
        return self.patch(f'{APIRoutes.EXERCISES}/{exercise_id}', json=request.model_dump(by_alias=True))

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

def get_exercises_client(user:AuthenticationUserSchema) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))
