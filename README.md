# whyb. {A Social Media Application}

This is a social media application developed as a project for the BusinessOnBot internship. The application allows users to create accounts, log in, share posts publicly, search for users, and more.

## Table of Contents

- [What is whyb?](#what-is-whyb?)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)

## What is whyb>

##### /vi-be'/

Welcome to whyb.: Your one-stop-shop for music mayhem! 🎵 Found yourself jamming to a tune and bursting with opinions? Whether it's Spotify, iTunes, or any other platform, whyb. has got your back! Imagine this: You're grooving to a killer track, and suddenly, you're hit with the urge to spill your thoughts. But where to? Fear not! whyb. is your musical soapbox in the digital cosmos!

It's your chance to unleash your inner critic or dive into the chaos of comments sections. 🎤 But here's the kicker: Your opinions aren't just whispers—they're heard across the globe! From Kkarnataka to Kazakhstan, anyone can tune in, read your reviews, and join the fun!

So, when you're ready to dissect a beat or praise a riff, remember one word: whyb. 🎸 Because in life's symphony, your voice deserves to be the star solo! 🌟

## Features

- Fortify your online presence with secure password-based authentication.
- Take control of your profile with easy editing and updating options.
- Engage with the community through effortless post sharing and exploration.
- Find and connect with like-minded users with intuitive search functionality.
- Enjoy a seamless user experience across all devices with responsive design.

## Technologies Used

- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript (with Jinja templating)
- Database: SQLAlchemy (with SQLite)
- Deployment: PythonAnywhere

## Installation

1. Clone the repository:

```bash
   git clone https://github.com/your-username/social-media-app.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Set up the database:
   Modify config.py to specify your database configuration.
   Run Flask migrations:

```
flask db init
flask db migrate
flask db upgrade
```

4. Set up environment variables:
   Create a .env file and add necessary environment variables like URI, secret key, etc.

5. Run the application:

```
flask run
```

## Usage

1. Visit the deployed URL to access the application.
2. Register for a new account or log in with an existing one. To try login with :

````
username: bzhal
password: bilal
```
3. Explore different functionalities such as creating posts, updating profile, searching for users, and many more.

##  API Endpoints
Users:
````

GET /api/users: List all users
GET /api/users/{name}: Search for users by name

```
Posts:
```

GET /api/posts: List all posts
GET /api/posts/{name}: List all posts by a specific user

```

## Screenshots
Include screenshots of your application to showcase its UI and features.
```
