import random

def primary():
	f = open("quotes.txt")
	quotes = f.readlines()
	f.close()

	last = 13
	for x in range(0, 2):
		rnd = random.randint(0, last)
		print(quotes[rnd])


if __name__== "__main__":
	primary()
