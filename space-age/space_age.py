class SpaceAge:
    PLANET_SECONDS = [(p, s * 31557600) for (p, s) in (
        ('earth', 1.0),
        ('mercury', 0.2408467),
        ('venus', 0.61519726),
        ('mars', 1.8808158),
        ('jupiter', 11.862615),
        ('saturn', 29.447498),
        ('uranus', 84.016846),
        ('neptune', 164.79132)
    )]

    def __init__(self, seconds):
        self.seconds = seconds

        for planet, seconds in self.PLANET_SECONDS:
            setattr(self, 'on_' + planet, self.planet_age(seconds))

    def planet_age(self, planet_seconds):
        return lambda x=planet_seconds: round(self.seconds / x, 2)
