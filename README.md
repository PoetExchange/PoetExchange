PoetExchange
============

All web applications associated with the PoetExchange.com website.

--------------
ANNOUNCEMENTS
--------------
*11/20/12* Models are now in feature freeze. Please do not add new models, add new fields/methods to models, or add new parameters to model fields without approval from the entire development team. All development efforts should now be redirected toward the implementation of forms.
---------------------
GENERAL DEV GUIDELINES
--------------
These are some general guidelines which I thought would make our lives much easier when it comes to code collaboration. Feel free to add to the list if you think of more

Comment your code!
-----------------
- We aren't the only ones readig the code we write anymore. It's nice when we can look at each other's code and understand what the hell the author is attempting to do.
- It's going to make code maintenence 100x easier in 2, 3, 4 months when we can look at the code and actually remember why we wrote it
- Working in Django means most of the time, we know what the code is doing based purely on what file it's in. This mostly applies to any custom written code we end up including.
- Please include docstrings in any functions you write outside of views.py!

Please don't push broken code up to GitHub!
----------------------------------------------
- I don't care if you commit broken code to your local repository, but before you push your changes to GitHub, please make sure all the code you wrote is functioning.
- If you aren't sure what the difference between a push and a commit is, please look it up or ask me. It is a subtle, but important distinction.

Please use the GitHub repository page to report issues!
---------------------------------------------------------
- I know we meet 3 times/week, but the GitHub issues tracking is top notch stuff. Plus GitHub issues tracking is persistent. You DO want to be able to report an issue at any time on any day of the week, don't you?
- This applies more to things like bugs and technical problems than something like troubles understanding Django. For problems understanding python or the framework, refer to the documentation, google, or me (I don't promise I'll know the answer.. but I can certainly help find it).

We all hate to write Documentation. But we all need to do it.
---------------------------------------------------------------
- The GitHub repository also provides a wiki section
- We should use the wiki section to document each application we write for PoetExchange.
- Writing documentation blows, but it's going to make our website more maintainable, especially as it expands to include more features and more applications.

If you screw up the development Database, please fix it.
--------------------------------------------------------
- We're all sharing a sqlite database in the dev files folder.
- When you're developing, stuff happens, and things break.
- Don't use that as an excuse to leave them broken. 
- Try pulling down the old (non-screwed up) database if you can; if that doesn't work, delete the screwed up database and start with a fresh one.
- Remember to set the superuser name and password to 'admin'!

Please don't commit static files, media files, or custom styles!
-----------------------------------------------------------------------
- Remember that everything we put on GitHub is open sourced.
- It's all well and good if people want to use parts of our web applications, but we need to protect our branding!
- This means try to avoid commiting things like our banner, our logo, our thumbnails, or our css styles (at least until we formally decide to license them under the creative commons :p)
- Keep media & static files in a separate folder from the main project if you need to.

Remember, we on the same team, yo.
-------------------------------------
- When thinking minds come together to share ideas, disagreement is almost a given.
- Don't let silly disagreements blow up into something crazy. Writing code is torturous enough. We don't need to give each other hell on top of that.
- If you ever need help on a site component, feel free to lean on your fellow developers! We can brainstorm with you or help you crack problems!
- On the other side of that, if a fellow developer is struggling, be helpful. Don't be a dick.

Add guidelines!
-----------------
- We want to make sure we're all contributing to a healthy, productive working environment.
- If you think of guidelines for the group that will make our collaboration go more smoothly, add them to this list!
- This is a list of  guidelines. It's not the law. If one of our conventions isn't working, we'll get rid of it.
