right = 3
down = 1

goto_spot_y = down
current_spot_x = 0
current_row = 0
amount_of_trees = 0

# Open input and assign variables
with open('input.txt') as f:
    lines = f.readlines()
    num_lines = sum(1 for line in open('input.txt'))

for x in lines:
    current_row += 1
    row = list(x.strip())
    width = len(row)
    if current_spot_x >= width:
        current_spot_x = current_spot_x % width
    if current_row == goto_spot_y:
        if row[current_spot_x] == "#":
            amount_of_trees += 1
            current_spot_x += right
        else:
            current_spot_x += right
    else:
        current_spot_x += right
        current_row += down
        
print(amount_of_trees)