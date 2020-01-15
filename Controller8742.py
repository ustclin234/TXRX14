#coding = utf-8
import requests, time

class Controller:
    def __init__(self,name,ip):
        self.name = name
        self.ip = ip

    def scan(self,step=20,time_to_wait=1.0):
        for x in range(-10, 10, 1):
            urly = "http://" + self.ip + '/cmd_send.cgi?cmd=1PA' + str(x*step)+'&submit=Send'
            requests.get(urly)
            time.sleep(time_to_wait)
            for y in range(-10,10,1):
                urlx = "http://" + self.ip + '/cmd_send.cgi?cmd=2PA' + str(y*step) + '&submit=Send'
                requests.get(urlx)
                time.sleep(time_to_wait)
                # print(x*step,y*step)

    def set_position(self,url,step):
        requests.get(url)

if __name__ == "__main__":
    davidRX = Controller("davidRX","192.168.25.80")
    davidRX.scan(step=20,time_to_wait=1.5)

    davidTX = Controller("davidTX","192.168.25.81")
    davidTX.scan(step=20,time_to_wait=1.5)

