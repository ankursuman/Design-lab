class Vehicle:
    def __init__(self,entry_time,exit_time,driver_name,car_plate_number):
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.driver_name = driver_name
        self.car_plate_number = car_plate_number
        
    def vehicle(self):
        if(self.entry_time is None):
            return "entry time cannot be None"
        elif(self.driver_name is None):
            return "driver name cannot be None"
        elif(self.driver_name.isnumeric()):
            return "driver name cannot be a number"
        elif(self.car_plate_number is None):
            return "car plate number cannot be None"
        elif(len(self.car_plate_number) != 10)
            return "enter a valid car plate number"
        else:
            return "true"
