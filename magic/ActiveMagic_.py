from Magic_ import Magic

class ActiveMagic(Magic):
    def __init__(self, name):
        super(ActiveMagic, self).__init__(type=Magic.TYPE_ACTIVE, name=name)

    def releaseMagic(self, pos, ourGroup, enemy): #武将释放技能
        pass
