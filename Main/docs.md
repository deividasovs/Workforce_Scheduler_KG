# Documentation

## Employee data explanation

"""
    # Fixed assignment: (employee, shift, day).
    # This fixes the first 2 days of the schedule.
    fixed_assignments = [
        (0, 0, 0),
        (1, 0, 0),
        (2, 1, 0),
        (3, 1, 0),
        (0, 1, 1),
    ]

                # Request: (employee, shift, day, weight)
            # A negative weight indicates that the employee desire this assignment.
            # Could be used for days off requests
    requests = [
        # Positive weight = does not want, negative weight = wants
        # Employee 3 wants Saturday off
        (3, 0, 5, -2),
        # Employee 5 wants a night shift on the second Thursday (negative weight).
        # (5, 3, 10, -2),
        # Employee 2 does not want a night shift on the first Friday (positive
        # weight).
        (2, 2, 4, 4)
    ]


    # daily demands for work shifts (morning, afternon, night) for each day
    # of the week starting on Monday.
    weekly_cover_demands = [
        (1, 1),  # Monday
        (1, 1),  # Tuesday
        (1, 1),  # Wednesday
        (1, 1),  # Thursday
        (1, 2),  # Friday
        (1, 1),  # Saturday
        (1, 1),  # Sunday
    ]


    def __init__(self):
        #self.num_employees = 0
        self.num_employees = 5
        #self.shifts = []
        self.shifts = ['O', 'M', 'A']
        self.requests = [
            # Positive weight = does not want, negative weight = wants
            # Employee 3 wants Saturday off
            (3, 0, 5, -2),
            # Employee 5 wants a night shift on the second Thursday (negative weight).
            # (5, 3, 10, -2),
            # Employee 2 does not want a night shift on the first Friday (positive
            # weight).
            (2, 2, 4, 4)
        ]
        #self.requests = []
        self.num_days = 7
        #self.weekly_demands = []
        self.weekly_demands = [
            (1, 1),  # Monday
            (1, 1),  # Tuesday
            (1, 1),  # Wednesday
            (1, 1),  # Thursday
            (1, 2),  # Friday
            (1, 1),  # Saturday
            (1, 1),  # Sunday
        ]
        #self.fixed_assignments = []
        self.fixed_assignments = [
            (0, 0, 0),
            (1, 0, 0),
            (2, 1, 0),
            (3, 1, 0),
            (0, 1, 1),
        ]



"""