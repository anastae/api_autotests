from api_client_create_course import create_course_request
from clients.authentication.authentication_client import AuthenticationClient
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client, CreateUserDict
from clients.files.files_client import get_files_client, CreateFileRequestDict, FilesClient
from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from tools.fakers import get_random_email

public_users_client = get_public_users_client()
# Создаем пользователя
create_user_request = CreateUserDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)
#clients
authentication_user =  AuthenticationUserSchema(
    email=create_user_request["email"],
    password=create_user_request["password"]
)
# files_client = get_files_client(authentication_user)
# courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

# #download file
# create_file_request = CreateFileRequestDict(filename="img2.png",
#     directory="courses",
#     upload_file="./testdata/files/img.png")
# create_file_response = files_client.create_file(create_file_request)
# print('Create file data:', create_file_response)
#
# # create course
# create_course_request = CreateCourseRequestDict(title="Python3",
#     maxScore=269,
#     minScore=10,
#     description="Python API course",
#     estimatedTime="2 weeks",
#     previewFileId=create_file_response['file']['id'],
#     createdByUserId=create_user_response['user']['id'])
# create_course_response = courses_client.create_course(create_course_request)
# print('Create course data:', create_course_response)

#create exercise
create_exercise_request = CreateExerciseRequestDict(title='my exercise',
    courseId='exc1',
    maxScore=962,
    minScore=4,
    orderIndex=10,
    description='oh my exercise',
    estimatedTime='1 hour')
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)
