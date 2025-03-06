a, b, c = 0, 0, 0  # Scores for A, B, and C

# Read input and update scores
for _ in range(3):
    rel = input()
    if rel[1] == '>':  # Example: "A>B" means A is greater
        if rel[0] == 'A':
            a += 1
        elif rel[0] == 'B':
            b += 1
        else:
            c += 1
    else:  # Example: "A<B" means B is greater
        if rel[2] == 'A':
            a += 1
        elif rel[2] == 'B':
            b += 1
        else:
            c += 1

# Create a list of characters with their scores
order = [('A', a), ('B', b), ('C', c)]

# Sort by score (lower score means smaller value)
order.sort(key=lambda x: x[1])

# Check if ordering is valid (should be exactly 0, 1, 2)
if [x[1] for x in order] == [0, 1, 2]:
    print("".join(x[0] for x in order))
else:
    print("Impossible")