class Robot:
    def __init__(self, name, color, weight):
            self.name = name
            self.color = color
            self.weight = weight
    def introduce_self(self):
        print("My name is " + self.name)

class Person:
    def __init__(someone, name, personality, issitting):
        someone.name = name
        someone.personality = personality
        someone.issitting = issitting
    def sit_down(someone):
        someone.issitting = True
    def stand_up(someone):
        someone.issitting = False
r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry","blue", 40)
p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)
p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()
p2.robot_owned.introduce_self()
