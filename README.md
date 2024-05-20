# Hefestus Cave
(Developer: Valentino Braga)

HefestusCave is a comprehensive digital project developed as a full-stack application. Serving as a B2C (Business-to-Consumer) online platform, it seamlessly integrates both front-end and back-end functionalities. Primarily developed using Django for the back-end and Bootstrap for the front-end, it is integrated with Stripe for secure payment processing.

The platform offers users the opportunity to explore and purchase a curated selection of illustrations, books, and dice sets. Behind HefestusCave lies a personal connection and inspiration; it is a tribute to my husband's talents and passions. As an illustrator and contributor to numerous books, his dedication and creativity have inspired the creation of this platform. All illustrations and books within Hefestus's Books are real products from previous projects.

Through HefestusCave, my goal is to provide a platform for showcasing his art and offering users a chance to own a piece of his imaginative world. Created with passion and driven by the intention to showcase my husband's drawings, HefestusCave represents not only a technical achievement but also a genuine dedication to sharing his talent with the world.

I guess I should close with a branded call. Welcome to HefestusCave: where imagination meets commerce, and creativity knows no bounds!

![Website Mockup Image](/documentation/hefestuscave-mockup.png)

[Live Website](https://www.hefestuscave.com/)

## Table of Contents

- [Hefestus Cave](#hefestus-cave)
  * [User Stories](#user-stories)
    + [Development Setup](#development-setup)
    + [User Authentication and Account Management](#user-authentication-and-account-management)
    + [Product Management and Shopping Cart](#product-management-and-shopping-cart)
    + [Checkout and Payment](#checkout-and-payment)
    + [Content Management and User Interaction](#content-management-and-user-interaction)
    + [SEO and Marketing](#seo-and-marketing)
  * [Design](#design)
    + [Typography](#typography)
    + [Colour Scheme](#colour-scheme)
    + [Imagery](#imagery)
  * [SEO and Marketing](#seo-and-marketing-1)
    + [Business Model](#business-model)
    + [SEO](#seo)
    + [Social Media Marketing](#social-media-marketing)
    + [Newsletter Marketing](#newsletter-marketing)
  * [Wireframes](#wireframes)
    + [Homepage Wireframes](#homepage-wireframes)
    + [All Products Wireframes](#all-products-wireframes)
    + [Product's Detail Wireframes](#product-s-detail-wireframes)
    + [Sign Up Wireframes](#sign-up-wireframes)
    + [Sign In Wireframes](#sign-in-wireframes)
    + [Sign Out Wireframes](#sign-out-wireframes)
    + [Cart Wireframes](#cart-wireframes)
    + [Checkout Wireframes](#checkout-wireframes)
    + [Order Confirmation Page Wireframes](#order-confirmation-page-wireframes)
  * [Features](#features)
    + [Existing Features](#existing-features)
    + [Future Features](#future-features)
  * [Database Design](#database-design)
    + [UserAllAuth Model](#userallauth-model)
    + [UserProfile Model](#userprofile-model)
    + [Order model](#order-model)
    + [OrderLineItem Model](#orderlineitem-model)
    + [Product Model](#product-model)
    + [Category Model](#category-model)
    + [Contact Model](#contact-model)
    + [CouponCode Model](#couponcode-model)
    + [NewsletterSubscribe Model](#newslettersubscribe-model)
  * [Agile Development](#agile-development)
    + [GitHub Projects](#github-projects)
    + [GitHub Issues](#github-issues)
    + [MoSCoW Prioritization](#moscow-prioritization)
  * [Technologies Used](#technologies-used)
    + [Languages and Frameworks](#languages-and-frameworks)
    + [Resources and Tools](#resources-and-tools)
    + [Django and Python Packages](#django-and-python-packages)
  * [Testing](#testing)
  * [Deployment](#deployment)
    + [ElephantSQL Database](#elephantsql-database)
    + [Stripe API](#stripe-api)
    + [Deploy with Heroku](#deploy-with-heroku)
    + [Custom Domain and SSL Certificate:](#custom-domain-and-ssl-certificate-)
    + [Fork](#fork)
    + [Clone](#clone)
  * [Credits](#credits)
  * [Acknowledgements](#acknowledgements)

## User Stories

For the project's advancement, I generated user stories that detailed the essential tasks for achieving a well-constructed website. Following an agile development approach, I then categorized these user stories into six distinct Epics on the Kanban board to manage the project's progression effectively.

To see the User Stories list, click [here](https://github.com/tinobragaa/hefestus-cave/issues?q=is%3Aissue+sort%3Acreated-asc).
<br>

To see the Epics List, click [here](https://github.com/tinobragaa/hefestus-cave/milestones).
<br>

To see the Kanban Board, click [here](https://github.com/users/tinobragaa/projects/5).

### Development Setup

- As a developer, I want to create user stories for project planning using agile methodology so that I can efficiently plan and organize project requirements.
- As a developer, I want to create a wireframe so that I can visualize the project's layout and design and have a clear reference for implementation.
- As a developer, I want to create a README file so that I can provide comprehensive information about the project, ensuring clarity and facilitating usage.
- As a developer, I need to set up the base Django application so that we can build features.
- As a developer, I want to deploy the website to Heroku early so that I can make sure all initial settings are correct.
- As a developer, I want to create reusable resources so that further pages can be developed.
- As a developer, I want to create a database schema for the project so that I can have a clear idea of what models I need to create.
- As a developer, I want to plan my database interactions so that I can effectively organize and structure my project.

### User Authentication and Account Management

- As a user, I want to be able to create an account on the site so that I can conveniently save my billing and shipping details, as well as access a history of my purchases in one central location.
- As a user, I want to be able to edit the details saved to my account so that I can keep my information up-to-date and accurate.
- As a user, I want to sign in with one of my social accounts so that I can sign in or sign up quickly and easily.
- As a user, I want to be able to reset my password if I forget it so that I can access my account.
- As a developer, I need to style the allauth pages so that they fit with the theme styling.

### Product Management and Shopping Cart

- As a user, I want to be able to view a comprehensive list of all products available on the site so that I can browse and explore the full range of offerings.
- As a user, I want to be able to see the prices of products clearly so that I can make informed decisions about whether or not to purchase.
- As a user, I want to be able to view a product on its own individual page so that I can access comprehensive information about the product.
- As a user, I want to be able to search for a product by name or description so that I can find what I want quickly.
- As a user, I want to be able to add a product to my shopping cart so that I can easily purchase it later.
- As a user, I want to be able to view my shopping cart so that I can review the contents and total cost of my intended purchase.
- As a user, I want to be able to edit the quantity of a product in my shopping cart so that I can purchase the quantity I desire.
- As a user, I want to be able to delete items from my shopping cart so that I can remove unwanted products before proceeding to checkout.
- As a user, I want to be able to sort products by various criteria (price, newest) so that I can easily find items that match my preferences and needs, enhancing my shopping experience.
- As a user, I want to be able to add products to a wishlist so that I can keep a collection of items I am interested in buying in the future.
- As a user, I want to be able to review products that I have purchased so that I can share my experience with other potential customers.

### Checkout and Payment

- As a user, I want to be able to securely pay for my purchase using Stripe during checkout, so that I can complete the transaction smoothly and begin enjoying my products.
- As a user, I want to be able to receive an order confirmation email after I purchase from the shop so that I can have a record of what I've purchased in my email inbox.
- As a site user, I want to be able to apply discount codes in my cart so that I can receive a discount on my purchase.
- As a user, I want to have an express checkout option that allows me to save my payment information securely in a digital wallet within my account, so that I can complete transactions quickly without having to enter payment details every time I make a purchase.

### Content Management and User Interaction

- As a user, I want to be able to navigate between related pages easily so that I can find relevant content and information quickly and efficiently.
- As a user, I want to be able to clearly understand the purpose of the website so that I can form an impression and decide whether or not to engage further.
- As a user, I would like the site to have a customised favicon so I can easily identify it when I have multiple tabs open.
- As a user, I want to be able to contact the website administrators through a "Contact Us" page using a form so that I can communicate any inquiries, feedback, or issues.
- As a developer, I need to create a 404 page so that users are redirected when entering a broken URL.
- As a site admin, I want to ensure that the website is designed and developed with accessibility features so that users with disabilities can navigate and interact with the site effectively.
- As a site admin, I want to be able to ensure the web app's responsiveness across all screen sizes so that users can smoothly switch devices and access the application without any constraints, ensuring a seamless user experience.
- As a user, I want to view product prices and complete transactions in my preferred currency so that I can better understand the costs and avoid currency conversion fees.

### SEO and Marketing

- As a site admin, I want to be able to optimize SEO so that my website ranks higher in search engine results, increasing visibility and attracting more organic traffic.
- As a site admin, I want to leverage social media marketing strategies, specifically through meta platforms, to maximize brand visibility, engage with potential customers, and drive conversions.
- As a user, I want to be able to share content from the website on various social media platforms, including Facebook, Instagram, X, and Pinterest, so that I can engage with my social network and amplify the reach of interesting content.
- As a user, I want to be able to change the language of the website so that I can access content in a language that is more familiar or comfortable for me.
- As a site user, I want to be able to subscribe to the site's mailing list so that I can receive exclusive offers and updates directly in my inbox, enhancing my engagement with the website.
- As a user, I want to earn points for every purchase I make, which I can redeem for discounts or free products in the future, so that I feel rewarded for my loyalty and continue shopping at this store.

## Design

In crafting the design for HefestusCave, I drew inspiration from a fusion of high culture aesthetics and modern design principles. My goal was to evoke an air of artistry while maintaining a contemporary appeal, resonating with both the streets and renowned museums like [Moco](https://mocomuseum.com/).

### Typography

For the typography, I opted for a blend of sophistication and modernity. The logo and primary headings feature the bespoke font "Spikle," designed by [Valentino Vergan](https://www.behance.net/valentinovergan), specifically acquired for the website. Complemented by various weights of the "Alegreya Sans" font from Google Fonts, the typography conveys a sense of refinement and abstraction.

![Spikle Font](/documentation/spikle-font.png)

![Alegreya Sans Font](/documentation/alegreya-font.png)

### Colour Scheme

The colour palette employed in our design revolves around a playful interplay between classic contrasts of black and white, with a vibrant pop of bright neon orange. This combination not only exudes a modern vibe but also adds a dynamic energy to the overall aesthetic.

![Colour Scheme](/documentation/colour-scheme.png)

### Imagery

All illustrations and books showcased on the website are authentic works created by my husband through previous commissions. To visualize these products, we utilized mockups created in Photoshop, with the structural framework sourced from ls.graphics. It's important to note that the dice designs are generated using [OpenArt](https://openart.ai/) and do not exist as physical products. If you are interested in comssioning a draw, you can contact my husband on [HefestusCave Instagram](https://www.instagram.com/hefestuscave/) on through the email hefestuscave@gmail.com.

## SEO and Marketing

### Business Model

HefestusCave operates on a straightforward Business to Customer (B2C) model, catering to individual customers without the need for subscriptions or recurring fees. In its developmental phase, the platform already incorporates essential features such as a newsletter and integration with social media platforms for marketing purposes.

Social media integration is crucial for HefestusCave's growth strategy, as it has the potential to build a strong community around the business and increase site traffic, particularly on widely used platforms like Facebook. The newsletter functionality allows the business to maintain direct communication with site users, informing them about special offers, new product releases, changes in business operations, upcoming events, and other relevant updates.

These features are integral to HefestusCave's user engagement strategy, providing avenues for both marketing outreach and customer retention as the platform continues to develop and expand its offerings.

### SEO

- Descriptive meta tags were added to base.html which is extended on all the pages. Including title, description and keywords. Meta tags are important for SEO as they help search engines to understand what the page is about. Meta tags are also important for accessibility as they are used by screen readers to describe the page to the user.

- Used xml-sitemaps to generate sitemap.xml file. Sitemap.xml file is important for SEO as it helps search engines to crawl the website. Sitemap.xml file is also important for accessibility as it helps screen readers to navigate the website.

- Used robots.txt to tell search engines which pages to crawl and which pages to ignore. robots.txt file is important for SEO as it helps search engines to crawl the website. robots.txt file is also important for accessibility as it helps screen readers to navigate the website.

- Add rel attribute to all links. rel attribute is important for SEO as it helps search engines to understand the relationship between pages. rel attribute is also important for accessibility as it helps screen readers to navigate the website.

### Social Media Marketing

Building a robust social presence with active engagement can significantly enhance sales. Integrating popular platforms like Facebook, known for their extensive user base, can effectively drive traffic to the business website.

Furthermore, I've utilized a [Balsamiq](https://balsamiq.com/) template provided by Code Institute to design a mockup Facebook business account.

![Facebook Mockup](/documentation/facebook-mockup.png)

### Newsletter Marketing

A newsletter sign-up form has been seamlessly integrated into the website footer. Streamlined for user convenience, this single-field form ensures a hassle-free experience for subscribers. The inclusion of a newsletter sign-up form holds significant importance in web marketing endeavors, as it serves as a conduit to engage with a broader audience. The service is facilitated through [Mailchimp](https://mailchimp.com/), a trusted platform renowned for its reliability and functionality.

![Mailchimp Form](/documentation/newsletter-marketing.png)

## Wireframes

To streamline the site's design process, I've generated wireframes for each page, ensuring alignment with industry best practices by producing versions tailored for both mobile and desktop interfaces. [Balsamiq](https://balsamiq.com/wireframes/?gad_source=1&gclid=CjwKCAiAloavBhBOEiwAbtAJO391J15sKFC7QKvUeqWQ4LfYPMV7B8CcAIxDhhL2wFml7luEHdXmChoCU6sQAvD_BwE) was utilized as the primary tool for crafting these wireframes.

### Homepage Wireframes
<details>
<summary>Homepage Desktop</summary>
<br>

![Homepage Desktop](/documentation/wireframes/homepage-desktop.png)

</details>
<details>
<summary>Homepage Mobile</summary>
<br>

![Homepage Mobile](/documentation/wireframes/homepage-mobile.png)

</details>

### All Products Wireframes
<details>
<summary>All Products Desktop</summary>
<br>

![All Products Desktop](/documentation/wireframes/all-products-desktop.png)

</details>
<details>
<summary>All Products Mobile</summary>
<br>

![All Products Mobile](/documentation/wireframes/all-products-mobile.png)

</details>

### Product's Detail Wireframes
<details>
<summary>Product's Detail Desktop</summary>
<br>

![Product's Detail Desktop](/documentation/wireframes/product-details-desktop.png)

</details>
<details>
<summary>Product's Detail Mobile</summary>
<br>

![Product's Detail Desktop](/documentation/wireframes/product-details-mobile.png)

</details>

### Sign Up Wireframes
<details>
<summary>Sign Up Desktop</summary>
<br>

![Sign Up Desktop](/documentation/wireframes/sign-up-desktop.png)

</details>
<details>
<summary>Sign Up Mobile</summary>
<br>

![Sign Up Mobile](/documentation/wireframes/sign-up-mobile.png)

</details>

### Sign In Wireframes
<details>
<summary>Sign In Desktop</summary>
<br>

![Sign In Desktop](/documentation/wireframes/sign-in-desktop.png)

</details>
<details>
<summary>Sign In Mobile</summary>
<br>

![Sign In Mobile](/documentation/wireframes/sign-in-mobile.png)

</details>

### Sign Out Wireframes
<details>
<summary>Sign Out Desktop</summary>
<br>

![Sign Out Desktop](/documentation/wireframes/sign-out-desktop.png)

</details>
<details>
<summary>Sign Out Mobile</summary>
<br>

![Sign Out Mobile](/documentation/wireframes/sign-out-mobile.png)

</details>

### Cart Wireframes
<details>
<summary>Cart Desktop</summary>
<br>

![Cart Desktop](/documentation/wireframes/cart-desktop.png)

</details>
<details>
<summary>Cart Mobile</summary>
<br>

![Cart Mobile](/documentation/wireframes/cart-mobile.png)

</details>

### Checkout Wireframes
<details>
<summary>Checkout Desktop</summary>
<br>

![Checkout Desktop](/documentation/wireframes/checkout-desktop.png)

</details>
<details>
<summary>Checkout Mobile</summary>
<br>

![Checkout Mobile](/documentation/wireframes/checkout-mobile.png)

</details>

### Order Confirmation Page Wireframes
<details>
<summary>Order Confirmation Desktop</summary>
<br>

![Order Confirmation Desktop](/documentation/wireframes/order-confirmation-desktop.png)

</details>
<details>
<summary>Order Confirmation Mobile</summary>
<br>

![Order Confirmation Mobile](/documentation/wireframes/order-confirmation-mobile.png)

</details>

## Features

### Existing Features

- **Landing Page**

    - When users arrive at the site for the first time, they are welcomed and given several options: explore products via the "Shop Now" button, browse links in the navigation bar, and find additional information in the footer.
    <br>
    <details>
    <summary>Landing Page</summary>
    <br>

    ![screenshot](/documentation/features/landing-page.jpg)

    </details>

- **Sign Up Page**

    - This is where the user can create an account for themselves by entering their desired email, username and password. If the user accidentally comes to this page instead of the login page they can get to the right page using the link in the card text.
    <br>
    <details>
    <summary>Sign Up Page</summary>
    <br>

    ![screenshot](/documentation//features/sign-up-page.jpg)

    </details>

- **Sign In Page**

    - This is where users with existing accounts can log in with their username or email and password. They can choose to let their browser remember them if they plan on returning to the site on the same device to avoid having to log in again. There's a link to the sign up page too if the user accidentally navigated to this page instead of trying to create an account.
    <br>
    <details>
    <summary>Sign In Page</summary>
    <br>

    ![screenshot](/documentation/features/sign-in-page.jpg)

    </details>

- **Sign Out Page**

    - When the user wants to finish their session and logout, they can do so from the nav menu. When a user clicks the "Sign Out" button they're met with a page asking them to confirm they want to log out. They're redirected to the landing page if they click the confirmation button and a message pops up confirming that they've logged out.
    <br>
    <details>
    <summary>Sign Out Page</summary>
    <br>

    ![screenshot](/documentation/features/sign-out-page.jpg)

    </details>

- **Reset Password Page**

    - If a user is trying to log in and has forgotten their password they can visit the password reset page. Here a user must enter their email address they used to sign up with and an email will be sent to them with further instructions on resetting their password to regain access to their account.
    <br>
    <details>
    <summary>Reset Password Page</summary>
    <br>

    ![screenshot](/documentation/features/reset-password-page.jpg)

    </details>
    <details>
    <summary>Reset Password Email</summary>
    <br>

    ![screenshot](/documentation/features/reset-password-email.jpg)

    </details>
    <details>
    <summary>Change Password Page</summary>
    <br>

    ![screenshot](/documentation/features/change-password-page.jpg)

    </details>
    <details>
    <summary>New Password Confirmation</summary>
    <br>

    ![screenshot](/documentation/features/change-password-confirmation.jpg)

    </details>

- **Navigation Bar**

    - The main navigation bar is accessible throughout the entire site, offering essential features such as a logo link redirecting to the homepage, a search bar for easy product discovery, access to the user's account/profile, a cart link displaying the number of items and running total if items are added to the cart, a banner advertising free shipping and links to product categories for streamlined navigation.
    <br>
    <details>
    <summary>Navigation Bar</summary>
    <br>

    ![screenshot](/documentation/features/navigation-bar.jpg)

    </details>

- **Category Navigation**

    - Through the navigation bar, users can filter products when selecting to view all products. They can sort products by price, category, sale status, and newest arrivals. Additionally, users can choose specific categories and subcategories they wish to explore further.
    <br>
    <details>
    <summary>All Products Filtering</summary>
    <br>

    ![screenshot](/documentation/features/all-product-filtering.jpg)

    </details>
    <details>
    <summary>Category/Subcategory Navigation</summary>
    <br>

    ![screenshot](/documentation/features/categories-subcategories.jpg)

    </details>

- **Search Bar**

    - Users can use the navigation's search bar to find specific products. The search term is matched up with products' name and description to give the user a list of products to match their search query.
    <br>
    <details>
    <summary>Search Bar</summary>
    <br>

    ![screenshot](/documentation/features/search-bar.jpg)

    </details>

- **Footer**

    - This appears across the whole site and contains links to the contact us page, returns & exchanges pages, policies, social media pages (instagram and artstation) and a form to subscribe to the newsletter (mailchimp integration).
    <br>
    <details>
    <summary>Footer</summary>
    <br>

    ![screenshot](/documentation/features/footer.jpg)

    </details>

- **All Products Page**

    - This page displays all the products available for sale on the site. It includes a button to quickly return to the top of the page, a product count section, and a dropdown box for filtering products.
    <br>
    <details>
    <summary>All Products Page</summary>
    <br>

    ![screenshot](/documentation/features/all-products-page.jpg)

    </details>

- **Product Stock Count**

    - Every product has a finite stock left for each product. If the product has less than 3 (2 or 1) stock left then the badge displaying the count is displayed to add a sense of urgency. When a product is purchased, the stock will automatically decrease by the number of units of each product the customer purchases. When a product's stock reaches 0, the "add to cart" button replaced with a "sold out" text and button is disabled so product is not able to be added to the user's cart.
    <br>
    <details>
    <summary>Product Stock</summary>
    <br>

    ![screenshot](/documentation/features/product-stock.jpg)

    </details>

- **Add to Cart Button**

    - Every product has a button that lets the user to add it to their cart when viewing it both on the products listing pages or the individual product page. This adds one unit of the product to the user's cart and they can increase the quantity from their cart if they want to purchase more than one. When clicking on the button, the user is shown a message confirming when an item has been added to their cart. If there is no stock, the button is disabled and the text is changed to "sold out". 
    <br>
    <details>
    <summary>Add to Cart Button</summary>
    <br>

    ![screenshot](/documentation/features/add-to-cart-button.jpg)

    </details>
    <details>
    <summary>Added to Cart Confirmation Message</summary>
    <br>

    ![screenshot](/documentation/features/add-to-cart-message.jpg)

    </details>
    <details>
    <summary>Sold Out Button</summary>
    <br>

    ![screenshot](/documentation/features/sold-out-button.jpg)

    </details>

- **Product Card**

    - Each product is displayed on its own card, featuring the product image, name, price, "add to cart"/"sold out" button and a low stock tag if the stock is under 3 (1 or 2). If a product is out of stock, the "Add to Cart" button is disabled and shows "Sold Out." Logged-in admins will also see edit and delete buttons for each product.
    <br>
    <details>
    <summary>Product Card</summary>
    <br>

    ![screenshot](/documentation/features/product-card.jpg)

    </details>

- **Product Filtering**

    - When the user is viewing the products listing pages, they can sort the products in a number of ways. Products can be sorted by: Price (low to high), Price (high to low), Name (A-Z), Name (Z-A), Category (A-Z) and Category (Z-A).
    <br>
    <details>
    <summary>Product Filtering</summary>
    <br>

    ![screenshot](/documentation/features/product-filtering.jpg)

    </details>

- **Individual Product Page**

    - Each product also has its own individual page for the user to see more information about the product including a description, stock information, quantity selector along with buttons to add the product to the user's cart or to return to the all products page and keep shopping. Logged-in admins will also see edit and delete buttons for each product.
    <br>
    <details>
    <summary>Individual Product Page</summary>
    <br>

    ![screenshot](/documentation/features//individual-product-page.jpg)

    </details>

- **Quantity Selector**

    - Each individual product page contains a quantity selector if the product is in stock. The selector lets the user add a minimum of 1 and a maximum of whatever the product's current stock is to their cart. After setting the quantity, a user can click the add to cart button to add that number of the product to their cart. If the user enters a number higher than the stock available an error is raised.
    <br>
    <details>
    <summary>Quantity Selector</summary>
    <br>

    ![screenshot](/documentation/features/product-quantity.jpg)

    </details>

- **Account Options**

    - If the user is logged in, the my account dropdown in the navigation will contain a link to the user's profile. If the user is a guest they will be given the option to either register for an account or sign in to an existing account. If the user is logged in as admin, they will see a link for product management.
    <br>
    <details>
    <summary>User Account</summary>
    <br>

    ![screenshot](/documentation/features/user-account.jpg)

    </details>
    <details>
    <summary>Guest Account</summary>
    <br>

    ![screenshot](/documentation/features/guest-account.jpg)

    </details>
    <details>
    <summary>Admin Account</summary>
    <br>

    ![screenshot](/documentation/features/admin-account.jpg)

    </details>

- **Add - Product Management Page**

    - If the user is logged in and has admin permissions, they can add new products to the site from the admin dropdown in the navigation. The add product page contains a form for the admin to fill out with the details of the new product.
    <br>
    <details>
    <summary>Add Product</summary>
    <br>

    ![screenshot](/documentation/features/product-management-page.jpg)

    </details>

- **Edit - Product Management Page**

    - If the user is logged in and has admin permissions, they can edit site products by clicking the edit button on either the product card on the all products page or the individual product page. The edit product page contains the same form as the add product page but the fields are already populated with the product's current data.
    <br>
    <details>
    <summary>Edit Product</summary>
    <br>

    ![screenshot](/documentation/features/edit-product-management-page.jpg)

    </details>

- **Remove Product**

    - If the user is logged in and has admin permissions, they can delete site products by clicking the delete button on either the product card on the all products page or the individual product page. After deleting the product, a confirmation message will be displayed on the screen. 
    <br>
    <details>
    <summary>Remove Product</summary>
    <br>

    ![screenshot](/documentation/features/delete-product-message.jpg)

    </details>

- **User Profile**

    - When a user has completed registration on the site, they are given a profile. The profile is pretty simple in that it contains the user's default delivery information if set and a list of the user's previous orders.
    <br>
    <details>
    <summary>User Profile</summary>
    <br>

    ![screenshot](/documentation/features/user-profile-page.jpg)

    </details>

- **Newsletter**

    - Using the form in the footer, users can sign up to the site's newsletter. Users can only sign up to the newsletter once and if they try to sign up with an already registered email address, a message will be displayed to inform they are already subscribed. 
    <br>
    <details>
    <summary>Newsletter Subscription</summary>
    <br>

    ![screenshot](/documentation/features/newsletter-subscription.jpg)

    </details>
    <details>
    <summary>Already Subscribed Message</summary>
    <br>

    ![screenshot](/documentation/features/already-subscribed-message.jpg)

    </details>
    <details>
    <summary>Mailchimp Confirmation</summary>
    <br>

    ![screenshot](/documentation/features/mailchimp-subscription.jpg)

    </details>

- **Contact Us Page**

    - This is a simple form that a user can fill out to contact the site owners. When the form is submitted, the user is sent an automated email confirming that their message has been seen and that a member of the team will follow up with them.
    <br>
    <details>
    <summary>Contact Us Form</summary>
    <br>

    ![screenshot](/documentation/features/contact-us-page.jpg)

    </details>
    <details>
    <summary>Support Email Confirmation</summary>
    <br>

    ![screenshot](/documentation/features/email-confirmation-contact.jpg)

    </details>

- **Returns & Exchanges Page**

    - When a user click on the Returns and Exchanges page, they can view pertinent information regarding product returns and exchanges. 
    <br>
    <details>
    <summary>Returns & Exchanges Page</summary>
    <br>

    ![screenshot](/documentation/features/returns-and-exchanges-page.jpg)

    </details>

- **Policies Page**

    - When a user click on the Policies page, they can view pertinent information regarding the store's policies. 
    <br>
    <details>
    <summary>Policies Page</summary>
    <br>

    ![screenshot](/documentation/features/policies-page.jpg)

    </details>

- **Cart**

    - The cart can be accessed from the main navigation. In the navigation a running total is shown of the items in the user's cart. When the user clicks on this they can see all the items in their cart, individual price of each product, subtotal per product if the quantity is greater than 1 and a quantity selector for each product with buttons to update the quantity or remove the product completely from their cart. If a user doesn't have anything in their cart, a message will appear prompting the user to continue shopping.
    <br>
    <details>
    <summary>Cart</summary>
    <br>

    ![screenshot](/documentation/features/cart.jpg)

    </details>
    <details>
    <summary>Empty Cart</summary>
    <br>

    ![screenshot](/documentation/features/empty-cart.jpg)

    </details>

- **Coupon**

    - If a user has a discount code, they can add it in their cart to receive a percentage off their order. If a user enters a code that doesn't exist they will see a message telling them so. If the code they use does exist, they will see a message confirming the discount has been added and the form will be replaced with the amount that has been taken off their order. When a user successfully adds a discount code, the amount that has been taken off is displayed in place of the discount code form. A delete icon appears next to the discount amount if the user wants to use a different discount code and on clicking, a message appears confirming the discount has been removed and the discount code form will appear in place of the discount amount.
    <br>
    <details>
    <summary>Discount Code Field</summary>
    <br>

    ![screenshot](/documentation/features/discount-field.jpg)

    </details>
    <details>
    <summary>Valid Code</summary>
    <br>

    ![screenshot](/documentation/features/existent-code.jpg)

    </details>
    <details>
    <summary>Invalid Code</summary>
    <br>

    ![screenshot](/documentation/features/inexistent-code.jpg)

    </details>
    <details>
    <summary>Discount Added</summary>
    <br>

    ![screenshot](/documentation/features/discount-added.jpg)

    </details>

- **Checkout**

    - This page contains a form for the user's delivery and payment information and a summary of the user's order. If the user has an account on the site, they can save their delivery information on their profile to automatically be filled in the checkout.
    <br>
    <details>
    <summary>Checkout</summary>
    <br>

    ![screenshot](/documentation/features/checkout.jpg)

    </details>

- **Customer Detail Form**

    - In the checkout the user can add their details and if they're logged in, can check the box to save their details for future transactions. Users must enter their payment information before completing the checkout and all payments are handled via Stripe.
    <br>
    <details>
    <summary>Customer Detail Form</summary>
    <br>

    ![screenshot](/documentation/features/customer-detail-form.jpg)

    </details>

- **Order Summary**

    - A final summary of the user's order is shown containing all the user's cart items, quantity and subtotal for each item. The user can also see their order total, delivery costs, any discounts that have been applied and the grand total in the summary.
    <br>
    <details>
    <summary>Order Summary</summary>
    <br>

    ![screenshot](/documentation/features/order-summary.jpg)

    </details>

- **Checkout Buttons**

    - At the very end of the checkout the user will see two buttons, one to adjust their cart and another to complete their order. The grand total is displayed under the complete order button to further inform the user of how much their card will be charged on order completion.
    <br>
    <details>
    <summary>Checkout Buttons</summary>
    <br>

    ![screenshot](/documentation/features/checkout-buttons.jpg)

    </details>

- **Order Confirmation Email**

    - Once the order is complete and payment has been received, the user will receive an order confirmation email containing their order number and a receipt with the total paid.
    <br>
    <details>
    <summary>Order Confirmation Email</summary>
    <br>

    ![screenshot](/documentation/features/order-confirmation-email.jpg)

    </details>

- **Order Confirmation Page**

    - After the order has been completed, the user is redirected to a confirmation page letting them know an order confirmation email has been sent to their provided email address. This page contains a final rundown of the order and what the user purchased. This page can be accessed again from the user's profile if they have an account on the site by clicking the order number from the list of past orders.
    <br>
    <details>
    <summary>Order Confirmation Page</summary>
    <br>

    ![screenshot](/documentation/features/order-confirmation-page.jpg)

    </details>

- **Error Pages**

    - If a user ends up on a page that either doesn't exist or that they shouldn't be on (regular user using admin page links or trying to edit/delete something through a link) then they'll be shown an error page with a button to bring them back to the shop.
    <br>
    <details>
    <summary>403</summary>
    <br>

    ![screenshot](/documentation/features/403-page.jpg)

    </details>
    <details>
    <summary>404</summary>
    <br>

    ![screenshot](/documentation/features/404-page.jpg)

    </details>
    <details>
    <summary>500</summary>
    <br>

    ![screenshot](/documentation/features/500-page.jpg)

    </details>

### Future Features

A few features that could make the website even better are listed here. These features have been logged as "Future Release" in my [Kanban Board](https://github.com/users/tinobragaa/projects/5/views/1).

- **Multi-Language Support**
  - Introduce multi-language support to cater to a diverse global audience. Allow users to choose their preferred language from a list of available options, ensuring that all website content, including product descriptions, navigation menus, and checkout pages, is displayed in the selected language. 
- **Wishlist Functionality**
  - Introduce a wishlist feature that allows users to save products they're interested in for future purchase consideration. Users can easily add products to their wishlist from the product detail page or the listing page.
- **Social Media Login**
  - Enable social media login/signup options for users and incorporate social sharing buttons for products. Additionally, integrate features like user reviews and ratings, allowing customers to share their shopping experiences on social media platforms.
- **Express Checkout and Wallet Integration**
  - Simplify the checkout process for returning customers by offering an express checkout option. Enable users to save their payment information securely in a digital wallet within their account. This allows them to complete transactions quickly without having to enter payment details every time they make a purchase. 
- **Loyalty Program and Discounts** 
  - Create a loyalty program where customers can earn points for every purchase they make, which can be redeemed for discounts or free products in the future. Offer special discounts and promotions to loyal customers.
- **Multi-Currency Support**
  - Implement a multi-currency system that allows users to view product prices and complete transactions in their preferred currency. Provide an option for users to select their currency from a dropdown menu or automatically detect their location and display prices accordingly. Utilize currency conversion APIs or services to ensure accurate and up-to-date exchange rates. Additionally, enable users to switch between different currencies seamlessly 
- **Product Review**
  - Develop a comprehensive review system that allows users to rate products on multiple criteria such as quality, value for money, and usability. Users can leave detailed written reviews and upload images or videos of the products, enhancing the credibility and usefulness of the feedback. 
- **Social Media Sharing**
  - Add social media sharing buttons to product pages, allowing users to easily share products on platforms like Facebook, Twitter, Instagram, and Pinterest. This can help increase product visibility and attract more potential customers through social media channels.

## Database Design

I utilized [dbdiagram](https://dbdiagram.io/home) to create an entity relationship diagram, offering a clear visualization of the interconnections among my data structures. This streamlined the development process by offering a comprehensive visualization.

![Database Design](/documentation/database-design.png)

### UserAllAuth Model

- The user model is the default Django user model.

| Key          | Field Type    | Validation                  |
| ------------ | ------------- | --------------------------- |
| username     | CharField     |                             |
| email        | EmailField    | max_length=254, unique=True |
| password     | CharField     |                             |
| is_superuser | BooleanField  |                             |
| is_staff     | BooleanField  |                             |
| date_joined  | DateTimeField |                             |
| last_login   | DateTimeField |                             |

### UserProfile Model

| Key                     | Field Type   | Validation                                                  |
| ----------------------- | ------------ | ----------------------------------------------------------- |
| default_phone_number    | CharField    | max_length=20, null=True, blank=True                        |
| default_country         | CountryField | blank_label="Country", max_length=40, null=True, blank=True |
| default_postcode        | CharField    | max_length=20, null=True, blank=True                        |
| default_town_or_city    | CharField    | max_length=40, null=True, blank=True                        |
| default_street_address1 | CharField    | max_length=80, null=True, blank=True                        |
| default_street_address2 | CharField    | max_length=80, null=True, blank=True                        |
| default_county          | CharField    | max_length=80, null=True, blank=True                        |

### Order model 

| Key             | Field Type    | Validation                                                                           |
| --------------- | ------------- | ------------------------------------------------------------------------------------ |
| order_number    | CharField     | max_length=32, null=False, editable=False                                            |
| user_profile    | ForeignKey    | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' |
| full_name       | CharField     | max_length=50, null=True, blank=True                                                 |
| email           | EmailField    | max_length=254, null=True, blank=True                                                |
| phone_number    | CharField     | max_length=20, null=True, blank=True                                                 |
| country         | CountryField  | blank_label="Country", max_length=40, null=True, blank=True                          |
| postcode        | CharField     | max_length=20, null=True, blank=True                                                 |
| town_or_city    | CharField     | max_length=40, null=True, blank=True                                                 |
| street_address1 | CharField     | max_length=80, null=True, blank=True                                                 |
| street_address2 | CharField     | max_length=80, null=True, blank=True                                                 |
| county          | CharField     | max_length=80, null=True, blank=True                                                 |
| date            | DateTimeField | auto_now_add=True                                                                    |
| delivery_cost   | DecimalField  | max_digits=6, decimal_places=2, null=False, default=0                                |
| discount        | DecimalField  | default=False                                                                        |
| order_total     | DecimalField  | max_digits=6, decimal_places=2, null=False, default=0                                |
| grand_total     | DecimalField  | max_digits=6, decimal_places=2, null=False, default=0                                |
| original_bag    | TextField     | null=False, blank=False, default=''                                                  |
| stripe_pid      | CharField     | max_length=254, null=False, blank=False, default=''                                  |

### OrderLineItem Model

| Key            | Field Type   | Validation                                                                           |
| -------------- | ------------ | ------------------------------------------------------------------------------------ |
| order          | ForeignKey   | Order, null=False, blank=False, on_delete=models.CASCADE, , related_name='lineitems' |
| product        | ForeignKey   | Product, null=False, blank=False, on_delete=models.CASCADE                           |
| quantity       | IntegerField | null=False, blank=False, default=0                                                   |
| lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False              |

### Product Model

| Key         | Field Type     | Validation                                                 |
| ----------- | -------------- | ---------------------------------------------------------- |
| category    | ForeignKey     | Category, null=True, blank=True, on_delete=models.SET_NULL |
| sku         | CharField      | max_length=255, null=True, blank=True                      |
| description | TextField      | null=True, blank=True                                      |
| year        | IntegerField   | max_digits=4, decimal_places=0, null=True, blank=True      |
| condition   | ForeignKey     | null=True, blank=True                                      |
| price       | DecimalField   | max_digits=6, decimal_places=2                             |
| image       | ImageField     | null=True, blank=True                                      |
| stock       | IntegerField   | null=True, blank=True                                      |

### Category Model

| Key           | Field Type    | Validation     |
| ------------- | ------------- | -------------- |
| name          | CharField     | max_length=250 |

### Contact Model

| Key          | Field Type | Validation      |
| ------------ | ---------- | --------------- |
| name         | CharField  | max_length=100  |
| email        | EmailField | max_length=100  |
| order_number | CharField  | max_length=32   |
| message      | TextField  | max_length=1000 |

### CouponCode Model

| Key      | Field Type   | Validation                 |
| -------- | ------------ | -------------------------- |
| code     | CharField    | max_length=50, unique=True |
| discount | IntegerField |                            |

### NewsletterSubscribe Model

| Key   | Field Type | Validation     |
| ----- | ---------- | -------------- |
| email | EmailField | max_length=100 |

## Agile Development

### GitHub Projects

GitHub Projects was utilized as an Agile tool for managing this project. This platform facilitated the planning and tracking of user stories, issues, and epics, which were then monitored on a weekly basis using a basic Kanban board setup.

- 42 User Stories: full list [here](https://github.com/tinobragaa/hefestus-cave/issues?q=is%3Aissue+sort%3Acreated-asc).
- 6 Epics: Development Setup, User Authentication and Account Management, Product Management and Shopping Cart, Checkout and Payment, Content Management and User Interaction and SEO and Marketing.

![Kanban Board](/documentation/kanban-board.png)

### GitHub Issues

GitHub Issues functioned as an additional Agile tool for me. I employed my custom User Story Template within it to organize user stories effectively. Additionally, it facilitated tracking milestones (Epics) for the project.

To see the User Stories list, click [here](https://github.com/tinobragaa/hefestus-cave/issues?q=is%3Aissue+sort%3Acreated-asc).
<br>

To see the Epics List, click [here](https://github.com/tinobragaa/hefestus-cave/milestones).
<br>

To see the Kanban Board, click [here](https://github.com/users/tinobragaa/projects/5).

### MoSCoW Prioritization

I broke down my Epics into individual stories before prioritizing and implementing them. This method allowed me to utilize the MoSCoW prioritization and apply labels to the user stories in the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

## Technologies Used

### Languages and Frameworks

This project was created using the following languages and frameworks:

- [HTML](https://en.wikipedia.org/wiki/HTML) as the markup language and templating language.
- [CSS](https://en.wikipedia.org/wiki/CSS) as the style sheet language.
  - [Bootstrap](https://getbootstrap.com/) as the CSS framework.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) to create carousel on index.html.
  - [jQuery](https://jquery.com/) to simplify DOM manipulation.
- [Python](https://www.python.org/) as the backend programming language.
  - [Django](https://www.djangoproject.com/) as the Python web framework.

### Resources and Tools

The following resources and tools were used to develop the website:

- [Amazon AWS](https://aws.amazon.com/) - Used to store the static and media files for the site.
- [Mailchimp](https://mailchimp.com/) - Used to create the newsletter signup form.
- [Stripe](https://stripe.com/gb) has been used for the payment processing and webhooks handling.
- [GitHub](https://github.com/) - Source code hosted on GitHub, deployed using Git Pages.
- [GitPod](https://www.gitpod.io/) - Used to commit, comment and push code during the development process.
- [Font Awesome](https://fontawesome.com/) - Used to source necessary icons used in the project.
- [ls.graphics](https://www.ls.graphics/free-mockups) - Used to to create the store's placeholders and mockups.
- [Behance](https://www.behance.net/) - Used to research design trends.
- [OpenArt](https://openart.ai/create) - Used to create the dice images.
- [Balsamiq](https://balsamiq.com/) - Used to create wireframes and website structure map for the project.
- [Adobe Photoshop](https://www.adobe.com/ie/products/photoshop.html) - Used to design the store's mockups and placeholders. 
- [Gramarly](https://app.grammarly.com/) - Used for general spell-check.
- [Google Fonts](https://fonts.google.com/) - Used to import fonts to the project.
- [Heroku](https://www.heroku.com/) - Used to deploy the project.
- [dbdiagram](https://dbdiagram.io/home) - Used to make the database design.
- [Am I Responsive?](https://ui.dev/amiresponsive) - Used to create the website mockup.
- [TOC](https://ecotrust-canada.github.io/markdown-toc/) - Used to create the TOC of this file.
- [ElephantSQL](https://www.elephantsql.com/) - Free and open-source relational database management system (RDBMS).
- [Bootstrap](https://getbootstrap.com/) - Used for adding predefined styled elements and creating responsiveness.
- [JsHint](https://jshint.com/) - Used for validating the javascript code.
- [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used for validating the python code.
- [HTML W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - Used for validating the HTML.
- [CSS Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - Used for validating the CSS.
- [Chrome Del Tools](https://developer.chrome.com/docs/devtools/) - For debugging the project.
- [W.A.V.E.](https://wave.webaim.org/) - Used for testing accessibility.
- [LightHouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used for testing performance.
- [Stack Overflow](https://stackoverflow.com/) - Used for finding solutions to coding issues and asking programming-related questions.

### Django and Python Packages

The following Django applications and Python Packages were used to develop the website:
- [asgiref](https://pypi.org/project/asgiref/) - ASGI (Asynchronous Server Gateway Interface) framework, a standard interface between web servers and Python web applications.
- [boto3](https://pypi.org/project/boto3/) - Amazon Web Services (AWS) SDK for Python, providing access to AWS services.
- [botocore](https://pypi.org/project/botocore/) - Low-level, core functionality of AWS SDK for Python (Boto3).
- [dj-database-url](https://pypi.org/project/dj-database-url/) - A utility for utilizing database URLs in Django applications.
- [Django](https://www.djangoproject.com/) - A Python-based web framework that follows the model-template-view architectural pattern, used for building the project.
- [django-allauth](https://django-allauth.readthedocs.io/) - A Django application used for account registration, management, and authentication.
- [django-countries](https://pypi.org/project/django-countries/) - A Django application for providing country choices for forms.
- [django-crispy-forms](https://pypi.org/project/django-crispy-forms/) - A Django application that makes it easy to style Django forms.
- [django-storages](https://pypi.org/project/django-storages/) - A collection of custom storage backends for Django.
- [gunicorn](https://pypi.org/project/gunicorn/) - A Python Web Server Gateway Interface (WSGI) HTTP server.
- [jmespath](https://pypi.org/project/jmespath/) - A query language for JSON, allowing you to search and manipulate JSON data.
- [oauthlib](https://pypi.org/project/oauthlib/) - A generic and reusable Python library for implementing OAuth1 and OAuth2 providers.
- [Pillow](https://pypi.org/project/Pillow/) - The Python Imaging Library adds image processing capabilities to your Python interpreter.
- [psycopg2](https://pypi.org/project/psycopg2/) - A PostgreSQL adapter for Python.
- [python3-openid](https://pypi.org/project/python3-openid/) - A set of Python packages for implementing OpenID Connect.
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) - OAuthlib authentication support for Requests.
- [s3transfer](https://pypi.org/project/s3transfer/) - An Amazon S3 Transfer Manager for Python.
- [sqlparse](https://pypi.org/project/sqlparse/) - A non-validating SQL parser module for Python.
- [urllib3](https://pypi.org/project/urllib3/) - A powerful HTTP client for Python, which provides features such as connection pooling, request retries, and more.
- [stripe](https://pypi.org/project/stripe/) - A Python library for the Stripe API.

## Testing

All Testing documentation can be found on the [TESTING.md](TESTING.md) file.

## Deployment

[Click Here To See The Live Website](https://www.hefestuscave.com/)

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: hefestus-cave).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://hefestus-cave.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Deploy with Heroku

This project uses [Heroku](https://www.heroku.com/) to host and deploy the website

To deploy your website using Heroku, begin by signing up for a Heroku account. Then, proceed with the following steps:s
1. Go on to [Heroku](https://www.heroku.com/) website and [log in](https://id.heroku.com/login) if you already have an account or [sign up](https://signup.heroku.com/) if you don't. 
2. Click on the "New" button on the top right of the home page and select "Create new App" from the drop-down menu.
3. In the "App name" field enter the name of your app. This name has to be unique. 
    - Heroku displays a green tick if your app name is available.
4. In the "Choose a region" field choose either the United States or Europe based on your location.
5. Click the "Create app" button.
6. Next page, top centre of the screen, select the "Settings" tab. 
7. In the "Config Vars" section, click on the "Reveal config Vars" button.
8. In this section you need to enter your environment variables. Usually stored in the env.py file locally. In my case, I have 10 variables: 
    - SECRET_KEY - Django secret key.
    - AWS_ACCESS_KEY_ID - Amazon AWS access key.
    - AWS_SECRET_ACCESS_KEY - Amazon AWS secret access key.
    - AWS_STORAGE_BUCKET_NAME - Amazon AWS bucket name.
    - DATABASE_USER - Amazon RDS database user.
    - EMAIL_HOST_PASS - Email password.
    - EMAIL_HOST_USER - Email address.
    - DATABASE_HOST - Amazon RDS database host.
    - DATABASE_NAME - Amazon RDS database name.
    - DATABASE_PASS - Amazon RDS database password.
9. Copy and paste these variables into the KEY field and their values into the VALUE field.
10. Go back to the top of the screen and select the "Deploy" tab.
11. In the "Deployment method" section select "GitHub".
    1. In "Connect to GitHub" click on the "Search" button. Find the project repository in the list and click on the "Connect" button.
    2. Scroll to the bottom of that page. Click on the "Deploy Branch" button to deploy.
    3. You should also see an option to enable automatic deployment. If you enable this, every time you push to GitHub, Heroku will automatically deploy the app.
12. You will see build log scrolling at the bottom of the screen after that. When successfully finished building the app, you should see the link to your app.

NB: You will need to add your Heroku app link to the ALLOWED_HOSTS in the settings.py file. You also need to make sure that DEBUG is set to False, requirements.txt and Procfile are up to date and pushed to GitHub.

### Custom Domain and SSL Certificate:

This project utilizes a custom domain purchased through [GoDaddy](https://www.godaddy.com/) and hosted on Heroku.

- To add a custom domain to Heroku, follow these steps:

1. Log in to the [Heroku](https://www.heroku.com/) website.
2. Navigate to the desired app.
3. Access the "Settings" tab and scroll down to the "Domains" section.
4. Click on "Add Domain" and enter your new domain (assuming you've already purchased it from a registrar).
5. Proceed to the next step.
6. Copy the _DNS target_ provided by Heroku.
7. Create a new CNAME record within your registrar account and point your domain to the _DNS target_ provided by Heroku.
8. Allow for the propagation period, which may take up to 48 hours.

For SSL certificate management, this project utilizes the free SSL certificate provided by Heroku's [Automatic Certificate Management (ACM)](https://devcenter.heroku.com/articles/automated-certificate-management) system. 

- To add the ACM SSL Certificate, follow these steps:

1. Log in to the [Heroku](https://www.heroku.com/) website.
2. Select the relevant app.
3. Navigate to the "Settings" tab and locate the "SSL Certificates" section.
4. Click on "Configure SSL".
5. Choose "Automatic Certificate Management (ACM)" and proceed.
6. Wait for the SSL certificate to be issued to your domain, which may take up to 60 minutes for propagation.

### Fork

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/tinobragaa/hefestus-cave)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Clone

You can clone the repository by following these steps:

1. Go to the [GitHub Repository](https://github.com/tinobragaa/hefestus-cave) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/tinobragaa/hefestus-cave`
7. Press Enter to create your local clone.

## Credits

A list of references used for the site:

* [How to Point a Custom Domain to Heroku](https://stackoverflow.com/questions/49321317/setting-up-a-godaddy-domain-name-with-heroku).
* [Bad Request Error After Adding a Custom Domain](https://stackoverflow.com/questions/23252733/i-get-an-error-400-bad-request-on-custom-heroku-domain-but-works-fine-on-foo-h/27402083#27402083).
* [Removing input Background Colour for Chrome Autocomplete](https://stackoverflow.com/questions/2781549/removing-input-background-colour-for-chrome-autocomplete).
* The developer leveraged their past projects, including [Mil's Kitchen](https://tinobragaa.github.io/mils-kitchen/) (GitHub repository [here](https://github.com/tinobragaa/mils-kitchen)), [codit Quiz - Your JavaScript Quiz](https://tinobragaa.github.io/codit-quiz/) (GitHub repository [here](https://github.com/tinobragaa/codit-quiz)), [Password Creator](https://password-creatorr.herokuapp.com/) (GitHub repository [here](https://github.com/tinobragaa/password-creator)), and [Eire Settlers](https://eire-settlers-9b0e3e0c192c.herokuapp.com/) (GitHub repository [here](https://github.com/tinobragaa/eire-settlers)), as primary references for accessing code solutions and CSS, as well as for README documentation purposes.
* The development process relied on The Code Institute's Boutique Ado walkthrough.

## Acknowledgements

I'd like to take a moment to thank myself for the relentless effort and determination I've shown in completing my bootcamp journey. It's been a challenging road, but I've pushed through every obstacle and stayed committed to my growth and learning. This experience has taught me invaluable lessons and has helped me develop both personally and professionally. Here's to acknowledging the hard work and dedication that have brought me to this point, and to continuing this journey with resilience and determination.