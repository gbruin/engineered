EngineeredComic
===============

A simple Django project with comics app to upload and serve webcomics.
It was written to cater to Robin's engineered webcomic (currently being
served at http://engineered.trianglebruins.com/).

The templates for the project are located under `templates/comics/` folder.

RSS feeds generation (simple) is supported. 

To view an individual comics strip, the URL `/<id>/` is used, where `<id>`
is the unique ID of a strip.
The URL `/random/` picks an existing strip at random.
The URL `/archive/` lists all existing strips as a list of linked titles.

To set up a development environment:

1.  Sync database (default settings use an sqlite3 flat file).

    ``$ ./manage.py syncdb``

2.  Add some sample data by navigating to the admin interface
    (http://localhost:8000/admin/) and select the "Strips" panel.
3.  Latest comics strip should now be able to be served from its URL root
    (http://loaclhost:8000/).

To deploy, change the media root and URL in project settings. Then, copy or
symlink everything under `comics/media/` to media root. Uploaded strips will
be stored in `comics/media/strips/` folder. Also, set up a different
database and sync the models before use.
