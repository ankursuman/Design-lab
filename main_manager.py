import datetime
import time
from sensor_module import Slot,Sensor_API,Sensor_manager
from vehicleClass import Vehicle
          
class Display_driver(Veichle,Slot):
    def __init__(self,entry_time,exit_time,driver_name,car_plate_number):
        self.position = None
        Slot.__init__(self)
        
    def getPosition(self,position):
        self.position = position
        
    def Update_status(self,status):
        self.slot_list[self.position] = status
            
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
    
    def get_slot(self):
        for slot in range(1001):
            if self.slot_list[slot] is not True:
                return slot    
          
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

    veichle_list = {}
    veichle_slot_list = {}
    inputt = int(input("Number of available slot: "))
    object2=Main_manager(inputt)
    Run_program = "y"
    _id = 0
    while(Run_program == "y" or Run_program == "Y"): 
        veichle_detected = bool(int(input("veichle detected at entry gate? : ")))
        while (veichle_detected):   
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
                #car_palte = object2.detect_car_plate()
                car_plate = input("enter the car plate number: ")
                driver_name = input("enter driver name: ")
                print("gate opened")
                time.sleep(2)
                print("gate closed")
                entry_time = datetime.datetime.now()  
                object1=Sensor_manager(entry_time,None,driver_name,car_plate)
                veichle_list[car_plate] = object1
                _id+=1
                slot_no = object2.get_slot()
                self.slot_list[slot_no] = True
                veichle_slot_list[car_plate]=slot_no
                object1.detectVeichle(True)
                count = object2.update_available_slot(True)
                print("Current available slots is {}".format(count))
            
            else:
                pass
            
            veichle_detected = bool(int(input("veichle detected at entry gate? : ")))
        
        veichle_detected = bool(int(input("veichle detected at exit gate? : ")))
        while(veichle_detected):
            exitgate_status = None
            if available_slots>0 :
                exitgate_status = bool(input("exit gate status: "))
            
            if( exitgate_status ):
                car_plate = input("enter the car plate number: ")
                exit_obj = veichle_list[car_plate]
                exit_time = datetime.datetime.now()
                object1.exit_time = exit_time
                total_payment = (exit_time.second - exit_obj.entry_time.second )*60
                print("total payable amount is {}".format(total_payment) )
                payment_status = bool(input("payment status: "))
                if payment_status:
                    print("gate opened")
                    time.sleep(3)
                    print("gate closed")
                    slot_no = veichle_slot_list[car_plate]
                    self.slot_list[slot_no] = False
                    count = object2.update_available_slot(False)
                    print("Current available slots is {}".format(count))
                else:
                    print("Payment unsuccessfull")
            
            else:
                exitgate_status = False
            veichle_detected = bool(int(input("veichle detected at exit gate? : ")))

        Run_program = input("Enter y to continue else press any key : ")

    # if object2.display_available_slots():
    #     print(object2.detect_car_plate())
    #     available_slot=object2.display_available_slots()
    #     if available_slot:
    #         if object2.open_entry_gate_signal(True):
    #             print("GateOpened")
    #         if object2.close_entry_gate_signal(True):
    #             print("gateclose")
                
                
                
            
