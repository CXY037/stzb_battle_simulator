from Magic_ import Magic
from State_ import State
import random
import math

PrintOrNot = 1

class General:
    TOP_LEVEL = 50
    '''
    string mName 武将名字
    int mLevel 武将等级
    int mForce 兵力
    int mPower  体力
    int mService 兵种
    double mCost 统率值
    int mStrikeDistance 攻击距离
    int mCountry 阵营
    double mAttack 攻击
    double mAttackInc 攻击成长
    double mDefence 防御
    double mDefenceInc 防御成长
    double mStrategy 谋略
    double mStrategyInc 谋略成长
    double mSiege 攻城
    double mSiegeInc 攻城成长
    double mVelocity 速度
    double mVelocityInc 速度成长
    double toEnemyAttackEnhance 我方攻击伤害提升（下降）百分比
    double toEnemyMagicAttackEnhance 我方策略攻击伤害提升（下降）百分比
    double getAttackDamageEnhance 我方受到攻击伤害提升（下降）百分比
    double getMagicAttackEnhance 我方受到策略攻击伤害提升（下降）百分比
    Magic mMagic1；
    Magic mMagic2；
    Magic mMagic3；
    '''
    #mMagic1 = Magic()
    #mMagic2 = Magic()
    #mMagic3 = Magic()

    def __init__(self, name, firstMagic, service=1, cost=10, distance=5, country=0, attack=0, defence=0,\
                strategy=0, siege=0, velocity=0, a_inc=0, d_inc=0, str_inc=0, siege_inc=0, \
                v_inc=0, level=1):
        self.mName = name                    # 武将名
        self.mService = service              # 兵种
        self.mStrikeDistance = distance      # 攻击距离
        self.mCountry = country              # 阵营

        self.mAttack = attack + a_inc * (self.TOP_LEVEL-level)                # 攻击值
        self.mDefence = defence + d_inc * (self.TOP_LEVEL-level)              # 防御值
        self.mStrategy = strategy + str_inc * (self.TOP_LEVEL-level)           # 谋略值
        self.mSiege = siege + siege_inc * (self.TOP_LEVEL-level)               # 攻城值
        self.mVelocity = velocity + v_inc * (self.TOP_LEVEL-level)             # 速度值
        #self.mAttackInc = a_inc              # 攻击成长
        #self.mDefenseInc = d_inc             # 防御成长
        #self.mStrategyInc = str_inc          # 谋略成长
        #self.mSiegeInc = siege_inc           # 攻城成长
        #self.mVelocityInc = v_inc            # 速度成长

        self.mMagic1 = firstMagic            # 第一战法

        self.mLevel = level                  # 武将等级，为方便计算默认50级
        self.currentState = 0                # 武将状态(正常、混乱、暴走、犹豫、怯战)
        self.mForce = 10000                  # 武将兵力，为方便计算默认10000

        self.toEnemyAttackEnhance = 0        # 武将受到战法效果，攻击伤害提升（负值为降）
        self.toEnemyMagicAttackEnhance  = 0  # 武将受到战法效果，策略攻击伤害提升（负值为降）
        self.getAttackEnhance  = 0           # 武将受到战法效果，受到攻击伤害提升（负值为降）
        self.getMagicAttackEnhance  = 0      # 武将受到战法效果，受到策略攻击伤害提升（负值为降）

    # 武将受到控制效果
    def changeState(self, state):
        self.currentState = self.currentState | state

    # 武将受到战法效果导致属性变化
    def changeStats(self, attack=0, defence=0, strategy=0,velocity=0,strikeDistance=0):
        self.mAttack += attack
        self.mStrategy += strategy
        self.mDefence += defence
        self.mVelocity += velocity
        self.mStrikeDistance += strikeDistance

    # 攻击增减伤类效果
    def changeEffect(self,toEnemyAttackEnhance ,toEnemyMagicAttackEnhance ,\
                     getAttackEnhance,getMagicAttackEnhance ):
        self.toEnemyAttackEnhance += toEnemyAttackEnhance
        self.toEnemyMagicAttackEnhance += toEnemyMagicAttackEnhance
        self.getAttackEnhance += getAttackEnhance
        self.getMagicAttackEnhance += getMagicAttackEnhance

    # 士兵数变化，受到攻击兵力减少，受到治疗兵力增加
    def changeForce(self, changeNumbers, isHeal=False):
        if isHeal == True:
            self.mForce += changeNumbers
        else:
            self.mForce -= changeNumbers

    def releaseMagic(self, generalPos, ourGroup, enemy):
        self.mMagic1().releaseMagic(generalPos, ourGroup, enemy)

    def normalAttack(self, generalPos, ourGroup, enemy): # 发动普通攻击
        '''
        :param generalPos:  该武将站的位置 int
        :param ourGroup:  我军阵营 list of General objects
        :param enemy:  敌军阵营 list of General objects
        :return:
        '''
        if ourGroup[generalPos].currentState & State.STATE_CRAZY:
            attackDistance = 0
            while attackDistance== 0:
                attackDistance= random.randint(generalPos-(len(ourGroup)-1),\
                                            min(self.mStrikeDistance, len(ourGroup)+generalPos))
            if attackDistance < 0:
                attackGeneral = ourGroup[generalPos-attackDistance]
            else:
                attackGeneral = enemy[attackDistance-generalPos-1]
        else:  # 未暴走
            if self.mStrikeDistance <= generalPos:  # 攻击距离太小，打不到敌军，不能进行普攻
                #print (self.mStrikeDistance, generalPos)
                return

            attackDistance = 0
            while attackDistance == 0:
                attackDistance = random.randint(max(1,generalPos+1), min(self.mStrikeDistance, len(ourGroup)+generalPos))
            attackGeneral = enemy[attackDistance-generalPos-1]

        realHurt = 4.8 * math.sqrt(ourGroup[generalPos].mForce) * (\
                (200.0 + ourGroup[generalPos].mAttack) / (200.0 + attackGeneral.mDefence)\
                ) * (1.0 + ourGroup[generalPos].toEnemyAttackEnhance \
                                  + attackGeneral.getAttackEnhance)
        attackGeneral.changeForce(changeNumbers=realHurt, isHeal=False)
        if PrintOrNot: print("%s进行攻击，造成%s损失%d兵力" % (self.mName, attackGeneral.mName, realHurt))  # 待修改
        #print(self.mStrikeDistance, generalPos)
    # 战斗时，确定该武将站位 0前锋 1中军 2大营
    def changePos(self, pos):
        self.pos = pos
    # 返回该武将在战斗时的站位
    def getPos(self):
        return self.pos

    def reset(self):
        self.mForce = 10000
