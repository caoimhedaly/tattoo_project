
# The Tattoo Project

View the Tattoo Project at <https://keves-tattoo-project.herokuapp.com/>

Css validated by jigsaw.
<http://jigsaw.w3.org/css-validator/check/referer >
 
## Overview
 
I designed this website with two aims in mind:

1. To provide a platform for independent Tattoo artists to diplay their artwork, and make a name for themselves amongst other artists and potential consumers. 

2. To allow consumers to browse the portfolios of different artists and to display their own tattoos for other tattoo fanatics. 


## Wireframe 

<https://balsamiq.cloud/s66rq4k/px2ud9x>

Click the link to view my wireframe for The Tattoo project on balsamiq.
 
## UX

####Megan: I am a 37yr old independent Tattoo artist. By signing up to The Tattoo Project website I was able to create my own profile page with details about my designs, my experience and how to contact me. I can also upload photos of my artwork for potential consumers to view. Not only that, The Tattoo Project is the perfect platform to sell copies of my prints. 

####John: I am a 41yr old carpenter and tattoo fanatic. I'm always on the lookout for new artists and tattoo ideas. By signing up to The Tattoo Project, I am able to browse the profiles of independent Tattooists and buy their prints. I can also browse the tattoos uploaded by likeminded ink fans and have uploaded pictures of some of my own. 



## Features
 
### Existing Features

* Home page with clear, easy navbar links to website pages.
Parallax scrolling with colorful images. 

* Registration- users can chose to register as either an artist or a tattoo 'addict'. 

* Users can view their profile when logged in. 

* As an artist, users can upload images of their prints for sale. These are displayed in a 'prints' gallery. 

* Cart - users can add items to their cart when signed in and when ready, move items to checkout.

* Stripe- payment with stripe implemented. 

* Artist profile- Artists can write a bio with contact details.

* Artist gallery- artist profiles are displayed in a gallery for other users to browse. 

* Print gallery - Artists can upload their prints for sale and these are displayed in the 'Prints' gallery. 

* Reviews - users can write reviews on prints when logged in. 

* Tattoo gallery - users can upload images of their tattoos when logged in and these are diplayed in the 'Tattoo' gallery. 

* Likes and comments - users can comment and like tattoo images when logged in. 



### Features Left to Implement

- Delete and edit profile. 
- Search for tattoos by tag. 
- Search for artists by location. 

## Tech Used

### Some of the tech used includes:
- **HTML**, **CSS** , **python**,  **JQuery**

[Django](https://www.djangoproject.com/)
I used the python web framework Django to create an object relational database. 

[Pillow](https://pypi.org/project/Pillow/)
- Python imaging library. 

[Bootstrap](https://getbootstrap.com/)

[Psycopg](http://initd.org/psycopg/)
 
[Jinja2](http://jinja.pocoo.org/docs/2.10/)
 - Jinja is easy to debug, has ahead-of-time compilation and sandboxed template execution. 
 

[Javascript](https://www.javascript.com/)
- Twitter, Facebook like and pinterest media buttons. 

    

[Balsamiq](https://balsamiq.com/)
- I used Balsamiq cloud to create my mockup.

[Stripe](https://stripe.com/ie)
- I used stripe to enable payment processing. 

[Whitenoise](https://pypi.org/project/whitenoise/)
- Whitenoise allowed my app to serve its own static files. 

[Gunicorn](https://gunicorn.org/)
- I used gunicorn to handle requests. 


## Libraries:

- [Fontawesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com)
- [W3 Schools colorpicker](https://www.w3schools.com/colors/colors_picker.asp)


## Testing

- Manual testing was carried out as follows: 
  

### Home page:

* Mobile view:  
  On smaller screens, the navbar collapses to a dropdown menu.   
  The 'Let's go! button navigates to the 'Now' page with a list of current medications.   
  The hover-to-sweep action does not work on smaller screens. However clicking on each of the icons will take the user to the appropriate page.   

* Larger screens:  
  The navbar is clear and functioning.   
  The hover-to-sweep action works on the 'create a medication'/'weekly calendar'/'view current medications' links. These links are functioning and open the appropriate pages.   
  The 'Let's go! button navigates to the 'Now' page with a list of current medications.   

### Now page:

* Mobile view:  
  By clicking on the 'Now' link in the navbar the "Now page" with a list of currently due medications. 

* Larger screens:  
  By clicking on the 'Now' link in the navbar the "Now page" with a list of currently due medications. 

### Your Weekly schedule:

* Mobile view/larger screens:   
  By clicking on the "your weekly schedule" link in the navbar this page opens.   
  An accordian of the days of the days of the week opens to display medication list for each day of the week.   
  By clicking on the floating addition button at the bottom right corner of the page, the 'add medication' form will render.  
  By clicking on the floating edit button on the bottom roght corner of the page, the 'edit medications' form will render.   

 

### Add medication:

* Mobile View/larger screens:  
  By clicking on the "Add medication" link in the navbar this form opens.   
  By clicking on the calendar icon, a popup calendar appears to select the dates prescribed and discontinued.   
  By clicking om each of the 'time of day' and 'weekday' boxes, a tick will appear.   
  I can enter the name, generic name, doseage and physician name.   
  By clicking on the 'add medication' button, I am brought to the 'edit medication list' page and the new medication has been added to the list. 

### Edit Medication: 

* Mobile View/larger screens:  
  By clicking on the "Edit medications" link in the navbar,  a list of all medications appears in accordian form.   
  By clicking on each medication name, the accordian opens to display the details of that medication.   
  By clicking on the delete button i can delete the medication from the list.  
  By clicking on the edit icon, the edit form renders.  
  By clicking on the calendar icon, a popup calendar appears to change the dates prescribed and discontinued.   
  By clicking on each of the 'time of day' and 'weekday' boxes, a tick will appear.   
  I can edit the name, generic name, doseage and physician name.   
  By clicking on the 'save' button, I am brought to the 'edit medication list' page and the medication has been edited and saved.   



## Contributing

Validation by W3C [Css validator](https://jigsaw.w3.org/css-validator/) 

I followed a [W3 schools](https://www.w3schools.com/howto/howto_css_parallax.asp) tutorial to complete the parallax affect on the homepage. 

I followed a [W3 schools](https://www.w3schools.com/howto/howto_css_image_text.asp) tutorial to create the text overlay on the homepage.

I obtained code for the facebook like button from [Facebook for developers](https://developers.facebook.com/docs/plugins/like-button/).

Code for the pinterest button was taken from [pinterest.com](https://about.pinterest.com/en/browser-button-confirmation-page).

Code for the twitter button was taken from [twitter for developers website](https://developer.twitter.com/en/docs/twitter-for-websites/tweet-button/overview.html).

I followed a [Bootstrtap](https://getbootstrap.com/docs/4.0/components/card/) tutorial to create the cards used in the artist gallery.


## Deployment

<https://keves-tattoo-project.herokuapp.com/>

1. I deployed My django project using the Heroku cloud app platform as follows: 

2. I logged into my Heroku account and clicked on my dashboard link. From here I clicked on the 'New' link in the top right corner and chose 'create new app'.

3. I typed in my app name and chose Europe region in the drop down menu and clicked the 'create app' button. 

4. I scrolled down to deployment method and clicked the 'github' link. I connected to my github account and chose the appropriate repository name. 

5. I clicked on the settings link and entered config variables. 

5. I scrolled down to manual deploy and chose 'master' branch to deploy and clicked the 'deploy branch' button. Finally I enabled automatic deploys so that with each Github push, the updated App would be deployed. 

* I used os.getenv(PORT, 8080) as the port and os.getenv(IP, 0.0.0.0) as the host in my scripts. 

 
### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone <project's Github URL>``` command
2. After you've that you'll need to make sure that you have **npm** installed
  1. You can get **npm** by installing Node from [here](https://nodejs.org/en/)
4. After those dependencies have been installed you'll need to make sure that you have **http-server** installed. You can install this by running the following: ```npm install -g http-server # this also may require sudo on Mac/Linux```
5. Once **http-server** is installed run ```http-server -c-1```
6. The project will now run on [localhost](http://127.0.0.1:8080)
7. Make changes to the code and if you think it belongs in here then just submit a pull request

## Credits

### Media

- The video on the homepage was shared from [youtube](https://www.youtube.com/)

#### Images
- The photos used in this site were obtained from [Unsplash](https://unsplash.com/)

### Content

- No external information sources were used. 




