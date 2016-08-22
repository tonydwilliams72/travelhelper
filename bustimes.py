import requests
import json


class BusTimes(object):

    def __init__(self):
        self.baseURL = "https://api.tfl.gov.uk/StopPoint/{}/arrivals/"

    def getAllBusTimes(self, stopCode):
        api_url = self.baseURL.format(stopCode)
        response = requests.get(api_url)
        bus_times_all = json.loads(response.text)
        return bus_times_all

    def getArrivalTimes(self, stopCodes=None, filter=None, results_returned=4):
        bus_times = []

        for stopcode in stopCodes:
            arrival_time = self.getAllBusTimes(stopcode)

            if len(arrival_time) > 0:
                print "Appending Bus Times List"
                bus_times += arrival_time

        # Filter Buses
        for bus in bus_times[:]:
            if filter:
                print "Filter"
                if bus['lineId'] not in filter:
                    bus_times.remove(bus)
                    print "Removed"
                    print bus
            bus[u'timeToStationMins'] = bus['timeToStation'] / 60
        print "Final Bus"
        print bus_times

        if len(bus_times) > 0:
            print "Sorting"
            return sorted(bus_times, key=lambda x: x['timeToStation'])
        else:
            print bus_times
            return bus_times

    def getDisruptionInformation(self, stopcode):
        return self.getAllBusTimes(
            stopcode)['serviceDisruptions']['criticalMessages']
