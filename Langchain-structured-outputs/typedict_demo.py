from typing import TypedDict

class Person(TypedDict):
    name:int
    age:int

new_person: Person={'name':'nitish','age':'15'}

print(new_person)