class Vehicle:
    def __init__(self,Max_Speed,Mileage):
        self.Max_Speed = Max_Speed
        self.Mileage = Mileage

Tesla = Vehicle(245,19)
print(f"Max Speed is {Tesla.Max_Speed} \n Mileage is {Tesla.Mileage}")