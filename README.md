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

### Testing Deployment
- All of the code written was tested and re-tested.
- Defensive Design was tested by manually adding URL endpoints.
- Login system was tested using bogus emails and passwords.
- Sign-up system was tested using same emails.
- Login system was tested using correct emails and passwords.
- Sign-up system was tested using different emails.
- Search bar was tested by: using bogus input values, searching for the value that does not exist in the database, searching for the value that exists, inputting symbols, and numbers.

Here is the list of all manually tested user stories:

1. Page anchor tags:
    1. Go to the "Home" page.
    2. Try to click on the brand logo "Max Fitness'' found in the top left corner it should reload the page.
    3. Try to repeat the same process for all of the anchor tags present on the "Home" page, each anchor should lead to another page or its content.
    4. Go to the "All Products" by clicking on the nav link.
    5. Try to click on the brand logo "Max Fitness" found in the top left corner it should load the "Home" page.
    6. Try to repeat the same process for all of the anchor tags present on the "All Products" page, each anchor should lead to another page or its content.
    7. Go to the "Membership" page.
    8. Try to click on the brand logo "Max Fitness" found in the top left corner it should load the "Home" page.
    9. Try to repeat the same process for all of the anchor tags present on the "Membership" page, each anchor should lead to another page or its content.
    10. Go to the "Blog" page.
    11. Try to click on the brand logo "Max Fitness" found in the top left corner it should load the "Home" page.
    12. Try to repeat the same process for all of the anchor tags present on the "Blog" page, each anchor should lead to another page or its content.

2. Navigation bar:
    1. Go to the "Home" page. 
    2. Try to downsize the browser window, at one point navigation links should collapse into hamburger icons.
    3. Try to click the hamburger icon, it should open a mobile navigation menu.
    4. Try to increase browser window size while nav is open, at one point links should go back to their initial positions.
    
3. Product app search button:
    1. Go to the "Home" page.
    2. Try to click on the input field, enter any value. 
    3. Try to click search button on the right side of input field, it should redirect you to the "product" page showing you the results of your search. 
    3. Try to repeat the process using different values or empty fields.

4. Checkout page input fields:
    1. Go to the "Bag" page.
    2. Try to click the "Secure Checkout" button, checkout page should open now displaying form inputs including the Stripe card input.
    4. Try to fill in the form, as the fields require you to do so and submit it.
    5. Try to click the "Complete Order" button with just one input filled, the website should display message telling you to fill required fields.

5. Blog page post CRUD operations: 
    1. Go to the "Blog" page.
    2. Try to create blog using empty fields.
    7. Try to post blog with no image.
    8. Try to edit blog post, by deleting all of the content from current post object.

6. Blog comments CRUD:
    1. Go to the "Blog" page.
    2. Click "Read More" button on one of the posts.
    3. Try to submit an empty field as comment. 

Using the Bootstrap layout, and mobile fist development method, it allowed me to create a responsive website. All of the content resizes appropriately to the size of the displayed screen.
This was tested using Google's Inspect Tool that allowed me to resize the screen and see how my website responds to different device screen sizes. 

- HTML was validated using [validator.w3](https://validator.w3.org/).
- I used HTML of deployed website inside the validator, so that I can bypass the templating syntax.
- CSS was validated with [jigsaw.w3](https://jigsaw.w3.org/css-validator/).
- CSS vendor prefixes were added using [autoprefixer](https://autoprefixer.github.io/).
- JavaScript was validated with [jshint.com](https://jshint.com/).
- Python syntax was checked using [pep8online.com](http://pep8online.com/).
- All of the code was formated.

## Deployment

For this project, I used [Github](https://github.com/) platform, where I created [repository](https://github.com/Manojlovic1998/Max_Fitness_MS_4) using a template provided to me by [Code Institute](https://codeinstitute.net/).
Once the repository was created, I have used browser IDE addon for GitHub called [GitPod](https://www.gitpod.io/), to open the repository.
This online IDE that allowed me to access repository as, ["Gitpod knows where you are coming from and beams you into the right context."](https://chrome.google.com/webstore/detail/gitpod-online-ide/dodmmooeoklaejobgleioelladacbeki?hl=en).
Using this IDE I was able to make my commits and push all of my code to the [Github](https://github.com/). After project was complited it was hosted and deployed through [Heroku](https://www.heroku.com).

- Deployment step by step process:
1. Go to [repository](https://github.com/Manojlovic1998/Max_Fitness_MS_4).
2. Open [repository](https://github.com/Manojlovic1998/Max_Fitness_MS_4) using [GitPod](https://www.gitpod.io/) IDE.
3. In terminal run "pip3 freeze --local > requirements.txt" command to create a .txt file with all of the dependencies used that [Heroku](https://www.heroku.com) needs to know what dependencies app uses.
4. In the terminal run the "echo web: python app.py > Procfile" command to create Procfile that [Heroku](https://www.heroku.com) needs to know what file runs the app.
5. Check the files that you have created, if Procfile has a blank line under the first line, delete the blank line.
6. Go to [Heroku](https://www.heroku.com) and log in.
7. Once logged in, and in your dashboard, click on "Create New App".
8. Under "Create New App" click on the input field called "App Name".
9. Give your app a unique name using a dash or minus instead of spaces.
10. Select the region closes to your location.
11. Click "create app".
12. To connect the app, we are gonna set up automatic deployment by clicking on the "Github" icon inside of the "Deployment Method" section.
13. Under the "Deployment Method" section there will be a new section called "Connect to GitHub", make sure that your GitHub profile is displayed inside it.
14. Insert repo-name inside the "Connect to Github" section input. This input can be found to the right of where your profile is displayed.
15. Click Search.
16. Once it finds your repo, click the "connect" button.
17. Before clicking the "Enable Automatic Deployment" button, click on the settings tab in the top part of the page.
18. Click on "Reveal Config Var".
19. Here you can tell Heroku which variables are required, do not include quotes for the key or the value.
20. Variables inserted (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DATABASE_URL, SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET, USE_AWS).
21. Go back to GitPod IDE and make sure that you have pushed your requirements.txt and Procfile to the repo.
22. Head back to Heroku and click on "Enable Automatic Deployment".
23. Select your branch. Branch selected (master).
24. Click "Deploy Branch"
25. It will take some time for Heroku to build the app.
26. Once the site is deployed click "View" to launch the new app.

- Local Deployment:
 1. To run the code locally you can go to [Github repository](https://github.com/Manojlovic1998/Max_Fitness_MS_4)).
 2. There you can download a zip file that includes all of the files used to create this website. 
 3. Once you have downloaded the files you can use IDE such as [VScode](https://code.visualstudio.com/) to open them.
 4. From there you use any addon that allows you to run the server locally. 
 5. In order to have a functional app, you will have to load the json data from fixtures.

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

### Content

- The **text content** of the one blog post presented on the website is not my creation. Websites is created solely for educational purposes to showcase my programing logic.
It will not be used for any commercial benefits only for educational purposes.

### Media
- The photos used in this site were obtained from [Unsplash.com](https://unsplash.com/).

### Acknowledgements

- I received inspiration for this project from Code Institute school lessons.
- My mentor Aaron