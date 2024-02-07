import random

import arcade
# 10.0 Jedi Training (15pts)  Name:________________

'''
CLASSY ANIMALS (5pts)
---------------------
 A. Write code that defines a class named Animal:
     * Add a constructor for the Animal class that prints 'An animal has been born.'
     * Add an attribute for the animal name.
     * Add an eat() method for Animal that prints 'Munch munch.'
     * Add a make_noise() method for Animal that prints 'Grrr says [animal name].'

     
 B. Write code that defines a class named Cat:
     * Make Animal the parent.
     * Add a constructor for Cat that prints 'A cat has been born.'
     * Modify the constructor so it calls the parent constructor as well.
     * Add a make_noise() method for Cat that prints 'Meow says [animal name].'

     
 C. Write code that defines a class named Dog:
     
     * Make Animal the parent.
     * Add a constructor for Dog that prints 'A dog has been born.'
     * Modify the constructor so it calls the parent constructor as well.
     * Add a make_noise() method for Dog that prints 'Bark says [animal name].'

     
 D. Write a main program with:
     
     * Code that creates a cat, two dogs, and an animal with names.
     * Code that calls eat() and make_noise() for each animal.
     
 OUTPUT:
An animal has been born.
A cat has been born.
Munch munch
Meow says (cat name) .
An animal has been born.
A dog has been born.
Munch munch
Bark says (dog name).
An animal has been born.
A dog has been born.
Munch munch
Bark says (another dog name) .
An animal has been born.
Munch munch
Grrr says (animal name) .
'''


class Animal:
    def __init__(self, name):
        self.name = name
        print("An Animal has been born")

    def eat(self):
        print("Munch Munch")

    def make_noise(self):
        print("Grr, says " + self.name)


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("A Cat has been born")

    def make_noise(self):
        print("Meow, says " + self.name)


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("A Dog has been born")

    def make_noise(self):
        print("Bark, says " + self.name)


def main():
    cat = Cat("Dinah")
    cat.eat()
    cat.make_noise()
    dog1 = Dog("Bella")
    dog1.eat()
    dog1.make_noise()
    dog2 = Dog("Edward")
    dog2.eat()
    dog2.make_noise()
    animal = Animal("Jacob")
    animal.eat()
    animal.make_noise()


if __name__ == "__main__":
    main()
    '''
CLASSY BOATS (5pts)
-------------------
Use the following Pseudocode to create this program:

1.) Create a class called Boat( )
2.) Use a constructor that sets two attributes: name and isDocked.
3.) The name should be entered as an argument when the object is created.
4.) The isDocked attribute is a Boolean variable. Set it to True.
5.) Add a method called dock( )
6.) In this method, if the boat is already docked print "(boat name) is already docked."
7.) If it is not docked, print "(boat name) is docking" and set the isDocked attribute to True.
8.) Add another method called undock( )
9.) In this method, if the boat is already undocked print "(boat name) is already undocked."
10.) If it is docked print "(boat name) is undocking" and set the isDocked attribute to False.
11.) Add another class called Submarine( ) that will inherit the Boat( ) class.
12.) In the Submarine( ) class create a method called submerge( ) that will print "(boat name) is submerging" 
if the boat is undocked and "(boat name) can't submerge" if the boat is docked.
'''
print()


class Boat:
    def __init__(self, name):
        self.name = name
        self.isdocked = True

    def dock(self):
        if self.isdocked:
            print(self.name + " is already docked")
        else:
            print(self.name + " is docking")
            self.isdocked = True

    def undock(self):
        if not self.isdocked:
            print(self.name + " is already undocked")
        else:
            print(self.name + " is undocking")
            self.isdocked = False


class Submarine(Boat):
    def __init__(self, name):
        super().__init__(name)

    def submerge(self):
        if self.isdocked:
            print(self.name + " is submerging")
        else:
            print(self.name + " cannot submerge")


'''
Let's Float the Boat
13.) Instantiate an object of the Submarine( ) class. Don't forget to pass in a name.
14.) Call the dock( ) method once
15.) Call the undock( ) method twice
16.) Call the dock( ) method two more times
17.) Call the submerge( ) method once
18.) Call the undock( ) method once
19.) Call the submerge( ) method a final time.
'''


def main():
    boat = Submarine("Foot-Long Sub")
    boat.dock()
    boat.undock()
    boat.undock()
    boat.dock()
    boat.dock()
    boat.submerge()
    boat.undock()
    boat.submerge()


if __name__ == "__main__":
    main()

print()
'''
OUTPUT:
USS Hermon is already docked.
USS Hermon is undocking
USS Hermon is already undocked.
USS Hermon is docking
USS Hermon is already docked.
USS Hermon can't submerge!
USS Hermon is undocking
USS Hermon is submerging!
'''

'''
1000 CIRCLES (5pts)
-------------------
Open an arcade window that is 500 x 300 pixels and named 1000 Circles.
Create a class called Circle.
Initialize the x and y positions to be randomly placed somewhere in the window.
Initialize the radius to be 10 pixels.
Initialize the color to randomized 0-255 RGB color format.
Add a method to the Circle Class called draw_circle and draw the circle.
In the main program, use a for loop to call the Circle class and draw it 1000 times.
Feel free to see what happens if you draw it 10,000 times as well.
'''


SW = 500
SH = 300


class Circle:
    def __init__(self):
        self.x = random.randint(0, SW)
        self.y = random.randint(0, SH)
        self.rad = 10
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw_circle(self):
        arcade.draw_circle_filled(self.x, self.y, self.rad, self.color)


def main():
    arcade.open_window(500, 300, "1000 Circles")
    arcade.set_background_color(arcade.color.PINK)
    arcade.start_render()
    for i in range(1000):
        my_circle = Circle()
        my_circle.draw_circle()
    arcade.finish_render()
    arcade.run()


if __name__ == "__main__":
    main()
