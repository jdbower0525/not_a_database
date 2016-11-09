import random
import sys
import os

class Database:
    def __init__(self, data_filename="data.csv"):
        self.data_filename = data_filename
        self.data = []
        with open(self.data_filename, "r") as f:
            for line in f:
                self.data.append(line.strip())


    def __getitem__(self, index):
        return self.data[index]


    def _save(self):
        with open(self.data_filename, "w") as f:
            for data in self.data:
                f.write(data)
                f.write("\n")


    def add_user(self, new_user):
        self.data.append(",".join(new_user))
        self._save()


    def remove_user(self, user_name):
        for row in self.data:
            if user_name in row:
                self.data.remove(row)
                self._save()


    def clear(self):
        self.data = []
        self._save()


def user_login():
    db = Database()
    login = input("User Name: ")
    password = input("Password: ")
    for line in db.data:
        new_line = line.split(',')
        if login == new_line[0]:
            if password == new_line[1]:
                clear()
                print("Username: {}\nPassword: {}\nAge: {}\nGender: {}\nOccupation: {}".format(new_line[0], new_line[1], new_line[2], new_line[3], new_line[4]))
                add_item_interface()
            elif password != new_line[1]:
                print("Your login information was invalid. Try again.")
                user_login()
        else:
            continue
    print("Your login information was invalid.")
    user_login()


def add_item_interface():
    db = Database()
    new_choice = input("Would you like to add a user or log out? ")
    if new_choice[0] == 'a':
        user1 = input("What is the new username? ")
        for row in db.data:
            new_row = row.split(',')
            if user1 == new_row[0]:
                print("That username is already taken! Choose another.")
                add_item_interface()
        clear()
        print("Great! That username hasn't been taken!")
        pass1 = input("What would you like {}'s password to be? ".format(user1))
        age1 = input("What is {}'s age? ".format(user1))
        gender1 = input("What is {}'s gender? ".format(user1))
        job1 = input("What is {}'s occupation? ".format(user1))
        new_user = (user1,pass1,age1,gender1,job1)
        db.add_user(new_user)
        add_item_interface()
    else:
        clear()
        main()

def main():
    db = Database()
    login = ''
    password = ''
    user_login()


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
    main()
