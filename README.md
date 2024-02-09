   ~~~ This program was created by TruFoox ~~~

***** IMPORTANT INFORMATION BEFORE YOU DO ANYTHING *****
If you dont want to risk a ban, it is highly recommended that you keep an eye on the bot's posts. They may contain extremely offensive or against TOS content, especially if any subreddits in the config have such posts. Additionally, the bot may post nonsense, such as a person's selfie or an image that lacks context. This occurs when the subreddit contains irrelavant or otherwise contextually lacking posts.


Open config.json and change these settings to your discretion:
** READ CAREFULLY **


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
** HIGHLY RECOMMENDED THAT YOU KEEP AT FALSE & AVOID SUBREDDITS WITH FREQUENT UNMARKED NSFW; NSFW IS AGAINST INSTAGRAM TOS **

 - API_Key -
Go to this url and input your temporary API key:
https://developers.facebook.com/tools/debug/accesstoken
After you do that, press the blue "Debug" button. After the new webpage loads, scroll down to the bottom and press "Extend Access Token"
This will give you a different access token, which will last much longer than an ordinary access token. Place the result inside this section of the config
