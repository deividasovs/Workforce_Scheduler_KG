import json

from Main.json_to_employee_data import convert_to_employee_data

def test_convert_to_employee():
    payload = open('./testData/test_dept_1_optimal.json')
    payload_json = json.load(payload)
    expected_ans = open('./testData/test_converted_dept_1_optimal.json')
    expected_ans_json = json.load(expected_ans)

    res = convert_to_employee_data(payload_json)
    assert res == expected_ans_json
