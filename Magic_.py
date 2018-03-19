class Magic:
    TYPE_CHASE = 3   #追击战法
    TYPE_COMMAND = 1 #指挥战法
    TYPE_ACTIVE = 2   #主动战法
    TYPE_PASSIVE = 0  #被动战法
    '''
    string mName; #战法名称 
    
    int mType; #战法类型
    
    int mServices; #战法限制使用兵种  
    
    int mDistance; #战法攻击距离
    
    double probability; #战法发动几率
    
    boolean toEnemy = true;  //战法针对敌人还是我军

    int toMin;  //战法作用最小人数

    int toMax;  //战法作用最大人数

    int prepareRound = 0;  //需要准备的回合数

    boolean canNormalAttack = false;  //能否物理攻击

    double hurt;  //总物攻伤害

    boolean canMagicAttack = false;  //能否策略攻击

    double magicHurt;  //策略伤害
    '''

    def __init__(self, type, name, service=7, distance=5, prob=1.0, toEnemy=True, \
                toMin=3, toMax=3, prepareRound=0, canNormalAttack=False, canMagicAttack=False,\
                ):
        self.mType = type
        self.mName = name
        self.mService = service
        self.mDistance = distance
        self.mProbability = prob
        self.toEnemy = toEnemy
        self.toMin = toMin
        self.toMax = toMax
        self.prepareRound = prepareRound
        self.canNormalAttack = canNormalAttack
        self.canMagicAttack = canMagicAttack

    def getMagicHurt(self): #返回满级最大攻击伤害
        return self.magicHurt

    def getHurt(self): #返回满级最大策略攻击伤害
        return self.hurt

    def setHurt(self, hurt1, hurt2): #计算满级伤害值，需提供第一级和第二级伤害
        self.canNormalAttack = True
        step = hurt2 - hurt1
        self.hurt = hurt1 + step * 9

    def setMagicHurt(self, magicHurt1, magicHurt2): #计算满级策略伤害值，需提供第一级和第二级伤害
        self.canMagicAttack = True
        step = magicHurt2 - magicHurt1
        self.magicHurt = magicHurt1 + step * 9

    def releaseMagic(self, pos, ourGroup, enemy): #武将释放技能
        pass

    def printout(self):
        print("战法名称:"+ self.mName)
        if(self.canNormalAttack):
            print("物理伤害："+ self.getHurt())

        if(self.canMagicAttack):
            print("策略伤害:" + self.getMagicHurt())
