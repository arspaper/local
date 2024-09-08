print("x y z w num 5")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                expression = not(x <= z) or (y == w) or y
                if not expression:
                    print(x, y, z, w)

print()
print("x y z w num 6")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                expression = (x or not y) and not(w == z) and w
                if expression:
                    print(x, y, z, w)

print()
print("x y z w num 7")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                expression = not((x or y) <= (z and w)) and (x <= w)
                if expression:
                    print(x, y, z, w)
