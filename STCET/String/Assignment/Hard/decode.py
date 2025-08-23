def decode_rle(s):
    decoded = ""
    i = 0
    while i < len(s):
        char = s[i]
        count = ""
        i += 1
        while i < len(s) and s[i].isdigit():
            count += s[i]
            i += 1
        decoded += char * int(count)
    return decoded

print(decode_rle("a3b2c1d3"))  # aaabbcddd
