import os 

base_path = '/home/ubuntu/github-pro/'

for root, dirs, files in os.walk(base_path):
	for file in files:
		print(root+file)
	for dir in dirs:
		print(dir)
