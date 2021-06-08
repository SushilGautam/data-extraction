# def my_request(url, description):
#     print(f"You requested this url: {url} and desciption is {description}")


# my_request("www.facebook.com", "this is a social media site.")
# my_request("www.google.com", "this is google")


def sum(num1, num2):
    print("Inside Function")
    result = num1 + num2
    print("#####inside function result#####")
    return result


def subtract(num1, num2):
    print("Inside Function")
    result = num1 - num2
    print("#####inside function result#####")
    return result


result1 = sum(1, 2)
result2 = subtract(10, 5)
print("#######outside functionr result############")

print(result1)
print(result2)


# function defintion with "def" keyword
# function recives input as an argument e.g sum(num1, num2)
# function body -> does the work what is specified inside of a function
# variables made inside of a function cant be accessed outside of it
# to get value(not variable) out of a function use "return" keyword. e.g return result -> will return value stored in result
