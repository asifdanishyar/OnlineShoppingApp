# Homemate

## Full Stack Frameworks with Django Milestone Project-4

![Homemate](media/foods.jpg)

## Table of Contents  
1. [Description](#description)  
2. [UX](#ux)  
    - [Target Audience](#target-audience) 
    - [Target Audience Goals](#target-audience-goals) 
    - [Site Owner's Goals](#site-owners-goals)
    - [Project Suitability](#project-suitability)
    - [User Stories](#user-stories)
3. [Design](#design)
4. [Wireframes](#wireframes)
5. [Database & Data Models](#database--data-models)
6. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
7. [Technologies Used](#technologies-used)
8. [Testing](#testing)
9. [Deployment](#deployment)
    - [Deployment to Heroku](#deployment-to-heroku)
    - [Local Deployment](#local-deployment)
10. [Credits](#credits)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)
11. [Disclaimer](#disclaimer)
    

## Description

Homemate is designed and developed for a small bussiness that started in the time of Covid19 pendmi. The idea of Homemate is to cook food at home,
and deliver it to the address of citizens. This project is in process but due to project deadline, i must hand in the amount of work i did.
Users can create an account and save profle information.
Users can order their foods and makesecure payments.
Users can see their order histories.

# UX

### Target Audience

 The target audience of this web application is people who wants to have good food with less expenses. 
 It can be both small group of people and big group of people who wants parties at their homes.
 
 ### Target Audience Goals

 - Able to browse the website easily.
 - Get information about the product and services.
 - Make secure payment.
 - Able to purchase anonymously.
 - Able to create account, save profile information and track order history.

 ### Site Owner's Goals

 Site owner's main goal is to create online presence, create brand awareness and attract more customers to 
 sell them online through a secure payment method.

 ### Project Suitability

This project is suitable to make purchases online;
- Users have the ability to search for all types of foods in store.
- Users have the ability to create an account and save their profile information.
- Users have the ability to purchase main dishes, desserts, cakes and make secure payments.
- Users can view their order history.

### User Stories

- **As a store owner:**
1. As a store owner, I want a simple responsive user friendly website.
2. As a store owner, I want to add new products/services in the store.
3. As a store owner, I want to update existing products/services in the store.
4. As a store owner, I want to delete a product/service from the store.  

- **As a site user:**
1. As a user, I expect the website is easy to navigate from one page to another page.
2. As a user, I expect the website to be responsive so I can use it from any device for example mobile, tablet or laptop.
3. As a user, I want to be able to search the items in the store.
4. As a user, I want to be able to see the detailed information about the products and services.
5. As a user, I want to be able to create an account.
6. As a user, I want to be able to add items in the shopping cart and adjust the shopping cart.
7. As a user, I want to be able to save delivery information to my profile.
8. As a user, I want to be able to make secure payments.
9. As a user, I want to be able to make purchases anonymously.
10. As a user, I want to be able to see the order history.
11. As a user, I want to be able to update the profile information.
12. As a user, I want to receive a confirmation email after the checkout.
13. As a user, I want to get in touch with the store owner.
14. As a user, I want to be able to add a review.
15. As a user, I want to be able edit or delete my review.

## Design

 The website design is simple and responsive which allows the user to navigate easily through the website from mobile, tablet 
 or laptop and make purchases. The design inspiration is taken from the **Code Institute's Boutique Ado Project**.

#### Fonts

-  Google fonts and fonts from Code Institute project is used.

#### Icons

- To make design appealing font awesome icons are widely used in the website.

#### Attribute

- The target_blank value is given to the social links in the footer so that they will open in a new tab / window on click.

#### Colors

The color scheme of the website is kept fairly simple to make it attractive and appealing for the users. 
- Dark blue color **#12375a** is used for headings, text and button background in the website.
- Light grey color **#f8f9fa** is used as a background color of navbar and footer to make navigation links and buttons prominenet. 
- White color **#fafafa** is used as a background color of the rest of the page so that products and the information can be displayed clearly.
- Red color **#e84610** is used in the breadcrum on landing page, in the delete button and in hover effect.    

#### Animation

- Animate in scroll library is also used to give nice effect on merchandise, exercise plans and nutrition plans.

#### Hover Effect

- Background color changes to red color **#e84610** when hover over the buttons.
- The color of the nav links and social media links also changes to red color **#e84610** when hovering over them.
- Cursor also changes to hand pointer when hover over buttons.
- Hovering over the free membership breadcrum on landing page, cursor changes to **no-drop**.

## Wireframes

Wireframes for this project were created by using [Balsamiq](https://balsamiq.com/). It includes wireframes for dektop,
tablet and mobile screen size.
 
- [Wireframes in PDF](static/others/Final-Project-Prototype-Balsamiq.pdf)

## Database & Data Models

- **[SQLite3](https://www.sqlite.org/index.html)** databse is used in the development which is pre-installed by django.

- **[PostgreSQL](https://www.postgresql.org/)** databse is used in the production.

## Features
### Existing Features

- **Navbar** - Navbar is fixed at the top all the time so user can easily navigate through the website. Logo is fixed 
at the top left corner. Navbar also contains links, **Merchandise**, **Fitness** and **Nutrition** as well as search bar, 
**My Account** and **Shopping Cart**. On screen size less than 992 px navbar design changes as it appears a burger button on the top 
left corner which contians the logo **All menus**, **???????**, **Main menu** and **Baverages** links. All fields will stay the same.
The search bar is used to search items in the database.

- **Sign Up/Log In** - User can log in if already have an account otherwise user has the option to create an accout. 
User will get an email to verify the account when an account is created on Homemate. 
User can also recover an account if user has forgotten the password.
- **Admin** - For website management the store owner will have extra links in my account dropdown when owner is logged in as 
a super user.
- **Customer Reviews** - When a user land on the home page, user can read the customer reviews by clicking on **Customer Reviews** button.
- **Search** - User can search for any items in the database either way, without logging in or after logging in the website.
- **Sign Out** - Sign out allows a user to end the session but user has to confirm it by clicking on **Sign Out** which 
will bring the user to the home page.
- **Add to Cart** - User can add any items to the shopping cart with **Add to Cart** button.
Then user will see an **info toast message** and at the top right side of the page and it will disappear after 4 seconds.
- **Shopping Cart Adjustment** - User can update the quantity of items in the shopping cart.
- **Checkout** - User can checkout and pay by filling out the order form.
- **Order Summary** - On checkout page user will be shown the order Summary and button to adjust the shopping cart.
- **Profile** - Logged in user can save the delivery information in his/her profile.
- **Profile Update** - Logged in user can aslo update his/her delivery information saved in profile.
- **Autofill** - If user has saved his/her delivery information then the order form will be prefilled on next purchase.
- **Order History & Order Details** Logged in user can see his/her order history and details of particular order by going into the profile page.
- **Add/Update/Delete items** - Logged in user can also add, update or delete an item if user has purchased something.
- **Deletion Confirmation**- If a user click on delete button, then a modal will pop up to confirm if user is sure to delete the review or not.
- **Add/Update/Delete Product/Plans** - Update and delete buttons will only show up to the Super User (Store Owner). Super User 
can add new items, update existing items and delete the items from the website.
- **Deletion Confirmation for super user**- If super user click on delete button, then a modal will pop up to confirm if super user is sure 
to delete the product or not.

### Features Left to Implement

- **Search** - At the moment search is performed only on the product items but the plan is to add the possiblities of searching by item types or links 
to the items that nearly matches the searched.
- **Social Media Log In** - Log In through social media functionality will also be added in the future.
- **Footer and other social links** -  Footer and other social contacts will add soon.
- **Discount percentage** - A discount percentage will also be added and calculated if customer buy more than 5000 kr, they recieve a special discount.

## Technologies Used

- **HTML5** - HTML5 is used to create the the structure of the website.
- **CSS3** - CSS3 is used for custom styling the HTML5 elements. 
- **JavaScript/JQuery** - is used to make the website interactive. 
- **[Bootstrap Framework](https://getbootstrap.com/)** - Front-end framework is used to make website responsive.
- **[Python](https://www.python.org/)** - Python is used as the back-end programming language.
- **[pip](https://pip.pypa.io/en/stable/)** - Used to install python packages.
- **[Django](https://www.djangoproject.com/)** - Python Web framework that encourages rapid development is used to create this project.
- **[Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)** - Django crispy forms are used to control the rendering behavior of Django forms.
- **[Jinja](https://jinja.palletsprojects.com/en/2.11.x/)** - Jinja templating language is used with Django in the HTML5 code.
- **[Balsamiq](https://balsamiq.com/)** - Balsamiq is used to create wireframes for this project.
- **[Google Fonts](https://fonts.google.com/)** - Google fonts are used in this project.
- **[Git](https://git-scm.com/)** - Used as a distributed version control system.
- **[Gitpod](https://www.gitpod.io/)** - Used as a online IDE.
- **[Github](https://github.com/)** - Used as a remote repository. 
- **[Heroku](https://www.heroku.com/#)** - It is used as hosting platform to deploy this project.
- **[Stripe](https://stripe.com/en-dk)** - Used to add secure payment feature in this project.
- **[HTML Formatter](https://webformatter.com/html)** - Used to format and beautify my code.
- **[Animate On Scroll](https://michalsnik.github.io/aos/)** - Used to make website visually appealing.
- **[AWS](https://aws.amazon.com/)** - Used to store static files.
- **[Am I Responsive](http://ami.responsivedesign.is/#)** - Used to create a responsive image on different screens.
- **[Gunicorn](https://gunicorn.org/)** - It is a Python Web Server Gateway Interface HTTP server used in deploying the project to Heroku. 
- **[Psycopg2](https://pypi.org/project/psycopg2/)** - Used to setup **PostgreSQL** database.
- **[Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)** - Used to create, configure, and manage AWS services, such as S3.
- **[Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)** - Used to create secret key.
- **[Temp Mail](https://temp-mail.org/en/)** - Used to get temporary mail address to test login functionality.

## Testing

Google developers tool has been used from the  beginning to see the the result after adding a feature or after making changes, how do they look
like on different screen sizes. Further I used **print statement** to debug the issues.
I created my own account and tested all the functions to make sure they work properly. In addition, I aslo asked my family and
friends to test the project and give their feedback.

### User Stories

User stories from the UX section were tested to see if they all work as intended. 

#### As a store owner

- *As a store owner, I want a simple responsive user friendly website.*
1. A simple minimalist design is created. 
2. Go to the **Home** Page and browse through the website to experience the design.
3. Right click and go to **inspect** and choose mobile, tablet or desktop screen size to test the page responsiveness.
- *As a store owner, I want to add new products/services in the store.*
1. Go to the **Home** Page.
2. Log In as a **super user** and click on **My Account**, a dropdown will open.
3. Go to **Homemate Admin**, click on add product.
4. Fill out the relevant form and click on **Add**.
5. Item will be added in the store.
- *As a store owner, I want to update existing products/services in the store.*
1. Go to the **Home** Page and log in as a **super user**.
2. Go to **Homemate**, **product**.
3. Under each product/service **Edit** button will show up.
4. Click on **Edit** button, make changes and click on **Update** button to make updates.
- *As a store owner, I want to delete a product/service from the store.*
1. Go to the **Home** Page and log in as a **super user**.
2. Go to **Merchandise**, **Exercise** or **Nutrition**.
3. Under each product/service **Delete** button will show up.
4. Click on **Delete** button, a modal will appear to confirm the deletion.
5. Click on **Yes**, item will be deleted.

#### As a site user

- *As a user, I expect the website is easy to navigate from one page to another page.*
1. Go to the **Home** Page.
2. Navbar stays at the top all the time and contains the main navigation links like **Merchandise**, **Exercise** and **Nutrition**
as well as a **Search bar**, **My Account** button and **Shopping Cart**.
3. **Home** button is also added in different placed in the website to bring user back to home page. Thus user can easily 
navigate through the website.
- *As a user, I expect the website to be responsive so I can use it form any device for example mobile, tablet or laptop.*
1. Go to the **Home** right click and go to **inspect**.
2. Choose mobile, tablet or desktop screen size you want to test the page responsiveness.
- *As a user, I want to be able to search the items in the store.*
1. Go to the **Search input box** in the navbar.
2. Add any search key word and click on search icon.
- *As a user, I want to be able to see the detailed information about the products and services.*
1. Go to the **Home** Page.
2. For **Merchandise** item's detail, go to **Merchandise** and click on **Detials** button.
3. A new window will open which contains the item detail.
4. For **Exercise Plans** detail, click on **Exercise**.
5. A new window will open which contains the **Exercise Plans** and their detail.
4. For **Nutrition Plans** detail, click on **Nutrition**.
5. A new window will open which contains the **Nutrition Plans** and their detail.
- *As a user, I want to be able to create an account.*
1. Go to the **Home** Page and click on **My Account**.
2. From the dropdown select **Register**.
3. Fill in the form and click on **Sign Up**.
4. Verification email will be sent to provided email address.
5. Verify your email addess, your account is created.
- *As a user, I want to be able to add items in the shopping cart and adjust the shopping cart.*
1. Go to the **Home** Page.
2. To add **Merchandise** items , go to **Merchandise** and click on **Detials** button.
3. A new window will open which contains the item detail and **Add to Cart** button.
4. Click on **Add to Cart** button to add item in the **Shopping Cart**.
5. To add **Exercise Plans**, click on **Exercise**.
6. A new window will open which contains the **Exercise Plans**.
7. Click on **Add to Cart** button to add the **Exercise Plan** in the **Shopping Cart**.
8. To add **Nutrition Plans**, click on **Nutrition**.
9. A new window will open which contains the **Nutrition Plans**.
10. Click on **Add to Cart** button to add the **Nutrition Plan** in the **Shopping Cart**.
11. To adjust the **Shopping Cart**, click on the **Shopping Cart**.
12. A new window will open which contain the **Shopping Cart** items.
13. To update the quantity of the merchandise item change the quantity in the input box.
14. Clik the **Update** button to adjust the **Shopping Cart**.
15. To delete any item from the **Shopping Cart** click on **Delete** button.
- *As a user, I want to be able to save delivery information to my profile.*
1. Go to the **Home** page and log in.
2. Add **Merchandise**, **Exercise Plan** or **Nutrition Plan** to **Shopping Cart**.
3. Click on **Shopping Cart** to view the items and then click on the **Checkout** button.
4. Fill in the order complete form and check **Save this delivery information to my profile** box.
- *As a user, I want to be able to make secure payments.*
1. Go to the **Home** page and log in.
2. Add **Merchandise**, **Exercise Plan** or **Nutrition Plan** to **Shopping Cart**.
3. Click on **Shopping Cart** to view the items and then click on the **Checkout** button.
4. Fill in the order complete form.
5. Add credit card number, expiry date, cvc, zip and click on **Complete Order** button.
- *As a user, I want to be able to make purchases anonymously.*
1. Go to the **Home** page.
2. Add **Merchandise**, **Exercise Plan** or **Nutrition Plan** to **Shopping Cart**.
3. Click on **Shopping Cart** to view the items and then click on the **Checkout** button.
4. Fill in the order complete form.
5. Add credit card number, expiry date, cvc, zip and click on **Complete Order** button.
- *As a user, I want to be able to see the order history.*
1. Go to the **Home** page and log in.
2. Click on **My Account** and select **My Profile** from the dropdown.
3. If user has already purchased something then in **User Info** section **My Orders** button will appear.
4. Click on **My Orders** button to view the order history.
- *As a user, I want to be able to update the profile information.*
1. Go to the **Home** page and log in.
2. Click on **My Account** and select **My Profile** from the dropdown.
3. A new window will open, which contains the delivery information.
4. Change any information and click on **Update** button.
- *As a user, I want to receive a confirmation email after the checkout.*
1. Go to the **Home** page and log in.
2. Add **Merchandise**, **Exercise Plan** or **Nutrition Plan** to **Shopping Cart**.
3. Click on **Shopping Cart** to view the items and then click on the **Checkout** button.
4. Fill in the order complete form.
5. Add credit card information and clik on **Complete Order** button.
6. An order confirmation email has sent to the user.
- *As a user, I want to get in touch with the store owner.*
1. Click on contact icon in the footer.
2. A new window will open which contains **Contact Us** form.
3. Fill in the form and clik on **Send** button.
- *As a user, I want to be able to add a review.*
1. Go to the **Home** page and log in.
2. Click on **My Account** and select **My Profile** from the dropdown.
3. If user has already purchased something then in **User Info** section **Add Review** button will appear.
4. Click on **Add Review** button, a new window will open which contains **Add Review** form.
5. Fill in the form and click **Add** button.
- *As a user, I want to be able edit or delete my items.*
1. Go to the **Home** page and click on **product items**.
2. **Edit** and **Delete** buttons will appear under your added items.
3. Click on **Edit** button, a new window will open to edit it.
4. Make the changes and click on **Update** button.
5. To delete the history or reviews, click on **Delete** button, a modal will appear to confirm the deletion.
6. Click on **Yes** to delete the  reviews.

### Responsiveness on different browsers & Mobiles

The website is tested on following browsers and mobiles, it looks fine and work properly on them.
- Google Chrome
- Microsoft Edge
- Firefox
- Opera 
- iPhone 6
- Huawei P30 lite
- ipad
- Samsung

### Code Validation

The code has been validated by using;

- [W3C Markup Validation Service for HTML](https://validator.w3.org/)
- [W3C Markup Validation Service for CSS](https://jigsaw.w3.org/css-validator/)
- [Pep8 Online for Pyhton](http://pep8online.com/)
- [JSHint](https://jshint.com/)

### Interesting Bugs / Issue

1. **Modal was not working properly** - I was working on profile and creating user, it was working perfect. then i jump to the products and wanted to
add some more functionalities to the product. Then accidentally i made a typo mistake. in the **settings.py** in stead of "LOGIN_REDIRECT_URL = '/'"
i typed "LOGIN_RDIRECT_URL = '/'". i spent almost 3 days on it. I with two tutor support from Code Institute spent 2 days and finally one of the 
tutor support could figure it out and we solved the issue. Then i learned that no matter how good you are in coding you will spend many hours and days
on very simple things. such types of errors are so difficult to find out.

## Deployment

The deployed project and project's **github repository** can be viewed on following links. To test card payments use 
Stripe test payments card number *4242 4242 4242 4242*, expiry *04/24*, CVC *242 42424* and click on complete order.

- **[Hommate Live Page](....)**

- **[Homemate Github Repository](https://github.com/asifdanishyar/OnlineShoppingApp)**

git add
