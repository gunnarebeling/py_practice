start = input("Enter start time: ")
duration = input("Enter duration: ")
week_day = input("Enter day of week: ")
def add_time(start, duration, week_day):
  week_day = week_day.lower()
  day_ls = ["monday","tuesday","wednesday" ,"thursday" , "friday", "saturday", "sunday"]
  start_hr = start.split(":")[0]
  start_min = start.split(":")[1].split(" ")[0]
  start_ampm = start.split()[1]
  dur_hr = duration.split(":")[0]
  dur_min = duration.split(":")[1]
  final_hr = int(start_hr) + int(dur_hr)
  final_min = int(start_min) + int(dur_min)
  final_ampm = start_ampm
  add_days = int(final_hr) / 24
  add_days = int(add_days)
  days_later = ""
  pm_sthr = 12 + int(start_hr)
  finalpm_hr = int(pm_sthr) + int(dur_hr)


  if int(final_min) > 60:
    final_hr = int(final_hr) + 1
    final_min = int(final_min) - 60

  if int(finalpm_hr) >= 24 and start_ampm == "PM":
      remander = int(final_hr) % 24


      if int(remander) == 0:
          final_hr = int(final_hr) - (24 * int(add_days))
          final_ampm = "PM,"
          days_later = "(" + str(add_days) + " days later)"
          if int(add_days) == 1:
              days_later = "(next day)"
      else:
          overlap = int(final_hr) - (24 * int(add_days))
          if int(overlap) >= 12:
              final_hr = int(overlap) - 12
              add_days = int(add_days) + 1
              if final_hr == 0:
                  final_hr = 12
              final_ampm = "AM,"
              days_later = "(" + str(add_days) + " days later)"
              if int(add_days) == 1:
                  days_later = "(next day)"
          elif int(overlap) < 12:
                  final_hr = int(overlap)
                  final_ampm = "PM,"
                  days_later = "(" + str(add_days) + " days later)"
                  if int(add_days) == 1:
                      days_later = "(next day)"

  elif int(final_hr) >= 24 and start_ampm == "AM":
      remander = int(final_hr) % 24


      if int(remander) == 0:
          final_hr = int(final_hr) - (24 * int(add_days))
          final_ampm = "PM,"
          days_later = "(" + str(add_days) + " days later)"
          if int(add_days) == 1:
              final_ampm = "PM,"
              days_later = "(next day)"
      else:
          overlap = int(final_hr) - (24 * int(add_days))
          if int(overlap) >= 12:
              final_hr = int(overlap) - 12

              if final_hr == 0:
                  final_hr = 12
              final_ampm = "PM,"
              days_later =  "(" + str(add_days) + " days later)"
              if int(add_days) == 1:
                  days_later = "(next day)"
          elif int(overlap) < 12:
                  final_hr = int(overlap)
                  final_ampm = "AM,"
                  days_later = "(" + str(add_days) + " days later)"
                  if int(add_days) == 1:
                      final_ampm = "PM,"
                      days_later = "(next day)"



  elif int(final_hr) < 24 and start_ampm == "AM":
      days_later = ""
      add_days = int(add_days) - 1
      if int(final_hr) >= 12:
          final_hr = int(final_hr) - 12
          final_ampm = "PM"



          if final_hr == 0:
              final_hr = 12

  elif  int(finalpm_hr) < 24 and start_ampm == "PM":
      final_hr = int(finalpm_hr) - 12

      if final_hr == 0:
          final_hr = 12



      if int(finalpm_hr) in range(24,35) and start_ampm == "PM":
          final_hr = int(final_hr) - 12
          if final_hr == 0:
              final_hr = 12
          final_ampm = "AM"
          days_later = "(next day)"
          add_days = int(add_days) + 1



  if int(final_hr) < 10:
    final_hr = "0" + str(final_hr)
  if int(final_min) < 10:
    final_min = "0" + str(final_min)

  if week_day in day_ls:
      new_date = day_ls.index(week_day) + int(add_days)
      if new_date > 6:
          weeks = int(add_days) / 7
          new_date = int(add_days) - (int(weeks) * 7) + 1
          if new_date == 7:
              new_date = 0
          week_day = day_ls[new_date]
          week_day = week_day.capitalize()
      else:
          week_day = day_ls[new_date]
          week_day = week_day.capitalize()






  final_time = str(final_hr) + ":" + str(final_min) + " " + final_ampm + " " + week_day + " " + days_later
  return final_time
print(add_time(start, duration, week_day))
