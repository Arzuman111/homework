class Car():
    def __init__(self,
                name: str,
                year: int,
                sign: str,
                speed: float,
                consumption: float,
                tank_size: float
                ) -> None:
        self.name = name
        self.year = year
        self.__sign__ = sign
        self.speed = speed
        self.consumption = consumption
        self.tank_size = tank_size
        self.__fuel__ = 20.0

        
    def calculate_time(self, distance: float) -> float:
        """Calculate time needed to travel distance.
        Parameters:
        -----------
            distance (float):           [Distance wished to travel]

        Returns:
        --------
            float:                      [Time needed to travel that distance]
        """
        return distance / self.speed

    def register(self, new_sign_number: str) -> bool:
        """Check if new sign is valid and register it if yes.

        Validation means, the first two chars of new sign must be digits,
        followed by two uppercase letters and 3 digits.
        Also, if car is already registered, return False and do not
        change anything.

        Parameters:
        -----------
            new_sign_number (str):      [New sign number]

        Returns:
        --------
            bool:                       [Registered or not]
        """
        if self.__sign__:
            return False
        if (len(new_sign_number) == 7 and
            new_sign_number[:2].isdigit() and
            new_sign_number[2:4].isalpha() and
            new_sign_number[2:4].isupper() and
            new_sign_number[4:].isdigit()):
            self.__sign__ = new_sign_number
            return True
        return False

    def fill(self, fuel_amount: float) -> None:
        """Fill car tank with the amount specified.

        Fill car tank, but do not exceed the tank's capacity.


        Parameters:
        ----------
            fuel_amount (float):        [Amount needed to be filled]
        """
        self.__fuel__ = self.__fuel__ + fuel_amount
        if self.__fuel__ > self.tank_size:
            self.__fuel__ = self.tank_size
        print(f'Tank filled to   {self.__fuel__} liter, Tank size:{self.tank_size} liters')



    def go(self, distance: float) -> bool:
        """Travel providen distance

        Calculate the fuel amount needed to be spent on the distance.
        If there is enough fuel, calculate how much fuel is left after distance,
        write the result in car's fuel amount field and return True.
        If there isn't enough fuel, return False.

        Parameters:
        -----------
            distance (float):           [Distance wished to travel]

        Returns:
        --------
            bool:                      [Traveled or not]
        """
        fuel_needed = (distance/100)*self.consumption

        if self.__fuel__ >= fuel_needed:
            self._fuel__ = self.__fuel__ - fuel_needed
            return True
        return False

    # # # # # # # # # # # # # # # # # # GETTERS # # # # # # # # # # # # # # # # # #

    def get_sign(self) -> str:
        """Return car registration sign."""
        return self.__sign__



    def get_fuel(self) -> float:
        """Return left fuel amount."""
        return self.__fuel__


    def max_distance_can_travel(self) -> float:
        """Return max distance car can travel with current fuel amount"""
        return (self.__fuel__/self.consumption) * 100


car = Car(name="Toyota Camry", year=2020, sign="", speed=120.0, consumption=15.0, tank_size=100.0)


distance_travel = car.calculate_time(2400.0)
print(distance_travel)

registered = car.register("99AA999")
print(registered)

go1 = car.go(50)
print(go1)

car.fill(30)
car.fill(20)

get_sign1 = car.get_sign()
print(get_sign1)

get_fuel1 =car.get_fuel()
print(get_fuel1)

max_distance_can_travel1 = car.max_distance_can_travel()
print(max_distance_can_travel1)






# Write an example for usage of your Car class.
# # # # # # # # # #
# YOUR CODE HERE! #
# # # # # # # # # #

















