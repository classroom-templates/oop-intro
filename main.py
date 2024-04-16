##########################

# DO NOT MODIFY THIS FILE
# except to comment and uncomment
# as described in the assignment

##########################

from Dog import Dog

def main():

    dog1 = Dog("poodle", 4, 13)
    
    print(dog1.getBreed())
    print(dog1.getAge())
    print(dog1.getWeight())
    dog1.bark()
    print(dog1.getAge())
    dog1.bark()
    print(dog1.getAge())
    print()
    
    dog2 = Dog("rottweiler", -14, 75)
    
    print(dog2.getBreed())
    print(dog2.getAge())
    print(dog2.getWeight())
    dog2.bark()
    print(dog2.getAge())
    dog2.bark()
    print(dog2.getAge())
    print(dog2.setWeight(-3))
    print(dog2.getWeight())
    print()

    dog3 = Dog("sheppard", 5, -7)
    
    print(dog3.getBreed())
    print(dog3.getAge())
    print(dog3.getWeight())
    dog3.bark()
    print(dog3.getAge())
    dog3.bark()
    print(dog3.getAge())
    print()

main()


