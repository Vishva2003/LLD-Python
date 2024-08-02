from datetime import datetime

class ParkingSpot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.is_occupied = False
        self.vehicle = None

    def park_vehicle(self, vehicle):
        self.is_occupied = True
        self.vehicle = vehicle

    def remove_vehicle(self):
        self.is_occupied = False
        self.vehicle = None


class Vehicle:
    def __init__(self, license_plate, type):
        self.license_plate = license_plate
        self.type = type


class ParkingLot:
    def __init__(self, num_spots):
        self.spots = [ParkingSpot(i) for i in range(num_spots)]

    def find_available_spot(self):
        for spot in self.spots:
            if not spot.is_occupied:
                return spot
        return None

    def park_vehicle(self, vehicle):
        spot = self.find_available_spot()
        if spot:
            spot.park_vehicle(vehicle)
            return spot
        return None

    def remove_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.vehicle == vehicle:
                spot.remove_vehicle()
                return spot
        return None


class Ticket:
    def __init__(self, ticket_id, spot_id, license_plate):
        self.ticket_id = ticket_id
        self.spot_id = spot_id
        self.license_plate = license_plate
        self.timestamp = datetime.now()


class ParkingLotSystem:
    def __init__(self, num_spots):
        self.parking_lot = ParkingLot(num_spots)
        self.tickets = {}
        self.ticket_counter = 0

    def issue_ticket(self, vehicle):
        spot = self.parking_lot.park_vehicle(vehicle)
        if spot:
            self.ticket_counter += 1
            ticket = Ticket(self.ticket_counter, spot.spot_id, vehicle.license_plate)
            self.tickets[vehicle.license_plate] = ticket
            return ticket
        return None

    def close_ticket(self, vehicle):
        ticket = self.tickets.pop(vehicle.license_plate, None)
        if ticket:
            self.parking_lot.remove_vehicle(vehicle)
            return ticket
        return None

    def display_parking_lot(self):
        for spot in self.parking_lot.spots:
            if spot.is_occupied:
                print(f'Spot {spot.spot_id}: Occupied by {spot.vehicle.license_plate}')
            else:
                print(f'Spot {spot.spot_id}: Available')
        print()

parking_system = ParkingLotSystem(5)
car1 = Vehicle('ABC123', 'Car')
car2 = Vehicle('XYZ789', 'Car')

ticket1 = parking_system.issue_ticket(car1)
ticket2 = parking_system.issue_ticket(car2)

parking_system.display_parking_lot()

parking_system.close_ticket(car1)
parking_system.display_parking_lot()
