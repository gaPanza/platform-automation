# REQUIRED SECTION
ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
# END OF REQUIRED SECTION

.PHONY: help build up start down destroy stop restart logs logs-auth logs-core logs-psp

build:
				docker-compose -f docker-compose.yml build $(c)
up:
				docker-compose -f docker-compose.yml up -d $(c)
start:
				docker-compose -f docker-compose.yml start $(c)
clean:
				docker-compose -f docker-compose.yml down $(c)
destroy:
				docker-compose -f docker-compose.yml down -v $(c)
stop:
				docker-compose -f docker-compose.yml stop $(c)
restart:
				docker-compose -f docker-compose.yml stop $(c)
				docker-compose -f docker-compose.yml up -d $(c)
logs: # with the c= param it's possible to specify containers by name (c=auth|c=core|c=psp-conn)
				docker-compose -f docker-compose.yml logs --tail=100 -f $(c)