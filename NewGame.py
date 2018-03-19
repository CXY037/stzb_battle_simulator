from Magic_ import Magic
from State_ import State
from General_ import General
from general.XunYu_ import XunYu
from Fighting_ import Fight

gen1 = XunYu(name="XunYu1")
gen1.changePos(2)
gen2 = XunYu(name="XunYu2")
gen2.changePos(1)
gen3 = XunYu(name="XunYu3")
gen3.changePos(0)
gen4 = XunYu(name="XunYu4")
gen4.changePos(0)
gen5 = XunYu(name="XunYu5")
gen5.changePos(1)
gen6 = XunYu(name="XunYu6")
gen6.changePos(2)

ourGroup = [gen3,gen2,gen1]
enemy = [gen4,gen5,gen6]
count = 0
for _ in range(100):
    print(count)
    fight = Fight(ourGroup, enemy)
    count += fight.fightingStart()
    fight.reset(ourGroup,enemy)
print("%d"%(count/100))
