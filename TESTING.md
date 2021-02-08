# Testing

### User Stories

- New Visitor

  - As a new user, I would like to know what the website is about upon opening the site.

    - The website landing page contains the main heading and a paragraph explaining what the application is for.
    - There is also an about us section just below and an about us page that's accessible from the navigation menu.

  - As a new user, I would like to get information about the website.
    - The user can visit the about us page to get information about the website.
    - The last 4 most recent posts are shown on the landing page to show the user what people are posting about.

  - As a new user, I would like to see some posts on the site.
      - As the user scrolls down the landing page they can see the last 4 most recent posts.

  - As a new user, I would like to easily register for the site.
    - The landing page contains a link for users to get to the signup page.
    - The users can also get here from the navigation menu.
   

  - As a new user, I would like to add a bio and an image to my user account.
    - The user account will be filled with the user's details.
    - The user will have the option to add their own picture and a bio when the click on update account.


  - As a new user, I would like to add a new post to the blog.
    - Once the user has registered and logged in the navigation menu will contain a link to the add post page.
    - Here the user can fill out the form to add a post.
    - Once the user fills in the form it will be saved in the database.


- Repeat users

  - As a repeat user, I would like to easily login upon opening the site.
    - The home page contains a link to the login page.
    - The user can also get here from the navigation menu.

  - As a repeat user, I would like to be able to like posts.
    - Each post has a like button that the user can click and it'll update with the number of likes the post has.

  - As a repeat user, I would like to be able to comment on posts.
    - Each post has a comment section where a user can fill in the form and upon submittal, the comment will be saved to the database and then appear on the site.
    - The user can then update or delete only their comments.
    

  - As a repeat user, I would like to edit and delete my posts.
    - The post page will contain an update or delete button if the current user wrote the post
    - the user can then follow these to update or delete the post.


  - As a repeat user, I would like to be able to edit and delete my account.
    - The user can edit their account by clicking on the update account button.
    - they will then be taken to the update account form which will be prefilled with the data already stored in the database.
    - They can also delete their account by clicking on the delete account button. 
    - They will be shown a warning modal first to confirm they want to delete.

-  All users.

   - As a user, I would like to get feedback when I have completed an action on the site.
     - Flash messaging is used across each route to update the user when they have completed an action

- As a user, I would like to be able to contact the website owners if there is an issue.
    - the navigation menu contains a link to the contact form.
    - Upon submit the user will be directed to the homepage and a message will flash telling them their contact message has been sent.
    - Flask-mail will then send a mail to the site owner.


- Website owner


  - As the owner, I want the user to be able to find information easily.
  - As the owner, I want the user to be able to sign up or login easily.
  - As the owner, I only want users who have signed up and loged in to see the full post page.
  - As a site owner, I only want the user to be able to delete their own posts, or comments.
  - As a site owner, I want to be able to see how many user there are and how many posts.
  - As a site owner, I want the ability to delete any post regardless to who has written them, eg they are offensive etc.