from datetime import date


class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))


def check_if_the_user_is_an_adult(func):
        def wrapper(user, *args):
            try:
                if user.age < 18:
                    raise
                func(user, *args)
            except:
                print("Usuario menor de edad")
        return wrapper


@check_if_the_user_is_an_adult
def perform_action(user):
    print("Usuario mayor de edad")


user1 = User(date(2025, 1, 1))
perform_action(user1)
user2 = User(date(2005, 1, 1))
perform_action(user2)