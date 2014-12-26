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

			if len(arrival_time) > 0:	
				print "Appending Bus Times List"
				bus_times += arrival_time

		if len(bus_times) > 0:
			print "Sorting"
			self.replaceDueArrivals(bus_times)
			return sorted(bus_times, key=lambda x: int(x['estimatedWait'][:2]))
		else:
			return bus_times

	def replaceDueArrivals(self,arrival_times=[]):
		for arrival_time in arrival_times:
			if "due" in arrival_time['estimatedWait']:
				arrival_time['estimatedWait'] = u'0 min'

	def getDisruptionInformation(self, stopcode):
		return self.getAllBusTimes(stopcode)['serviceDisruptions']['criticalMessages']

