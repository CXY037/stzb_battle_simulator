from Country_ import Country
from General_ import General
from Services_ import Services
from Magic_ import Magic
from magic.active.QuHuTunLang_ import QuHuTunLang
class XunYu(General):
    def __init__(self,name="荀彧", firstMagic=QuHuTunLang, service=Services.SERVICES_CAVALRY, cost=3, distance=2, country=Country.WEI, \
                            attack=47, defence=95, strategy=110, siege=6, velocity=90,
                a_inc=0.55, d_inc=1.56, str_inc=2.25, siege_inc=0.44, v_inc=1.49, level=5):
        super(XunYu, self).__init__(name, firstMagic, service, cost, distance, country, \
                            attack, defence, strategy, siege, velocity,
                a_inc, d_inc, str_inc, siege_inc, v_inc, level)

