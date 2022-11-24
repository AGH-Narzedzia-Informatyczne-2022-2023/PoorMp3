import random


def get_random_song_id(excluded_song=0):
    min_id, max_id = 1, 4
    if excluded_song < min_id or excluded_song > max_id:
        return random.randint(min_id, max_id)
    left_range = (min_id, excluded_song - 1)
    right_range = (excluded_song + 1, max_id)
    if excluded_song != min_id and (excluded_song == max_id or random.randint(0, 1) == 0):
        return random.randint(*left_range)
    else:
        return random.randint(*right_range)
