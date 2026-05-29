# What is a Class?- A class is a blueprint or template. It defines what data a thing has and what it can do.
class Student : 
    def __init__(self,name,branch,cgpa):
        self.name = name    # instance variable 
        self.branch=branch
        self.cgpa=cgpa

# creating method 

    def introduce(self):
        print(f'hi im {self.name} from {self.branch}')
    def eligible(self):
        return self.cgpa >=6.0
    
# creating objects 

s1=Student("aarya","aids",8.67)
s2=Student("alia","aiml",5.6)

s1.introduce()
print(s1.cgpa)
print(s2.eligible())


# INHERITENCE

class Animal :
    def __init__(self , name):
        self.name=name
    def speak(self):
        print(f'{self.name} is speaking')

class Dog (Animal):                  # child class inherits from animal   

    def speak(self):
        print(f" hi ! my name is {self.name} and im speaking")
    def fetch(self):
        print(f' {self.name}is fetching a ball')

d = Dog ( "bruno")
d.fetch()
d.speak()
            