import random


def get_random_song_id(excluded=0):
    min_id, max_id = 1, 4
    # Some dummy comment
    if excluded < min_id or excluded > max_id:
        return random.randint(min_id, max_id)
    left_range = (min_id, excluded - 1)
    right_range = (excluded + 1, max_id)
    if excluded != min_id and (excluded == max_id or random.randint(0, 1) == 0):
        return random.randint(*left_range)
    else:
        return random.randint(*right_range)
