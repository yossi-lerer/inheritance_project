from classes.employee import Employee
class Manager(Employee):
    def __init__(self, name, salary, bonus) -> None:
        super().__init__(name, salary)
        self.bonus = bonus

    def title(self): # type: ignore
        return "Manager"
    
    def monthly_cost(self):
        return self.salary + self.bonus

    def describe(self):
        return f"{self.name} ({self.title()}): {self.monthly_cost()}"
