import requests
import json
import datetime
import random

"""
     (1) asteroid data
"""

def get_random_date():
    start_date = datetime.date(2000, 1, 1)
    end_date = datetime.date(2022, 2, 5)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date.strftime("%Y-%m-%d")

blankURL = "https://api.nasa.gov/neo/rest/v1/feed?start_date={date}&end_date={date}&api_key={NASAAPIKEY}"



def get_asteroid_death():
    # get api url to asteroid data
    randomDate = get_random_date()
    apiURL = blankURL.format(date = randomDate, NASAAPIKEY = "INSERTAPIHERE")

    # get Json response
    response = requests.get(apiURL)
    json_data = json.loads(response.text)

    results = []
    asteroids = json_data["near_earth_objects"][randomDate]
    size = len(asteroids)

    for asteroid in asteroids:
        name = asteroid["name"][1:len(asteroid["name"])-1]
        distance = "{:.2f}".format(float(asteroid["close_approach_data"][0]["miss_distance"]["kilometers"]))
        diameter = "{:.2f}".format((asteroid["estimated_diameter"]["meters"]["estimated_diameter_min"] + asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"])/2)

        messages = []

        messages.append("Bro, you would've likely died on " + randomDate + " if asteroid " + name + " had come " + distance + " km closer to the Earth.")
        messages.append("Did you know? Asteroid " + name + " that's ~" + str(diameter) + " meters in length passed by Earth at a height of " + distance + " km on " + randomDate)
        messages.append("On " + randomDate + ", NASA JPL detected " + str(size) + " asteroids passing by Earth -- but not too close, of course.")
        results.append(messages)

    return results[random.randint(0, size - 1)][random.randint(0, 2)]


"""
     (2) solar eclipse
"""
def get_solar_eclipse():
    start_date = datetime.date.today()
    end_date = start_date
    type = ""
    num = random.randint(1, 3)

    if num == 1:
        type = "total"
        end_date = datetime.date(2023, 4, 20)
    elif num == 2:
        type = "partial"
        end_date = datetime.date(2022, 4, 30)
    else:
        type = "annular"
        end_date = datetime.date(2023, 10, 14)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    return "There are still " + str(days_between_dates) + " days before the next " + type + " solar eclipse on " + end_date.strftime("%B %d, %Y") + "."


if __name__ == '__main__':
    print(get_solar_eclipse())