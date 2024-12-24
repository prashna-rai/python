# employee_data = [
#     {"name":"ram","salary":35000, "bonus":2},
#     {"name":"shyam","salary":35000, "bonus":2},
#     {"name":"hari","salary":35000, "bonus":2},
#     {"name":"gopal","salary":35000, "bonus":2},
#     ]


# for item in employee_data:
#     name = item['name']
#     salary=item["salary"]
#     bonus=item["bonus"]
#     print(name,salary+bonus,)
# # data= {"name":"ram","salary":35000, "bonus":2}
# print(data['bonus']  + data["salary"])

class employee:
    def __init__(self,name,salary,bonus):
        self.name=name
        self.salary=salary
        self.bonus=bonus
    def calculate_total_salary(self):
        return  (self.salary + self.bonus )

    def display_info(self):
        print(f"{self.name}: Total Salary = {self.calculate_total_salary()}")

class list_1:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, salary, bonus):
        self.employees.append(employee(name, salary, bonus))

    def display_all_employees(self):
        for employee in self.employees:
            employee.display_info()

# Initialize list and add employees
manager =list_1()

data = [
    {"name": "ram", "salary": 35000, "bonus": 2},
    {"name": "shyam", "salary": 35000, "bonus": 2},
    {"name": "hari", "salary": 35000, "bonus": 2},
    {"name": "gopal", "salary": 35000, "bonus": 2},
]

for emp in data:
    manager.add_employee(emp['name'], emp['salary'], emp['bonus'])

manager.display_all_employees()
