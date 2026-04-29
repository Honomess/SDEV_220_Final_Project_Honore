class Member:
    def __init__(self, member_id, name, membership_type):
        self.member_id = member_id
        self.name = name
        self.membership_type = membership_type

class FitnessClass:
    def __init__(self, class_name, instructor, schedule):
        self.class_name = class_name
        self.instructor = instructor
        self.schedule = schedule
        self.attendance = []

class ManagementSystem:
    def __init__(self):
        self.members = []
        self.classes = []

    def add_member(self, member):
        self.members.append(member)

    def add_class(self, fitness_class):
        self.classes.append(fitness_class)