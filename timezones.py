#pip intsall pytz - added to requirements.txt
#https://preview.redd.it/imqp9i619a421.png?width=1080&crop=smart&auto=webp&s=6e0b06ca299483a0cb7445dd60d0cdb2a6730f46
import pytz
from datetime import datetime

all_timezones = pytz.all_timezones
#print(all_timezones)

print("Which timezone would you like to select?")
keyboard_input = input()
query = keyboard_input
print("Searching for", query)

#def search_timezones(query):
#    matching_timezones = [timezone for timezone in all_timezones if query.lower() in timezone.lower()]
#    return matching_timezones

#matching_timezones = search_timezones(query)
#print(f"Timezones matching '{query}':")
#for timezone in matching_timezones:
#    print(timezone)


def normalize_and_search_timezones(querry):
    normalized_query = query.lower().replace("_", " ")
    matching_timezones = [timezone for timezone in all_timezones 
                          if normalized_query in timezone.lower().replace("_", " ")]
    return matching_timezones

normalized_matching_timezones = normalize_and_search_timezones(query)

normalized_matching_timezones
print("Timezone foundOLD", normalized_matching_timezones)

are_multiple_timezones = len(normalized_matching_timezones) > 1

# Print the matching timezones
print("Matching Timezones:")
for timezone in normalized_matching_timezones:
    print(timezone)

# Print whether there are multiple timezones
print("Are there multiple timezone names? ", "Yes" if are_multiple_timezones else "No")

#error searching for india vs new york


#def amPM_identifier():
#    if currentTimeInNewYork < 12:
#        return "AM"
#    else:
#        return "PM"

newYorkTz = pytz.timezone("America/New_York")
timeInNewYork = datetime.now(newYorkTz)
currentTimeInNewYork = timeInNewYork.strftime("%H:%M")

print("The current time in New York is:", currentTimeInNewYork)

#select timezone then convert to 12hr