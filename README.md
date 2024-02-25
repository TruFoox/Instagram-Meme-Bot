# Instagram Meme Bot
   ~~~ Hello, welcome to my bot! ~~~
 - CREATED BY TRUFOOX -

***** IMPORTANT INFORMATION BEFORE YOU DO ANYTHING *****
If you dont want to risk a ban, it is highly recommended that you keep an eye on the bot's posts. They may contain extremely offensive or against TOS content, especially if any subreddits in the config have such posts. Additionally, the bot may post nonsense, such as a person's selfie or an image that lacks context. This occurs when the subreddit contains irrelavant or otherwise contextually lacking posts.
 !! Python 3 MUST be installed PRIOR to doing anything following this point !!
To allow this python script to run, you MUST put this command into a command prompt window:
pip install requests colorama pillow numpy
Doing so will allow the program to do what is necessary to work.
 !! IF YOU DO NOT DO THIS, IT WILL NOT RUN. !!

Open config.json and change these settings to your discretion:
** READ CAREFULLY. MANDATORY CHANGES WILL BE SURROUNDED BY ASTERISKS, LIKE THIS**


 - Time_to_Wait -

This setting is the amount of time the bot should wait before attempting another post, in minutes. Lower numbers will lead to a buildup of duplicate posts, and thus worse efficiency, faster. THIS MUST BE AN INTEGER <60.


 - Subreddits -

This setting is a list of all subreddits that the bot should retrieve top posts from. Make sure each subreddit is in quotes and seperated by a comma


 - Subreddit_Weights -

This setting is the odds of any given subreddit in the list being chosen to grab a post from. This setting is useful if different subreddits in the list are posted to at different rates (and thus you may get more duplicates faster for some subreddits than others) or if you simply want to post from certain subreddits more than others. Each index in the list corresponds to the same index in the "Subreddits" list.
For example, if your Subreddits list looks like ["me_irl","memes"] and your Subreddit_Weights list looks like [10,4], there will be a 10/14 chance r/me_irl will be picked, and a 4/14 chance r/memes will be picked (the divisor is 14 because the combined total of all the numbers in Subreddit_Weights is 14).
These numbers can be as high or as low are you want, but it must be above 0 (otherwise there will be a 0% chance of it being picked). Make sure the indexes of each weight DIRECTLY corresponds to the index of the subreddit you want it to apply to. If you want an equal chance for all subreddits, set them all to the same number.
DO NOT PUT MORE OR LESS WEIGHTS IN THE LIST THAN SUBREDDITS. THERE MUST BE AN EQUAL AMOUNT IN BOTH LISTS


 - Blacklist -

This setting is a list of all words that must not be in a post's caption in order for it to be picked. For example, if your Blacklist looks like ["skibidi","fortnite","sus"], posts containing any item in the list inside its caption can not be picked.


 - NSFW_Allowed - 

This setting is self-explanitory. Set to either "True" or "False" depending on whether or not you want to allow the bot to post NSFW.
HIGHLY RECOMMENDED THAT YOU KEEP AT FALSE & AVOID SUBREDDITS WITH FREQUENT UNMARKED NSFW; NSFW IS AGAINST INSTAGRAM TOS


*** - API_Key - ***
1. Go to this URL to generate an access token:
https://developers.facebook.com/tools/explorer/
2. Press the blue "Generate Access Token" button. It will ask you to log in to your facebook account, which is required. Make sure you log into whichever account owns the Instagram account you intend to use.
3. Go to this url and input the access token you just generated:
https://developers.facebook.com/tools/debug/accesstoken
4. Press the blue "Debug" button. After the new webpage loads, scroll down to the bottom and press "Extend Access Token"
5. It will give you a different access token, which will last much longer than an ordinary access token. Place the result inside this section of the config


*** - User_ID - ***
This setting should be changed to the account's User ID.

 - Caption -
This setting allows you to set the caption for every post. If you want to use hashtags, put them here.


 - Debug_Mode -
This setting is generally not for consumer usage. This is entirely for debugging (Finding errors in the code), and you should keep it as "False" if you do not want the console to be flooded with unnecessary data.
