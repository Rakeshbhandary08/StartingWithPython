class Color:
   def __init__(self,color):
      self.color=color

class Size:
   def __init__(self,size):
      self.size=size;


class Strength(Color,Size): #Multiple Inheritance
   def __init__(self,color,strength,size):
      Color.__init__(self,color);
      Size.__init__(self,size);
      self.strength=strength

   def callingChai(self):
      print(f"Chai color is {self.color} & strength is {self.strength} of size {self.size} ml")


strength1=Strength("Black","Solid",100)
strength1.callingChai()