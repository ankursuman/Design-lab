from vehicleClass import Vehicle
import unittest

class TestVehicle(unittest.TestCase):

    def test_if_true(self):
        obj = Vehicle("11:30:30",None,"abcd","ABCD123456")
        result = obj.vehicle()
        self.assertEqual(result,"true")
    def test_entry_time(self):
        obj = Vehicle(None,None,"abcd","ABCD123456")
        result = obj.vehicle()
        self.assertEqual(result,"entry time cannot be None")
    def test_driver_name_if_none(self):
        obj = Vehicle("11:30:30",None,None,"ABCD123456")
        result = obj.vehicle()
        self.assertEqual(result,"driver name cannot be None")
    def test_driver_name_if_number(self):
        obj = Vehicle("11:30:30",None,"1234","ABCD123456")
        result = obj.vehicle()
        self.assertEqual(result,"driver name cannot be a number")
    def test_car_plate_number_if_none(self):
        obj = Vehicle("11:30:30",None,"abcd",None)
        result = obj.vehicle()
        self.assertEqual(result,"car plate number cannot be None")
    def test_car_plate_number_if_not_valid(self):
        obj = Vehicle("11:30:30",None,"abcd","Ab1234")
        result = obj.vehicle()
        self.assertEqual(result,"enter a valid car plate number")
    
    def test_read_write_from_file(self):
        obj = vehicle("11:30:30",None,"abcd","ABCD123456")
        reslut = obj.file_search("ABCD123456")
        obj.write_exit_time(2,result,"12.59.58")
        
        

if __name__ == "__main__":
    unittest.main()
