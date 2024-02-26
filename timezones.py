#pip intsall pytz

from datetime import datetime

current_date = datetime.now()
print("The current date and time is", current_date)
current_time = current_date.strftime("%H:%M")
print("The current time is", current_time)

#def timezone():
#    return os.getenv("TIMEZONE")
