# Dispatch-script
Small script I wrote for my brother to use at work, takes a client's office address and runs it against a list of techs and their home addresses to generate a list of travel time/distance to the clients office for all their techs to determine the preferable order of who should handle the call.

Not super experienced with Python or Google Maps API so bit of a learning experience and could use some further optimization that I may do at a later date just for the practice.
Mainly that I used 4 or 5 different arrays to store all the different values and used a sort of roundabout sorting method, will want to look into how to make a custom data structs in python and see if overloading comparision operators is allowed like it is in C++ or Java.
Also, it currently uses 1 API call per entry in the original address file, so for 20 techs it'll use 20 API calls everytime its run(to my understanding at least) but the distance_matrix function I am using takes up to 25 origin/destination addresses, so can divide the list and parse it in batches of 24(24 tech home addresses + 1 client address) at a time. S

Included some .bat files to install the dependencies and to actually execute the script just to make it very simple to get going with it

Add names and addresses to addresses file as desired, create APIKEY file with your api key from GCP, and then run the dispatch.bat for Windows or execute the dispatch.py file however you feel like.
