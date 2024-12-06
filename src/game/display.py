from fastenum import Enum


class DisplayMode(Enum):
    CONSOLE_BASED = 'CONSOLE_BASED'
    WINDOWED = 'WINDOWED'
    FULLSCREEN = 'FULLSCREEN'


class Display:
    __slots__ = ['display_mode', 'resolution']
    def __init__(self, display_mode: DisplayMode, resolution: dict[str, int]):
        self.display_mode = display_mode
        self.resolution = resolution

    def initialise(self):
        pass

    def run(self):
        pass