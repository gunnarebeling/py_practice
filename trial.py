start = input("Enter start time: ")
duration = input("Enter duration: ")

def add_time(start, duration):
  start_hr = start.split(":")[0]
  start_min = start.split(":")[1].split(" ")[0]
  start_ampm = start.split()[1]
  dur_hr = duration.split(":")[0]
  dur_min = duration.split(":")[1]
  final_hr = int(start_hr) + int(dur_hr)
  final_min = int(start_min) + int(dur_min)
  final_ampm = start_ampm
  if int(final_min) > 60:
    final_hr = int(start_hr) + 1
    final_min = int(start_min) - 60
  if int(final_hr) >= 24 and start_ampm == "PM":
      add_days = int(final_hr) // 24
      remander = int(final_hr) % 24
      if int(remander) == 0:
          final_hr = int(final_hr) - (24 * int(add_days))
          final_ampm = "PM" + " " + "(" + str(add_days) + " days)"
      else:
          overlap = int(final_hr) - (24 * int(add_days))
          if int(overlap) >= 12:
              final_hr = int(overlap) - 12
              add_days = int(add_days) + 1
              if final_hr == 0:
                  final_hr = 12
              final_ampm = "PM" + " " + "(" + str(add_days) + " days)"
          elif int(overlap) < 12:
                  final_hr = int(overlap)
                  final_ampm = "" + " " + "(" + str(add_days) + " days)"


  final_time = str(final_hr) + ":" + str(final_min) + " " + final_ampm
  return final_time
print(add_time(start, duration))
