class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def __str__(self):
        return f'Работник {self.name} ({self.__class__.__name__}) получает {self.calculate_salary():.2f} руб.'


class Manager(Employee):
    BONUS_PER_TEAM_MEMBER = 5000

    def __init__(self, name, base_salary, team_size):
        super().__init__(name, base_salary)
        self.team_size = team_size

    def calculate_salary(self):
        return super().calculate_salary() + self.team_size * self.BONUS_PER_TEAM_MEMBER


class Developer(Employee):
    LEVEL_COEFFICIENTS = {'junior': 1.0, 'middle': 1.3, 'senior': 1.6}
    BASE_WAGES = 1000

    def __init__(self, name, base_salary, level, overtime_hours=0):
        super().__init__(name, base_salary)
        self.level = level
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        coefficient = self.LEVEL_COEFFICIENTS[self.level]

        return super().calculate_salary() * coefficient + self.overtime_hours * self.BASE_WAGES
