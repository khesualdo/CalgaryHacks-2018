# Shootify :gun: :bomb: :loudspeaker: 

![Shootify](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/000/605/974/datas/gallery.jpg)

Theme: "Long-range Internet of Things". 

Shootify is a scalable and reliable gunshot alerting analysis system for Smart Cities.

[Devpost](https://devpost.com/software/cerobuks)

## My contribution

* http://nodotcom.org/python-twitter-tutorial.html
* http://docs.tweepy.org/en/v3.5.0/getting_started.html

I worked on the the Twitter Bot - `TwitterBoy.py`, which automatically sent a tweet after a gunshot was detected. The tweet contained a message body as well as a map with the location of where the gunshot occurred.

## How to run

* `tweepy` works with Python3.6 and below
* Everything else works with Python3.6 and above

```
> python3.6 Main.py
```

## Inspiration

Occurrence of public shootings has increased in the last few years. In case of an emergency in is not always possible for the hostages and victims to contact the police, but even if they find the chance, it usually takes away precious time for emergency services to respond. On top of that, last year, 8 out of 10 gunfires were not reported to police service, which only more impends their jobs.

We decided to create a solution that will notify the emergency services in case a shooting has occurred. The following are some benefits our solution introduces: 

- Shorten the time for contacting the emergency services
- Reduced the overhead for emergency services
- Provide more safety for public
- Multiple services could be notified at once

## What it does

Shootify is a multilevel application, which was designed to notify users and emergency services in critical situations by modern ways of communication such as Twitter, phone calls, and SMS.

## How we built it

- Used Python, Java, and C programming languages
- Used the `tweepy` Python library to send custom tweets
- Used DreamWeaver to create analytical dashboard
- Used MySQL database to record and store metadata from the sensors
- Used Twilio to initiate phone calls and send SMS

Our team made use of a LoRaWAN technology based Arduino sensor setup with Grove loudness sensor and a LoRa transceiver to record and react to elevated noise levels. The Arduino sends data to the a LoRaWAN gateway, which propagates the packets to the crowdfunded The Thing Network (TTN) server. A background Python script communicates with the TTN server using the MQTT protocol, the script is notified once the sensor records noise above the specified threshold.

## Challenges we ran into

Instead of blindly sending every noise recording to the background script, we had to modify the sensor to only send notifications if the noise above the specified threshold was recorded.

## Accomplishments that we're proud of

This was mostly a learning experience for most members of the group to expose them to IoT, hardware low-level system implementation, as well as data processing and data visualization. Shootify is fully functional, and we hope to squish bugs, add features, and improve it's performance in the future.

## What we learned

- IoT technologies
- Hardware low-level system implementation
- Data processing
- Data visualization

## What's next for Shootify

- Replace the loudness sensor with an audio recording sensor
- Analyze sound data and compare it with known gun sound signatures
    - Based on matches provide an approximation of what kind of guns and how many gunshots were fired
- Make the system less prone to false positives
- Expand our data analysis tools base
