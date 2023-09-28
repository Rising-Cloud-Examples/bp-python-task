import json, typing

def readRequest() -> typing.Dict:
    '''
    readRequest will return a dict representation of the 
    rising cloud request made to the worker. This will always
    read from the "request.json" file which is created by
    the rising cloud worker when it recieves a request.
    '''

    with open("request.json", "r") as f:
        request = json.load(f)
        return request