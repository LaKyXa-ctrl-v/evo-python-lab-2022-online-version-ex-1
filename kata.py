facing = input("Початковий напрямок: ")
turn = input("На скільки градусів потрібно зміститись?: ")


def direction(facing, turn):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    if (type(turn) == int) and (turn % 45 == 0) and (-1080 <= turn <= 1080):
        if facing in directions:
            turns = turn // 45
            start_idx = directions.index(facing)
            end_idx = (start_idx + turns) % len(directions)
            print(directions[end_idx])
        else:
            print("Замість напрямку введено щось некоректне, спробуйте ще раз!")
    else:
        print("Замість градусів введено щось некоректне,спробуйте ще раз!")


direction(facing, turn)
