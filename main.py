from origins.SnowNmap import *
from origins.GetSub import *
from origins.SnowSpinner import *
from multiprocessing import Process


def main():
    x = GetSub().subNet()
    ss = SnowSpinner()
    rr = str(raw_input("Do you want to restart all Raspberry PI's found: (Y/N)"))    
    if rr == "Y":
      print "Rebooting all Raspberry PI's found"
      piPass = str(raw_input("Enter your Raspberry PI password to enable rebooting: "))
      for y in x:
          ss.start()
          a = Process(target=FindPi(y).nmap_awk_results_reboot(piPass))
          a.start()
          ss.start()
          a.join()
    else:
      for y in x:
        ss.start()
        a = Process(target=FindPi(y).nmap_awk_results())
        a.start()
        ss.stop()
        a.join()


if __name__ == '__main__':
    main()
