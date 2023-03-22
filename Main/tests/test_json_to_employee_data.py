import json

# Import parent directory
import sys
sys.path.insert(0,'../')

# Sample command: if pytest not in path:  python3 /Users/deividas/Library/Python/3.9/lib/python/site-packages/pytest

from json_to_employee_data import convert_to_employee_data

def test_convert_to_employee():
    payload = open('./testData/test-optimal-input.json')
    payload_json = json.load(payload)
    expected_ans = open('./testData/eeConversion.json')
    expected_ans_json = json.load(expected_ans)

    res = convert_to_employee_data(payload_json)
    print(res)
    assert payload_json == expected_ans_json
