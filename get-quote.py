import random

def main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len("quotes.txt")
  rnd = random.randint(0,last)
  print(quotes[rnd])

if __name__== "__main__":
  main()
