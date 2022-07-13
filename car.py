class Car():
    def __init__(self,cn,cmo,cy):
        self.cn=cn
        self.cmo=cmo
        self.cy=cy
        self.odometer_reading = 0
    def gdn(self):
        ln=self.cn+" "+self.cmo+" "+str(self.cy)
        return ln.title()
    
    def read_odometer(self):
        print('This car has '+str(self.odometer_reading)+' miles on it')
        
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print("The car has covered "+str(mileage)+" miles.")
        else:
            print("you can not roll back an odometer. ")
            
    def increament_odometer(self,miles):
        self.odometer_reading += miles
        
class ElectricCar(Car):
    def __init__(self,cn,cmo,cy):
        super().__init__(cn,cmo,cy)
        self.battery_size = 70
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
