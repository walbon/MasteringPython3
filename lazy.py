"""Laziness exercises"""


def reverse_difference(numbers):
    """Return list of reversed numbers subtracted from itself."""

    return [
        a-b for a,b in zip(numbers,reversed(numbers))
    ]


def get_shared_keys(dict1, dict2):
    """Return the keys that are shared by both dictionaries."""
    return {
            x for x in dict1.keys() if x in dict2.keys()
            }
