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
   
    def Store(self):
        f = open("data.txt", "a")
        f.write(str(self.entry_time)+" " +str(self.exit_time)+" "+self.driver_name+" "+self.car_plate_number)
        f.close()
    
    def file_search(self,car_plate_number):
        userInput = car_plate_number
        row=1
        with open("data.txt", 'r') as f:
            for x in f:
                if userInput in x:
                    return row
                    
                else:
                    row+=1


    def change_value(self,column, row, new_value):
        lines = []
        with open('data.txt', 'r+') as file:
            for line in file:
                lines.append(line.rstrip().split())

            lines[row - 1][column - 1] = str(new_value)
            file.seek(0)
            for line in lines:
                line[-1] += "\n"    
                file.write(' '.join(line))
    


