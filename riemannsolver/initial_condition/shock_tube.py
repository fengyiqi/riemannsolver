from .initial_condition import InitialCondition


class ShockTubeInitialCondition(InitialCondition):
    def __init__(self, density, velocityX, pressure):
        self.density = density
        self.velocityX = velocityX
        self.pressure = pressure