def is_fascinating(n):
    if n<100 or n>999:
        return False
    
    concatenated = str(n)+str(2*n)+str(3*n)

    digit_seen = set()
    for digit in concatenated:
        if digit == '0' or digit in digit_seen:
            return False
        digit_seen.add(digit)

    return len(digit_seen) == 9

print(is_fascinating(192))
print(is_fascinating(123))