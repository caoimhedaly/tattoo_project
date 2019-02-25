
# Inkspiration

View Inkspiration here https://keves-tattoo-project.herokuapp.com/>

Css validated by [jigsaw](https://jigsaw.w3.org/css-validator/).
 
## Overview
 
I designed this website with two aims in mind:

1. To provide a platform for independent Tattoo artists to diplay their artwork, and make a name for themselves amongst other artists and potential consumers. 

2. To allow consumers to browse the portfolios of different artists and to display their own tattoos for other tattoo fanatics. 


## Wireframe 
I designed the wireframe for Inkspiration using balsamiq. 

View my large screen wireframe [here](https://balsamiq.cloud/s66rq4k/px2ud9x).

View my mobile view wireframe [here](https://balsamiq.cloud/s66rq4k/pi0ekbn).

 
## UX

####Megan: I am a 37yr old independent Tattoo artist. By signing up to the Inkspiration website I was able to create my own profile page with details about my designs, my experience and how to contact me. I can also upload photos of my artwork for potential consumers to view. Not only that, Inkspirational is the perfect platform to sell copies of my prints. 

####John: I am a 41yr old carpenter and tattoo fanatic. I'm always on the lookout for new artists and tattoo ideas. By signing up to Inkspirational, I am able to browse the profiles of independent Tattooists and buy their prints. I can also browse the tattoos uploaded by likeminded ink fans and have uploaded pictures of some of my own. 



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
- I used Balsamiq cloud to create my wireframe.

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

- I implemented automatic testing of python functions, including forms, models and views, using [Unittest](https://docs.python.org/3/library/unittest.html). 

- Manual testing was carried out as follows: 
  

### Home page:

* Mobile view:  
  On smaller screens, the navbar collapses to a dropdown menu.   
   

* Larger screens:  
  The navbar is clear and functioning.   
  All links are functioning and open the appropriate pages.   
  The 'Signup' button initiates a modal to popup giving the user an option of artist or addict. 
  Each of these links take the user to the relevant sign up page. 


### Signup:

* If a user name that already exists is entered, the user will be informed. 
* If no profile image is uploaded, a default avatar image is assigned.
* If passwords do not match or do not meet criteria, the user is informed. 
* On submitting profile form, the site navigates back to the homepage and the user can now view their profile page. 

### Profile page:

* On clicking the profile page link in the navbar, the users profile page is rendered, when logged in. 

### Share you Art:

* On clicking the 'share your art' link in the navbar, a form is rendered which allows the user to upload images of their tattoos. 
* All form details must be filled in order to submit the form. 
* On submission, the user is brought to a page displaying their new post. 
* The back arrow navigates to the tattoo gallery. 

 

### Tattoo Gallery: 

* On clicking the 'Tattoos' link in the navbar, the user is brought to the Tattoo Gallery where all uploaded tattoos are displayed. 
* The user can click on any of the images for further details or to like or comment. 
* The back arrow navigates back to the home page.
* 

### Prints:

* On clicking the Prints link in the navbar, 'product_list.html' is rendered which displays a gallery of uploaded prints. Artists may click on the 'click' link to upload their prints for sale. 
* Addicts may click on each print title to render the 'product_detail' page and find out further info about the print. They may also add a review. 
* Add to cart - logged in users may click on the 'add to cart' button, the item is added to the users cart. 
* The back arrow renders the home page. 

### Cart: 

* By clicking on the 'cart' icon, the user is brought to cart view, where a list of their items in cart are displayed ion a table. 
* Remove - clicking the remove button will remove the item from the cart. 
* Checkout - this button will render the payment detail form. 



## Contributing

Validation by W3C [Css validator](https://jigsaw.w3.org/css-validator/) 

I followed a [W3 schools](https://www.w3schools.com/howto/howto_css_parallax.asp) tutorial to complete the parallax affect on the homepage. 

I followed a [W3 schools](https://www.w3schools.com/howto/howto_css_image_text.asp) tutorial to create the text overlay on the homepage.

I obtained code for the facebook like button from [Facebook for developers](https://developers.facebook.com/docs/plugins/like-button/).

Code for the pinterest button was taken from [pinterest.com](https://about.pinterest.com/en/browser-button-confirmation-page).

Code for the twitter button was taken from [twitter for developers website](https://developer.twitter.com/en/docs/twitter-for-websites/tweet-button/overview.html).

I followed a [Bootstrtap](https://getbootstrap.com/docs/4.0/components/card/) tutorial to create the cards used in the artist gallery.


## Deployment

View Inkspiration on heroku [here](https://keves-tattoo-project.herokuapp.com/).

1. I deployed My django project using the Heroku cloud app platform as follows: 

2. I logged into my Heroku account and clicked on my dashboard link. From here I clicked on the 'New' link in the top right corner and chose 'create new app'.

3. I typed in my app name and chose Europe region in the drop down menu and clicked the 'create app' button. 

4. I scrolled down to deployment method and clicked the 'github' link. I connected to my github account and chose the appropriate repository name. 

5. I clicked on the settings link and entered config variables. 

5. I scrolled down to manual deploy and chose 'master' branch to deploy and clicked the 'deploy branch' button. Finally I enabled automatic deploys so that with each Github push, the updated App would be deployed. 

* I used os.getenv(PORT, 8080) as the port and os.getenv(IP, 0.0.0.0) as the host in my scripts. 


## Credits

### Media

- The video on the homepage was shared from [youtube](https://www.youtube.com/)

#### Images
- The photos used in this site were obtained from [Unsplash](https://unsplash.com/)

### Content

- No external information sources were used. 




