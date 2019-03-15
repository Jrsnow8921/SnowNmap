import os
import shlex
import socket
from nmap import *
from RemoteRestart import *


class FindPi:

  def __init__(self, ip):
    self.ip = ip

  def nmap_awk_results(self):
    results = []
    ippp = []
    nm = nmap.PortScanner()
    nm.scan(self.ip, arguments= '-sP')
    for h in nm.all_hosts():
      if 'mac' in nm[h]['addresses']:
        for x in nm[h]['vendor'].keys():
          if x.startswith('B8:27:EB'):
            #print(nm[h]['vendor'])
            mac = (nm[h]['addresses']['mac'])
            ip = (nm[h]['addresses']['ipv4'])
            try:
	      results.append([mac, ip, socket.gethostbyaddr(ip)[0]])
              ippp.append(ip)
            except socket.herror:
	      results.append([mac, ip])
              ippp.append(ip)
    #x = len(results)
    for z in results:
      print z

  def nmap_awk_results_reboot(self, piPass):
    results = []
    ippp = []
    nm = nmap.PortScanner()
    nm.scan(self.ip, arguments= '-sP')
    for h in nm.all_hosts():
      if 'mac' in nm[h]['addresses']:
        for x in nm[h]['vendor'].keys():
          if x.startswith('B8:27:EB'):
            #print(nm[h]['vendor'])
            mac = (nm[h]['addresses']['mac'])
            ip = (nm[h]['addresses']['ipv4'])
            try:
              results.append([mac, ip, socket.gethostbyaddr(ip)[0]])
              ippp.append(ip)
            except socket.herror:
              results.append([mac, ip])
              ippp.append(ip)
    #x = len(results)
    for z in results:
      RemoteRestartPI().restartPI(z[1], piPass)

