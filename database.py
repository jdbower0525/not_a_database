

class Database:
    def __init__(self, data_filename="data.csv"):
        self.data_filename = data_filename
        self.data = []
        with open(self.data_filename, "r") as f:
            for line in f:
                self.data.append(line.strip())

    def __getitem__(self, user_name):
        for line in self.data:
            if line[0] == user_name:
                return line


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


def main():
    db = Database()
    user1 = ["Hello","World"]
    user2 = ["JohnBower","Password"]
    db.add_user(user1)
    db.add_user(user2)
    print(db.data)
    db.remove_user("JohnBower")
    print(db.data)

if __name__ == '__main__':
    main()
