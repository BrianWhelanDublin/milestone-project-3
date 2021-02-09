# Testing

### User Stories

- New Visitor

  - As a new user, I would like to know what the website is about upon opening the site.

    - The website landing page contains the main heading and a paragraph explaining what the application is for.
    - There is also an about us section just below and an about us page that's accessible from the navigation menu.

    - Landing page title
        - <div float="left">
            <img src="readme-images/features/main/landing.png" alt="Image of landing page" width="500px" height="280px" />
        </div>

    - Landing page about section.
        - <div float="left">
            <img src="readme-images/features/main/landing-about.png" alt="Image of about section on landing page" width="500px" height="280px" />
        </div>


  - As a new user, I would like to get information about the website.
    - The user can visit the about us page to get information about the website.
    - The last 4 most recent posts are shown on the landing page to show the user what people are posting about.

    - About Page
        - <div float="left">
            <img src="readme-images/features/main/about.png" alt="Image of about page" width="500px" height="280px" />
          </div>

  - As a new user, I would like to see some posts on the site.
      - As the user scrolls down the landing page they can see the last 4 most recent posts.

      - Landing page posts section 
        - <div float="left">
            <img src="readme-images/features/main/landing-posts.png" alt="Image landing page posts section" width="500px" height="280px" />
          </div>

  - As a new user, I would like to easily register for the site.
    - The landing page contains a link for users to get to the signup page.
    - The users can also get here from the navigation menu.

      - Landing page Signup link

        - <div float="left">
            <img src="readme-images/features/main/sign-up-link.png" alt="Image of signup link" width="350px" height="280px" />
        </div>

    - Landing page navigation menu.

        - <div float="left">
            <img src="readme-images/features/main/landing-nav.png" alt="Image of landing page navigation menu" width="350px" height="280px" />
        </div>


  - As a new user, I would like to add a bio and an image to my user account.
    - The user account will be filled with the user's details.
    - The user will have the option to add their own picture and a bio when the click on update account.

    - Users navigation menu

        - <div float="left">
            <img src="readme-images/features/main/account-nav.png" alt="Image of users navigation menu" width="350px" height="280px" />
        </div>

    - Account page with update and delete buttons.

        - <div float="left">
            <img src="readme-images/features/main/update-account-btns.png" alt="Image of account page" width="350px" height="320px" />
        </div>

     - Account page with update and delete buttons.

        - <div float="left">
            <img src="readme-images/features/main/update-account-btns.png" alt="Image of about section" width="350px" height="320px" />
        </div>
    
      - Update account page.

        - <div float="left">
            <img src="readme-images/features/main/update-account-form.png" alt="Image of update account form" width="550px" height="280px" />
        </div>

    - Account page with updated image and details.

        - <div float="left">
            <img src="readme-images/features/main/updated-account.png" alt="Image of account page" width="350px" height="420px" />
        </div>


  - As a new user, I would like to add a new post to the blog.
    - Once the user has registered and logged in the navigation menu will contain a link to the add post page.
    - Here the user can fill out the form to add a post.
    - Once the user fills in the form it will be saved in the database.

     - New post form
      - <div float="left">
            <img src="readme-images/features/posts/new-post.png" alt="Image of account page" width="550px" height="320px" />
        </div>


- Repeat users

  - As a repeat user, I would like to easily login upon opening the site.
    - The home page contains a link to the login page.
    - The user can also get here from the navigation menu.
       
       - Landing page login link

        - <div float="left">
            <img src="readme-images/features/main/login-link.png" alt="Image of login link" width="400px" height="280px" />
        </div>
       
       - Landing page navigation menu.

        - <div float="left">
            <img src="readme-images/features/main/landing-nav.png" alt="Image of landing page navigation menu" width="350px" height="280px" />
        </div>

  - As a repeat user, I would like to be able to like posts.
    - Each post has a like button that the user can click and it'll update with the number of likes the post has.

      - Post like button.

        - <div float="left">
            <img src="readme-images/features/posts/like-btn.png" alt="Image of post like button" width="250px" height="160px" />
        </div>

  - As a repeat user, I would like to be able to comment on posts.
    - Each post has a comment section where a user can fill in the form and upon submittal, the comment will be saved to the database and then appear on the site.
    - The user can then update or delete only their comments.
      
      - Post comment section.

        - <div float="left">
            <img src="readme-images/features/posts/comment.png" alt="Image of post like button" width="4000px" height="300px" />
        </div>
    

  - As a repeat user, I would like to edit and delete my posts.
    - The post page will contain an update or delete button if the current user wrote the post
    - the user can then follow these to update or delete the post.

     - Update post form.

        - <div float="left">
            <img src="readme-images/features/posts/update-post.png" alt="Image of update post form" width="450px" height="280px" />
        </div>
       
       - Delete post modal.

        - <div float="left">
            <img src="readme-images/features/posts/delete-post.png" alt="Image of landing page navigation menu" width="520px" height="270px" />
        </div>


  - As a repeat user, I would like to be able to edit and delete my account.
    - The user can edit their account by clicking on the update account button.
    - They will then be taken to the update account form which will be prefilled with the data already stored in the database.
    - They can also delete their account by clicking on the delete account button. 
    - They will be shown a warning modal first to confirm they want to delete.

    - Update account

        - <div float="left">
            <img src="readme-images/features/users/account.png" alt="Image of users account" width="450px" height="280px" />
        </div>
       
    - Delete post modal.

        - <div float="left">
            <img src="readme-images/features/users/delete-account.png" alt="Image of landing page navigation menu" width="650px" height="280px" />
        </div>
-  All users.

   - As a user, I would like to get feedback when I have completed an action on the site.
     - Flash messaging is used across each route to update the user when they have completed an action

      - Flashed message.

        - <div float="left">
            <img src="readme-images/features/users/flashed-message.png" alt="Image of landing page navigation menu" width="500px" height="180px" />
        </div>

- As a user, I would like to be able to contact the website owners if there is an issue.
    - the navigation menu contains a link to the contact form.
    - Upon submit the user will be directed to the homepage and a message will flash telling them their contact message has been sent.
    - Flask-mail will then send a mail to the site owner.

    - Users navigation menu

        - <div float="left">
            <img src="readme-images/features/main/account-nav.png" alt="Image of users navigation menu" width="350px" height="280px" />
        </div>

    - Contact Form

        - <div float="left">
            <img src="readme-images/features/main/contact.png" alt="Image of contact form" width="450px" height="280px" />
        </div>


- Website owner


  - As the owner, I want the user to be able to find information easily.
    - Information is made very clear and concise to the user. 
    - The about sections clearly describe the websites intentions.


  - As the owner, I want the user to be able to sign up or log in easily.
    - The home page contains both signup and login links as shown above.
    - The user can also navigate to them from the navigation menu as shown above.

  - As the owner, I only want users who have signed up and logged in to see the full post page.
    - If the user isn't authenticated they will be shown the landing page that only contains the last 4 posts summaries.
    - If they try to open these posts flask login will direct them to the login page.
    - Once they have logged in they will be brought to the home recent posts page.

    - Recent posts page.

        - <div float="left">
            <img src="readme-images/features/posts/recent-posts.png" alt="Image of recent posts page" width="450px" height="280px" />
        </div>

  - As a site owner, I only want the user to be able to delete their own posts or comments.
    - I have used flask login to and jinja if statements to only allow the update and delete buttons if the current user is the post or comment author.
    - If the current user isn't the author these buttons will not appear.
    - I have also placed code to check if the current user is the author and if not the application will throw a 403 error

       - 403 error.

        - <div float="left">
            <img src="readme-images/features/posts/403error.png" alt="Image of 403 error" width="450px" height="280px" />
        </div>


  - As a site owner, I want to be able to see how many users there are and how many posts.
    - The site owner has access as Admin that shows a dashboard containing information on the number of users and posts.
    - They also can add, update and delete comments.
      
       - Dashboard.

        - <div float="left">
            <img src="readme-images/features/admin/dashboard.png" alt="Image of admin dashboard" width="450px" height="280px" />
        </div>

  - As a site owner, I want the ability to delete any post regardless to who has written them, eg they are offensive etc.
    - the application has been coded that if the current user is admin then it will show all the update delete buttons throughout the site.