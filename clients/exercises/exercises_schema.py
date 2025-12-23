from pydantic import BaseModel, Field, ConfigDict


class ExerciseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str=Field(alias="courseId")
    max_score: int=Field(alias="maxScore")
    min_score: int=Field(alias="minScore")
    order_index: int=Field(alias="orderIndex")
    description: str
    estimated_time: str=Field(alias="estimatedTime")

class GetExercisesQuerySchema(BaseModel):
    """
        Описание структуры запроса на получение списка упражнений.
        """
    model_config = ConfigDict(populate_by_name=True)
    course_id: str=Field(alias="courseId")

class CreateExerciseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str = Field(min_length=1, max_length=250)
    course_id: str = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex", default=None)
    description: str = Field(min_length=1)
    estimated_time: str | None = Field(alias="estimatedTime")

class CreateExerciseResponseSchema(BaseModel):
    exercise: ExerciseSchema

class UpdateExerciseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str
    max_score: int=Field(alias="maxScore")
    min_score: int=Field(alias="minScore")
    order_index: int=Field(alias="orderIndex")
    description: str
    estimated_time: str=Field(alias="estimatedTime")

class GetExercisesResponseSchema(BaseModel):
    exercises: list[ExerciseSchema]