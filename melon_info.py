"""Print out all the melons in our inventory."""


from melons import melons


def print_melon(melons_info):
    """Print each melon with corresponding attribute information."""

    for melon in melons_info:
        print(melon)
        for ind, feature in enumerate(melons[melon]):
            if ind == 0:
                print(f"\t({melons[melon][ind][0]}  {melons[melon][ind][1]:.2f})")
            else:
                print(f"\t{melons[melon][ind]}")


print_melon(melons)

