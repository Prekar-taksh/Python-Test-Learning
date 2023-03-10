#This will contain Azure Test cases

import json
from azure.functions import HttpRequest

def test_function(function):
    req = HttpRequest(
        method="GET",
        body=None,
        url="/api/<your_function_route>",
        headers={
            "Content-Type": "application/json"
        }
    )
    res = function(req)
    assert res.status_code == 200
    assert res.get_json() == {"message": "Hello, world!"}
