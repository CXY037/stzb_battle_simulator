from ..Magic_ import Magic

class ChaseMagic(Magic):
    def __init__(self, name):
        super().__init__(type=Magic.TYPE_CHASE, name=name)

