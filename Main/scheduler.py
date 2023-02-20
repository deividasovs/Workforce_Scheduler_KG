# Adapted from https://github.com/google/or-tools/blob/master/examples/python/shift_scheduling_sat.py
# For more, take a look at https://developers.google.com/optimization/scheduling/employee_scheduling#nurse_scheduling
# and https://developers.google.com/optimization/cp/cp_solver

# TODO: Set each shift equal to a time they'd be working at?
# Or decouple that and set it in another script


# Imports
import pandas as pd

from ortools.sat.python import cp_model

from constraints import shift_constraints, weekly_sum_constraints, penalized_transitions, add_soft_sequence_constraint, add_soft_sum_constraint, excess_cover_penalties

from employee_data import EmployeeData


def solve_shift_scheduling(employeeData: EmployeeData):
    """Solves the shift scheduling problem."""

    #employeeData = EmployeeData()

    num_shifts, num_employees, num_days = len(employeeData.get_shifts()
                                              )-1, employeeData.get_num_employees(), employeeData.get_num_days()

    model = cp_model.CpModel()

    worker_names = []

    work = {}
    for e in range(num_employees):
        worker_names.append("worker " + str(e))
        for s in range(num_shifts):
            for d in range(num_days):
                work[e, s, d] = model.NewBoolVar('work%i_%i_%i' % (e, s, d))

    index = pd.Index(worker_names)
    res = pd.DataFrame(columns=['Mon', 'Tue', 'Wed', 'Thurs',
                       'Fri', 'Sat', 'Sun'], index=index)

    # Linear terms of the objective in a minimization context.
    obj_int_vars = []
    obj_int_coeffs = []
    obj_bool_vars = []
    obj_bool_coeffs = []

    # Exactly one shift per day.
    for e in range(num_employees):
        for d in range(num_days):
            model.AddExactlyOne(work[e, s, d] for s in range(num_shifts))

    # Fixed assignments.
    for e, s, d in employeeData.get_fixed_assignments():
        model.Add(work[e, s, d] == 1)

    for e, s, d in employeeData.get_fixed_assignments():
        obj_bool_vars.append(work[e, s, d])
        obj_bool_coeffs.append(1)

    # Shift constraints
    for ct in shift_constraints:
        shift, hard_min, soft_min, min_cost, soft_max, hard_max, max_cost = ct
        for e in range(num_employees):
            works = [work[e, shift, d] for d in range(num_days)]
            variables, coeffs = add_soft_sequence_constraint(
                model, works, hard_min, soft_min, min_cost, soft_max, hard_max,
                max_cost,
                'shift_constraint(employee %i, shift %i)' % (e, shift))
            obj_bool_vars.extend(variables)
            obj_bool_coeffs.extend(coeffs)

    # Weekly sum constraints
    for ct in weekly_sum_constraints:
        shift, hard_min, soft_min, min_cost, soft_max, hard_max, max_cost = ct
        for e in range(num_employees):
            works = [work[e, shift, d] for d in range(7)]
            variables, coeffs = add_soft_sum_constraint(
                model, works, hard_min, soft_min, min_cost, soft_max,
                hard_max, max_cost,
                'weekly_sum_constraint(employee %i, shift %i)' %
                (e, shift))
            obj_int_vars.extend(variables)
            obj_int_coeffs.extend(coeffs)

    # Penalized transitions
    for previous_shift, next_shift, cost in penalized_transitions:
        for e in range(num_employees):
            for d in range(num_days - 1):
                transition = [
                    work[e, previous_shift, d].Not(), work[e, next_shift,
                                                           d + 1].Not()
                ]
                if cost == 0:
                    model.AddBoolOr(transition)
                else:
                    trans_var = model.NewBoolVar(
                        'transition (employee=%i, day=%i)' % (e, d))
                    transition.append(trans_var)
                    model.AddBoolOr(transition)
                    obj_bool_vars.append(trans_var)
                    obj_bool_coeffs.append(cost)

    # Cover constraints
    for s in range(1, num_shifts):
        for d in range(7):
            works = [work[e, s, d] for e in range(num_employees)]
            # Ignore Off shift.
            min_demand = employeeData.get_weekly_demands()[d][s - 1]
            worked = model.NewIntVar(min_demand, num_employees, '')
            model.Add(worked == sum(works))
            over_penalty = excess_cover_penalties[s - 1]
            if over_penalty > 0:
                name = 'excess_demand(shift=%i,  day=%i)' % (s, d)
                excess = model.NewIntVar(0, num_employees - min_demand,
                                         name)
                model.Add(excess == worked - min_demand)
                obj_int_vars.append(excess)
                obj_int_coeffs.append(over_penalty)

    # Objective
    model.Minimize(
        sum(obj_bool_vars[i] * obj_bool_coeffs[i]
            for i in range(len(obj_bool_vars))) +
        sum(obj_int_vars[i] * obj_int_coeffs[i]
            for i in range(len(obj_int_vars))))

    # Solve the model.
    solver = cp_model.CpSolver()
    solution_printer = cp_model.ObjectiveSolutionPrinter()
    status = solver.Solve(model, solution_printer)

    # Print solution.
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print()
        header = '          M T W T F S S '
        print(header)
        for e in range(num_employees):
            schedule = ''
            for d in range(num_days):
                for s in range(num_shifts):
                    if solver.BooleanValue(work[e, s, d]):
                        schedule += employeeData.get_shifts()[s] + ' '
                        res.iloc[e, d] = employeeData.get_shifts()[s]

            print('worker %i: %s' % (e, schedule))

        print()
        print(res)
        print('Penalties:')
        for i, var in enumerate(obj_bool_vars):
            if solver.BooleanValue(var):
                penalty = obj_bool_coeffs[i]
                if penalty > 0:
                    print('  %s violated, penalty=%i' % (var.Name(), penalty))
                else:
                    print('  %s fulfilled, gain=%i' % (var.Name(), -penalty))

        for i, var in enumerate(obj_int_vars):
            if solver.Value(var) > 0:
                print('  %s violated by %i, linear penalty=%i' %
                      (var.Name(), solver.Value(var), obj_int_coeffs[i]))

    # print()
    statistics = 'Statistics' + '\n'
    statistics += '  - status          : %s' % solver.StatusName(status) + '\n'
    statistics += '  - conflicts       : %i' % solver.NumConflicts() + '\n'
    statistics += '  - branches        : %i' % solver.NumBranches() + '\n'
    statistics += '  - wall time       : %f s' % solver.WallTime() + '\n'

    # print(statistics)

    # res.to_csv('shift_scheduling.csv')

    # return res.iloc[:, 0:2].to_json()
    return res.to_csv(), statistics
