import json, typing

def readRequest() -> typing.Any:
    '''
    readRequest will return the rising cloud request made to the worker.
    By default, this returns a dict. This reads from the "request.json" file
    which is created by Rising Cloud when the worker recieves a request.
    '''

    with open("request.json", "r") as f:
        request = json.load(f)

        # Perform any transformations of the input data here

        return request

def writeResponse(response: typing.Any):
    '''
    writeResponse takes any json-serializable object and writes the serialized
    string to "response.json". This file is automatically read by Rising Cloud
    after the main function terminates.
    '''

    # Perform any transformations to output data here.
    
    with open("response.json", "w") as f:
        json.dump(response, f)