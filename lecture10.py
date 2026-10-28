line = ['10','20','abc','30']
total = 0
for lines in line:
    try:
        total += float(lines)
    except ValueError:
        print(f"Bad number {lines}")