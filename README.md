# Voice Your Way
2016 Spring Penn Apps

## Inspiration

We want to build a web application that's both useful and fun. Voice control and voice query may prove to be extremely useful and promising in the future because it not only brings convenience to modern users but also potentially helpful for handicapped people. 

## What it does

Our app currently has two main functions. First, you could speak out your query or question (or basically anything you want to know or search for) and get a voice answer back. It is quite powerful since it includes domains span from a lot of different fields, e.g. weather, time, music, sports, restaurant, hotel, cities, etc. The voice search frees you from hand typing and provides convenience for people who need assist. 

The second feature is “voice tweets”. You can speak out the thing you want to tweet and it can be posted to twitter with a simple click. 

## How we built it

We built our web app mainly using python flask framework. The voice to text and voice search was achieved using Houndify API. We have also made use of the twitter API for posting to twitter. 

## Challenges we ran into

This is the first time we wrote a web application using python. We learned everything in two days and thus need to brush up a lot of things in order to make it work. The biggest challenge has been to incorporate Houndify API into our app seamlessly and parse the response JSON object and extract the part we need. Also it was a bit challenging to convert this result back into voice, and play it instantaneously. 

## Accomplishments that we're proud of

The biggest accomplishment for us – our app is working! Actually we learned a lot of new things and had a great time hacking together.  

## What we learned

Python flask for web development, properly embed open APIs into our application, also HTML and Javascript. 

## What's next for Voice Your Way

The next step is to implement features that allows picture and video response for voice queries. Also we would like to give directions by speaking out your starting point and destination. These would be some advanced features that build upon our current program.

