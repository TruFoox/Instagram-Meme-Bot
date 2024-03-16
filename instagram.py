import requests, datetime, time, json, sys, math, random
from colorama import Fore, Back, Style
from PIL import Image
from io import BytesIO
from datetime import datetime

with open("used_images.json", "r") as infile:
    images = json.load(infile)
    print(f"{len(images)} previous URLS in storage")

with open("config.json", "r") as infile:
    config = json.load(infile)
    timeWait = config["Time_to_Wait"]
    subreddits = config["Subreddits"]
    subredditWeights = config["Subreddit_Weights"]
    blacklist = config["Blacklist"]
    nsfwAllowed = config["NSFW_Allowed"]
    access_token = config["API_Key"]
    user_id = config["User_ID"]
    defaultCaption = config["Use_Post_Caption"]
    captionCriteria = config["Post_Caption_Criteria"]
    caption = config["Fallback_Caption"]
    hashtags = config["Hashtags"]
    debug = config["Debug_Mode"]
    
media_url = ""
countattempt = 0
totalcountattempt = 0
countsuccess = 0
postCaption = ""
chosenSubreddit = ""
upload_url = f"https://graph.facebook.com/v18.0/{user_id}/media"
publish_url = f"https://graph.facebook.com/v18.0/{user_id}/media_publish"
tempList = []
i = 0

for subreddit in subreddits:
    n = subredditWeights[i]
    i += 1
    for x in range(n):
        tempList.append(subreddit)
subreddits = tempList

def image_shape(url):
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        width, height = image.size
        aspect_ratio = width / height
        threshold = 1.35
        return 1 / threshold <= aspect_ratio <= threshold
    else:
        delete_previous_line()
        print(Fore.RED + f"Failed to fetch the image from {url}. HTTP Status Code: {response.status_code}")
        return False
def delete_previous_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K') 

currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'Client started - {currentTime}')
print("")
while True:
    try:
        time.sleep(timeWait*60)
        countattempt = 0
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
            while True:
                countattempt += 1
                totalcountattempt += 1
                response = requests.get(api_url, headers={'User-Agent': 'Mozilla/5.0'})
                if debug == "True":
                    print(f"Response: {response.json()}")
                if response.status_code == 200:
                    if countattempt < 50:
                        post_data = response.json()
                        nsfw = post_data.get("nsfw", False)
                        image_url = post_data.get("url", api_url)
                        postCaption = post_data.get("title")
                        print(Fore.WHITE + f"The image URL is: {image_url}", end='\r')
                        if nsfwAllowed == "True" or not nsfw:
                            if image_shape(image_url):
                                if not ".gif" in image_url:
                                    if not image_url in images:
                                        if not any(item.lower() in postCaption.lower() for item in blacklist):
                                            images.append(image_url)
                                            with open("used_images.json", "w") as outfile:
                                                json.dump(images, outfile)
                                            countsuccess += 1
                                            return image_url
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
                            print(Fore.RED + f"The image is marked as NSFW. Trying again... x{countattempt}", flush=True)
                    else:
                        print(Fore.RED + f"Something is causing a loop - Fix may require reopening this program or waiting for more posts... r/{subreddit}", flush=True)
                        return ""
                else:
                    delete_previous_line()
                    print(Fore.RED + f"Failed to fetch data. Status Code: {response.status_code} x{countattempt}", flush=True)
                time.sleep(1)
        chosenSubreddit = random.choice(subreddits)
        api_url = f"https://meme-api.com/gimme/{chosenSubreddit}"
        media_url = get_random_image_url(api_url)
        if not media_url == "":
            if defaultCaption == "False" or any(item.lower() in postCaption.lower() for item in captionCriteria):
                upload_data = {
                    "image_url": media_url,
                    "caption": caption + " " + hashtags,
                    "access_token": access_token
                }
            else:
                upload_data = {
                "image_url": media_url,
                "caption": postCaption + " " + hashtags,
                "access_token": access_token
                }
            upload_response = requests.post(upload_url, params=upload_data)
            upload_json = upload_response.json()
            print(Fore.WHITE)
            test_if_close_attempt = 1/countattempt
            if "error" in upload_json:
                delete_previous_line()
                if debug == "True":
                    print(upload_json)
                print(Fore.RED + f"Error: {upload_json['error']['message']}")
                print(Fore.RED + f"Error URL: {media_url}")
            else:
                delete_previous_line()
                if debug == "True":
                    print(upload_json)
                print(Fore.GREEN + f"{datetime.now().strftime('%H:%M')} - {media_url} from r/{chosenSubreddit} SUCCESSFULLY uploaded - {countattempt} Attempt(s) - {math.ceil((countsuccess/totalcountattempt)*1000)/10}% Success Rate")
                print("")
                if "id" in upload_json:
                    creation_id = upload_json["id"]

                    publish_data = {
                        "creation_id": creation_id,
                        "access_token": access_token
                    }
                    publish_response = requests.post(publish_url, params=publish_data)
                    publish_json = publish_response.json()
    except:
        print(Fore.RED + "CRITICAL ERROR - Whoops, something is wrong! - Please check your config (Check AboutTheConfig.txt)")
        input("Press Enter to exit...")
