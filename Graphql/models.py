from collections import namedtuple

Student = namedtuple("Student", ['name', 'id', 'age'])

data = {
    1: Student("Puja", 101, 28),
    2: Student("Dipika", 102, 25),
    3: Student("Kaveri", 103, 20),
    4: Student("Rupali", 104, 21)
}
