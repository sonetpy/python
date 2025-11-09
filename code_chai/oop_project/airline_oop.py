import random
import string
from datetime import datetime

# -------------------------
# Helper functions
# -------------------------
def random_pnr(length=6):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

def booking_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# -------------------------
# Base Class: Passenger
# -------------------------
class Passenger:
    capacity = 180

    def __init__(self, first_name, last_name):
        self.first_name = first_name.strip().title()
        self.last_name = last_name.strip().title()
        self.pnr = random_pnr()
        self.booking_time = booking_time()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.full_name} | PNR: {self.pnr}"

# -------------------------
# Subclass: FrequentFlyer
# -------------------------
class FrequentFlyer(Passenger):
    def __init__(self, first_name, last_name, miles=0, tier='Bronze'):
        super().__init__(first_name, last_name)
        self.miles = miles
        self.tier = tier.title()
        self.update_tier()

    def add_miles(self, miles):
        self.miles += miles
        self.update_tier()

    def update_tier(self):
        if self.miles >= 10000:
            self.tier = 'Gold'
        elif self.miles >= 5000:
            self.tier = 'Silver'
        else:
            self.tier = 'Bronze'

    def __str__(self):
        return f"{super().__str__()} | {self.tier} Member ({self.miles} miles)"

# -------------------------
# Flight Class (uses composition, NOT inheritance)
# -------------------------
class Flight:
    def __init__(self, flight_number, origin, destination, capacity=180):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, passengers):
        if not isinstance(passengers, Passenger):
            print("❌ Only Passenger or FrequentFlyer objects can be added.")
            return False
        if len(self.passengers) < self.capacity:
            self.passengers.append(passengers)
            print(f"✅ Seat booked for {passengers.full_name} on flight {self.flight_number} | Seats: {len(self.passengers)}/{self.capacity}")
        else:
            print(f"❌ Flight {self.flight_number} is FULL! Cannot add {passengers.full_name}")

    @property
    def seats_available(self):
        return f"Seats Available: {self.capacity - len(self.passengers)}"
    
    def __str__(self):
        return (f"Flight {self.flight_number}: {self.origin} → {self.destination} | "
                f"Occupied: {len(self.passengers)}/{self.capacity} | "
                f"Available: {self.seats_available}")

# =========================
# TESTING THE CODE
# =========================
if __name__ == "__main__":
    random.seed(42)  # For reproducible PNRs during testing

    # Create a flight
    flight = Flight("AI202", "Delhi", "Mumbai", capacity=5)  # Small capacity for testing
    print(flight)
    print("-" * 60)

    # Create passengers
    p1 = Passenger("rahul", "kumar")
    p2 = FrequentFlyer("priya", "singh", miles=7500)
    p3 = Passenger("amit", "sharma")
    p4 = FrequentFlyer("neha", "verma", miles=12000)
    p5 = Passenger("vikas", "mehta")
    p6 = Passenger("sonia", "gandhi")

    # Book passengers
    flight.add_passenger(p1)
    flight.add_passenger(p2)
    flight.add_passenger(p3)
    flight.add_passenger(p4)
    flight.add_passenger(p5)
    flight.add_passenger(p6)  # Should fail

    print("-" * 60)
    print("Final Flight Status:")
    print(flight)
    print(f"{flight.seats_available} seats available")

    print("-" * 60)
    print("Passenger Manifest:")
    for passenger in flight.passengers:
        print(f"  • {passenger}")

    # Test mileage upgrade
    print("-" * 60)
    p2.add_miles(4000)
    print(f"After adding 4000 miles: {p2}")