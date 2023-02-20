import json

from json_to_employee_data import convert_to_employee
from scheduler import solve_shift_scheduling


def lambda_handler(event, context):
    #body_str = event.get('body', '{}')
    #body = json.loads(body_str)
    # ------ for testing purposes & without container-------
    body = event  # temp
    #sampleInputf = open('./sampleInput.json')
    #sampleInput = json.load(sampleInputf)
    #res = lambda_handler(sampleInput, 0)

    # End testing purposes

    employeeData = convert_to_employee(body)

    schedule, stats = solve_shift_scheduling(employeeData)

    responseBody = {
        "schedule": schedule,
        "stats": stats
    }

    responseBody = json.dumps(responseBody)

    return {
        'statusCode': 200,
        'body': responseBody,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Amz-Date, X-Api-Key, X-Amz-Security-Token, X-Amz-User-Agent',
            'Content-Type': 'application/json',
        }

    }


# For testing purposes
if __name__ == "__main__":
    #res = lambda_handler(0, 0)
    #    sampleInputf = open('./Examples/sampleInput2.json')
    sampleInputf = open('./Main/sampleInput2.json')
    sampleInput = json.load(sampleInputf)
    res = lambda_handler(sampleInput, 0)
    print(res)
