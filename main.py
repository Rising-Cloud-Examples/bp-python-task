from rcFunctions import readRequest, writeResponse

if __name__ == "__main__":

    # We first read the request from "request.json".
    # If you'd like to do any preprocessing to the
    # request, edit the readRequest() function accordingly.
    request = readRequest()

    # To process the request with an arbitrary function,
    # import the function and replace this line with
    # `response = arbitraryFunctionName(request)`
    response = request

    # Below is a quick example of logs that will be captured
    # by the rising cloud worker and reported in the app's
    # /jobs page under "Std Error" and "Std Out" respectively.
    import sys
    print("This is a log to stderr", file=sys.stderr)
    print("This is a log to stdout")

    # We then serialize and write out the response
    # to "response.json". If you'd like to do any
    # post processing to the response, edit the
    # writeResponse() function accordingly.
    writeResponse(response)
