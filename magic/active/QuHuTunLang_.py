from Services_ import Services
from ..ActiveMagic_ import ActiveMagic
from Magic_ import Magic
from State_ import State
import random
import math

PrintOrNot = 1
class QuHuTunLang(Magic):
    magicHurt1 = 76.5
    magicHurt2 = 85.0
    def __init__(self, name="驱虎吞狼", type=Services.SERVICES_CAVALRY, service=1, distance=5, \
                         prob=0.3, toEnemy=True, toMin=3, toMax=3, prepareRound=0, canNormalAttack=False,\
                         canMagicAttack=True):
        super(QuHuTunLang, self).__init__(name, type, service, distance, \
                         prob, toEnemy, toMin, toMax, prepareRound, canNormalAttack,\
                         canMagicAttack)
        self.mName = "驱虎吞狼"

    def releaseMagic(self, generalPos, ourGroup, enemy): #释放战法，考虑暴走和非暴走状态
        '''
        :param generalPos: 释放战法的武将站位
        :param ourGroup: 0前锋 1中军 2大营
        :param enemy: 0前锋 1中军 2大营
        :return:
        '''
        mayAttackList = []
        for enemyGeneralIndex in range(len(enemy)):     #先判断敌军
                if enemyGeneralIndex < self.mDistance - generalPos:
                    mayAttackList.append(enemy[enemyGeneralIndex])

        if (ourGroup[generalPos].currentState & State.STATE_CRAZY):
            #如果该武将进入暴走状态无差别攻击，则把所有可能攻击的武将放入同一个list

            for friendGeneralIndex in range(len(ourGroup)):   #再判断友军
                if abs(generalPos - friendGeneralIndex) <= self.mDistance and \
                                generalPos != friendGeneralIndex:
                    mayAttackList.append(ourGroup[friendGeneralIndex])

        if random.random() < 0.5: #确定战法攻击人数
            attackNumber = self.toMin
        else:
            attackNumber = self.toMax

        self.setMagicHurt(self.magicHurt1, self.magicHurt2)
        initialHurt = self.getMagicHurt() # 战法初始伤害率

        # 随机选择攻击对象
        attackList = []
        while len(attackList) < attackNumber:
            attackIndex = random.randint(0,len(mayAttackList)-1) # a <= randint(a,b) <= b
            if mayAttackList[attackIndex] not in attackList:
                attackList.append(mayAttackList[attackIndex])
        if PrintOrNot : print("%s释放了技能%s，造成:"%(ourGroup[generalPos].mName, self.mName), end=' ')
        for gen in attackList: # 暂时没有考虑兵种克制, 被攻击者兵力减少

            realHurt = 4.8 * math.sqrt(ourGroup[generalPos].mForce) * (\
                (200.0 + ourGroup[generalPos].mStrategy) / (200.0 + gen.mStrategy)\
                * initialHurt / 100.0) * (1.0 + ourGroup[generalPos].toEnemyMagicAttackEnhance \
                                  + gen.getMagicAttackEnhance)
            gen.changeForce(changeNumbers=realHurt, isHeal=False)
            if PrintOrNot : print("%s损失%d兵力"%(gen.mName, realHurt),end=',') #待修改
        if PrintOrNot : print()

