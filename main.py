import time
import datetime

delay=1.0  

def FormatedList(title, presents_file, delay):
  with open(presents_file) as file:
    presents_list = file.readlines()

  print(title)
  time.sleep(0.4)
  for item in presents_list:
    print(f'--{item.strip()}') 
    time.sleep(delay)
  print(" ")

input(f' Whats the last two digits of the current year? \n')
print("\nMy Christmas List \n")

now = time.time()
time.sleep(0.4)
christmas = time.strptime("25 dec 24", "%d %b %y")
#christmas = time.strptime("25 dec",(input), "%d %b %y")
#ability to select the year
how_long_to_wait = time.mktime(christmas) - now
#would like to make it so seconds and hours are rounded up always 
#28days 5 hours to go is then 29 days

print(f'Today is {time.asctime()}.')
time.sleep(0.4)

print(f'christmas is {time.asctime(christmas)}')
time.sleep(0.5)

print("That's {} to go... \n".format(datetime.timedelta(seconds=how_long_to_wait)))
time.sleep(0.6)

FormatedList("1. BOOKS:", "books.txt", delay)
FormatedList("2. CLOTHING:", "clothing.txt", delay)
FormatedList("3. DIY(WD(with Dad)):", "diy.txt", delay)
