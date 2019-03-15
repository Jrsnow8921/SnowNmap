import os, sys
import getpass
#from subprocess import *
from pexpect import pxssh

class RemoteRestartPI:

  def restartPI(self, ip, piPass):
    #call(["ssh", "-t", "pi@" + ip,  "echo " +  piPass + "| sudo -S shutdown -r now"])
    try:
      s = pxssh.pxssh()
      s.login(ip, 'pi', piPass)
      s.sendline('echo' + piPass + '| sudo -S shutdown -r now')  
    except pxssh.ExceptionPxssh as e:
      print("pxssh failed on login.")
      print(e)


