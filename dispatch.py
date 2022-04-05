import pandas as pd
import googlemaps
from itertools import tee

#reads in API key from file
api_file = open("apikey")
apikey = api_file.read()
api_file.close()

#creating arrays
distance_value = []
distance_list = []
time_list = []
name_list = [] 

#parsing data from excel spreadsheet and gets destination address from user    
addresses = pd.read_excel('addresses.xlsx')
destination = input("Enter destination address: ")

#connecting to google map API with our API key
gmaps = googlemaps.Client(key=apikey)

#creates output file, overwriting any exist files with same name
file_output = open(destination + ".txt", "w")

#loops through address list and runs it against the destination address
#currently not very optimized, it does 1 API call per entry in the excel sheet
#but the distance_matrix function takes up to 25 destinations or origins so we could
#divide the technician list into batches and process 24 at a time(24 tech home addresses + 1 client address)
#however this was a quicky and dirty script I knocked out in a couple hours and its going to be run manually and
#you get something like 6000 API calls for free so not super concerned with hitting that limit
#it also uses 4 seperate arrays instead of a multidimensional one or custom data struct like I would probably use
#in another language I'm more familiar with, like I said I knocked this out in a couple hours so just keeping it simple
#may come back to this and optimze it later just as an exercise to get more familiar with Python
for (i1, row1) in addresses.iterrows():
    origin = row1['Address']
    temp_name = row1['Name']
    result = gmaps.distance_matrix(origin, destination, mode = 'driving', units = "imperial")
    result_distance_value = result["rows"][0]["elements"][0]["distance"]["value"] 
    result_distance = result["rows"][0]["elements"][0]["distance"]["text"]
    result_time = result["rows"][0]["elements"][0]["duration"]["text"]
    name_list.append(temp_name)
    time_list.append(result_time)
    distance_list.append(result_distance)
    distance_value.append(result_distance_value)

#sorts techs by distance to destination address
for step in range(len(distance_value)):
        min_idx = step

        for i in range(step + 1, len(distance_value)):
            if distance_value[i] < distance_value[min_idx]:
                min_idx = i
        (distance_value[step], distance_value[min_idx]) = (distance_value[min_idx], distance_value[step])
        (distance_list[step], distance_list[min_idx]) = (distance_list[min_idx], distance_list[step])
        (time_list[step], time_list[min_idx]) = (time_list[min_idx], time_list[step])
        (name_list[step], name_list[min_idx]) = (name_list[min_idx], name_list[step])

#prints output to the console and then writes it to file
#probably a better way to write to files than just directly piping print output into the file but keeping it simple for now
for x in range(len(name_list)):
    print("Name: " + name_list[x], file=open(destination + ".txt", "a"))
    print("Distance: " + distance_list[x], file=open(destination + ".txt", "a"))
    print("Travel time: " + time_list[x], file=open(destination + ".txt", "a"))
    print("\n", file=open(destination + ".txt", "a"))
    print("Name: " + name_list[x])
    print("Distance: " + distance_list[x])
    print("Travel time: " + time_list[x])
    print("\n")

print("Results written to: " + destination + ".txt")

