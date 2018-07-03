class SchoolMember:
    """Represents any school member."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {}'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('Name:"{}" Age:""{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''Represent a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.slary = salary
        print('(Initialized Teacher: {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.slary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Alya', 18, 95)

# Print a blank line
print()

members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()