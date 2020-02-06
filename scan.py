#!/usr/bin/python3
# -*- coding: utf-8 -*-

from terminaltables import AsciiTable
from halo import Halo
import requests,sys,os,time,random,json

def banner():
    banner = """
    \033[1;32m
  _____   ______ _______  _____  ______  _______
 |   __| |_____/ |       |     | |     \ |______
 |____\| |    \_ |_____  |_____| |_____/ |______
    \033[0m

    """
    print(banner)

class ScanQR():
    def __init__(self,filex):
        self.url = "http://api.qrserver.com/v1/read-qr-code/"
        self.file = open(filex, "rb")
    def text(self,text):
        for self.x in text + "\n":
            sys.stdout.write(self.x)
            sys.stdout.flush()
            time.sleep(random.random() * 0.1)
    def check(self):
        self.msg = Halo(text="Cracking QR...",spinner="line",color="green")
        self.msg.start()
        time.sleep(5)
        self.msg.stop()
        try:
            os.system("clear")
            banner()
            self.param = {"file":self.file}
            self.post = requests.post(self.url, files=self.param)
            self.scrapp = json.loads(self.post.text)
            for self.q in self.scrapp[0]["symbol"]:
                self.header = [
                        ["TYPE","DATA","ERROR"],
                        [self.scrapp[0]["type"],self.q["data"],self.q["error"]]
                ]
                self.table = AsciiTable(self.header)
                print(self.table.table)
        except:
            self.text("[!] Error Found !!!")
            sys.exit()


if __name__=="__main__":
    try:
        import requests,terminaltables,halo
    except ModuleNotFoundError as e:
        os.system("pip install requests terminaltables halo")
        os.system("clear")
    banner()
    filex = input("image : ")
    ScanQR(filex).check()
