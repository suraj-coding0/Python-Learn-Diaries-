# ******* Method Overriding in Python *******

# Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.

class Shape:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def area(self):
      return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
      self.radius = radius
      super().__init__(radius, radius)

    def area(self):
        return 3.14 *  super().area()
      
# rec = Shape(3, 5)
# print(rec.area())

c = Circle(5)
print(c.area())



# In conclusion, method overriding is a powerful feature in Python that allows you to customize the behavior of a class based on its specific needs. By using method overriding, you can create more robust and reliable code, and ensure that your classes behave in the way that you need them to. Additionally, by using the super function, you can extend the behavior of a base class method, rather than replace it, giving you even greater flexibility and control over the behavior of your classes.