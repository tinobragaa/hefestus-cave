# Testing

Return back to the [README.md](README.md) file.

During the evolution of this project, I've conducted a multitude of tests to verify the functionality of the site. Within this section, you'll discover comprehensive documentation detailing every test performed across the site.

# HTML Validation

The Nu HTML Checker [HTML W3C Validator](https://validator.w3.org) was used to validate HTML documents. The files passed without any errors.

| Page | W3C | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | W3C | ![screenshot]() | Pass: No Errors |
| All Products | W3C | ![screenshot]() | Pass: No Errors |
| Individual Product | W3C | ![screenshot]() | Pass: No Errors |
| Contact | W3C | ![screenshot]() | Pass: No Errors |
| Blog | W3C | ![screenshot]() | Pass: No Errors |
| Blog Post | W3C | ![screenshot]() | Pass: No Errors |
| Sign Up | W3C | ![screenshot]() | Pass: No Errors |
| Sign In | W3C | ![screenshot]() | Pass: No Errors |
| Password Reset | W3C | ![screenshot]() | Pass: No Errors |
| Search | W3C | ![screenshot]() | Pass: No Errors |
| Log Out | W3C | ![screenshot]() | Pass: No Errors |
| Basket | W3C | ![screenshot]() | Pass: No Errors |
| Checkout | W3C | ![screenshot]() | Pass: No Errors  |
| Checkout Success | W3C | ![screenshot]() | Pass: No Errors |
| Profile | W3C | ![screenshot]() | Pass: No Errors |
| Add Product | W3C | ![screenshot]() | Pass: No Errors |
| Edit Product | W3C | ![screenshot]() | Pass: No Errors |
| Delete Product | W3C | ![screenshot]() | Pass: No Errors |
| Add Blog | W3C | ![screenshot]() | Pass: No Errors |
| Edit Blog | W3C | ![screenshot]() | Pass: No Errors |
| Delete Blog | W3C | ![screenshot]() | Pass: No Errors |
| Open Tickets | W3C | ![screenshot]() | Pass: No Errors |

### CSS

The [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) was used to validate CSS files.

| File | Validator | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | Jigsaw | ![screenshot]() | Pass: No Errors |

### JavaScript

The [JShint Validator](https://jshint.com) was used to validate JS files.

| File | Validator | Screenshot | Notes |
| --- | --- | --- | --- |
| script.js  | JShint | ![screenshot]() | Pass: No Errors |

### Python

The [CI Python Linter](https://pep8ci.herokuapp.com) was used to validate Python files.

| File | Validator | Screenshot | Notes |
| --- | --- | --- | --- |
| settings.py | CI PEP8 | ![screenshot]() | Pass: No Errors |
| urls.py (main) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| forms.py (comments) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| models.py (comments) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| urls.py (home) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| views.py (home) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| forms.py (messaging) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| models.py (messaging) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| urls.py (messaging) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| views.py (messaging) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| models.py (notifications) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| urls.py (notifications) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| views.py (notifications) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| notification_tags.py (notifications) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| forms.py (posts) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| models.py (posts) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| urls.py (posts) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| views.py (posts) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| models.py (profiles) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| urls.py (profiles) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| views.py (profiles) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| urls.py (search) | CI PEP8 | ![screenshot]() | Pass: No Errors |
| views.py (search) | CI PEP8 | ![screenshot]() | Pass: No Errors |


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