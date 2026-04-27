# q013_encode_decode_strings.py

def encode(strs: list[str]) -> str:
    # TODO
    result = []
    for s in strs:
        result.append(str(len(s)))
        result.append('#')
        result.append(s)
    return ''.join(result)


def decode(s: str) -> list[str]:
    # TODO
    result = []
    i = 0
    while i < len(s):
        # Read the length of the next string
        j = i
        while j < len(s) and s[j] != '#':
            j += 1
        length = int(s[i:j])
        # Read the string of the specified length
        str_start = j + 1
        str_end = str_start + length
        result.append(s[str_start:str_end])
        i = str_end
    return result


if __name__ == "__main__":
    data = ["hello", "world"]
    encoded = encode(data)
    print("Encoded:", encoded)

    decoded = decode(encoded)
    print("Decoded:", decoded)