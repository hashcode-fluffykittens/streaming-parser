n_videos, n_endpoints, n_requests, n_caches, size_caches = input().split(" ")

video_sizes = []
for i in range(n_videos):
	video_sizes.append(int(input()))
print(n_videos, n_endpoints, n_requests, n_caches, size_caches)