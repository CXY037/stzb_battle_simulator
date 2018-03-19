from ..Magic_ import Magic
class CommandMagic(Magic):

    #战法生效的回合
    mStart=1

    #战法失效的回合（不含）
    mEnd = 9

    mHurtEnhancement = 0
    mMaigcHurtEnhancement = 0

    def __init__(self, name, services, distance):
        super().__init__(type=Magic.TYPE_COMMAND, name=name)
        self.mName = name
        self.mServices = services
        self.mDistance = distance
