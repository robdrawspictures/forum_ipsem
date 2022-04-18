# Forum Ipsem
### How To Run:
* dropdb
* createdb
* psql -d forum_ipsem -f forum_ipsem.sql
* python 3 console.py
* flask run
* psql -d forum_ipsem
* python3 app.py

---

### Overview
Welcome to my Python project. For reasons I can't quite recall, I decided to construct a forum. At time of writing the it contains the following functionality:
* Create accounts
* Create Threads
* Post to Threads
* Delete posts/threads
* Ban users (if Admin)
* Lock threads

Planned features I will probably never get around to:
* Pull random post text to replace the random quote generator on the homepage
* Tidy up CSS
* Have a static user selected that persists over all areas of the site, rather than having to select your user for each action
* More robust user pages (display all user posts, post count, bio etc)
