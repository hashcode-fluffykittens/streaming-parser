# ----- CLASSES

class Video:
    def __init__(self, number, size):
    	self.number = number
    	self.size = size

class Endpoint:
    def __init__(self, number, datacenter_latency):
    	self.number = number
    	self.datacenter_latency = datacenter_latency
    	self.caches = []

class CacheConnection:
    def __init__(self, cache_number, latency):
    	self.cache_number = cache_number
    	self.latency = latency

class Request:
	def __init__(self, amount, to_video, from_endpoint):
		self.amount = amount
		self.to_video = to_video
		self.from_endpoint = from_endpoint
# -------------

class InputParser():
	def parse(self):
		# Getting how many things there are of each
		self.n_videos, self.n_endpoints, self.n_requests, self.n_caches, self.size_caches = input().split(" ")

		# Getting videos
		self.video_sizes = input().split(" ")
		self.videos = []
		for video_number, video_size in enumerate(self.video_sizes):
			self.videos.append(Video(video_number, video_size))

		# Getting endpoints and connections to cache
		self.endpoints = []
		for i in range(int(self.n_endpoints)):
			datacenter_latency, n_connected_caches = input().split(" ")
			endpoint = Endpoint(i, datacenter_latency)
			for j in range(int(n_connected_caches)):
				cache_number, latency = input().split(" ")
				endpoint.caches.append(CacheConnection(cache_number, latency))

			self.endpoints.append(endpoint)

		# Getting all requests
		self.requests = []
		for i in range(int(self.n_requests)):
			video_number, endpoint_number, latency = input().split(" ")
			self.requests.append(Request(latency, self.videos[int(video_number)], self.endpoints[int(endpoint_number)]))

		print(self.videos, self.endpoints, self.requests)


def main():
	parser = InputParser()
	parser.parse()

if __name__ == '__main__':
	main()
