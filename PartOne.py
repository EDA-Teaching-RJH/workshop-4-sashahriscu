# define principal function
def main():
    camel_case = input("Please enter the name of the variable in camel case: ")
    snake_case = ""

    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
# else part covers everything that is not uppercase (numbers etc)
        else:
            snake_case += char
    print(snake_case)

# call principal function
main()
