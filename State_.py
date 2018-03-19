class State:
    #暴走：不分敌我攻击
    STATE_CRAZY = 0x1
    #混乱：既不能物攻也不能法攻
    STATE_CHAOS = 0x2
    #怯战：不能普攻
    STATE_TIMID = 0x4
    #犹豫：不能发动主动战法
    STATE_HESITATE = 0x8
