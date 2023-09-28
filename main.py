from risingCloudIO import readRequest, writeResponse

if __name__ == "__main__":

    # We first read the request from "request.json".
    # If you'd like to do any preprocessing to the
    # request, edit the readRequest() function accordingly.
    request = readRequest()

    # To process the request with an arbitrary function,
    # import it above and replace this line with
    # `response = arbitraryFunctionName(request)`
    response = request

    # We then serialize and write out the response
    # to "response.json". If you'd like to do any
    # post processing to the response, edit the
    # writeResponse() function accordingly.
    writeResponse(response)


def placeholderFunction():
    pass