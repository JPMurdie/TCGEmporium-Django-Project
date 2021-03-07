# Fullstack Development Milestone Project - TCG Emporium

In this project I will create a fullstack e-commerce store specifically for a small business focused on the sales of individual Magic: The Gathering cards. It should be simple and straight forward for both the store owner and the customer to use. 

## UX

### Strategy 

The idea behind this project is to create the basis of a small template/start up that will allow a collectable card collector to sell their single card products online. This is a small but functional market and I've taken inspiration from more developed e-commerce stores like the following below:

[Magic Card Market](https://www.cardmarket.com/en/Magic)
[Star City Games](https://starcitygames.com/)
[Channel Fireball](https://shop.channelfireball.com/)

### User Stories

There are two users of this e-commerce application. The store owner and the customer. 

#### Store owner
1. As a store owner you should be able to carry out CRUD actions for your stock, within the website. 

#### customer
1. As a customer you should be able to register an account.
2. As a customer you should be able to view your order history.
3. As a customer you should be able to navigate through stock easily and efficiently.
4. As a customer you should be able to checkout with/without registering. 

### Scope

With regards to the user stories above these are the following requirements:

#### Minimal Functional Requirements
1. The project requires both frontend and backend development.
2. A customer should be able to view and buy products online.
3. A store owner should be able to manage products through a super user account on the website. 

#### Additional Functional Requirements
1. The customer's ability to register and account and view order history.

#### Non-Functional Requirements
1. The store should be simple and straight forward to use. 
2. The design should be enticing and promote the use of the site for both shopping and card information.

#### Content Requirements
1. The project will need to contain images.
2. The project will need to contain text information.
3. The project will need to contain a multitude of forms.

### Structure

The above scope of the application of creating an e-commerce store requires a multipage website. I will also be using django as the backend of this project. I will split the following structure into application and then html pages:

1. Application: home<br>
    a. Page 1: index.html

2. Application: product<br>
    a. Page 1: products.html<br>
    b. Page 2: product_detail.html

3. Application: bag<br>
    a. Page 1: bag.html

4. Application: checkout<br>
    a. Page 1: checkout.html<br>
    b. Page 2: checkout_success.html

5. Application: profiles<br>
    a. Page 1: profile.html

The wireframes for these pages can be found here [Wireframes](https://github.com/JPMurdie/TCGEmporium-Django-Project/blob/d82607342b356e19774cddf3130e899555b4098d/media/wireframes)
    
### Surface

#### Colours

My idea with colour is to allow the products artwork stand out against a white background. My overall theme will be black/grey/white with areas of fading when the user interacts with the website. This will make the website look clean while also drawing the customer to the products themselves. 

#### Interactions

Buttons and links: Buttons and links should contain a negative fade based on how they are coloured as standard. 

Images/Products: Hovering over a product image should add a grey faded box shadow to the product area. 

## Features

### All Page Features:
* **Semantic HTML**: All pages have been written using semantic HTML.
* **Responsive Design**: All pages have been built to act responsively to different devices.
* **Fullstack Development**: Each page works through django/python to incorporate frontend and backend development. 

### Specific Features:
* **Product Search Bar**: The product search bar responds to full and partial searches.
* **Customer Accounts**: Customers can create accounts and view their order history.
* **Payment System**: A functioning test payment system has been implemented into the checkout application using Stripe.
* **Web Hooks**: Website contains the use of webhooks to improve the security and data capture of the checkout application. 

There are two features that could be added to develop this e-commerce store further:

### Additional Features for Further Development:
* **Reward Points**: Allow customer's to earn reward points on their account by making purchases. 
* **Alternative Products**: Allow more flexibility in the application to allow for other product items. 

## Technology Used

The below list forms the basis of the technology used on this project, but you can also find installed software via the [requirements.txt](https://github.com/JPMurdie/TCGEmporium-Django-Project/blob/d82607342b356e19774cddf3130e899555b4098d/requirements.txt) file.

### Frontend:
    HTML
    CSS
    Javascript/JQuery
    Font Awesome
    Bootstrap

### Backend:
    Django
    Python
    SQL
    jinja


## Testing

I did not write-up any of the testing work I performed on the website but can confirm that each application within the django project works and was tested during creation.

Checkout - Webhooks were tested through Stripe's ability to send tests and came back correctly.<br>
Super User - The super user's ability to carry out CRUD activity on the store was tested in production as well as live.<br>
Responsiveness - Each webpage was checked on a number of devices and through the use of Chrome's developer tools.<br>

## Deployment

This product has been deployed via Heroku. The website can be found here: [TCG Emporium](https://tcgemporium-django-project.herokuapp.com/)

## Credits

### Content 

- All Magic: The Gathering content on this page was taken from [Scryfall](https://scryfall.com/) 

### media

- All images provided by [Magic: The Gathering](https://magic.wizards.com/en)

### Acknowledgements

- Inspiration for this website came from the stores relating to my hobby as listed above.
- The design and layout of this site was heavily influenced by the walkthrough material provided on the course. 









