import pickle

class Employee:
    def __init__(self, empcode, empname, dojoin, salary):
        self.empcode = empcode
        self.empname = empname
        self.dojoin = doj
        self.salary = salary

emp = Employee(106, "ray", "2025-02-01", 90000)

# Serialize
with open("employee.pkl", "wb") as file:
    pickle.dump(emp, file)

# Deserialize
with open("employee.pkl", "rb") as file:
    loaded_emp = pickle.load(file)
    print(vars(loaded_emp))
