from graphene import (
    ObjectType,
    String,
    Int,
    Field,
    Schema,
    List
)

from models import data
class StudentType(ObjectType):
    name = String()
    id = Int()
    age = Int()

    # resolvers
    def resolve_name(Student, info):
        return Student.name

    def resolve_id(Student, info):
        return Student.id

    def resolve_age(Student, info):
        return Student.age


class Query(ObjectType):
    all_student = List(StudentType)
    single_Student = Field(StudentType, key=Int())

    def resolve_all_student(root, info):
        return data.values()

    def resolve_single_Student(root, info, key):
        return data[key]


# schema
schema = Schema(query=Query)


# #query
# query_string = "{allPeople{name,id,age}}"

# print(schema.execute(query_string))
