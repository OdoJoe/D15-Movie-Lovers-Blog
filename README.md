# D15 Movie Lovers Club Blog

## Placeholder for responsive design example on differing screen types

# Strategy

## <u>Agile</u>
* The Agile framework was applied to this project using Github views and issues tab. I created a template and applied the template to each user story.
* I collected the user stories by interviewing a family member as a mock user.
* I assembled the user stories onto a kanban board in Github under the headings 'To Do', 'In Progress' and 'Done'. Using each column effectively kept the project moving toward completion. Breaking the work up into iterations helped to reduce the enormity of the project to manageable work sessions.
* Not all user stories were effectively completed and have been retained as a baseline for improvemnt and adding features in the future.

## <u>Project Goal</u>
* The idea behind the D15 Movie Lovers Blog was to create a blog that can easily fit in with my previous portfolio projects: PP1 The D15 Movie Lovers Club and PP2 The D15 Movie Lovers Quiz
* I kept the styling, colours and overall look in line with my PP1 and PP2 with a long term goal of merging the three projects together to create a viable club website with member(user) interactivity and contributions with a focus on responsive and simple design
* I wanted Users to register, log in and log out in a simple manner while being able to write a Blog, comment on a blog and edit and delete their own comments.
* Adding a blog to the D15 movile Lovers Club is a powerful way to maintain engagement with the club and foster unity with the club members, club officials and the club presence online

## <u>Models</u>
* I used the two main models from the course content Codestar walkthrough project and added a third model the CommentValidator model.
![Models screenshot](documentation/model_schema/models-pp4.png)

## <u>User Stories</u>
1. As an admin of the D15 Movie Lovers Club Blog I can approve or disapprove comments giving the admin the ability to disapprove questionable content

2. As a member of the D15 Movie Lovers Club and Blog I can access the blog on all my devices from Phone to Desktop

3. As a member of the D15 Movie Lovers Club and Blog I can recognise that the Blog page is linked to the main D15 Movie Lovers page by colour and style

4. As a member of the D15 Movie Lovers Club and Blog I can easily find and read the blog posts

5. As a member of the D15 Movie Lovers Club and Blog I can log onto the Blog with minimal fuss

6. As a member of the D15 Movie Lovers Club I can register to join the blog in a simple and accessible log on page

7. As a member of the D15 Movie Lovers Club and Blog I can vote on the monthly directors best film on a simple and accessible voting/survey box

8. As a member of the D15 Movie Lovers Club and Blog I can add suggestions to a suggestion submission box for the next monthly Director focus

9. As a member of the D15 Movie Lovers Club and Blog I can delete my comments made to Blog Posts

10. As a member of the D15 Movie Lovers Club and Blog I can edit my comments on Blog Posts

11. As a member of the D15 Movie Lovers Club and Blog I can comment on a Blog Post

## <u>Scope and structure</u>
The project scope was reduced and simplified as I approached my deadline. I decided to concentrate on coding the blog in a simple fashion with full CRUD functionality intact. 

The user stories relating to 'voting on Monthly Directors best film' and 'submitting suggestions for the next monthly director focus', while not implemented at this stage of development due to timing constraints will be added to the blog at a later date

The blog is designed to represent the blog if it were clicked into from the main D15 Movie Lovers Club (my PP1) as another page to that projects nav bar. Once the user clicks in they are presented with up to 4 Blogs per page, which will paginate into a second page once more than 4 blogs have been written. Users can navigate to 'Home', 'Register', 'Login' and 'About'

## <u>Features</u>

* Each navigational button on the Nav Bar highlights when hovered on

![nav bar highlight](documentation/feature_screenshots/underline-hover-on-nav-options.png)

* The selected page will maintain the highlighted bar to inform the user

![nav bar selection remains underlined](documentation/feature_screenshots/nav-selection-underline-to-display-current-page.png)

* Navbar reduces to burger button to accomodate smaller screen sizes

![nav bar burger](documentation/feature_screenshots/burger-responsive.png)

* Footer in place with links to social media

![footer and social links](documentation/feature_screenshots/s-media-links.png)

* A total of 4 Blog Posts will be shown before pagination moves further Blog Posts to a new page

![pagination](documentation/feature_screenshots/pagination-option.png)

* Once the comment has been submitted the User also has the option to edit the comment or delete the comment

![nav bar highlight](documentation/feature_screenshots/edit-delete-option.png)

* The time of post and the number of likes wil display under each post

![time of post and number of likes](documentation/feature_screenshots/time-of-post-like-count.png)

* The user log in will be displayed in the top right of the page until they log out

![user log in display](documentation/feature_screenshots/user-login-display.png)

* A notification will display showing users they have logged in or logged out

![log in, log out display](documentation/feature_screenshots/sign-in-notification.png)
![log in, log out display](documentation/feature_screenshots/sign-out-notification.png)

* A user friendly sign in form was used to make the user experience when signing in as simple as possible

![simple sign in form](documentation/feature_screenshots/sign-in.png)

* A user friendly registration form was used to make the user experience when registering as simple as possible

![simple registration form](documentation/feature_screenshots/registration-form.png)

* The author of the post will be displayed on the post itself

![post author displayed on post](documentation/feature_screenshots/post-author.png)

* The logout option displays for the user once they are successfully logged in

![log out option is displayed once a user logs in](documentation/feature_screenshots/logout-option-when-logged-in.png)


## <u>Blog Posts</u>

* The blog Posts are viewable from the main page and paginated to a new page once the number of posts hits 4 plus. The user can then click into the blog post to extend the post and read its contents. Each post is accompanied buy an appropriate picture hosted in Cloudinary.

* Users will have to register using a Username, email and password to leave, edit and delete a comment. The registration process is simple and user friendly incorporating Django AllAuth.

* Five total posts have been made to the Blog to present the pagination

* The space to the right of the Blog posts was intended for the user Polling/vote interactivity. I plan to write a simple polling/vote box containing the options for Next Months Director focus and the list of films for each director giving users the ability to vote on their faourite from that director.


## <u>Future Features</u>

* As previously noted the original scope of the project included a Polling option to allow users to poll/vote on next months director focus and to vote on the current directors best film. This option will bring more interactivity to the user base increasing engagement and fostering an atmosphere of unity among the club members. I planned to write two simple poll option boxes to the right of the Blog posts on the Home Page. The top box would contain a list of 4 potential directors to vote on for the upcoming director focus in which users will click the directors name and the count for that director would increase by that vote. The second box, placed underneath the first, will contain a list of the current directors movies allowng users to vote on their favourite film and that count would increase by one. At the end of each month a follow up blog would be created to discuss the polling/vote results and hopefully garner engagement among the members in the comments.

* The eventual goal for this project is to merge it with my portfolio project 1 and portfolio project 2 and create a viable club site with interactivity to promote engagement through the D15 Movie Lovers Quiz(PP2) and through the Blog posts, comments and polling from this project.

* I also plan to develop a club logo and replace the rudimentary D15 Movie Lovers heading on each of the PP1, PP2 and PP4 projects.

* Future ambitions include adding a link to a physical media store in which users can purchase Blu Ray, DVD or 4k UHD blu Rays of their favourite movies, potential discounting using the club profile. Also an option to add soundtracks, T-Shirts and other collectible, movie focused memorabilia.

* I plan to have the comment edits return the user to the original comment instead of back to the home page.

* I want to make the blog posts accessible when th euser clicks the movie poster aswell as the blog title.

* The only blog entry to contain an original blog post written by me is the blog entry titled 'Why Jaws the Revenge is better than you think'. The other Blog entries contain copy and pasted Wikipedia entries used solely due to time constraints. I will write personal blog entries for these posts that touch on my own feelings about the individual subjects which will generate talking points for the club members in the comments section. However, should you have the time to read the Jaws the Revenge blog, I hope you give it a rewatch.

* The about page will be styled more appropriately and will include a club picture/logo. As the page stands now was simply due to time constraints.

* The empty pace to the right of the home page will be used to display the voting options as previously noted


## <u>Wireframes</u>


* Home page desktop:

![Home page desktop](documentation/wireframes/homepage-desktop.png)

* Login page desktop:

![Login page desktop](documentation/wireframes/loginpage-desktop.png)

* Register page desktop:

![Register page desktop](documentation/wireframes/registerpage-desktop.png)

* About page desktop:

![About page desktop](documentation/wireframes/aboutpage-desktop.png)

* Home page tablet:

![Home page tablet](documentation/wireframes/homepage-tablet.png)

* Login page tablet

![Login page tablet](documentation/wireframes/loginpage-tablet.png)

* Register page tablet:

![Register page tablet](documentation/wireframes/registerpage-tablet.png)

* About page tablet:

![About page tablet](documentation/wireframes/aboutpage-tablet.png)

* Home page mobile:

![Home page mobile](documentation/wireframes/homepage-mobile.png)

* Login page mobile:

![Login page mobile](documentation/wireframes/loginpage-mobile.png)

* Register page mobile:

![Register page mobile](documentation/wireframes/registerpage-mobile.png)

* About page mobile:

![About page mobile](documentation/wireframes/aboutpage-mobile.png)

* Blog post page desktop:

![Blog post page desktop](documentation/wireframes/blogpost-desktop.png)

* Blog post page tablet:

![Blog post page tablet](documentation/wireframes/blogpost-tablet.png)

* Blog post page mobile:

![Blog post page mobile](documentation/wireframes/blogpost-mobile.png)

## <u>Differences between the Wireframes and finished blog</u>

* The poll option and vote option were not completed due to time constraints and have been noted for future implementation.

* The login and register pages were simplified. Instead on incasing the forms in a container I left them fee on the page. The view is elegant and simple.

* The club logo as seen on the About page is not yet designed. This has been noted for future implementation.

* I intended that a smaller blog appropriate image would display with the full blog post however a cropped portion now displays. This has been noted for a future fix.

* I planned to display a blog appropriate image on the mobile screen. However the responsive design works well in its current state sans image.

## <u>Design</u>

* The design focused on maintaining the look and feel of the previous D15 Movie Lovers projects (PP1 and PP2) using the same header, footer and body colours. The colour scheme, as per the previous D15 Movie Lovers projects is used to generate an emotional response to the typical muted colours associated with visiting the cinema or those nostalgic trips to the video store, walking the aisles to find your next rental, etc. The overall design is very simple to keep the screen minimalist and decluttered.

* A default image related to cinema was used as a fallback

* Sans-serif was used to keep the font simple and elegant

* I note the overall design may be considered too simple when compared to more contempory blog/club sites. My goal is to improve the design by incorporating a new club logo and refreshing the overall style.

## <u>Testing</u>
* Goal
* Action
* Expected Outcome
* Actual Outcome
* Test passed

## <u>Known Bugs</u>

* The create comment submission view returns to the Post Detail page without clearing the form request. As a result if the user hits refresh the form will be resubmitted and the same comment will be created again. This is a future fix.

* The comment image populates a cut off portion of the main post image. This will be redesigned in a future update to display a more complete image.

## <u>Technologies Used</u>

* HTML5
* CSS
* Bootstrap
* Python
* Django
* Allauth - within Django framework
* Crispy Forms - within Django framework
* gunicorn - within Django framework
* Summernotes - within Django framework
* Cloudinary
* Heroku postgres
* Gitpod
* Github
* fontawesome
* Balsamiq - Wireframes
* W3C Validation
* W3C CSS Validation
* PEP8 validation

## <u>Credits</u>
* I heavily relied on the course content walkthrough project for the Code Star blog presented by Matt Rudge. The entire project was built using the guidance of Matts course content in particular the bootsrap application and some CSS to make the site responsive. My sincere thanks to Matt and his content as without it I dont think I would've completed this project.