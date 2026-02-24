from abc import ABC, abstractmethod


class User(ABC):
    @abstractmethod
    def get_role(self):
        pass
    
    @abstractmethod
    def has_permission(self, permission):
        pass

class AdminUser(User):
    def __init__(self, name):
        self.name = name

    def get_role(self):
        self.role = "Admin"

    def has_permission(self, permission):
        return True


class RegularUser(User):
    def __init__(self,name):
        self.name = name

    def get_role(self):
        self.role = "RegularUser"

    def has_permission(self, permission):
        if permission == "read":
            self.permission = True
            return self.permission
        self.permission = False
        return self.permission


user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

user1.get_role()
print(f"\n{user1.name} {[user1.role]}")
print(user1.has_permission("delete"))
print(user1.has_permission("read"))
print()

user2.get_role()
print(f"\n{user2.name} {[user2.role]}")
print(user2.has_permission("delete"))
print(user2.has_permission("read"))
print()