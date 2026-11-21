
import station



class Game():
    def __init__(self,count,has_ticket,has_backed):
        self.count = count
        self.has_ticket = has_ticket
        self.has_backed = has_backed
        self.location = station.Entrance

    def buy_ticket(self):
        if self.count < 2:
            return False
        self.has_ticket = True
        self.count -= 2
        self.location = station.Ticket_office
        return True

    def buy_from_machine(self):
        if self.count <= 0:
            return False
        if self.has_backed:
            self.count -= 1
            self.location = station.Ticket_Machine
            self.has_ticket = True
            return True
        else:
            return False

    def pick_up_backed(self):
        if self.has_backed:
            return False
        else:
            self.has_backed = True
        self.count -= 1
        self.location = station.Lockers
        return True

    def go_to_platform(self):
        if self.count <= 0:
            return False
        self.count -= 1
        self.location = station.Platform
        return self.has_ticket and self.has_backed