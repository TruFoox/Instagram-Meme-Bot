 ######## THIS HORRIBLE (BUT WORKING) CODE WAS MADE BY LANDEN LAFLAMME (TRUFOOX) ########
import requests, datetime, time, json, sys, math, random, os
from colorama import Fore, Back, Style
from PIL import Image
from io import BytesIO
from datetime import datetime
from os import system

with open("used_images.json", "r") as infile: # Get used images & file size
    images = json.load(infile)
    cwd = os.getcwd()
    storageSize = os.path.getsize(f'{cwd}\\used_images.json')
    print(f"{len(images)} used URLs in storage ({math.floor(storageSize/1000)}kb)")

with open("config.json", "r") as infile: # Starts config
    config = json.load(infile)
    timeWait = config["Time_to_Wait"]
    subreddits = config["Subreddits"]
    subredditWeights = config["Subreddit_Weights"]
    blacklist = config["Blacklist"]
    nsfwAllowed = config["NSFW_Allowed"]
    access_token = config["API_Key"]
    user_id = config["User_ID"]
    defaultCaption = config["Use_Post_Caption"]
    captionCriteria = config["Post_Caption_Blacklist"]
    caption = config["Fallback_Caption"]
    hashtags = config["Hashtags"]
    debug = config["Debug_Mode"]
    timeout = config["Attempts_Before_Timeout"]

# Establish variables & Misc
media_url = ""
countattempt = 0
totalcountattempt = 0
countsuccess = 0
postCaption = ""
chosenSubreddit = ""
upload_url = f"https://graph.facebook.com/v19.0/{user_id}/media"
publish_url = f"https://graph.facebook.com/v19.0/{user_id}/media_publish"
tempList = []
usedDefaultCaption = "False"
i = 0
system("title " + "Instagram Meme Bot") # Sets cmd line window name
for subreddit in subreddits: # Janky fix to a bug where the subreddit weights arent being utilized
    n = subredditWeights[i]
    i += 1
    for x in range(n):
        tempList.append(subreddit)
        tempList.append(subreddit)
        tempList.append(subreddit)
subreddits = tempList
random.shuffle(subreddits)
class style:
   BOLD = '\033[1m'
   END = '\033[0m'

def image_shape(url): # Test image aspect ratio (Whether or not it can fit in instagram)
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        width, height = image.size
        aspect_ratio = width / height
        return 0.72 <= aspect_ratio <= 1.8
    else:
        delete_previous_line()
        print(Fore.RED + style.BOLD + f"{datetime.now().strftime('%H:%M')} - Failed to fetch the image from {url}. HTTP Status Code: {response.status_code}" + style.END)
        return False

def delete_previous_line(): # Highly utilized, used to clear previous lines to make the command line less cluttered/more sleek
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K') 

if debug == "True":
    print("Debug mode ENABLED")
currentTime = datetime.now().strftime('%Y-%m-%d @ %H:%M:%S')
print(f'{currentTime} - Client started - {timeWait} min. interval')
print("")
while True: # Main code
    try:
        print(Fore.WHITE)
        print("Attempting new image", end='\r')
        def get_random_image_url(api_url):
            global countsuccess
            global countattempt
            global totalcountattempt
            global subreddits
            global postCaption
            global blacklist
            global chosenSubreddit
            global timeout
            while True:
                countattempt += 1
                totalcountattempt += 1
                response = requests.get(api_url, headers={'User-Agent': 'Mozilla/5.0'})
                if debug == "True":
                    print(f"Response: {response.json()}")
                if response.status_code == 200: # Test if request sucessful
                    if countattempt < timeout: # Ensures the code is not stuck in a loop
                        post_data = response.json()
                        nsfw = post_data.get("nsfw", False)
                        image_url = post_data.get("url", api_url)
                        postCaption = post_data.get("title")
                        print(Fore.WHITE + f"Image URL: {image_url} from r/{chosenSubreddit}. Testing...", end='\r')
                        if nsfwAllowed == "True" or not nsfw: # Make sure not nsfw if nsfwAllowed is false
                            if image_shape(image_url):
                                if not ".gif" in image_url: # Make sure not .gif
                                    if not image_url in images: # Make sure not duplicate
                                        if not any(item.lower() in postCaption.lower() for item in blacklist): # Make sure caption doesnt contain blacklisted strings
                                            if "https://i.redd.it" in image_url: # Prevents weird image URLs (This fixes an error that occurs with non-reddit image URLs)
                                                images.append(image_url)
                                                with open("used_images.json", "w") as outfile: # Add successful URL to previously used URLS list
                                                    json.dump(images, outfile)
                                                countsuccess += 1
                                                return image_url
                                            else:
                                                delete_previous_line()
                                                print(Fore.RED + f"Invalid URL. Trying again... x{countattempt}", flush=True)
                                        else:
                                            delete_previous_line()
                                            print(Fore.RED + f"Caption contains blacklisted string. Trying again... x{countattempt}", flush=True)
                                    else:
                                        delete_previous_line()
                                        print(Fore.RED + f"Duplicate URL. Trying again... x{countattempt}", flush=True)
                                else:
                                    delete_previous_line()
                                    print(Fore.RED + f"Image is GIF. Trying again... x{countattempt}", flush=True)
                            else:
                                delete_previous_line()
                                print(Fore.RED + f"Image is not square. Trying again... x{countattempt}", flush=True)
                        else:
                            delete_previous_line()
                            print(Fore.RED + f"Image is marked as NSFW. Trying again... x{countattempt}", flush=True)
                    else:
                        print(Fore.RED + f"{datetime.now().strftime('%H:%M')} - Unable to find suitable url in r/{subreddit}. Skipping post. r/{subreddit}", flush=True)
                        print("")
                        return ""
                else:
                    delete_previous_line()
                    if response.status_code == 530:
                        print(Fore.RED + style.BOLD + f"{datetime.now().strftime('%H:%M')} - Failed. Cloudfare HTTP Status Code: 530 - The API this program utilizes is inaccessible. Skipping post w/ +6 hour delay." + style.END)
                        time.sleep(10800)
                    else:
                        print(Fore.RED + style.BOLD + f"{datetime.now().strftime('%H:%M')} - Failed. HTTP Status Code: {response.status_code} x{countattempt}" + style.END, flush=True)
                        time.sleep(5)
                time.sleep(1)
        chosenSubreddit = random.choice(subreddits)
        api_url = f"https://meme-api.com/gimme/{chosenSubreddit}"
        media_url = get_random_image_url(api_url) # Get post from API
        if not media_url == "": # There was a loop and does not continue if one occurred
            if defaultCaption == "False" or any(item.lower() in postCaption.lower() for item in captionCriteria): # Set caption to either fallback or post caption
                upload_data = {
                    "image_url": media_url,
                    "caption": caption + '\n\n.' + '\n\n' + hashtags,
                    "access_token": access_token
                }
                usedDefaultCaption == "False"
            else:
                upload_data = {
                "image_url": media_url,
                "caption": postCaption + '\n\n.' + '\n\n' + hashtags,
                "access_token": access_token
                }
                usedDefaultCaption == "True"
            upload_response = requests.post(upload_url, params=upload_data)
            upload_json = upload_response.json()
            print(Fore.WHITE)
            #test_if_close_attempt = 1/countattempt # Re-add if u cant close or something
            if "error" in upload_json: # Error message handling
                delete_previous_line()
                if debug == "True":
                    print(upload_json)
                if "Error validating access token" in upload_json['error']['message']:
                    print(Fore.RED + f'CRITICAL ERROR: Your Instagram API access token has expired. Follow these instructions to get a new one:')
                    print(Fore.WHITE + '\n1. Go to this URL to generate an access token (You must have created a Facebook app linked to your Instagram account):' + Fore.CYAN + '\n https://developers.facebook.com/tools/explorer/ ' + Fore.WHITE + '\n\n2. Press the blue "Generate Access Token" button. It will ask you to log in to your facebook account, which is required.\n  - Make sure you log into whichever account owns the Instagram account you intend to use. \n\n3. Go to this url and input the access token you just generated:' + Fore.CYAN + ' \n https://developers.facebook.com/tools/debug/accesstoken' + Fore.WHITE + ' \n\n4. Press the blue "Debug" button. After the new webpage loads, scroll down to the bottom and press "Extend Access Token" \n 5. It will give you a different access token, which will expire in 2 months instead of 1 hour. \n\n 5. Place the result inside the "API_Key" of the config')
                    print()
                    input(style.END + "Press Enter to exit...")
                    exit()
                else:
                    print(Fore.RED + f"API Error: {upload_json['error']['message']}")
                    print(Fore.RED + f"Error URL: {media_url}")
            else:
                delete_previous_line()
                if usedDefaultCaption == "True": # Success messages
                    print(Fore.GREEN + f"{datetime.now().strftime('%H:%M')} - {media_url} from r/{chosenSubreddit} SUCCESSFULLY uploaded - {countattempt} Attempt(s) - {math.ceil((countsuccess/totalcountattempt)*1000)/10}% Success Rate")
                    print("")
                else:
                    print(Fore.GREEN + f"{datetime.now().strftime('%H:%M')} - {media_url} from r/{chosenSubreddit} uploaded w/ FALLBACK CAPTION - {countattempt} Attempt(s) - {math.ceil((countsuccess/totalcountattempt)*1000)/10}%")
                    print("")
                if "id" in upload_json: # Finishes uploading
                    creation_id = upload_json["id"]

                    publish_data = {
                        "creation_id": creation_id,
                        "access_token": access_token
                    }
                    publish_response = requests.post(publish_url, params=publish_data)
                    publish_json = publish_response.json()
        time.sleep(timeWait*60) # Wait amount of time specified in config
        countattempt = 0
    except Exception as error:
        print(Fore.RED + style.BOLD + "Whoops, something is wrong! - Please check your config (See Config Help.txt for help)" + style.END)
        print()
        print(style.BOLD + "ERROR INFO:" + style.RED, error)
        print()
        input(style.END + "Press Enter to exit...")
        exit()
