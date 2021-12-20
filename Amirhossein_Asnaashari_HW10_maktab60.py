import redis
redis_client = redis.Redis()
redis_admin = "admin"


class Event:
    def __init__(self, date_time, location, total_capacity, remaining_capacity, cost):

        self.date_time = date_time
        self.location = location
        self.total_capacity = total_capacity
        self.remaining_capacity = remaining_capacity
        self.cost = cost

    def ticket(self, number):
        self.total_capacity = self.total_capacity - number
        self.remaining_capacity = self.remaining_capacity - number
        return f'you are going to buy {number} tickets'


class User:
    def __init__(self, first_name, last_name, age, job, number_of_tickets):
        user_number = redis_client.get("user_number").decode('utf-8')

        self.user_number = user_number
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.number_of_tickets = number_of_tickets

    def save(self):
        redis_client.hmset(
            f'user: {self.user_number}:info',
            {
                "name": self.first_name + self.last_name,
                "age": self.age,
                "job": self.job
            }
        )


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def logging(self):
        UserInput = input("what is your username?")
        if UserInput == self.username:
            UserInput = input("what is your password? ")
            if UserInput == self.password:
                print("Welcome")
            else:
                print("that is a wrong password")
        else:
            print("that is a wrong username")


class Cinema(Event):
    def __init__(self, movie, date_time, location, total_capacity, remaining_capacity, cost):
        super().__init__(date_time, location, total_capacity, remaining_capacity, cost)
        self.movie = movie

    def __str__(self):
        return f'choose a theater: {redis_client.lrange("list_of_movies", 0, 5)}'

    def movie_info(self):
        redis_client.hmset(
            f'cinema: {self.movie}:info',
            {
                "date time": self.date_time,
                "location": self.location,
                "total capacity": self.total_capacity,
                "remaining capacity": self.remaining_capacity,
                "cost": self.cost
            }
        )


class Concert(Event):
    def __init__(self, artist, date_time, location, total_capacity, remaining_capacity, cost):
        super().__init__(date_time, location, total_capacity, remaining_capacity, cost)
        self.artist = artist

    def __str__(self):
        return f'choose a theater: {redis_client.lrange("list_of_concerts", 0, 5)}'

    def concert_info(self):
        redis_client.hmset(
            f'concert: {self.artist}:info',
            {
                "date time": self.date_time,
                "location": self.location,
                "total capacity": self.total_capacity,
                "remaining capacity": self.remaining_capacity,
                "cost": self.cost
            }
        )

    def concert_selection(self, artist):
        self.artist = artist


class Theater(Event):
    def __init__(self, theater, date_time, location, total_capacity, remaining_capacity, cost):
        super().__init__(date_time, location, total_capacity, remaining_capacity, cost)
        self.theater = theater

    def __str__(self):
        return f'choose a theater: {redis_client.lrange("list_of_theaters", 0, 5)}'

    def movie_info(self):
        redis_client.hmset(
            f'theater: {self.theater}:info',
            {
                "date time": self.date_time,
                "location": self.location,
                "total capacity": self.total_capacity,
                "remaining capacity": self.remaining_capacity,
                "cost": self.cost
            }
        )


class DiscountAndPayment(Event, User):

    def discount(self):
        if self.job == "admin":
            self.cost = self.number_of_tickets * (self.cost*3)/10
            return f'you have 70% discount: {self.cost}'
        elif self.job == "student":
            self.cost = self.number_of_tickets * (self.cost*5)/10
            return f'you have 50% discount: {self.cost}'
        elif self.job == "employee":
            self.cost = self.number_of_tickets * (self.cost*75)/100
            return f'you have 25% discount: {self.cost}'
        else:
            return f'you dont have any discount: {self.cost}'


cinema = Cinema("Scarface", "2022,1,19", "Dallas", 196, 50, 45)
print(cinema)
disobj = DiscountAndPayment("2022,1,19", "Dallas", 196, 50, 45)
print(disobj)
