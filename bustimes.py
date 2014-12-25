import requests
import json

class BusTimes(object):

	baseURL = "http://countdown.tfl.gov.uk/stopBoard/"

	def getAllBusTimes(self, stopCode):
		api_url = BusTimes.baseURL + str(stopCode)
		response = requests.get(api_url)
		bus_times_all = json.loads(response.text)
		return bus_times_all

	def getArrivalTimes(self,stopCodes=[], results_returned=4):
		bus_times = []

		for stopcode in stopCodes:
			arrival_time = self.getAllBusTimes(stopcode)['arrivals']
			print "Arrival Times Len:" + str(len(arrival_time))
			print arrival_time

			if len(arrival_time) > 0:	
				print "Append Time.."
				bus_times.append(arrival_time)
				return sorted_bus_times[:results_returned]
			else:
				return bus_times

		if len(bus_times) > 0:
			print "Sorting"
			return sorted(bus_times, key=lambda x: int(x['estimatedWait'][:2]))
		else:
			return bus_times

	def getDisruptionInformation(self, stopcode):
		return self.getAllBusTimes(stopcode)['serviceDisruptions']['criticalMessages']

