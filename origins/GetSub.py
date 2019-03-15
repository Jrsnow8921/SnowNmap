import ipaddr
from GetIntrf import *

class GetSub:

  def subNet(self):
    searchIpList = []
    x = GetIntrf().getIntInUse()[0]
    if not x:
      print 'No IP address to search subnet for :('
    else:
      try:
        a = x.split('.')
        t = ipaddr.IPNetwork(a[0] + '.' + a[1] + '.' + a[2] + '.0/8').subnet(new_prefix=22)
        networks = [(str(n.network), str(n.broadcast)) for n in t][0][1].split('.')
        for j in range(0, int(networks[2]) + 2):
          searchIpList.append(a[0] + '.' +  a[1] + '.' + str(j) + '.0/24')
      except:
        print 'Something went wrong when searching for subnet'
    return searchIpList 

