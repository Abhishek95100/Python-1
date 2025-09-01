#wrt a class train which has methods to book a ticket,get status (no of seats) and gt fare information of train running under indian railways.
import random
class TrainNO:

    def __init__(self,trainNO):
         self.trainNo = trainNO
    def book(self,fro,to):
        print(f"Ticket is booked in train NO:{self.trainNo}from{fro}to{to}")
        

    def getstatus(self,):
        print(f"Ticket no:{self.trainNo}is running on time")

    def getfare(self,fro,to):
        print(f"Ticket fare in train no:{self.trainNo}from{fro}to{to}is{random.randint(222,5555)}")


t = TrainNO(12585)
t.book("delhi","koderma")
t.getstatus()
t.getfare("koderma","delhi")