<br/>
<p align="center">
  <a href="https://github.com/TruFoox/Instagram-Meme-Bot">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Instagram Meme Bot</h3>

  <p align="center">
    An Automated Meme-Posting Bot for Instagram!
    <br/>
    <br/>
    <a href="https://github.com/TruFoox/Instagram-Meme-Bot/issues">Report Bug</a>
    .
    <a href="https://github.com/TruFoox/Instagram-Meme-Bot/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/TruFoox/Instagram-Meme-Bot/total) ![Stargazers](https://img.shields.io/github/stars/TruFoox/Instagram-Meme-Bot?style=social) ![Issues](https://img.shields.io/github/issues/TruFoox/Instagram-Meme-Bot) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Authors](#authors)

## About The Project

This is a simple, lightweight, yet powerful meme-posting bot for instagram, with LOADS of features, and more to come! This bot works by grabbing memes off of various configurable subreddits.

Current features:
* NSFW filter
* Configurable subreddits
* Customizable caption/hashtags
* Customizable wait times between posts
* Word blacklist
* Duplicate post prevention
* Automatic error detection

## Built With

Programmed entirely in python using the requests, colorama, pillow, and numpy libraries

## Getting Started

Follow ALL the directions listed below in order for the bot to function correctly. See "AboutTheConfig.txt" for more information regarding the config.

### Prerequisites

Before anything, you need to have Python 3 downloaded and installed. [You can download the latest version of Python here](https://www.python.org/downloads/)
This program uses a few libraries that might require you to download them if you haven't used them before

* requests
* colorama
* pillow
* numpy

Use this command in the command prompt to download all of the requirements:
```sh
pip install requests colorama pillow numpy
```

### Installation

1. Go to [this URL](https://developers.facebook.com/tools/explorer/)
  
2. Press the blue "Generate Access Token" button. It will ask you to log in to your Facebook account, which is required. Make sure you log into whichever Facebook account owns the Instagram account you intend to use.

3. Go to [this URL](https://developers.facebook.com/tools/debug/accesstoken) and input the access token you just generated

4. Press the blue "Debug" button. After the new webpage loads, scroll down to the bottom and press "Extend Access Token"

5. It will give you a different access token, which will last much longer than an ordinary access token. Place the result inside this section of the config:
```py
"API_Key": "API KEY HERE",
```

## Usage

While the bot runs, YOU MUST MAKE SURE TO MONITOR WHAT THE BOT POSTS! If you fail to do so, the bot could post something against Instagram's TOS. This can be minimized, however, by only choosing from subreddits with decent moderation.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/TruFoox/Instagram-Meme-Bot/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please be a decent human being with your edits

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors

* **Landen Laflamme** - *Student, Developer* - [Landen Laflamme](https://github.com/TruFoox/) - *Created, programmed, and designed this bot!*
