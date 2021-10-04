class Animal:
    tale = True
    def speak(self):  
        print("Animal Speaking "+str(self.tale))  
        
#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")
        
d = Dog()  
d.bark()  
d.speak()
print("is tale ?",d.tale)
