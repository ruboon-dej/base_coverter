def reverse_str(message):
    number_of_text = len(message)
    text = ""
    for i in range(number_of_text):
        number = number_of_text - i - 1
        text += message[number]
    return text


def from_base(b, fstbase):
    ret = 0
    num1 = str(b)
    for i in range(len(num1)):
        x = num1[len(num1) - i - 1].isdigit()
        n = i
        if x == True:
            digit = int(num1[len(num1) - i - 1])
        else:
            asc = int(ord(num1[len(num1) - i - 1]))
            digit = int(asc-55)
        ensemble = digit * (fstbase**n)
        ret += ensemble
    return ret


def change_into_number(a, base):
    output = ""
    total = a
    while total > 0:
        remainder = total % base
        total = int((total - remainder) / base)
        if remainder > 9:
            number = (remainder - 9) + 64
            remainder = chr(number)

        output += str(remainder)
    output = reverse_str(output)
    return output


def convert(original, target, value):
    first_step = int(from_base(value, original))
    new_value = change_into_number(first_step, target)
    return new_value