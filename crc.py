def xor(a, b):
    return "".join("0" if x == y else "1" for x, y in zip(a, b))

def mod2div(dividend, key):
    n = len(key)
    tmp = dividend[:n]
    for i in range(n, len(dividend) + 1):
        if tmp[0] == "1":
            tmp = xor(key, tmp)[1:] + (dividend[i] if i < len(dividend) else "")
        else:
            tmp = tmp[1:] + (dividend[i] if i < len(dividend) else "")
    return tmp

data = input("Enter data bits: ")
key = "10001000000100001"

appended = data + "0" * (len(key) - 1)
rem = mod2div(appended, key)
print("CRC remainder:", rem)
print("Codeword:", data + rem)
print("Receiver remainder:", mod2div(data + rem, key))
