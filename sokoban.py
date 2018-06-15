map = {
    "size_x" : 8,
    "size_y" : 8
}
player = {
    "x": 3,
    "y": 4,
}
boxes = [
    { "x": 1,"y": 1},
    { "x": 2,"y": 2},
    { "x": 3,"y": 3}
]
destination = [
    {"x": 2, "y": 1},
    {"x": 3, "y": 2},
    {"x": 4, "y": 3}
]
walls = [
    {"x": 6, "y": 7},
    {"x": 5, "y": 6},
    {"x": 4, "y": 5}
]
x1 = 0
y1 = 0
x2 = 0
y2 = 0

by = 0
bx = 0
undo_limit = 1

while True:
    for y in range(map["size_y"]):
        for x in range(map["size_x"]):
            box_is_here = False
            player_is_here = False
            des_is_here = False
            wall_is_here = False

            for w in walls:
                if (x == w["x"]) and (y == w["y"]):
                    wall_is_here = True
                    break

            for box in boxes:
                if (x == box["x"]) and (y == box["y"]):
                    box_is_here = True
                    break

            for des in destination:
                if (x == des["x"]) and (y == des["y"]):
                    des_is_here = True
                    break

            if (x == player["x"]) and (y == player["y"]):
                player_is_here = True

            if player_is_here:
                print("P  ", end='')

            elif box_is_here:
                print("B  ", end='')
            elif des_is_here:
                print("D  ", end='')
            elif wall_is_here:
                print("W  ", end='')
            else:
                print("-  ", end='')
        print()

    win = True
    for box in boxes:
        if box not in destination:
            win = False

    if win:
        print("you win ")
        break
    dy = 0
    dx = 0
    while True:
        move = input(" move or undo: ").lower()
        if move == "w":
            dy = -1
            y1 = -1
            x1 = 0
            break
        elif move == "a":
            dx = -1
            x1 = -1
            y1 = 0
            break
        elif move == "s":
            dy = 1
            y1= 1
            x1 = 0
            break
        elif move == "d":
            dx = 1
            x1 = 1
            y1 = 0
            break
        elif (move == "undo") and (undo_limit > 1):
            print("undo 1 lần thôi, 2 lần chơi cc à =))")
            print("you lose")
            x1 = 0
            y1 = 0
            x2 = 0
            y2 = 0
            break
        elif move == "undo":
            print("undo")
            undo_limit += 1
            break
        else:
            print("nghỉ mẹ game đi")
            break
    if (0 <= player['x'] + dx <= map['size_x']-1) and (0 <= player['y']+dy <= map["size_y"]-1):
        player['x'] += dx
        player['y'] += dy

    for wall in walls:
        if (player['x'] == wall['x']) and (player['y'] == wall['y']):
            player['x'] -= dx
            player['y'] -= dy
            break
    for box in boxes:
        if (0 > box['x'] + dx) and (0 > box['y']+dy):
            player['x'] -= dx
            player['y'] -= dy
    for i in range(len(boxes)):
        for box in boxes:
            if (player["x"] == box['x']) and (player["y"] == box["y"]) and \
                    (0 <= box['x'] + dx <= map['size_x'] - 1) and (0 <= box['y'] + dy <= map["size_y"] - 1):
                bx = dx
                by = dy
                x2 = bx
                y2 = by
                for box_x in boxes:
                    for box_y in boxes:
                        if (box_x['x'] == box_y['x'] + dx) and (box_x['y'] == box_y['y'] + dy):
                            player['x'] -= dx
                            player['y'] -= dy
                            y1 = 0
                            x1 = 0
                            bx = 0
                            by = 0
                for wall in walls:
                    if (wall['x'] - dx == box['x']) and (wall['y'] - dy == box['y']):
                        bx = 0
                        by = 0
                        player['x'] -= dx
                        player['y'] -= dy
                        y1 = 0
                        x1 = 0
                box['x'] += bx
                box['y'] += by
        if move == "undo":
            box['x'] == box['x'] - x2
            box['y'] == box['y'] - y2
    if move == "undo":
        player['x'] == player['x'] - x1
        player['y'] == player['y'] - y1