import robots



class Melon(object):
    """Melon."""

    def __init__(self, melon_type):
        """Initialize melon.

        melon_type: type of melon being built.
        """

        self.melon_type = melon_type
        self.weight = 0.0
        self.color = None
        self.stickers = []

    def prep(self):
        """Prepare the melon."""

        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)

    def __str__(self):
        """Print out information about melon."""

        if self.weight <= 0:
            return self.melon_type
        else:
            return "{} {:.2f} lbs {}".format(self.color,
                                             self.weight,
                                             self.melon_type)

# FIXME: Add Squash class definition here.
class Squash(Melon):
    def __init__(self, squash_type):
        """initializing squash.

        squash_type: type of squash being painted.
        """
        self.melon_type = squash_type
        self.weight = 0.0
        self.color = None
        self.stickers = []

    def prep(self):
        """preparing bot for inspection"""

        robots.painterbot.paint(self)
        robots.stickerbot.apply_logo(self)


    pass


standing_orders1 = open('standing_orders1.log')

