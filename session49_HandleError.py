try:
    print(myName)
except:
    print("an error occured")


def get(d, key):
    try:
        return d[key]
    except KeyError:
        return "no key found"
    except IndexError:
        return "index error"


person = {
    "name": "Saber",
    "family": "Galedar",
}

print(get(person, "age"))


while True:
    try:
        num = int(input("please enter a number: "))
    except:
        print("that is not a number")
    else:
        print("you have entered a number")
        break
    finally:
        print("this is finally section")


def divide(first, second):
    try:
        return first / second
    except TypeError as Error:
        print(Error)
        return "please enter a number"
    except ZeroDivisionError as err:
        print(err)
        return "you can not use ZERO!!!"


print(divide(1, 0))
