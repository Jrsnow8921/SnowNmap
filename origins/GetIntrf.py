import netifaces



class GetIntrf:

  def getIntInUse(self):
    tmpList = []
    for x in netifaces.interfaces():
      try:
         if x != 'lo0':
           tmpList.append(netifaces.ifaddresses(x)[2][0]['addr'])
           print 'IP found for interface ' + x
      except KeyError:
        print 'No IP found for interface ' + x
    return tmpList




