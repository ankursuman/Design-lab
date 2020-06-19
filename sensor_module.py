from vehicleClass import Vehicle

class Slot:
    def __init__(self):
        self.slot_list = []
        status = False
        for _ in range(1001):
            self.slot_list.append(status)
            
class Sensor_API(Slot,Veichle):
    def __init__(self,entry_time,exit_time,driver_name,car_plate_number):
        Slot.__init__(self)
        Veichle.__init__(self,entry_time,exit_time,driver_name,car_plate_number)
    
    def update_slot(self,slot_no,status):
        self.slot_list[slot_no] = status
        
    def receive_update(self):
        return self.slot_list
    
    def send_details(self):
        pass
        
class Sensor_manager(Slot):
    def __init__(self,entry_time,exit_time,driver_name,car_plate_number):
        Slot.__init__(self)
        Sensor_API.__init__(self,entry_time,exit_time,driver_name,car_plate_number)
        self.Number_of_Vehicle=0
    
    def detectVeichle(self,SensorValue):
        if SensorValue==True:
            self.Number_of_Vehicle+=1
            return "Vehicle Detected"
     
    def send_slot_detail(self):
        return self.slot_list
