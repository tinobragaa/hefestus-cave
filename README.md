# Hefestus Cave
(Developer: Valentino Braga)

Project description.

![Mockup image]()

[Live Website]()

# UX (User Experience)

## User Stories

### Developer
1. As a developer I can use local IDE to develop the project.
2. As a developer I can deploy the project to Heroku early in the development process.
3. As a developer I can create wireframes for the project so that I have a clear idea of what I want to achieve.
4. As a developer I can create a database schema for the project so that I have a clear idea of what models I need to create.

### User/Shopper
1. As a user, I want to be able to create an account so that I can have my address saved for future purchases.

# Design

Design description.

### Wireframes

The initial concept of the design can be seen here and they were made through Figma. 

<details>
<summary>Wireframe</summary>
<br>

![Wireframe]()

</details>


### Typography

Typography description.

![Font Name]()

![Font Name]()

### Colour Palette

Colour description.

* [ColorSpace](https://mycolor.space/)
* [Coolors](https://coolors.co/)

![Colour Palette]()

### Imagery

Imagery description.

* [Pexels](https://www.pexels.com/)
* [Unsplash](https://unsplash.com/)
* [Hefestus Cave](https://www.instagram.com/hefestuscave/)

Icons were used for social links and buttons. The icons used on the site were taken from:

* [Font Awesome](https://fontawesome.com/)

# Database Schemas

# Agile Development

# Features 

### Homepage
- 
-
-
<details>
<summary>Homepage</summary>
<br>

![Homepage]()

</details>

# Future Features

1.
2.
3.
4.
5.

# Technologies Used

### Language
The following language were used to develop the website:
- Python
- HTML
- CSS

### Tools and Resources
The following tools and resources were used to develop the website:
- Git
- Github
- Gitpod
- Google
- Heroku
- Favicon
- Lucidchart
- Codecademy
- W3 Schools
- Stack Overflow
- Github Projects
- CI Python Linter
- Techsini Mockup Generator
- GitHub Wiki TOC generator

# Testing

# Bugs

Bug:
Fix: 

Bug:
Fix: 

Bug:
Fix: 

# Deployment

[Click Here To See The Live Website](https://password-creatorr.herokuapp.com/)

# Deployment

### Deploy with Heroku

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

### Fork
1. Go to the desired repository
2. Click "Fork" in the upper right corner
3. Select the owner, and set the repository name. A description can be added if desired
4. Choose whether to copy the default branch, or all branches
5. Click "Create Form"

### Clone

1. Go to the desired repository
2. Click the "Code" button at the top of the files section of the page
3. Select your desired method for cloning (HTTPS/SSH/GitHub CLI)
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory
6. Type "git clone", and then paste the URL you copied earlier. It will look like this, with your GitHub username instead of "YOUR-USERNAME": "$ git clone https://github.com/YOUR-USERNAME/DESIRED-REPOSITORY"
7. Press Enter. Your local clone will be created.

### Heroku

1. Create a user account with Heroku.
2. Click New in the top-right corner of your Heroku Dashboard.
3. Click on the dropdown menu and select create new.
4. The app name is unique to all apps within Heroku so select one that is not currently in use.
5. Select a region, EU or USA.
6. Click Create App.
7. In the app settings click Reveal Config vars, set the value of KEY to PORT, and the value to 8000 and click add.
8. Click Add Buildpack.
9. Choose Python first and click add.
10. Choose Node.js second.
11. The order is important, Python needs to be first, then Node.js second.
12. Click on the Deploy tab, select connect to Github and search for your repository.
13. Click on Enable automatic deploy or Deploy branch depending on your use case.

# Credits

A list of references used for the site:

### References and Tutorials

*
*
*

# Acknowledgements

I would like to take this opportunity to acknowledge and thank the following people:

-
-
-
-