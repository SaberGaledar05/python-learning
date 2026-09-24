# default value

def exponent(number, power=2):
    return number**power


print(exponent(5))


def full_name(first_name, last_name):
    return f"{first_name} {last_name}"


print(full_name("Saber", "Galedar"))

print(full_name(last_name="Galedar", first_name="Saber"))
