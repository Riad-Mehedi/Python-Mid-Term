from datetime import datetime

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seat = [[0 for _ in range(cols)] for _ in range(rows)]

    def entry_show(self, movie_name, id, time):
        show = (movie_name, id, time)
        self.show_list.append(show)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self, show_id, seats_to_book):
        if show_id in self.seats:
            show_seats = self.seats[show_id]
            for rows, cols in seats_to_book:
                if 1 <= rows <= self.rows and 1 <= cols <= self.cols:
                    if show_seats[rows - 1][cols - 1] == 0:
                        show_seats[rows - 1][cols - 1] = 1
                    else:
                        print("Seat is already booked.")
                        return False
                else:
                    print("Invalid seat.")
                    return False
            return True
        else:
            print("Show not found.")
            return False

    def view_show_list(self):
        for show in self.show_list:
            print(show)

    def view_available_seats(self, show_id):
        if show_id in self.seats:
            show_seats = self.seats[show_id]
            print(f"Available seats for show {show_id}:")
            for rows in show_seats:
                print(" ".join(map(str, rows)))
        else:
            print("Show not found.")


class Star_Cinema:
    def __init__(self):
        self.hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

    def hall_by_no(self, hall_no):
        for hall in self.hall_list:
            if hall.hall_no == hall_no:
                return hall
        return None


def view_all_shows(cinema):
    for hall in cinema.hall_list:
        print(f"\nHall No: {hall.hall_no}")
        for movie_name, show_id, time in hall.show_list:
            formatted_time = datetime.strptime(time, "%I:%M %p").strftime("%d/%m/%y %I:%M%p")
            line = f"Movie_name = {movie_name.ljust(8)} Movie_ID = {show_id.ljust(6)} Time = {formatted_time}"
            print(line)


def view_available_seats(cinema, show_id):
    hall = None
    for i in cinema.hall_list:
        if show_id in i.seats:
            hall = i
            break
    if hall:
        hall.view_available_seats(show_id)
    else:
        print("Show not found.")


def book_tickets(cinema, show_id):
    hall = None
    for i in cinema.hall_list:
        if show_id in i.seats:
            hall = i
            break
    if hall:
        try:
            count = int(input("Enter the number of seats to book: "))
            booking_seat = []
            for _ in range(count):
                seat_input = input(f"Enter seat {_ + 1} (for example: row-col, e.g., 1-2): ")
                seat = tuple(map(int, seat_input.split('-')))
                booking_seat.append(seat)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        if hall.book_seats(show_id, booking_seat):
            print("Booking successful.")
        else:
            print("Booking failed. Please provide correct information.")
    else:
        print("Show not found.")


cinema = Star_Cinema()
hall1 = Hall(rows=10, cols=10, hall_no=1)
hall2 = Hall(rows=10, cols=10, hall_no=2)

hall1.entry_show(movie_name='Jawan',id='100', time='10:00 PM')
hall1.entry_show(movie_name='Pathan', id='101', time='1:00 PM')
hall1.entry_show(movie_name='Dunky', id='103', time='4:00 PM')

hall2.entry_show(movie_name='KGF', id='201', time='11:00 PM')
hall2.entry_show(movie_name='KGF 2', id='202', time='2:00 PM')
hall2.entry_show(movie_name='Salaar', id='203', time='5:00 PM')

cinema.entry_hall(hall1)
cinema.entry_hall(hall2)

while True:
    print('\n')
    print('Here are the Options: ')
    print("1. View all shows today")
    print("2. View available seats")
    print("3. Book tickets")
    print("4. Exit")

    option = input("Enter the option between 1 to 4: ")

    if option == '1':
        view_all_shows(cinema)
    elif option == '2':
        show_id = input("Enter Show ID: ")
        view_available_seats(cinema, show_id)
    elif option == '3':
        show_id = input("Enter Show ID: ")
        book_tickets(cinema, show_id)
    elif option == '4':
        print("Goodbye")
        break
    else:
        print("Invalid. Please choose a valid option.")
