#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

import sys
import Ice
Ice.loadSlice('Printer.ice')
import Example


class PrinterI(Example.Intermediary):
    n = 0

    def __init__(self,Broker):
        self.broker = Broker

    def send(self, message, server, current=None):
        #print("{0}: {1}".format(self.n, message))
        proxy = self.broker.stringToProxy(server)
        printer = Example.PrinterPrx.checkedCast(proxy)

        printer.write(message)
#		sys.stdout.flush()
        self.n += 1


class Proxy(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        servant = PrinterI(broker)

        adapter = broker.createObjectAdapter("PrinterAdapter")
        proxy = adapter.add(servant, broker.stringToIdentity("printer1"))

        print(proxy, flush=True)
        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0


Proxy = Proxy()
sys.exit(Proxy.main(sys.argv))
