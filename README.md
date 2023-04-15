Savory Junction
=

Introduction
=

Savory Junction is a restaurant website with a fully functioning booking system. Users accessing this website will be able to reserve a table at a date and time that is suitable for them. It also informs the user if the restaurant is full at the selected time and date or if they have already reserved a table at that specific time. Users can also leave a review about their experience at the restaurant and give it a star rating.

The website can be viewed here: [Expense Tracker](https://savory-junction-rz.herokuapp.com/ "javory Junction").

# Table of contents
- [User Experience](#userexperience)
- [How To Use](#how-to-use)
- [Features](#features)
- [Future Ideas / Development](#future)
- [Testing](#testing)
- [Deployment](#deployment)
- [Technologies Used](#technologies)
- [Credits](#credits)

<div id='userexperience'/>

User Experience
=

## **User Stories**
- ## **As an website owner I want that:**

    1. The website provides an easy and friendly experience when reserving a table.
    2. The website alerts the user when the complete an action ie. register/reserve/update/delete.
    3. The website allows the user to have an idea of what cuisine is available and to see previous customer reviews.
------

- ## **As an website user I want:**
    1. To easily understand how to navigate the website.
    2. Confident that the reservation system works.
    3. Any actions that the user does gets displayed as alerts.
 ------

- ## **As a returning website user I want:**
    1. To be able to view/update my reservation.
    2. To be able to reserve another table.
    3. To view the menu.


# 1. Strategy

- The main purpose of this website is so users can reserve a table at their desired date and time.
- Each user creates an account so they can create/read/update/delete their reservation.

# 2. Scope
- After a few design choices. A simple 2-page website (excluding the log-in/log-out pages) was chosen for ease of navigation.
- Using UX design, mobile responsiveness and simple color profile.

# 3. Structure
- The user would be greeted with a restaurant image and a call to action button.
- To create a reservation the user would be prompted to log in or register.
- The reservation page would a have simple form design for the user to select a desired date and time.
- The user would be alerted if the booking was successful or that the reservation failed due to the restaurant being full.
- The user could then see their current reservations on the "manage bookings" page.
- In the manage bookings page, the user would be allowed to update their reservation which would include either updating the time 
  of the reservation or deleting the reservation.

# 4. Skeleton
## **Design**
- The initial design was made using Wireframes.

    - ![Wireframe](/static/images/wireframe.png)

- The initial idea of how the system was going to work was sketched on Lucid Charts:

    - ![Lucid Charts](/static/images/lucid-chart.png)

# 5. Surface
 - ## **Color**
   - The basic color scheme would be dominated by white. With navy/black nav and footer bars. And the images would have a more 
     dominant orange color.
   - Buttons to log in/register and make a reservation would be green.
   - To update/delete a reservation they would be red.

<div id='how-to-use'/>

How To Use
=

## Data Used
 - Lorem ipsum dolor sit amet, consectetur adipiscing elit,
 - Lorem ipsum dolor sit amet, consectetur adipiscing elit,
 ## - Income Data
 ![photo](#) 

 ## - Expense Data
 ![photo](#)

# 1. Upon Accessing Site
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
# 2. Home Page
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
# 3. Options
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 


<div id='features'/>

Features
=

The website Savory Junction is a simple website that allows the user to create a reservation for the restaurant. Even though it looks very simple on the outside there are a lot of things working in the background so the user can have a pleasant experience while using the website.

- ## **HOMEPAGE**
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
    
    ![home page](#)

- ## **bookings**
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 

    ![bookings](#)

- ## **Validation**
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
    ![modal](#)

<div id='future'/>

Future Development
=

## **Further Development**
- Dietary information implementation into reservation.
- Shows available dates and not just a date to choose.


 ## **Reasons they are not currently not implemented**
- Due to the time constraints and scope of the project. I would not have enough time to develop and test these new functions before the project deadline.


<div id='testing'/>

Testing
=

## **Solved Bugs**
- The Star rating system acting weird.
- Update reservation wasn't updating properly and even tho 10 tables it would create a second reservation for a reserved table.

## **Unfixed Bugs**
- once a user selects a rating if they click away or decide they want to write a review the star rating selection disappears.
This is purely aesthetical as the rating the user selected will still be posted to the database.
The way to fix this would be to use javascript for the star rating system rather then just css.

## **Validator Testing**

- **Testing**
    - PEP8online.com was down during testing so I installed pycodestyle in VSCode. Then I searched for Linter and selected 'pycodestyle'. This showed if I had any errors which as of deployment is error-free.
    - The 3 problems that are shown are not related to the project itself. They are from the Code Institute template.
    
    ![Linter Check](assets/images/errorfree.png)

## **Manual Testing**
The Following was tested manually and passed:

- **Username Input**
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
- **Options**
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
- **BOOKINGS**
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 

<div id='deployment'/>

Deployment
=

**The app was deployed using Code Institute's github template on Heroku. The steps to deploy are as follows:**
- Create a new Heroku app.
- Set the buildbacks for Python and NodeJS in that order.
- Link the Heroku app to the repository.
- Click on Deploy. 

The live link can be found here [Savory Junction](https://savory-juction-rz.herokuapp.com/ "Savory Junction").

<div id='technologies'/>

Technologies Used
=

- ## Languages
    - Html / CSS / Javascript
    - Django
    - Python


- ## Modules
Some of the modules used included:
- Balsamiq Wireframe
- python Library "Black" - Formating code.
- python Library "ruff" - Checking for errors.

<div id='credits'/>

Credits
=
For insipration and guidance on how a booking system should I work:
- https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78

Custom datepicker code:
- https://jqueryui.com/datepicker/

How to add attributes to fields in views.py:
- http://www.learningaboutelectronics.com/Articles/How-to-add-a-class-or-id-attribute-to-a-Django-form-field.php#:~:text=and%20id%20attributes.-,In%20order%20to%20add%20a%20class%20or%20id%20attribute%20to,%3D%7B'class'%3A'some_class'%7D.


## **Content**
Main Homepage Image by Nick Karvounis:
- https://unsplash.com/photos/YH7KYtYMET0

About us section image by Jay Wennington:
- https://unsplash.com/photos/N_Y88TWmGwA

This service was used to format the website logo in a favicon:
- https://favicon.io/favicon-converter/

The Restaurant Menu was created using Canva and one of its inbuilt templates:
- https://www.canva.com/