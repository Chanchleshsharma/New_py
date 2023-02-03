print("hey")
class human:
  def eating (self):
    print("this is eating :")
    
class student(human):
  def study (self):
    print ("this is study:")
    
obj= student()
obj.study()
obj.eating()
