def strsort(str):
    new_str = []
    for c in reversed(str):
        new_str.append(f"{c}")
    return ''.join(new_str)

print(strsort('Ask'))
