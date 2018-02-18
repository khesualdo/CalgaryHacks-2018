# CalgaryHacks2018

## Inspiration

Occurance of public shootings has increases in the last few years. In case of an emergency in is not always possible for the hostages to contact the police, but even if they find the chanse, it usually take at least a minute.

We decided to create a solution that will notify the emergency services in case a shooting has happened, the following are some benefits our solution introduces: 

- Shorten the time for contacting the emergency services.
- Reduced the overhead for emergency services.
- Provide more safety for public.
- Multiple services could be notifed at once.

## What it does

CeroBuks is a multilevel application, which was designed to notify users is critical situations by moderm ways of communication such as Twitter, phone calls, and SMS.

## How we built it

- Used Python, Java, and C programming languages.
- Used the `tweepy` Python library to send custom tweets.
- Used DreamWeaver to create analytical dashboard.
- Used MySQL database to record and store metadata from the sensors.

Our team made use of an arduino sensor setup with grove loudness sensor and a LORA transiver to record noice levels. The arduino sends data to the a default gateway, which progpogates the packets to the The Thing Network (TTN) server. A background script communicates with the TTN server using the MQTT protocol, the script is notified once the sensor records a noice above the specified threshold.

## Challenges we ran into

Instead of blindly sending every noice recording to the background script, we had to modify the sensor to only send notifications if the noice above the specified threshold was recorded.

## Accomplishments that we're proud of

## What we learned

## What's next for CeroBuks



# Tech

## Charting Frameworks
* Chart.js - http://www.chartjs.org/
* D3.js - https://d3js.org/

## CSS Frameworks
* Materialize - http://materializecss.com/

## Color Schemes
* Coolors - https://coolors.co/browser/latest/1

## TwitterBot

* http://nodotcom.org/python-twitter-tutorial.html
* http://docs.tweepy.org/en/v3.5.0/getting_started.html
