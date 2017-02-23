# ----- CLASSES

class Video:
    def __init__(self, number, size):
    	self.number = number
    	self.size = size

class Endpoint:
    def __init__(self, number, datacenter_latency, size):
    	self.number = number
    	self.datacenter_latency = datacenter_latency
    	self.size = size
    	self.caches = []

class CacheConnection:
    def __init__(self, cache_number, latency):
    	self.cache_number = cache_number
    	self.latency = latency

# -------------

n_videos, n_endpoints, n_requests, n_caches, size_caches = input().split(" ")

video_sizes = input().split(" ")
videos = []
for video_number, video_size in enumerate(video_sizes):
	videos.append(Video(video_number, video_size))

for i in range(n_endpoints):
	endpoint_number, n_connected_caches = input().split(" ")
	for j in range(n_connected_caches):
		cache_number, latency = input().split(" ")
		CacheConnection(cache_number, latency)


print(videos)