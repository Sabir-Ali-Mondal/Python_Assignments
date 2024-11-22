# Grandparent class
class Grandfather:
    def __init__(self, name):
        self.name = name

    def show_role(self):
        print(f"{self.name} is the Grandfather.")

# Father class inheriting from Grandfather
class Father(Grandfather):
    def __init__(self, name, grandparent_name):
        super().__init__(grandparent_name)
        self.father_name = name

    def show_role(self):
        super().show_role()
        print(f"{self.father_name} is the Father.")

# Uncle class inheriting from Grandfather
class Uncle(Grandfather):
    def __init__(self, name, grandparent_name):
        super().__init__(grandparent_name)
        self.uncle_name = name

    def show_role(self):
        super().show_role()
        print(f"{self.uncle_name} is the Uncle.")

# Child class inheriting from Father
class Child(Father):
    def __init__(self, name, father_name, grandparent_name):
        super().__init__(father_name, grandparent_name)
        self.child_name = name

    def show_role(self):
        super().show_role()
        print(f"{self.child_name} is the Child (Uncle's Brother's Son).")

# Main function to create objects based on user input
def main():
    grandparent_name = input("Enter the name of your Grandfather: ")
    father_name = input("Enter the name of your Father: ")
    uncle_name = input("Enter the name of your Uncle: ")
    child_name = input("Enter your name (the Child): ")

    print("\nFamily Hierarchy:\n")

    # Creating objects and showing roles
    grandfather = Grandfather(grandparent_name)
    grandfather.show_role()

    father = Father(father_name, grandparent_name)
    father.show_role()

    uncle = Uncle(uncle_name, grandparent_name)
    uncle.show_role()

    child = Child(child_name, father_name, grandparent_name)
    child.show_role()

if __name__ == "__main__":
    main()
