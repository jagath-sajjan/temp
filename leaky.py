def simleak(cap, leak_r, packets):
    bucket = 0
    rows = []

    for time, incoming in enumerate(packets, 1):
        accepted = min(incoming, cap - bucket)
        dropped = incoming - accepted
        bucket += accepted
        leaked = min(bucket, leak_r)
        bucket -= leaked
        rows.append((time, incoming, accepted, dropped, leaked, bucket))

    return rows

cap = int(input("Enter bucket capacity: "))
leak_r = int(input("Enter leak rate: "))
packets = list(map(int, input("Enter packets per tick: ").split()))

print("Time  In  Accepted  Dropped  Leaked  Bucket")
for row in simleak(cap, leak_r, packets):
    print(*row, sep="     ")
