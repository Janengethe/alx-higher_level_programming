#!/usr/bin/python3
for i in range(0, 99):
    print("{:02d}".format(i), end=(", "))
print("{:d}".format(i + 1))

# OR
# print(", ".join("{:02d}".format(i) for i in range(0, 100)))
