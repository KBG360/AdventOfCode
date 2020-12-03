amount_of_trees = 0
right = 1
down = 2
current_spot_x = 0
current_spot_y = 0
where_you_have_to_be = down
rowNo = 0

# Open input and assign variables
with open('input2.txt') as f:
    lines = f.readlines()
    num_lines = sum(1 for line in open('input.txt'))

for x in lines:
    rowNo += 1
    row = list(x)
    if current_spot_y == where_you_have_to_be:
        if row[current_spot_x] == "#":
            current_spot_x += right
            current_spot_y += down
            where_you_have_to_be += down
            amount_of_trees += 1
        else:
            current_spot_y += down
            current_spot_x += right
            where_you_have_to_be += down
    else:
        current_spot_y += down
        current_spot_x += right

print(amount_of_trees)