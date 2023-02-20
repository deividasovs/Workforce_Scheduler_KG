from employee_data import EmployeeData


# TODO: Instead of employee numbers, assign IDs to them!


def convert_to_employee(payload):
    employeeData = EmployeeData()

    print(payload)

    requests = convertInnerToTuple(payload['Requests'])
    numEmployees = payload['EmployeeCount']
    fixedAssignments = convertInnerToTuple(payload['FixedAssignments'])

    shifts = payload['Shifts']
    weeklyCoverDemand = convertInnerToTuple(payload['WeeklyCoverDemand'])

    employeeData.set_num_employees(numEmployees)
    employeeData.set_requests(requests)
    employeeData.set_shifts(shifts)
    employeeData.set_fixed_assignments(fixedAssignments)
    employeeData.set_weekly_demands(weeklyCoverDemand)

    return employeeData


def convertInnerToTuple(arr2d):
    arr2dTupl = []
    for i in range(len(arr2d)):
        arr2dTupl.append(tuple(arr2d[i]))
    return arr2dTupl
