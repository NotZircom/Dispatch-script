# Dispatch-script
Small script I wrote for my brother to use at work, takes a client's office address and runs it against a list of techs and their home addresses to generate a list of travel time/distance to the client's office for all their techs to determine the preferable order of who should handle the call.

Not super experienced with Python or Google Maps API so bit of a learning experience and could use some further optimization that I may do at a later date just for the practice.
Mainly that I used 4 or 5 different arrays to store all the different values and used a sort of roundabout sorting method, will want to look into how to make a custom data structs in python and see if overloading comparision operators is allowed like it is in C++ or Java, or maybe leverage an existing data structure from panda and store it all in there, I admittedly did not poke around very much in it aside from using it to parse the excel sheet.
Also, it currently uses 1 API call per entry in the original address file, so for 20 techs it'll use 20 API calls every time its runs. The distance_matrix function from the maps API I am using takes up to 25 origin/destination addresses though, so can divide the addresses list and parse it in batches to use less requests just for efficiency's sake.

Additional features to add may be only showing people on the list based on who is currently on call when you run the script, or sorting it by on call order, etc. Would need to add an additional column in the addresses file as well as the additional logic to filter the list but that shouldnt' be too hard, and also would probably rename the addresses file at that point to something else since it's no longer just about their distance to the client site.

I'm currently taking an SQL class so may try writing something to port the excel data into a SQL database and work with it from there instead just as an exercise for the practice.

Included some .bat files to install the dependencies and to actually execute the script just to make it very simple to get going with it

Add names and addresses to addresses file as desired, create apikey file with your api key from GCP, and then run the dispatch.bat for Windows or execute the dispatch.py file however you feel like.


