# blackboxai-discord-bot

<p align="center"><img src="https://imgur.com/a/dO43tNI"></p>

AI based discord bot that simply sends a request to blackbox.ai's api and grabs a resposne with no api key needed.
Why blackbox ai? Well aside from the free aspect in terms of their api usage, blackbox.ai also provides sources to the response(s) in which it derives the context from. This gives you an ai, and sources to follow up with for validation or in depth explanations.

# Prerequisites
```
pip3 install -r requirements.txt 
```

# setup
Insert token in blackbox.py file in the token variable, or load token in alternative (safer) ways.

# usage
In discord:
```
!blackbox How many planets are in our solar system?
```