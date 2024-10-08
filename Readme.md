# Instagram Automation Project - using Selenium - Monitoring using telegram Chatbot

![SocialMediaGIF](https://github.com/user-attachments/assets/a195c71f-2800-4332-9bdf-4e1328dd99d1) 

### Desclaimer

- This project is made only for automation of manual process of Following relevant group of people (who you might know) & unfollowing those you don't want to keep on your Insta. Any unethical use of this code is strongly condemned
- Some features might be deprecated or Insta structure whould have been changed. Project delivers a static code with no intention of future updation. So configure accordingly. Though Contribution is welcomed

### Quick start

user.py -> enter your userId here

secret.py -> enter your password here

Required.py -> Configurations (#Follows + target page)

insta.py -> main

### Telegram

retreive your bot id and chat id from telegram

ChatBot.py -> enter telegram bots credentials

### Features


- Web Automation Framework: Developed a Python-based automation tool using Selenium WebDriver to interact with Instagram's dynamic DOM. Implemented headless browser support for background execution and incorporated anti-detection measures including randomized delays (10-40 seconds) between actions.

- Modular Architecture and Error Handling: Designed a modular system with separate scripts for following (Insta2.py) and unfollowing (Insta3Unfollower.py) operations. Implemented robust error handling with automatic retries and page reloads, including a cache clearing function to resolve persistent errors after three failed attempts.

- Configurable Parameters and Scalability: Created a flexible configuration system (Required.py) allowing users to set follow/unfollow limits, scroll counts (scrollN), and target pages. Implemented a main script (insta.py) with a command-line interface for easy switching between headless/headed modes and follow/unfollow operations.
- API Integration and Data Management: Integrated optional Telegram API support for real-time notifications. Managed user authentication securely using separate files for username (user.py) and password (secret.py). Implemented functions to track operation progress, including followed/unfollowed counts and execution timestamps using the datetime library.