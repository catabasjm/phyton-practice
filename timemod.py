import time

print(time.ctime(1000000))  #  convert a time in secs since epoch(comp thinks time began) to a readable string

print(time.time())  #  return current secs since epoch

print(time.ctime(time.time()))  #  current date and time

#  time_object = time.localtime()  # local time
#  time_object = time.gmtime()  # UTC time
#  print(time_object)
#  local_time = time.strftime('%B %d %Y %H: %M: %s', time_object)
#  print(local_time)

#  time_string = "19 March, 2021"
#  time_object = time.strptime(time_string, "%d %B, %Y")
#  print(time_object)


# (yr, mon, day, hrs, mins, secs, #day of week, #day of year, dst)
time_tuple = (2024, 4,20, 4, 20,0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)


time_tuple = (2024, 4,20, 4, 20,0, 0, 0, 0)
time_string = time.mktime(time_tuple)    #  converts secs since epoch
print(time_string)
