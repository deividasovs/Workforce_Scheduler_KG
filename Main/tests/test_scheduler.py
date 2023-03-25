import json

import sys
sys.path.insert(0,'../')

# Sample command: if pytest not in path:  python3 /Users/deividas/Library/Python/3.9/lib/python/site-packages/pytest
from scheduler import solve_shift_scheduling

def test_convert_to_employee():
    expected_ans = open('./testData/eeConversion.json')
    expected_ans_json = json.load(expected_ans)

    schedule, stats = solve_shift_scheduling(expected_ans_json)
    #print(res)
    #assert payload_json == expected_ans_json
    ## assert stats contains the string infeasible
    assert "infeasible" in stats
