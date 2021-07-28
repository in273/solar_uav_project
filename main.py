# this is the first draft of the main program in python
# containing psuedocode where the code is as yet unwritten or unclear.

# all imports go here
import datetime
import pandas as pd
import pytz
import pvlib
from timezonefinder import TimezoneFinder

# global variables (if any) and constants go here


# def plane_launch():
#     check landing gear is engaged
#     start engines
#     gain altitude
#     disengage landing gear


# def get_power_level():
#     fetch power_level
#     return power_level


def get_coordinates():
    # code for fetching gps location here
    # below are placeholder coordinates for london
    current_lat = 51.523659
    current_long = -0.158541
    return current_lat, current_long


def get_time():
    # calculate current timezone
    current_lat, current_long = get_coordinates()
    timezone = TimezoneFinder()
    current_timezone = timezone.timezone_at(lng=current_long, lat=current_lat)
    timestamp = pd.Timestamp.now().tz_localize(tz=current_timezone)
    # note to self: the code above may appear to be redundant or not to work.
    # this is because timestamp.now gets the local time. in order for the later code 
    # to work this must be localised to a timezone, hence the first few lines of this
    # subroutine. when the coordinates fetched differ in timezone from where the code
    # is executed this will produce an error. however, given that the computer and its 
    # gps are always in the same location, in practice this is impossible.
    time = pd.DatetimeIndex([timestamp])
    return time


def scout_light():
    current_time = get_time()
    current_lat, current_long = get_coordinates()
    previous_times = pvlib.solarposition.sun_rise_set_transit_ephem(current_time, current_lat, current_long, next_or_previous='previous')
    next_times = pvlib.solarposition.sun_rise_set_transit_ephem(current_time, current_lat, current_long)
    # calculate if now is day or night
    if previous_times.iloc[0,0] > previous_times.iloc[0,1]:
        day = True
        length_of_day = next_times.iloc[0][1] - previous_times.iloc[0][0]
        length_of_night = next_times.iloc[0][0] - next_times.iloc[0][1]
    else:
        day = False
        length_of_day = next_times.iloc[0][1] - next_times.iloc[0][0]
        length_of_night =  next_times.iloc[0][0] - previous_times.iloc[0][1]
    return length_of_day, length_of_night, day


# def scout_path_weather():
#     fetch weather data for current outlined path
#     if weather_threat high:
#         return danger
#     else:
#         return weather        


# def scout_alternate_path_weather(power_level):
#     fetch weather data for surrounding area within a day's reach
#     determine weather_threat for each unit of area
#     attempt to find alternate_path using simple square-to-square algorithm
#     ## a square-to-square algorithm might look at all surrounding areas, pick the one with best sunlight based on forecast, then perform the same check from the next square, and so on. This is just an idea and there are almost definitely better ways of doing this--take this algorithm as a placeholder.
#     if not successful, use brute force algorithm, excluding paths that have already been assessed
#     ## both of these algorithms would follow a similar structure to the following from the main_loop:
#     ## scout_light()
#     ## get_time()
#     ## calculate power_gained using sunlight, weather, and sunrise/sunset times
#     ## calculate remaining_length_of_day
#     ## calculate power_used during the day
#     ## calculate power_left to fly during the night
#     if successful:
#         return alternate_path
#     else:
#         return NULL


# def schedule_emergency_landing(power_level):
#     scout_alternate_path_weather()
#     locate safest landing location within reach of power_level if it exists
#     if no safe landing locations exist:
#         send distress signal
#         emergency_landing()
#     else:
#         return alternate_path


# def main_loop():
#     get_power_level()
#     if power_level critical:
#         emergency_landing()
#     else if power_level low:
#         scout_path_weather()
#         if danger:
#             scout_landing_locations()
#             schedule_emergency_landing(power_level)
#         else:
#             scout_light()
#             get_time()
#             calculate power_gained using sunlight, weather, and sunrise/sunset times
#             calculate remaining_length_of_day
#             calculate power_used during the day
#             calculate power_left to fly during the night
#             if power_left is not enough to fly throughout the night:
#                 scout_alternate_path_weather(power_level)
#                 if alternate_path exists:
#                     alter_path()
#                 else:
#                     schedule_emergency_landing(power_level)
#             else:
#                 continue with current path
