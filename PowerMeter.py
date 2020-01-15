__author__ = 'Hwaipy'
__version__ = 'v1.1.20200115'

import visa, time, sys, re
from SCPI import SCPI

sys.path.append('D:\\program\\Hydra\\Pydra')

class PM200:
    def __init__(self, id):
        self.id = id
        self.rm = visa.ResourceManager().open_resource(id)
        self.scpi = SCPI(self.rm.query, self.rm.write)

    def rest(self):
        self.rm.write('*RST')
        return 'Device had been rest.'

    def setLineFrequency(self):
        return self.scpi.SYSTem.LFRequency.write([50])

    def getIdentity(self):
        return self.scpi._IDN.query()

    def getSensorInfo(self):
        return  self.scpi.SYSTem.SENsor.IDN.query()

    def getWavelength(self):
        wl = self.scpi.SENSE.CORRECTION.WAVELENGTH.query()
        return float(wl)

    def setWavelength(self, wavelength):
        self.scpi.SENSE.CORRECTION.WAVELENGTH.write([wavelength])

    def isAutoRange(self):
        return self.scpi.SENSE.POWER.DC.RANGE.AUTO.query()

    def getMeasureRange_at_W(self):
        return self.scpi.SENSE.POWER.DC.RANGE.query()

    def setMeasureRange_at_W(self, range):
        self.scpi.SENSE.POWER.RANGE.write([range])

    def setAutoRange(self, status):
        self.scpi.SENSE.POWER.RANGE.AUTO.write([1 if status else 0])

    def measure(self):
        return float(self.scpi.MEASure.query())*1.0e9

    def Beeper(self):
        self.scpi.SYSTem.BEEPer.write()
        return 'Beeper had been activated'

    def setbeamdiameter(self, diameter):
        self.scpi.SENSE.CORRECTION.BEAMdiameter.write([diameter])

    def setdefaultbeamdiameter(self):
        self.setbeamdiameter('DEFault')

    def getbeamdiameter(self):
        return self.scpi.SENSE.CORRECTION.BEAMdiameter.query()

    def getbandwidth(self):
        return self.scpi.INPut.FILTer.query()


    def onBandwidthFilter(self):
        self.scpi.INPut.FILTer.write([1])

    def offBandwidthFilter(self):
        self.scpi.INPut.FILTer.write([0])

    def setAveragingRate(self, rate):
        self.scpi.SENSe.AVERage.COUNt.write([rate])

    def getAveragingRate(self):
        return self.scpi.SENSe.AVERage.COUNt.query()


class DeviceException(Exception):
    def __init__(self, msg, exception=None):
        self.message = msg
        self.exception = exception

def init_PM():
    rm = visa.ResourceManager()
    instIDs = rm.list_resources()
    print(instIDs)

if __name__ == '__main__':
    rm = visa.ResourceManager().list_resources()
    print(rm)
    pm = PM200(rm[0])
    print(pm.getSensorInfo())
    print(pm.getWavelength())
    while True:
        print("%.3f"%pm.measure())
        time.sleep(0.2)