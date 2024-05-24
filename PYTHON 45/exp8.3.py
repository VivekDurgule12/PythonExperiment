# Vehicle class
class Vehicle:
    def _init_(self, seating_capacity: int):
        """
        Initialize a Vehicle instance.

        :param seating_capacity: The seating capacity of the vehicle.
        """
        self.seating_capacity = seating_capacity

    def calculate_fare(self) -> float:
        """
        Calculate the default fare for any vehicle.

        :return: The default fare (seating capacity * 100).
        """
        return self.seating_capacity * 100


# Bus class (child of Vehicle)
class Bus(Vehicle):
    def _init_(self, seating_capacity: int):
        """
        Initialize a Bus instance.

        :param seating_capacity: The seating capacity of the bus.
        """
        super()._init_(seating_capacity)

    def calculate_fare(self) -> float:
    
        
