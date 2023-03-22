class EmployeeData:
    def __init__(self):
        self.num_employees = 0
        self.num_employees = 5
        self.shifts = []
        self.requests = []
        self.num_days = 7
        self.weekly_demands = []
        self.fixed_assignments = []

    def get_num_days(self):
        return self.num_days

    def set_num_employees(self, num_employees):
        self.num_employees = num_employees

    def get_num_employees(self):
        return self.num_employees

    def get_shifts(self):
        return self.shifts

    def set_shifts(self, shifts):
        self.shifts = shifts

    def get_fixed_assignments(self):
        return self.fixed_assignments

    def set_fixed_assignments(self, fixed_assignments):
        self.fixed_assignments = fixed_assignments

    def get_weekly_demands(self):
        return self.weekly_demands

    # These can be modified either manually from the JSON or automatically by the ML model
    def set_weekly_demands(self, weekly_demands):
        self.weekly_demands = weekly_demands

    def get_requests(self):
        return self.requests

    def set_requests(self, requests):
        self.requests = requests
