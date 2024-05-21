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
| script.js  | JShint | ![screenshot](/documentation/testing/) | Pass: No Errors |

### Python

The [CI Python Linter](https://pep8ci.herokuapp.com) was used to validate Python files.

| File | Validator | Screenshot | Notes |
| --- | --- | --- | --- |
| settings.py | CI PEP8 | ![screenshot](/documentation/testing/) | Pass: No Errors |
| urls.py (main) | CI PEP8 | ![screenshot](/documentation/testing/) | Pass: No Errors |
| forms.py (comments) | CI PEP8 | ![screenshot](/documentation/testing/) | Pass: No Errors |
| models.py (comments) | CI PEP8 | ![screenshot](/documentation/testing/) | Pass: No Errors |
| urls.py (home) | CI PEP8 | ![screenshot](/documentation/testing/) | Pass: No Errors |
| views.py (home) | CI PEP8 | ![screenshot](/documentation/testing/) | Pass: No Errors |
| forms.py (messaging) | CI PEP8 | ![screenshot](/documentation/testing/) | Pass: No Errors |

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
| Mobile (DevTools) | ![screenshot](/documentation/testing/) | Works as expected |
| Tablet (DevTools) | ![screenshot](/documentation/testing/) | Works as expected |
| Desktop | ![screenshot](/documentation/testing/) | Works as expected |

## Lighthouse Audit

All pages were tested with [Google Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/). Testing was performed in private browsing mode and on the live website on Heroku.

| Page | Image |
| --- | --- |
| Homepage | ![Lighthouse Screenshot](/documentation/testing/) |
| All Products Page | ![Lighthouse Screenshot](/documentation/testing/) |

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
