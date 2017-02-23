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

# Getting how many things there are of each
n_videos, n_endpoints, n_requests, n_caches, size_caches = raw_input().split(" ")

# Getting videos
video_sizes = raw_input().split(" ")
videos = []
for video_number, video_size in enumerate(video_sizes):
	videos.append(Video(video_number, video_size))

# Getting endpoints and connections to cache
endpoints = []
for i in range(int(n_endpoints)):
	datacenter_latency, n_connected_caches = raw_input().split(" ")
	endpoint = Endpoint(i, datacenter_latency)
	for j in range(int(n_connected_caches)):
		cache_number, latency = raw_input().split(" ")
		endpoint.caches.append(CacheConnection(cache_number, latency))

	endpoints.append(endpoint)

# Getting all requests
requests = []
for i in range(int(n_requests)):
	video_number, endpoint_number, latency = raw_input().split(" ")
	requests.append(Request(latency, videos[int(video_number)], endpoints[int(endpoint_number)]))

print(videos, endpoints, requests)
