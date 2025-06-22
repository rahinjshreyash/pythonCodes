class Elevator :
    occupancy_limit = 8

    def __init__(self, occupants=0,floor=0):
        self.occupants = occupants
        self.floor = floor
        if occupants <= Elevator.occupancy_limit :
            self.occupants = occupants
            print('no of occupants are',occupants)
        else :
            self.occupants =Elevator.occupancy_limit
            print('too many occupants.',occupants-Elevator.occupancy_limit,'are waiting outside') 

    def add_occupants(self,num):
        self.occupants += num

        if self.occupants > Elevator.occupancy_limit :
            print('too many occupants.',self.occupants - Elevator.occupancy_limit,'are remaining outside')
            self.occupants = Elevator.occupancy_limit

    def goto_floor(self,num):
        self.floor += num
        if num > 50 :
           print('floors above 50 do not exist')
           num = 50
        elif num < -5 :
            print('floors below -5 does not exist')
        else :
            print("you are on the",num,'th floor') 
  
    def remain_occupants(self,num):
        self.occupants = self.occupants - num
        if self.occupants <= 0 :
            print('no occupants left')
             

elevator1 = Elevator(5)   
elevator2 = Elevator(15) 
elevator1.add_occupants(12)
elevator1.goto_floor(8)
elevator1.remain_occupants(5)
print(elevator1.__dict__)        
