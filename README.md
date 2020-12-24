# Max Fitnesss

Max Fitness is a fitness subscription application, and an e-commerce website. \
It is an active community built around a product, based on subscription and individual payment models.\
Within the extent of offers such as nutrition and exercise plans, Max Fitness also offers a gym membership plan to all of its potential customers.

Some of the main functionalities of this website are:
    - Search Bar.
    - Register option.
    - Login option.
    - Logout option.
    - Save orders and checkout information to your profile account.
    - Post comments or if blogs that you and other users of the website can see.

![Site Logo](/readme_resources/img_readme/logo.jpg)

## UX

### Viewing and Navigation 

 1. As a shopper, I want to be able to view a list of products so that I can select some to purchase.
 2. As a shopper, I want to be able to view individual product details so that I can indentify the price, description, product rating, product image and available sizes.
 3. As a shopper, I want to be able to quickly indentify deals and special offers so that I can take advantage of special free offer on product I'd like to purchase.
 4. As a shopper, I want to be able to easily view the total of my purchases at any time so that I can avoid spending too much.

### Registration and User Accounts 

 5. As a site user I want to be able to easily register for an account so that I can create a personal account and be able to view my profile.
 6. As a site user I want to be able to easily login or logout so that I can access my personal account information.
 7. As a site user I want to be able to easily recover my password in case I forget it so that I can recover access to my account.
 8. As a site user I want to be able to recive an email confirmation after registering so that I can verify that my account registration was successful.
 9. As a site user I want to be able to have a personalized user profile so that I can view my personal order history, order confirmations, save my payment information and comment on blog posts.
 10. As a site user I want to be able to comment on blog posts, so that I can engage in community discussion.
 11. As a site user I want to join a fitness community and purchase exercise plans and merchandise.

 ### Sorting and Searching

 12. As a shopper I want to be able to sort the list of available products, so that I can easily indentify the best rated, best priced and categorically sorted products.
 13. As a shopper I want to be able to sort specific category of product, so that I can find the best-priced or best-rated product in a specific category, or sort the products in that category by name.
 14. As a shopper I want to be able to sort multiple categories of products simultaneously, so that I can find the best-priced or best-rated products across broad categories, such as "Nutrition" or "Fitness".
 15. As a shopper I want to be able to search for a product by name or description so that I can find a specific product I'd like to purchase.
 16. As a shopper I want to be able to easily see what I've searched for and the number of results, so that I can quickly decide whether the product I want is available.

 ### Purchase and Checkout

 17. As a shopper I want to be able to easily select the quantity and the type of a product when purchasing it, so that I can ensure I don't accidentally select the wrong product, quantity or type.
 18. As a shopper I want to be able to view items in my bag to be purchased, so that I can indentify the total cost of my purchase and all items I will recive.
 19. As a shopper I want to be able to adjust the quantity and type of individual items in my bag, so that I can easily make changes to my purchase before checkout.
 20. As a shopper I want to be able to easily enter my payment information, so that I can check out quickly and with no hassies.
 21. As a shopper I want to be able to feel my personal and payment information is safe and secure, so that I can confidently provide the needed information to make a purchase.
 22. As a shopper I want to be able to view an order confirmation after checkout, so that i can verify that I haven't made any mistakes.
 23. As a shopper I want to be able to recive an email confirmation after checking out, so that I can keep the confirmation of what I've purchased for my records.

 ### Admin and Store Management

 24. As a store owner I want to be able to add a product so that I can add new items to my store.
 25. As a store owner I want to be able to edit/update a product, so that I can change product prices, description, images, and  other product criteria.
 26. As a store owner I want to be able to delete a product, so that I can remove items that are no longer for sale.
 27. As a store owner I want to be able to have a blog, so that I can write and post articles about training.
 28. As a store owner I want to build an active community around product based on subscription and individual payment model.

 ### Strategy plane:

 #### As a Developer

- [x] I aim to build a Django project backend by a relational database to create a website that allows users to store and manipulate data records about a particular domain. 
- [x] The project must be a brand new Django project, composed of multiple apps (an app for each potentially reusable component in your project
- [x] Design a relational database schema well-suited for my domain. Put some thought into the relationships between entities.
- [x] Create at least 2 custom django models beyond the examples shown on the course.
- [x] User Authentication: The project should include an authentication mechanism, allowing a user to register and log in.
- [x] Include at least one form with validation that will allow users to create and edit models in the backend.
- [x] At least one of your Django apps should contain some e-commerce functionality using Stripe.
- [x] Incorporate a main navigation menu and structured layout 
- [x] The frontend should contain some JavaScript logic you have written to enhance the user experience.
- [x] Use Git & GitHub for version control.
- [x] Maintain clear separation between code written by you and code from external sources.
- [x] Deploy the final version of my code to a hosting platform such as Heroku.


## Features

- [x] The home app is used to render a landing page, where there will be a displayed overview of what this store/community is about and what it has to offer.
- [x] Product app used to render product pages. Contains product and category model, as well as front-end javascript ajax logic that will allow sorting of given products.
- [x] Allauth app is used to allow easier handling of user accounts and their registration.
- [x] Bag app used to store, display products user would like to purchase. Allows the user to change contents, contents quantity, and contents type of his purchase before he goes to checkout.
- [x] Checkout app used to handle the purchase of bag items. Uses Stripe for secure card payments.
- [x] Blog app used by superusers to post blogs, and by normal users to post comments on blogs.
- [x] Membership app used to display offers of different subscription models.

## Version Control (git)

The project uses the Git tool to capture changes made in each version of the project build. Below you will find some relevant notes on specific versions that I as a developer find important noting.

## Technologies Used

- [Bootstrap](https://getbootstrap.com/)
    - The project uses **Bootstrap** to provide a responsive toolkit for building the base of the website.
- [Django](https://www.djangoproject.com/)
    - The project uses **Django** framework to provide developer with tools, libraries and technologies that allow faster build of the web application.
- [Stripe](https://stripe.com/en-se)
    - The project uses **Stripe** services to handle checkout functionality.
- [Amazon Aws](https://aws.amazon.com/)
    - The project uses **Amazon Aws** to handle storage of website's static files.
- [Fontawesome](https://fontawesome.com/)
    - The project uses **Fontawesome** in order to use icons for the website.
- [Fonts Google](https://fonts.google.com/)
    - The project uses **Google Fonts** for changing the font family.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Heroku](https://www.heroku.com)
    - The project uses **Heroku** to deploy finished project.
- [Python](https://www.python.com)
    - The project uses **Python** for routing and CRUD functionality.
- [Github](https://www.GitHub.com)
    - The project uses **GitHub** remote repository to store git commits.
- [PhotoShop](https://www.adobe.com/)
    - The project uses **PhotoShop** for downsizing images.

### Notes:
- 