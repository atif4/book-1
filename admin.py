class Admin():
    def __init__(self,name,position):
        self.name=name
        self.position=position
    def gdn(self):
        x = self.name+' '+self.position
        return x.title()
class Privileges():
    def __init__(self,power):
        self.power=power
    def dp(self):
        for i in self.power:
            print(a.name+i)
        while self.power:
            z=self.power.pop()
            print(b.position+z)
        
class User(Admin):
    def __init__(self,name,position):
        super().__init__(name,position)
        self.privileges = [' can add post. ',' can select post. ',' can delect post. ',' can be a user. ']
    def show_privileges(self):
        print(self.privileges)
