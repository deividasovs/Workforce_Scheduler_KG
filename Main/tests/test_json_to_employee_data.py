import json

# Import parent directory
import sys
sys.path.insert(0,'../')

# Sample command: if pytest not in path:  python3 /Users/deividas/Library/Python/3.9/lib/python/site-packages/pytest

from json_to_employee_data import convert_to_employee

def test_convert_to_employee():
    payload = open('./testData/SampleOptimalInput.json')
    payloadJson = json.load(payload)
    expectedAns = open('./testData/eeConversion.json')
    expectedAnsJson = json.load(expectedAns)

    res = convert_to_employee(payloadJson)
    print(res)
    assert payloadJson == expectedAnsJson
