#!/usr/bin/make -f
# -*- mode:makefile -*-

clean:
	$(RM) *.out

run-server:
	./Server.py --Ice.Config=Server.config | tee server-proxy.out

run-client:
	./Client.py '$(shell head -1 intermediary-proxy.out)' '$(shell head -1 server-proxy.out)' 'John Doe'
