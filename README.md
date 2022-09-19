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
- PLACEHOLDER FOR SCREENSHOTS
* The selected page will maintain the highlighted bar to inform the user
- PLACEHOLDER FOR SCREENSHOTS
* Navbar reduces to burger button to accomadate smaller screen sizes
- PLACEHOLDER FOR SCREENSHOTS
* Footer in place with links to social media
- PLACEHOLDER FOR SCREENSHOTS
* A total of 4 Blog Posts will be shown before pagination moves further Blog Posts to a new page
- PLACEHOLDER FOR SCREENSHOTS
* User is notified that their comment is submitted for authorisation
- PLACEHOLDER FOR SCREENSHOTS
* Once the comment has been submitted the User also has the option to edit the comment or delete the comment
- PLACEHOLDER FOR SCREENSHOTS

## <u>Blog Posts</u>

* The blog Posts are viewable from the main page and paginated to a new page once the number of posts hits 4 plus. The user can then click into the blog post to extend the post and read its contents. Each post is accompanied buy an appropriate picture hosted in Cloudinary.

* Users will have to register using a Username, email and password to leave, edit and delete a comment. The registration process is simple and user friendly incorporating Django AllAuth.

* Five total posts have been made to the Blog to present the pagination

* The space to the right of the Blog posts was intended for the user Polling/vote interactivity. I plan to write a simple polling/vote box containing the options for Next Months Director focus and the list of films for each director giving users the ability to vote on their faourite from that director.


## <u>Future Features</u>

* As previously noted the original scope of the project included a Polling option to allow users to poll/vote on next months director focus and to vote on the current directors best film. This option will bring more interactivity to the user base increasing engagement and fostering an atmosphere of unity among the club members. I planned to write two simple poll option boxes to the right of the Blog posts on the Home Page. The top box would contain a list of 4 potential directors to vote on for the upcoming director focus in which users will click the directors name and the count for that director would increase by that vote. The second box, placed underneath the first, will contain a list of the current directors movies allowng users to vote on their favourite film and that count would increase by one. At the end of each month a follow up blog would be created to discuss the polling/vote results and hopefully garner engagement among the members in the comments.

* The eventual goal for this project is to merge it with my portfolio project 1 and portfolio project 2 and create a viable club site with interactivity to promote engagement through the D15 MOvile Lovers Quiz(PP2) and through the Blog posts, comments and polling from this project.

* I also plan to develop a club logo and replace the rudimentary D15 Movie Lovers heading on each of the PP1, PP2 and PP4 projects.

* Future ambitions include adding a link to a physical media store in which users can purchase Blu Ray, DVD or 4k UHD blu Rays of their favourite movies, discounted using the club profile. ALso an option to add soundtracks, T-Shirts and other collectible, movie focused memorabilia

* I plan to have the comment edits return the user to the original comment instead of back to the home page


## <u>Wireframes</u>

- PLACEHOLDER FOR SCREENSHOTS

## <u>Data Models</u>

- PLACEHOLDER FOR SCREENSHOTS

## <u>Design</u>

* The design focused on maintaining the look and feel of the previous D15 Movie Lover projects (PP1 and PP2) using the same header, footer and body colours. The colour scheme, as per the previous D15 Movie Lovers projects is used to generate an emotional response to the typical muted colours associated with visiting the cinema or those nostalgic trips to the video store, walking the aisles to find your next rental, etc. The overall design is very simple to keep the screen minimalist and decluttered.

* A default image related to cinema was used as a fallback

* Sans-serif was used to keep the font simple and elegant

* I note the overall design may be considered too simple when compared to more contempory blog/club sites. My goal is to improve the design by incorporating a new club logo and refreshing the overall style.

## <u>Known Bugs</u>

* The create comment submission view returns to the Post Detail page without clearing the form request. As a result if the user hits refresh the form will be resubmitted and the same comment will be created again. This is a future fix.

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
* I heavily relied on the course content walkthrough project for the Code Star blog presented by Matt Rudge. The entire project was built using the guidance of Matts course content in particular the bootsrap application to make the site responsive. My sincere thanks to Matt and his content as without it I dont think I would've completed this project.