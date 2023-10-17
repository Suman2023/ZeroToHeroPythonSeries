# INHERITANCE


class Person:
    def __init__(self, name, age):
        print("Calling Person")
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, id):
        print("calling Student")
        super().__init__(name, age)
        # self.name = name
        # self.age = age
        self.id = id

    def display_student_info(self):
        # print(f"Name: {self.name}")
        # print(f"Age: {self.age}")
        super().display_person_info()
        print(f"Id: {self.id}")


student1 = Student("ABC", 1, "123")
print(student1.name)
print(student1.age)
# student1.display_person_info()
student1.display_student_info()


class Camera:
    def click_photo(self):
        print("Clicking a Photo")

    def record_video(self):
        print("Recording a Video")


class Player:
    def play_music(self):
        print("Playing a Music")

    def play_video(self):
        print("Playing Video")


class SmartPhone(Camera, Player):
    def boot(self):
        print("Starting the Phone")


# camera = Camera()
# camera.click_photo()
# camera.record_video()
# camera.play_music()

smartphone = SmartPhone()
smartphone.boot()
smartphone.click_photo()
smartphone.play_music()
