import random


<<<<<<< HEAD
def get_random_song_id(excluded=0):
    min_id, max_id = 1, 4
    # Some dummy comment
    if excluded < min_id or excluded > max_id:
        return random.randint(min_id, max_id)
    left_range = (min_id, excluded - 1)
    right_range = (excluded + 1, max_id)
    if excluded != min_id and (excluded == max_id or random.randint(0, 1) == 0):
=======
def get_random_song_id(excluded_song_id=0):
    # Below specify songs id range
    min_id, max_id = 1, 4
    if excluded_song_id < min_id or excluded_song_id > max_id:
        return random.randint(min_id, max_id)
    left_range = (min_id, excluded_song_id - 1)
    right_range = (excluded_song_id + 1, max_id)
    if excluded_song_id != min_id and (excluded_song_id == max_id or random.randint(0, 1) == 0):
>>>>>>> refactor/shuffle
        return random.randint(*left_range)
    else:
        return random.randint(*right_range)
