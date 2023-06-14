from math import gcd


def get_entity_position(entity, room_number, dimensions):
    room_x, room_y = room_number
    entity_x, entity_y = entity
    dim_x, dim_y = dimensions

    res_x = dim_x * room_x + entity_x if room_x % 2 == 0 else dim_x * room_x + (dim_x - entity_x)
    res_y = dim_y * room_y + entity_y if room_y % 2 == 0 else dim_y * room_y + (dim_y - entity_y)

    return (res_x, res_y)


def solution(dimensions, your_position, trainer_position, distance):
    dim_x, dim_y = dimensions
    your_x, your_y = your_position
    trainer_x, trainer_y = trainer_position

    width = (2 * distance // dim_x + 1) * dim_x + 1
    height = (2 * distance // dim_y + 1) * dim_y + 1

    matrix = [[0] * height for _ in range(width)]

    hits = 0
    shots_taken = set()

    for room_x in range(-distance // dim_x - 1, distance // dim_x + 2):
        for room_y in range(-distance // dim_y - 1, distance // dim_y + 2):
            trainer_pos = get_entity_position(trainer_position, (room_x, room_y), dimensions)
            player_pos = get_entity_position(your_position, (room_x, room_y), dimensions)

            matrix[trainer_pos[0]][trainer_pos[1]] = 1
            matrix[player_pos[0]][player_pos[1]] = 2

    for room_x in range(-distance // dim_x - 1, distance // dim_x + 2):
        for room_y in range(-distance // dim_y - 1, distance // dim_y + 2):
            trainer_pos = get_entity_position(trainer_position, (room_x, room_y), dimensions)

            if distance < ((trainer_pos[0] - your_x) ** 2 + (trainer_pos[1] - your_y) ** 2) ** 0.5:
                continue

            delta_x = trainer_pos[0] - your_x
            delta_y = trainer_pos[1] - your_y
            gcd_val = gcd(delta_x, delta_y)
            delta_x //= gcd_val
            delta_y //= gcd_val

            if (delta_x, delta_y) in shots_taken:
                continue

            shots_taken.add((delta_x, delta_y))

            pos_x, pos_y = your_x, your_y

            while True:
                pos_x += delta_x
                pos_y += delta_y

                if matrix[pos_x][pos_y] == 1:
                    hits += 1
                    break
                elif matrix[pos_x][pos_y] == 2:
                    break

    return hits
