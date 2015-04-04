#!/usr/bin/python
import sys
import Pyro4
from tranceiver import TransCiver
transciver = Pyro4.Proxy("PYRONAME:Yuvals.transciver")
transciver.Hello
transciver.Get
