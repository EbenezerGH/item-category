Udacity Full-Stack Nanodegree
Project 3 : Item Catalog
by Ebenezer Ackon

Overview

Project 3 is focused on the creation of an item catalog that incorporates CRUD operations and user authentication from a 3rd party provider, in this case GOOGLE.  To utilize this project completely you would need A google account and internet access.

The libraries used in this project consist of:
*SQLALCHEMY - Database work
*FLASK - Routing
*HTTPLIB - Json Calls
*JSON - Json Calls
*REQUESTS - Json Calls

We are not using a virtual machine, in order to run this project you must:

1) Download and extract Folder onto computer
2) Run main.py within terminal
3) Open up browser of your choice and navigate to http://LocalHost:8000
4) From this point on you should be on the main catalog page, explore and enjoy.

The only endpoints you should need is:
/
/category
/categories

~JSON~
/category/JSON
/category/<int:category_id>/menu/<int:menu_id>/JSON’-
/category/<int:category_id>/menu/JSON

Everything else is accessible through routing
Examples:
/login
/gconnect
/gdisconnect
/category/add
/category/<catid>/edit
/category/<catid>/delete
/category/<catid>/add
/category/<catid>/<menuid>/edit
/category/<catid>/<menuid>/delete