# class: what is class? class is like a vanding machenine that a have the food or drinks and by input the number is give you the thing that you ordered,
#so class is the stuff inside it have all the info in one place the data base ansd you job is to use this data base. we can add functions

class mml:

    def __init__(self,name,age,country):
        self.name = name
        self.age=age
        self.country=country

max_info=mml("MAX","12","japan")

sara_info=mml("SARA","19","egypt")
    
print(sara_info.name, sara_info.age)    

print(max_info.name,max_info.country)


# text file
#first way

file_read = open('./file_read_test.txt', 'r')
file = file_read.read()
print(file)
file_read.close()
# better way

with open('./file_read_test.txt', 'r') as stream:
    files=stream.readlines()
    print(files)


# genaratour 
def loll():
    lol= [1,2,4,5,6,7]
    for i in lol:
        yield i
l=loll()
print(l)

for value in l:
    print(value)

class m():
    def __init__(self,name,age,county):
        self.name= name
        self.age=age
        self.country= county
    @property
    def info(self):
       return f"{self.name}, {self.age}, {self.country}"
    @info.setter
    def info(self,namm):
       self.name,self.age,self.country= namm.split(" ") 
    

k=m("l","k","g")
k.info= ("mahmoud 19 egypt")
print(k.info)

class Dog:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_breed(cls, breed_name):
        # Create a Dog object with name based on breed
        name = breed_name + " Doggo"
        return cls(name)  # create and return Dog object
my_dog = Dog.from_breed("Bulldog")
print(my_dog.name)  # prints: Bulldog Doggo
