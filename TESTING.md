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