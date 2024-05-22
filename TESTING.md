# Table of Contents

- [Testing](#testing)
  * [Validation](#validation)
    + [HTML](#html)
    + [CSS](#css)
    + [JavaScript](#javascript)
    + [Python](#python)
  * [Browser Compatibility](#browser-compatibility)
  * [Responsiveness Testing](#responsiveness)
  * [Lighthouse Audit](#lighthouse-audit)
  * [Manual Testing](#manual-testing)
  * [User Story Testing](#user-story-testing)
  * [Bugs](#bugs)

**Return back to the [README.md](README.md) file.**

# Testing

During the evolution of this project, I've conducted a multitude of tests to verify the functionality of the site. Within this section, you'll discover comprehensive documentation detailing every test performed across the site.

## HTML Validation

The Nu HTML Checker [HTML W3C Validator](https://validator.w3.org) was used to validate HTML documents. The files passed without any errors.

| Page | W3C | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | W3C | ![screenshot](/documentation/testing/) | Pass: No Errors |
| All Products | W3C | ![screenshot](/documentation/testing/) | Pass: No Errors |

### CSS

The [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) was used to validate CSS files.

| File | Validator | Screenshot | Notes |
| --- | --- | --- | --- |
| base.css | Jigsaw | ![screenshot](/documentation/testing/base-css-validation.jpg) | Pass: No Errors |
| checkout.css | Jigsaw | ![screenshot](/documentation/testing/checkout-css-validation.jpg) | Pass: No Errors |

### JavaScript

The [JShint Validator](https://jshint.com) was used to validate JS files.

| File | Validator | Screenshot | Notes |
| --- | --- | --- | --- |
| countryfields.js | JShint | ![screenshot](/documentation/testing/country-js-validation.jpg) | Pass: No Errors |
| stripe_elements.js | JShint | ![screenshot](/documentation/testing/stripe-elements-js.jpg) | Pass: No Errors |
| products.html (postloadjs) | JShint | ![screenshot](/documentation/testing/products-js.jpg) | Pass: No Errors |
| cart.html (postloadjs) | JShint | ![screenshot](/documentation/testing/cart-js.jpg) | Pass: No Errors |
| quantity_input_script.html (script) | JShint | ![screenshot](/documentation/testing/quantity-input-js.jpg) | Pass: No Errors |
| add_product.html (postloadjs) | JShint | ![screenshot](/documentation/testing/edit-add-product-js.jpg) | Pass: No Errors |
| edit_product.html (postloadjs) | JShint | ![screenshot](/documentation/testing/edit-add-product-js.jpg) | Pass: No Errors |

### Python

The [CI Python Linter](https://pep8ci.herokuapp.com) was used to validate Python files.

| File | Validator | Screenshot | Notes |
| --- | --- | --- | --- |
| context.py (cart) | CI PEP8 | ![screenshot](/documentation/testing/context-cart-python-validation.jpg) | Pass: No Errors |
| urls.py (cart) | CI PEP8 | ![screenshot](/documentation/testing/urls-cart-python-validation.jpg) | Pass: No Errors |
| views.py (cart) | CI PEP8 | ![screenshot](/documentation/testing/views-cart-python-validation.jpg) | Pass: No Errors |`
| admin.py (checkout) | CI PEP8 | ![screenshot](/documentation/testing/admin-checkout-python-validation.jpg) | Pass: No Errors |
| forms.py (checkout) | CI PEP8 | ![screenshot](/documentation/testing/forms-checkout-python-validation.jpg) | Pass: No Errors |
| models.py (checkout) | CI PEP8 | ![screenshot](/documentation/testing/models-checkout-python-validation.jpg) | Pass: No Errors |
| signals.py (checkout) | CI PEP8 | ![screenshot](/documentation/testing/signals-checkout-python-validation.jpg) | Pass: No Errors |
| urls.py (checkout) | CI PEP8 | ![screenshot](/documentation/testing/urls-checkout-python-validation.jpg) | Pass: No Errors |
| views.py (checkout) | CI PEP8 | ![screenshot](/documentation/testing/views-checkout-python-validation.jpg) | Pass: No Errors |
| webhooker_handler.py (checkout) | CI PEP8 | ![screenshot](/documentation/testing/webhook-handler-checkout-python-validation.jpg) | Pass: No Errors |
| webhooks.py (checkout) | CI PEP8 | ![screenshot](/documentation/testing/webhooks-checkout-python-validation.jpg) | Pass: No Errors |
| admin.py (contact) | CI PEP8 | ![screenshot](/documentation/testing/admin-contact-python-validation.jpg) | Pass: No Errors |
| forms.py (contact) | CI PEP8 | ![screenshot](/documentation/testing/forms-contact-python-validation.jpg) | Pass: No Errors |
| models.py (contact) | CI PEP8 | ![screenshot](/documentation/testing/models-contact-python-validation.jpg) | Pass: No Errors |
| urls.py (contact) | CI PEP8 | ![screenshot](/documentation/testing/urls-contact-python-validation.jpg) | Pass: No Errors |
| views.py (contact) | CI PEP8 | ![screenshot](/documentation/testing/views-contact-python-validation.jpg) | Pass: No Errors |
| admin.py (discount_code) | CI PEP8 | ![screenshot](/documentation/testing/admin-discount-python-validation.jpg) | Pass: No Errors |
| forms.py (discount_code) | CI PEP8 | ![screenshot](/documentation/testing/forms-discount-python-validation.jpg) | Pass: No Errors |
| models.py (discount_code) | CI PEP8 | ![screenshot](/documentation/testing/models-discount-python-validation.jpg) | Pass: No Errors |
| urls.py (home) | CI PEP8 | ![screenshot](/documentation/testing/urls-home-python-validation.jpg) | Pass: No Errors |
| views.py (home) | CI PEP8 | ![screenshot](/documentation/testing/views-home-python-validation.jpg) | Pass: No Errors |
| admin.py (product) | CI PEP8 | ![screenshot](/documentation/testing/admin-products-python-validation.jpg) | Pass: No Errors |
| forms.py (product) | CI PEP8 | ![screenshot](/documentation/testing/forms-products-python-validation.jpg) | Pass: No Errors |
| models.py (product) | CI PEP8 | ![screenshot](/documentation/testing/models-products-python-validation.jpg) | Pass: No Errors |
| urls.py (product) | CI PEP8 | ![screenshot](/documentation/testing/urls-products-python-validation.jpg) | Pass: No Errors |
| views.py (product) | CI PEP8 | ![screenshot](/documentation/testing/views-products-python-validation.jpg) | Pass: No Errors |
| forms.py (profiles) | CI PEP8 | ![screenshot](/documentation/testing/forms-profiles-python-validation.jpg) | Pass: No Errors |
| models.py (profiles) | CI PEP8 | ![screenshot](/documentation/testing/models-profiles-python-validation.jpg) | Pass: No Errors |
| urls.py (profiles) | CI PEP8 | ![screenshot](/documentation/testing/urls-profiles-python-validation.jpg) | Pass: No Errors |
| views.py (profiles) | CI PEP8 | ![screenshot](/documentation/testing/views-profiles-python-validation.jpg) | Pass: No Errors |
| settings.py (hefestus_cave) | CI PEP8 | ![screenshot](/documentation/testing/settings-hefestus-python-validation.jpg) | Pass: No Errors |
| urls.py (hefestus_cave) | CI PEP8 | ![screenshot](/documentation/testing/urls-hefestus-python-validation.jpg) | Pass: No Errors |
| views.py (hefestus_cave) | CI PEP8 | ![screenshot](/documentation/testing/views-hefestus-python-validation.jpg) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](/documentation/testing/chrome-compatibility.jpg) | Works as expected |
| Firefox | ![screenshot](/documentation/testing/firefox-compatibility.jpg) | Works as expected |
| Safari | ![screenshot](/documentation/testing/safari-compatibility.jpg) | Works as expected |
| Edge | ![screenshot](/documentation/testing/edge-compatibility.jpg) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](/documentation/testing/mobile-responsiveness.jpg) | Works as expected |
| Tablet (DevTools) | ![screenshot](/documentation/testing/tablet-responsiveness.jpg) | Works as expected |
| Desktop | ![screenshot](/documentation/features/landing-page.jpg) | Works as expected |

## Lighthouse Audit

All pages were tested with [Google Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/). Testing was performed in private browsing mode and on the live website on Heroku.

| Page | Image |
| --- | --- |
| Homepage | ![Lighthouse Screenshot](/documentation/testing/homepage-lighthouse.jpg) |
| All Products | ![Lighthouse Screenshot](/documentation/testing/all-products-lighthouse.jpg) |
| Individual Product | ![Lighthouse Screenshot](/documentation/testing/individual-product-lighthouse.jpg) |
| Sign In | ![Lighthouse Screenshot](/documentation/testing/sign-in-lighthouse.jpg) |
| Sign Out | ![Lighthouse Screenshot](/documentation/testing/sign-out-lighthouse.jpg) |
| Sign Up | ![Lighthouse Screenshot](/documentation/testing/sign-up-lighthouse.jpg) |
| Profile | ![Lighthouse Screenshot](/documentation/testing/profile-lighthouse.jpg) |
| Product Management | ![Lighthouse Screenshot](/documentation/testing/product-management-lighthouse.jpg) |
| Contact | ![Lighthouse Screenshot](/documentation/testing/contact-lighthouse.jpg) |
| Policies | ![Lighthouse Screenshot](/documentation/testing/policies-lighthouse.jpg) |
| Returns & Exchanges | ![Lighthouse Screenshot](/documentation/testing/returns-lighthouse.jpg) |
| Cart | ![Lighthouse Screenshot](/documentation/testing/cart-lighthouse.jpg) |
| Empty Cart | ![Lighthouse Screenshot](/documentation/testing/empty-cart-lighthouse.jpg) |
| Checkout | ![Lighthouse Screenshot](/documentation/testing/checkout-lighthouse.jpg) |
| Order Confirmation Page | ![Lighthouse Screenshot](/documentation/testing/order-confirmation-lighthouse.jpg) |

## Manual Testing

## User Story Testing

The following are user stories I've implemented with screenshots accordingly. 

| User Story | Screenshot |
| --- | --- |
| As a user, I want to sign in with one of my social accounts so that I can sign in or sign up quickly and easily. | ![screenshot](/documentation/features/sign-in-page.jpg) |
| As a user, I want to be able to reset my password if I forget it so that I can access my account. | ![screenshot](/documentation/features/reset-password-page.jpg) |
| As a user, I want to be able to view a comprehensive list of all products available on the site so that I can browse and explore the full range of offerings. | ![screenshot](/documentation/features/all-products-page.jpg) |
| As a user, I want to be able to see the prices of products clearly so that I can make informed decisions about whether or not to purchase. | ![screenshot](/documentation/features/products-grid.jpg) |
| As a user, I want to be able to view a product on its own individual page so that I can access comprehensive information about the product. | ![screenshot](/documentation/features/individual-product-page.jpg) |
| As a user, I want to be able to search for a product by name or description so that I can find what I want quickly. | ![screenshot](/documentation/features/search-bar.jpg) |
| As a user, I want to be able to add a product to my shopping cart so that I can easily purchase it later. | ![screenshot](/documentation/features/add-to-cart-button.jpg) |
| As a user, I want to be able to view my shopping cart so that I can review the contents and total cost of my intended purchase. | ![screenshot](/documentation/features/cart.jpg) |
| As a user, I want to be able to edit the quantity of a product in my shopping cart so that I can purchase the quantity I desire. | ![screenshot](/documentation/features/edit-cart.jpg) |
| As a user, I want to be able to delete items from my shopping cart so that I can remove unwanted products before proceeding to checkout. | ![screenshot](/documentation/features/remove-cart.jpg) |
| As a user, I want to be able to sort products by various criteria (price, newest) so that I can easily find items that match my preferences and needs, enhancing my shopping experience. | ![screenshot](/documentation/features/product-filtering.jpg) |
| As a user, I want to be able to securely pay for my purchase using Stripe during checkout, so that I can complete the transaction smoothly and begin enjoying my products. | ![screenshot](/documentation/features/checkout.jpg) |
| As a user, I want to be able to receive an order confirmation email after I purchase from the shop so that I can have a record of what I've purchased in my email inbox. | ![screenshot](/documentation/features/order-confirmation-email.jpg) |
| As a site user, I want to be able to apply discount codes in my cart so that I can receive a discount on my purchase. | ![screenshot](/documentation/features/discount-added.jpg) |
| As a user, I want to be able to navigate between related pages easily so that I can find relevant content and information quickly and efficiently. | ![screenshot](/documentation/features/navigation-bar.jpg) |
| As a user, I want to be able to clearly understand the purpose of the website so that I can form an impression and decide whether or not to engage further. | ![screenshot](/documentation/features/landing-page.jpg) |
| As a user, I would like the site to have a customised favicon so I can easily identify it when I have multiple tabs open. | ![screenshot](/documentation/features/favicon.jpg) |
| As a user, I want to be able to contact the website administrators through a "Contact Us" page using a form so that I can communicate any inquiries, feedback, or issues. | ![screenshot](/documentation/features/contact-us-page.jpg) |
| As a developer, I need to create a 404 page so that users are redirected when entering a broken URL. | ![screenshot](/documentation/features/404-page.jpg) |
| As a site user, I want to be able to subscribe to the site's mailing list so that I can receive exclusive offers and updates directly in my inbox, enhancing my engagement with the website. | ![screenshot](/documentation/features/newsletter-subscription.jpg) |


The following are user stories I wasn't able to implement and have been set as Future Release on the [Kanban Board](https://github.com/users/tinobragaa/projects/5/views/1).

<details>
<summary>Future Release Issues</summary>
<br>

![screenshot](/documentation/testing/future-release-issues.jpg)

</details>

| User Story | Status |Issue |
| --- | --- | --- |
| As a user, I want to be able to change the language of the website so that I can access content in a language that is more familiar or comfortable for me. | Open | [Multi-Language Support](https://github.com/tinobragaa/hefestus-cave/issues/39) |
| As a user, I want to be able to add products to a wishlist so that I can keep a collection of items I am interested in buying in the future. | Open | [Wishlist Functionality](https://github.com/tinobragaa/hefestus-cave/issues/35) |
| As a user, I want to sign in with one of my social accounts so that I can sign in or sign up quickly and easily. | Open | [Social Media Login](https://github.com/tinobragaa/hefestus-cave/issues/25) |
| As a user, I want to be able to review products that I have purchased so that I can share my experience with other potential customers. | Open | [Product Review](https://github.com/tinobragaa/hefestus-cave/issues/33) |
| As a user, I want to be able to share content from the website on various social media platforms, including Facebook, Instagram, X, and Pinterest, so that I can engage with my social network and amplify the reach of interesting content. | Open | [Social Media Sharing](https://github.com/tinobragaa/hefestus-cave/issues/38) |
| As a user, I want to have an express checkout option that allows me to save my payment information securely in a digital wallet within my account so that I can complete transactions quickly without having to enter payment details every time I make a purchase. | Open | [Express Checkout and Wallet Integration](https://github.com/tinobragaa/hefestus-cave/issues/40) |
| As a user, I want to earn points for every purchase I make, which I can redeem for discounts or free products in the future so that I feel rewarded for my loyalty and continue shopping at this store. | Open | [Loyalty Program](https://github.com/tinobragaa/hefestus-cave/issues/41) |
| As a user, I want to view product prices and complete transactions in my preferred currency so that I can better understand the costs and avoid currency conversion fees. | Open | [Multi-Currency Support](https://github.com/tinobragaa/hefestus-cave/issues/42) |

## Bugs

`Bug`: I decided to add a custom domain to my project. After I bought the domain with the registrar and pointed to the heroku application, I was getting a error a bad request error (code 400) after pointing the new domain. [400 Error - Stack Overflow](https://stackoverflow.com/questions/23252733/i-get-an-error-400-bad-request-on-custom-heroku-domain-but-works-fine-on-foo-h/27402083#27402083).
<br>
`Fix`: I added the new domain into the list of allowed hosts on settings.py. 

`Bug`: When I was bulding up the homepage, I noticed a problem where the hero image and the footer were causing a white space on the left side. After inspecting it, I found out that the issue stemmed from the "row" class in Bootstrap, which has a negative margin. [Boostrap's "Row" Negative Margin - Stack Overflow](https://stackoverflow.com/questions/23153497/bootstrap-row-class-contains-margin-left-and-margin-right-which-creates-problems).
<br>
`Fix`: After reading the [Bootstrap Documentation](https://getbootstrap.com/docs/3.4/css/), I discovered that Bootstrap's "row" class naturally includes a negative margin. However, Bootstrap also offers containers such as container-fluid or container that automatically adjust margins to offset this negative margin. So, to fix the issue, I need to ensure that rows are properly nested within a container.

`Bug`: After uploading the product's images, the images uploaded to the AWS bucket were appearing as broken links on the deployed site. I observed that the CSS files were loading correctly, upon closer inspection of the AWS image paths, I discovered that the URLs included the AWS region, leading to the inaccessibility of the images on the production site.
<br>
`Fix`: The AWS_S3_CUSTOM_DOMAIN variable in the settings is updated to include the AWS region in the URL path. By setting AWS_S3_CUSTOM_DOMAIN to f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com', the URL paths for images are now valid, ensuring they are correctly displayed on the deployed version of the website.