#!/usr/bin/python
import sys
import Pyro4
from tranceiver_rev3 import TransCiver
transciver = Pyro4.Proxy("PYRONAME:Yuval")
transciver.Hello
## transciver.Get
