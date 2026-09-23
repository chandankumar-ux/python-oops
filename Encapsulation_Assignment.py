class Student:

    def __init__(self, name, roll_no, marks):
        self._name = name
        self._roll_no = roll_no
        self._marks = marks

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name
    def set_name(self, name):
        if name.strip() == "":
            print("Name cannot be empty")
        else:
            self._name = name
    # Getter for marks
    def get_marks(self):
        return self._marks


    # Setter for roll number
    def set_marks(self, marks):
        if 1 <= marks <= 100:
            self.marks = marks
        else:
            print("marks number must be between 1 and 100")

        # Getter for roll number
    def get_roll_no(self):
        return self._roll_no
    
    # Setter for marks
    def set_marks(self, marks):
        if marks >= 0:
            self._marks = marks
        else:
            print("Marks cannot be negative")
s1=Student("chandan",2201326288,98)
print(s1.get_marks())