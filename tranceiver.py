#!/usr/bin/python
##/usr/bin/env python3.4
## TransCiver rev 3
## 2/10/14
## reciver is the "file srver" reciving the data and writing the files to the NV memory
# file_sender.py this is rev2
# this object is running on the device streaming the data to the server
# it will take a file crate an Obj that holds "the file" and meta data of the file and send that object.
# line by line is beter cause it willl cunck the file in to little chunks easr on pyro.
# try on video file or a picture file.
# Sending the data from multy srcs
# have the streamr run on diff machine....
# obj Put obj Get obj send / recive
from __future__ import print_function
from __future__ import with_statement
from Pyro4 import threadutil
import Pyro4.util
import Pyro4.core
import Pyro4.naming
import sys
import os
import logging
from threading import Thread
from time import sleep
##import threading
if sys.version_info<(3,0):
    input=raw_input

class TransCiver(object):
    def __init__(self):
        self.outf=open('newOutfile', 'w') # place holder for data recived
        self.inf=open('newInfile', 'r') # place holder for data to send
        self.transciver = Pyro4.core.Proxy("PYRONAME:yuval")
        self.abort = 0
    @Pyro4.oneway
    #self.data
    # make a say hello and call it from a secnd program...
    def Hello(self):
        print("Hey did you call me ...?")
        print("Hello....")
    
    def Get(self):
        file_name_to_recive=input("tell me the file you want to Get: ").strip()
        snder=input("where shuold I get it from? ").strip()
        print("Connecting to {0} asking for {1}.".format(snder, file_name_to_recive))
        # a line that calls Ahmend sender function....Pyro
        #if file_name_to_recive:
        #    self.outf.write(item)
        #else:
        #    self.outf.close()

        print("{0} received a file {1}.".format(sys.Pyro4.nsc, file_name_to_recive))

    def send(self):
        print("transiver asked to send a file\n")
        item=input("Type the file name you want to send: ").strip()
        sendTo=input("type the file destenation server name: ").strip()
        if item:
            print("file to send %s",item)
            f= open(item, 'rb'  )
            for piece in self.read_in_chunks(f):
                sendTo.reciver(piece)
            
    def read_in_chunks(file_object, chunk_size=1024):
    #Lazy function (generator) to read a file piece by piece.
    #Default chunk size: 1k.
        print('in read_in_chanks function')
        while True:
            print('WHILE read_in_chunks')
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data

    def recive(self, data):
        print("Connecting to a peer to receive a file:", file_name_to_recive)
        print("Ahmed is sending you the file...: ").strip()
        if data:
            self.outf.write(data)
    def busyWait(self):
        print('The TranCiver is Now Running...')
        print('tell me what to do next ')
        try:
            try:
                while not self.abort:
                    cmd = input('> ').strip()
                    if cmd == '/quit':
                        break
                    if cmd == 'send':
                        self.send()
                    if cmd == 'get':
                        self.Get()
            except EOFError:
                pass
        finally:
            print('OK leaving now that was fun...')
            self.abort = 1
            self.DaemonThread()

### for clients ########## github.com #####
class DaemonThread(object):
    def __init__(self):
    	self.abort = 0
    def DaemonThread(self): #, transciver):
        if self.abort:
 			print("closing the name server")
			daemon.close()
			ns.close()
        #
        Pyro4.config.SERVERTYPE="thread"
        #hostname=socket.gethostname()
        #print("initializing services... servertype=%s" % Pyro4.config.SERVERTYPE)
        print("calling the Pyro4.core.Daemon")
        with Pyro4.core.Daemon() as daemon:
        	#print("try to locate NS")
            with Pyro4.naming.locateNS() as ns:
                uri = daemon.register(TransCiver())
                print('URI %s' % ns.register("Yuval", uri))
                print('Pyro NS "Yuval" now running...')
                #print("availabe name servers..." % daemon.locationStr)
            	daemon.requestLoop()

################################################################

# --- MAIN --- #
# craet the TranCiver obj call the deamon thread strat the Pyro obj and call the busy wating loop intf' with users
if __name__ == "__main__":
    transciver = TransCiver()
    daemon = DaemonThread()
    #daemonthread = Thread(target = DaemonThread(transciver))
    print("starting the deamon")
    deamonthread = Thread(target = daemon.DaemonThread)
    print("strting the Transiver while thread")
    busyloop = Thread(target = transciver.busyWait)
    deamonthread.start()
    busyloop.start()
    deamonthread.join()
    
    print('Exit.')

