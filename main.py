class Flight:
    def __init__(self, code, seats, price):
        self.code = code
        self.seats = seats
        self.price = price

    def book(self, qty):
        if qty <= self.seats:
            self.seats -= qty
            return qty * self.price
        return 0

    def info(self):
        return f"{self.code} | Joy: {self.seats} | Narx: {self.price}"


class Airline:
    def __init__(self):
        self.flights = []
        self.cash = 0

    def add_flight(self, f):
        self.flights.append(f)

    def show_flights(self):
        for i, f in enumerate(self.flights):
            print(i, f.info())

    def book_ticket(self, index, qty):
        cost = self.flights[index].book(qty)
        if cost:
            self.cash += cost
            print("Bron qilindi. Narx:", cost)
        else:
            print("Joy yetarli emas")

    def report(self):
        print("Daromad:", self.cash)


air = Airline()
air.add_flight(Flight("UZ101", 120, 900000))
air.add_flight(Flight("UZ202", 80, 1200000))

while True:
    print("\n1.Reyslar 2.Bron 3.Hisobot 0.Exit")
    c = input(">>> ")

    if c == "1":
        air.show_flights()
    elif c == "2":
        air.book_ticket(int(input("Index: ")), int(input("Joy soni: ")))
    elif c == "3":
        air.report()
    elif c == "0":
        break
