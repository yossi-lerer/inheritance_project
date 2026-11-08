class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def title(self):
        return "Employee"
    
    def monthly_cost(self):
        return self.salary

    def describe(self):
        return f"{self.name} ({self.title()}): {self.monthly_cost()}"
