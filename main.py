from rcFunctions import readRequest, writeResponse

if __name__ == "__main__":

    # We first read the request from "request.json". If you'd like to do any
    # preprocessing to the request, edit the readRequest() function accordingly.
    request = readRequest()

    # To process the request with an arbitrary function, import the function
    # and replace this line with `response = arbitraryFunctionName(request)`.
    response = request

    # Demonstration of logs that will be captured by the rising cloud worker.
    # These logs will be reported in the app's /jobs page under the "Std Error"
    # and "Std Out" respectively. They serve no purpose other than to show
    # how to implement logs and how they will be captured by Rising Cloud.
    import sys
    print("This is a demo log to stderr", file=sys.stderr)
    print("This is a demo log to stdout")

    # Serialize and write out the response to "response.json". If you'd like to
    # do any post processing to the response, edit the writeResponse() function.
    writeResponse(response)
