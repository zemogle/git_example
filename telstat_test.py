import serial, time, sys, json, urllib2, datetime
from datetime import datetime as dt
from BeautifulSoup import BeautifulSoup


def main():
    scope = { "0" : "Haleakala, Hawaii",
                "1" : "Siding Spring, Australia",}
    time.sleep(2)
    min = datetime.timedelta(seconds=10)
    tels = (0,1)
    for telid in tels:
        now = dt.now()
        teli = int(telid)
        try:
            posfeed = urllib2.urlopen("http://rti.faulkes-telescope.com/control/ExternalPosStatus.isa")
        except:
            text = "The internet is down % PANIC!" % chr(7)
        soup = BeautifulSoup(posfeed)
        alt = soup.findAll('td',attrs={"name":"alt_demand_value"})
        az = soup.findAll('td',attrs={"name":"az_actual_value"})


if __name__ == '__main__':
    main()
