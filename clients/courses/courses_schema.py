from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema

class CourseSchema(BaseModel):
    """
    Описание структуры курса
    """
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: str
    max_score: int=Field(alias="maxScore", default=None)
    min_score: int=Field(alias="minScore", default=None)
    description: str
    estimated_time: str=Field(alias="estimatedTime", default=None)
    preview_file: FileSchema=Field(alias="previewFile")
    created_by_user: UserSchema=Field(alias="createdByUser")


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)
    user_id: str=Field(alias="userId")

class CreateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str=Field(alias="previewFileId")
    created_by_user_id: str=Field(alias="createdByUserId")

class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema

class UpdateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")




