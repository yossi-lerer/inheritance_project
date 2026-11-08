from classes.employee import Employee

class Intern(Employee):
    def __init__(self, name, salary,inter_month) -> None:
        if  1 > inter_month or 12 < inter_month:
            raise ValueError("months must be 1-12")
        super().__init__(name, salary)
        self.inter_month = inter_month

    def title(self): # type: ignore
        return "Intern"
    