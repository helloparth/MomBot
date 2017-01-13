
MomBot was ideated when I got to work one morning soaked by the rain. I remembered the good days when my Mom would remind me to bring am umbrella.

## Send a text message from the terminal in 3 lines of code:
1. Set your configurations in configs.py
2. Open a python interpreter and type:
'''
> from sms import SMTPServer
> server = SMTPServer()
> server.sendText("parth", "Sup dude?")
''' 




## Scripts
MomBot's server API is modular and let's you write a new script in as little as 4 lines of code. Current Scripts:

* **Weather**: Sends me a text every morning with a description of the current weather conditions and temperature in SOMA. She will also tell me whether I should bring an umbrella.  
    @todo Store the mean from the past _N_ days and only notify me of the weather change if it is more than _M_ stdevs away from mean. 
    
I should also check for rain at any point of the work day, not just in the morning.
    
* **GameDay**: Perhaps the most useful. The quality of my 2 hour bart commute is greatly affected by how crowded it is. This module lets MomBot only send me a notification at 5:00pm with a name and time for every Raiders, A's, and Warriors game that will be happening that evening.
    
* **Inspiration**: Sends me a new inpsirational quote of the day every morning right before I wake up. :D
    
The last 2 were simpler and added for a friend.
    
* **Epipen**: For people with anaphylactic allergies, even the smallest amount of contact, even through cross contamination at restuarents can trigger a life-threatening anaphylaxis reaction. They must inject them selves with epinephrine immediately and be rushed to the hospital. This module let's MomBot reminds the user to carry their epinephrine when dinner time is approaching. 
    
* **Rent**: Pay your rent!
    
<img src="https://github.com/helloparth/MomBot/raw/master/weather.png" width="202"/><img src="https://github.com/helloparth/MomBot/raw/master/inspiration.png" width="202"/><img src="https://github.com/helloparth/MomBot/raw/master/epipen_rent.png" width="202"/>


    
## WikiBot

On the side, MomBot also has a side gig as a _WikiBot_ . This let's a user text momBot a query prefaced by the word _wiki_ . And wikibot will go and fetch a one-liner from the closest matching wikipedia article:

![WikiBot](http://i.giphy.com/GWlDzsdighIwo.gif)


