'''
video_store.py : Calculates the cost of renting new/old movies/videos
By: Will Colvill
10/22/2019
'''

#1 User input how many videos/how many days to rent
new_videos = input("How many new videos are you renting?")
new_videos_days = input("How many nights would you like to rent those videos?")
oldies_videos = input("How many oldies videos are you renting?")
oldies_videos_days = input("How many nights would you like to rent those videos?")

#2 Convert inputs to integers
new_videos = int(new_videos)
new_videos_days = int(new_videos_days)
oldies_videos = int(oldies_videos)
oldies_videos_days = int(oldies_videos_days)

#3 Calculate cost of each category of video
new_videos_price = new_videos * new_videos_days * 3
oldies_videos_price = oldies_videos_days * oldies_videos * 2

#4 Calculate total cost
total_cost = oldies_videos_price + new_videos_price

#5 Display the Cost and Information
print("The total cost of renting", new_videos, "new videos for", new_videos_days, "days is $" + str(format(new_videos_price, ",.2f")))
print("The total cost of renting", oldies_videos, "oldies videos for", new_videos_days, "days is $" + str(format(oldies_videos_price, ",.2f")))
print("Your total cost will be $" + str(format(total_cost, ",.2f")))
