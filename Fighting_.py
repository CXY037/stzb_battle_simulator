import random

PrintOrNot = 1

class Fight: #TODO 死亡判定需要很细节
    TOTAL_ROUND = 8
    '''
    战前准备：指挥技能效果；暂未考虑。
    战斗回合：最大8回合；
    记录回合数变量 round
    记录技能准备回合
    记录技能效果作用的回合数，回合结束后效果消失
    需要维护两个list， ourGroup和enemy
    记录所有武将的速度值，因为会影响出手顺序（包括先手状态，但暂不考虑）
    '''
    def __init__(self, ourGroup, enemy):
        self.ourGroup = ourGroup
        self.enemy = enemy

        #所有武将速度记录
        self.speedList = ourGroup + enemy
        # 按照速度大小排出出手顺序
        sorted(self.speedList, key=lambda gen: gen.mVelocity, reverse=True)

    def reset(self, ourGroup, enemy):
        for gen in ourGroup:
            gen.reset()
        for gen in enemy:
            gen.reset()

    def fightingStart(self):
        fightRound = 1
        flag = 0 # -1表示lose 0表示平局 1表示win
        while fightRound <= self.TOTAL_ROUND: #未考虑技能需要准备回合的情况
            if PrintOrNot : print("第%d回合:"%(fightRound))
            sorted(self.speedList, key=lambda gen: gen.mVelocity, reverse=True)
            for gen in self.speedList:
                if gen in self.ourGroup:
                    if random.random() < gen.mMagic1().mProbability:
                        gen.releaseMagic(gen.getPos(), self.ourGroup, self.enemy)

                    gen.normalAttack(gen.getPos(), self.ourGroup, self.enemy)
                elif gen in self.enemy:
                    if random.random() < gen.mMagic1().mProbability:
                        gen.releaseMagic(gen.getPos(), self.enemy, self.ourGroup)

                    gen.normalAttack(gen.getPos(), self.enemy, self.ourGroup)

                if self.ourGroup[2].mForce <= 0:
                    flag = -1
                    break
                elif self.enemy[2].mForce <= 0:
                    flag = 1
                    break
            if flag == 1 or flag == -1:
                break
            fightRound += 1
            if PrintOrNot : print("剩余兵力: %s: %d; %s: %d; %s: %d; %s: %d;%s: %d; %s: %d"%(self.ourGroup[2].mName, \
                 self.ourGroup[2].mForce, self.ourGroup[1].mName, self.ourGroup[1].mForce,\
                self.ourGroup[0].mName, self.ourGroup[0].mForce, self.enemy[0].mName, self.enemy[0].mForce, \
                self.enemy[1].mName, self.enemy[1].mForce, self.enemy[2].mName, self.enemy[2].mForce))

        if flag == 0:
            if PrintOrNot : print("Draw")
        elif flag == 1:
            if PrintOrNot : print("You win")
        else:
            if PrintOrNot : print("You lose")
        return flag




