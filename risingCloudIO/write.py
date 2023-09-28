import json, typing

def writeResponse(response: typing.Any):
    '''
    writeResponse takes any json-serializable object and
    writes the serialized string to "response.json". This
    file is automatically read by the rising cloud worker
    when the main function terminates.
    '''
    
    with open("response.json", "w") as f:
        json.dump(response, f)