def errorCode(num):
    match num:
        case 500:
            return "Internal Server Error"
        case 401:
            return "Unauthorised"
        case 400:
            return "Bad Request"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 501:
            return "Not Implemented"
        case 502:
            return "Service Temporarily Overloaded"
        case 503:
            return "Service Unavailable"

c = int(input("What is the code?"))
print(errorCode(c))

quit()