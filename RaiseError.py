# print(test)
# None = 1

# raise IndexError
# raise ValueError


def colorize(text, color):
    colors = ["red", "blue", "yellow", "green"]
    if type(text) and type(color) is not str:
        raise TypeError("must be a string")
    elif color not in colors:
        raise ValueError(f"{color} not in colors list")
    else:
        print(f"printed {text} in {color}")


colorize("hello", "blue")
