def bin2Dec(val):
    rev=val[::-1]
    dec = 0
    i = 0
    for dig in rev:
        dec += int(dig) * 2**i
    i += 1

    return dec



def oct2Hex(val):
    rev = val[::-1]
    dec = 0
    i = 0
    for dig in rev:
        dec += int(dig) * 8 ** i
        i += 1

    hex_val = ""  # Initialize an empty string to store the hexadecimal result

    while dec != 0:
        remainder = dec % 16  # Calculate the remainder when dividing by 16
        if remainder <= 9:
            hex_digit = str(remainder)  # Convert remainder to a string for hex representation
        else:
            hex_digit = chr(ord('A') + remainder - 10)  # Convert to hex letter (A-F)
        hex_val = hex_digit + hex_val  # Add the hex digit to the result
        dec = dec // 16  # Integer division to continue the process

    return hex_val
num1 = input("Enter a binary number : ")
print(bin2Dec(num1))
num2 = input("Enter a octal number : ")
print(oct2Hex(num2))
