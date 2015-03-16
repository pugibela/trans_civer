#!/usr/bin/python
import sys
import Pyro4
import Pyro4.util
from tranceiver import TransCiver
sys.excepthook = Pyro4.util.excepthook
#transciver = TransCiver()
print("creating hook to te server")
transciver = Pyro4.Proxy("PYRONAME:Yuvals.transciver")
print("calling the Hello function")
print("")
transciver.Hello
print("calling the get function")
print("")
transciver.Get
