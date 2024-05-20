# Ticket reservation system

class Event:
    def __init__(self, name, date, ticket_price):
        self.name = name
        self.date = date
        self.ticket_price = ticket_price

    def get_info(self):
        print(f"Event: {self.name}")
        print(f"Date: {self.date}")
        print(f"Price: {self.ticket_price}")

class Concert(Event):
    def __init__(self, name, date, ticket_price, max_participants, genre):
        super().__init__(name, date, ticket_price)
        self.max_participants = max_participants
        self.genre = genre

    def get_info(self):
        super().get_info()
        print(f"Max participants: {self.max_participants}")
        print(f"Genre: {self.genre}")
        print()

class Ticket:
    def __init__(self, event, seat_number):
        self.event = event
        self.seat_number = seat_number

    def get_info(self):
        print(f"Event: {self.event.name}")
        print(f"Date: {self.event.date}")
        print(f"Seat: {self.seat_number}")
        print()

class TicketReservationSystem:
    def __init__(self):
        self.available_concerts = []
        self.reserved_tickets = []

    def add_event(self, event):
        self.available_concerts.append(event)

    def show_events(self):
        for event in self.available_concerts:
            event.get_info()

    def make_reservation(self, event, seat_number):
        ticket = Ticket(event, seat_number)
        self.reserved_tickets.append(ticket)
        print(f"Reservation has been completed:")
        ticket.get_info()

    def cancel_reservation(self, ticket):
        if ticket in self.reserved_tickets:
            print(f"Cancelled reservation:")
            ticket.get_info()
            self.reserved_tickets.remove(ticket)
        else:
            print(f"Ticket not found on the tickets list")
            print()

    def print_reservations(self):
        for ticket in self.reserved_tickets:
            ticket.get_info()

event1 = Event("Hip-Hop Festival", "2024-06-15", 59)
event2 = Event("Opener Festival", "2024-07-01", 99)

concert1 = Concert("Asap Rocky", "2024-06-15", 59, 3000, "HipHop")
concert2 = Concert("Tame Impala", "2024-07-01", 99, 5000, "Rock")
concert3 = Concert("Sade", "2024-07-01", 99, 2000, "Jazz")
concert4 = Concert("Kanye West", "2024-06-15", 59, 4000, "HipHop")

res_system = TicketReservationSystem()
res_system.add_event(concert1)
res_system.add_event(concert2)
res_system.add_event(concert3)
res_system.add_event(concert4)

res_system.show_events()

res_system.make_reservation(concert1, "A199")
res_system.make_reservation(concert1, "B03")
res_system.make_reservation(concert2, "F99")
res_system.make_reservation(concert2, "G599")
res_system.make_reservation(concert3, "C11")
res_system.make_reservation(concert3, "H74")
res_system.make_reservation(concert4, "D43")
res_system.make_reservation(concert4, "I02")

res_system.cancel_reservation(res_system.reserved_tickets[0])
res_system.cancel_reservation(res_system.reserved_tickets[2])
res_system.cancel_reservation(res_system.reserved_tickets[4])

print("Reservations:")
res_system.print_reservations()