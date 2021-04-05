# MEALS ARCHIVE:
# -----------------------------------------------------
def load_archive():
    with open('data/archive.json', 'r') as f:
        archive = [json.loads(line) for line in f.readlines()]
        return [x for x in remove_old_meals(archive)]


def remove_old_meals(my_data):
    """Removes objects two weeks old or more."""
    for obj in my_data:
        if is_two_weeks_old(obj):
            pass
        else:
            yield obj
