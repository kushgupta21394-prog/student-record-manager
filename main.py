# Student Record Manager - uses a singly linked list
FILE_NAME = "students.txt"


class Node:
    def __init__(self, roll, name, branch, marks):
        self.roll = roll
        self.name = name
        self.branch = branch
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def add(self, roll, name, branch, marks):
        if self.search(roll):
            print("Roll number already exists.")
            return
        new_node = Node(roll, name, branch, marks)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print("Student added.")

    def search(self, roll):
        current = self.head
        while current:
            if current.roll == roll:
                return current
            current = current.next
        return None

    def update(self, roll, name, branch, marks):
        node = self.search(roll)
        if node is None:
            print("Student not found.")
            return
        node.name, node.branch, node.marks = name, branch, marks
        print("Record updated.")

    def delete(self, roll):
        current, previous = self.head, None
        while current:
            if current.roll == roll:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                print("Record deleted.")
                return
            previous, current = current, current.next
        print("Student not found.")

    def to_list(self):
        items, current = [], self.head
        while current:
            items.append(current)
            current = current.next
        return items

    def display(self, items=None):
        items = self.to_list() if items is None else items
        if not items:
            print("No records.")
            return
        print(f"{'Roll':<8}{'Name':<20}{'Branch':<10}{'Marks':<6}")
        for s in items:
            print(f"{s.roll:<8}{s.name:<20}{s.branch:<10}{s.marks:<6}")

    def sort_by_marks(self):
        self.display(sorted(self.to_list(), key=lambda s: s.marks, reverse=True))

    def save(self):
        with open(FILE_NAME, "w") as f:
            for s in self.to_list():
                f.write(f"{s.roll},{s.name},{s.branch},{s.marks}\n")
        print("Saved to", FILE_NAME)

    def load(self):
        try:
            with open(FILE_NAME) as f:
                for line in f:
                    roll, name, branch, marks = line.strip().split(",")
                    self.add(roll, name, branch, float(marks))
        except FileNotFoundError:
            pass


def get_marks():
    while True:
        try:
            return float(input("Marks: "))
        except ValueError:
            print("Enter a number.")


def main():
    students = StudentList()
    students.load()
    while True:
        print("\n1.Add 2.Search 3.Update 4.Delete 5.Show all")
        print("6.Sort by marks 7.Save 8.Exit")
        choice = input("Choose: ")
        if choice == "1":
            students.add(input("Roll no: "), input("Name: "), input("Branch: "), get_marks())
        elif choice == "2":
            s = students.search(input("Roll no: "))
            students.display([s] if s else [])
        elif choice == "3":
            students.update(input("Roll no: "), input("New name: "), input("New branch: "), get_marks())
        elif choice == "4":
            students.delete(input("Roll no: "))
        elif choice == "5":
            students.display()
        elif choice == "6":
            students.sort_by_marks()
        elif choice == "7":
            students.save()
        elif choice == "8":
            students.save()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()
