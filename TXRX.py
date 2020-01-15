# coding = utf-8
__author = "li shuanglin"
__date = 2020 / 1 / 15

import time,visa
from PowerMeter import PM200
from Controller8742 import Controller

class TXRX:
    def __init__(self,name, ip):
        self.name = name
        self.ip = ip

    def scan(self, step,pm,time_to_wait=1.0):
        controller = Controller(self.name,self.ip)

        for y in range(-10,11,1):
            urly = "http://" + self.ip + '/cmd_send.cgi?cmd=1PA' + str(step) + "&submit=Send"
            controller.set_position(urly,step)
            time.sleep(time_to_wait)
            for x in range(-10,10,1):
                urlx = "http://" + self.ip + '/cmd_send.cgi?cmd=2PA' + str(step) + "&submit=Send"
                controller.set_position(urlx,step)
                time.sleep(time_to_wait)
                with open("scan{}.txt".format(self.name,int(time.time())), "a+") as file:
                    file.write([x*step,y*step,pm.measure()])
                    print(x*step,y*step,pm.measure())

def main():
    print(visa.ResourceManager().list_resources())
    pm = PM200(visa.ResourceManager().list_resources()[0])
    print("Wavelength:%snm"%pm.getWavelength())
    print("PowerAutoRange:%s"%pm.isAutoRange())

    davidTX = TXRX("davidTX","192.168.25.81")
    davidRX = TXRX("davidRX","192.168.25.80")

    davidTX.scan(step=20,time_to_wait=1.5,pm=pm)
    davidRX.scan(step=20,time_to_wait=1.5,pm=pm)

if __name__ == '__main__':
    main()