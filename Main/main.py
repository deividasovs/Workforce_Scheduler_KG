import json

from json_to_employee_data import convert_to_employee_data
from scheduler import solve_shift_scheduling


def lambda_handler(event, context):
    body_str = event.get('body', '{}')
    body = json.loads(body_str)
    
    body = event  # Use when testing

    employee_data = convert_to_employee_data(body)

    print(employee_data)

    schedule, stats = solve_shift_scheduling(employee_data)

    response_body = {
        "schedule": schedule,
        "stats": stats
    }

    response_body = json.dumps(response_body)

    return {
        'statusCode': 200,
        'body': response_body,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Amz-Date, X-Api-Key, X-Amz-Security-Token, X-Amz-User-Agent',
            'Content-Type': 'application/json',
        }

    }


# For testing purposes
if __name__ == "__main__":
    test_input = open('./Main/tests/testData/sample_dept_4_input.json')
    test_input_json = json.load(test_input)
    res = lambda_handler(test_input_json, 0)
    res = json.loads(res['body'])

    print("\n")
    print(res['stats'])
