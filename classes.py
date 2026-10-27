# what is OOPs concept ?
# encapsulation : encapsulating data and functionality together.
# inheritance   : inherting property and methods of parents
#               : inheritance is an is-a relationship
#               : apple is-a Fruit, car is-a vehicle, dog is-a animal
# polymorphism  : same object/method/function acting differently with scenario change
#               : polymorphism is supported in python via method overriding and operator overloading
#               : in classic sense, python does not support overloading

# polymorphism in python with operator overloading
# Operator overloading is another type of polymorphism in which the same operator performs
# various operations depending on the operands. Python allows for operator overloading.
# 10 + 20 = 30 while '10' + '20 = '1020'
# [10] * 2 = [10, 10] while 10 * 2 = 20 while *args  give arguments

# polymorphism in python with function
# len() function acts differently for different objects

# polymorphism in python with class
# overriding same method name with different classes/inherting classes

# what is class and object ?
# class  : a skelton/bluprint of for an object.
# object : an object is collection of attribute and methods.

# what is class attribute and object attribute ?
# class attribute is meaned for sharing attribute values with different objects.
# object attribute is meaned for unique values with different objects.

# what is an abstract class ?
# abstract class is an interface class which should be implemented(all) by sub/child classes.

# what is method overriding ?
# the method in the subclass overrides the method in the superclass. concept called overriding.

# what is method overloading ?
# with variable number of arugument defining same method is called overloading.(not possible with python)

# what is operator overloading ?
# defining different behaviour for same operator is called operator overloading.

# what is difference between inheritance and composition ?
# use inheritance when you want to extend/modify feature/methods of parent class.
# use composition(create object inside class and use its object) when features modify/extend not required.

# what is duck typing ?
# The idea is that you don't need to specify a type(variable/object) in order to invoke an existing method on an object.
# if a method is defined on it, you can invoke it.

# what is method resolution order MRO in case of multiple inheritance ?
# method resolution is done with left most class. if found a method there it will be returned.
# otherwise it will follow order of left-to-right for MRO.

# decorators with classes : @classmethod, @staticmethod, @abstractmethod, @property

# @abstractmethod : to declare a method as abstract method

# @classmethod : transform a method into a class method.
#              : class method receives the class as an implicit first argument(cls).
#              : C.f()/C().f()
#              : if a class method is called for a derived class,
#              : the derived class object is passed as the implied first argument.

# @staticmethod : transform a method into a static method.
#               : a static method does not receive an implicit first argument.
#               : can be called C.f()/C().f()

# @property     : used to create getter, setter, deleter, doc
#               : property(fget, fset, fdel, doc)
#               : using property decorator can avoid breaking client code

