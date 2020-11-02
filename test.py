import time
def run_time(func):
	def wrap(*args, **kwargs):
		st = time.time()
		result = func(*args, **kwargs)
		print('{} function running spend time is: {}'.format(func.__name__, time.time()-st))
		return result
	return wrap


@run_time
def test():
	time.sleep(3)



if __name__ == '__main__':
	test()
