arr = list(map(int, input().split()))

fmsf = float("-inf")
smsf = float("-inf")
tmsf = float("-inf")

for item in arr:
    if item > fmsf:
        tmsf = smsf
        smsf = fmsf
        fmsf = item
    elif item > smsf:
        tmsf = smsf
        smsf = item
    elif item > tmsf:
        tmsf = item

print(fmsf, smsf, tmsf)
