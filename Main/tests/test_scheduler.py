import json

from Main.scheduler import solve_shift_scheduling

def test_convert_to_employee():
    expected_ans = open('./testData/test_dept_2_infeasible.json')
    expected_ans_json = json.load(expected_ans)

    schedule, stats = solve_shift_scheduling(expected_ans_json)

    assert "infeasible" in stats