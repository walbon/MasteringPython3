"""Strings exercises"""


def html_tag(tag_name, **attributes):
    """Make an HTML tag from the given tag name and attributes."""
    attr = [
        f'{param}="{value}"' for param, value in attributes.items()
    ]
    return f'<{tag_name} {" ".join(attr)}>'


def dollars(amount):
    """Format a number with a dollar sign and two decimal places."""
    return "${0:.2f}".format(amount)


def split_in_half(iterable):
    """Return two halves of the given iterable."""
    mid_point = int(len(iterable) / 2)
    return (iterable[:mid_point], iterable[mid_point:])
