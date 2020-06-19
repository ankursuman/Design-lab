import datetime
class Veichle:
    def __init__(self,entry_time,exit_time,driver_name,car_plate_number):
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.driver_name = driver_name
        self.car_plate_number = car_plate_number
        
class Slot:
    def __init__(self):
        self.slot_list = []
        status = False
        for _ in range(1001):
            self.slot_list.append(status)
          
class Display_driver(Veichle,Slot):
    def __init__(self,entry_time,exit_time,driver_name,car_plate_number):
        self.position = None
        Slot.__init__(self)
        
    def getPosition(self,position):
        self.position = position
        
    def Update_status(self,status):
        self.slot_list[self.position] = status
        

class Sensor_API(Slot,Veichle):
    def __init__(self,entry_time,exit_time,driver_name,car_plate_number):
        Slot.__init__(self)
        Veichle.__init__(self,entry_time,exit_time,driver_name,car_plate_number)
        
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
        
class Main_manager(Slot,Veichle):
    
    def __init__(self,available_Slot):
        self.notavailable=0
        self.available_Slot = available_Slot
        Slot.__init__(self)
        
    def recieve_update(self):
        return self.slot_list
    
    def display_available_slots(self):
        available_slot = []
        index = 0
        self.notavailable=0
        for slot in self.slot_list:
            if slot:
                available_slot.append(index)
            else:
                self.notavailable+=1
            index+= 1

        return self.available_Slot
        # if self.notavailable==len(self.slot_list):
        #     print("We dont have available slot, Sorry for any inconnvenience")
        #     return False
                
        # return True
    
    def update_available_slot(self,status_):
        if status_:
            self.available_Slot-=1
            return self.available_Slot
        else:
            self.available_Slot+=1
            return self.available_Slot

        
    def open_entry_gate_signal(self,signal):
        if signal:
            for slot in self.slot_list:
                if slot==False:
                    return False
            
            return True
        
    def close_entry_gate_signal(self,signal):
        if signal:
            return True
        
    def detect_car_plate(self):
        return self.car_plate_number
        
    def check_slot_update(self):
        return self.slot_list

    def payment_gateway(self):
        pass


        
        
if __name__ == "__main__":

    inputt = int(input("Number of available slot: "))
    object2=Main_manager(inputt)
    entrygate_status = bool(input("entry gate status: "))
    available_slots = object2.display_available_slots()
    if(available_slots == 1000):
        print("All slots are available right now ")
    if(available_slots == 0):
        print("No slot is available")

    print("the available slots is {}".format(available_slots))
    object1 = None
    if( entrygate_status and available_slots == 0):
        print("No slot is available right now")

    elif( entrygate_status and available_slots>0 and available_slots<1001):
        print("gate opened")
        #car_palte = object2.detect_car_plate()
        car_plate = input("enter the car plate number: ")
        driver_name = input("enter driver name: ")
        entry_time = datetime.datetime.now()  
        object1=Sensor_manager(entry_time,None,driver_name,car_plate)
        object1.detectVeichle(True)
        count = object2.update_available_slot(True)
        print("Current available slots is {}".format(count))
        print("gate closed")
       

    exitgate_status = bool(input("exit gate status: "))
    
    if( exitgate_status ):
        car_plate = input("enter the car plate number: ")
        exit_time = datetime.datetime.now()
        object1.exit_time = exit_time
        total_payment = (exit_time.hour - entry_time.hour )*30
        print("total payable amount is {}".format(total_payment) )
        payment_status = bool(input("payment status: "))
        if payment_status:
            print("gate opened")
            count = object2.update_available_slot(False)
            print("Current available slots is {}".format(count))
            print("gate closed")
        else:
            print("Payment unsuccessfull")
    
    exitgate_status = False

    # if object2.display_available_slots():
    #     print(object2.detect_car_plate())
    #     available_slot=object2.display_available_slots()
    #     if available_slot:
    #         if object2.open_entry_gate_signal(True):
    #             print("GateOpened")
    #         if object2.close_entry_gate_signal(True):
    #             print("gateclose")
                
                
                
            
