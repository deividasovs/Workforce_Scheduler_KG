from employee_data import EmployeeData

def convert_to_employee_data(payload):
    employee_data = EmployeeData()

    print(payload)

    requests = convertInnerToTuple(payload['Requests'])
    num_employees = payload['EmployeeCount']
    fixed_assignments = convertInnerToTuple(payload['FixedAssignments'])

    shifts = payload['Shifts']
    weekly_cover_demand = convertInnerToTuple(payload['WeeklyCoverDemand'])

    employee_data.set_num_employees(num_employees)
    employee_data.set_requests(requests)
    employee_data.set_shifts(shifts)
    employee_data.set_fixed_assignments(fixed_assignments)
    employee_data.set_weekly_demands(weekly_cover_demand)

    return employee_data


def convertInnerToTuple(arr):
    array_in_tuples = []
    for i in range(len(arr)):
        array_in_tuples.append(tuple(arr[i]))
    return array_in_tuples