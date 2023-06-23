import sys
for line in sys.stdin:
    words = line.split()
    try:
        print(len(words[-1]))
    except:
        break