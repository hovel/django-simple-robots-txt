Installation
============

`django-simple-robots-txt` requires `django-solo`.

Add this into INSTALLED_APPS:

    INSTALLED_APPS = (
        ....
        'solo',
        'simple_robots_txt',
    )

Add this into urls.py:

    url(r'^robots\.txt$', 'simple_robots_txt.views.robots_txt', name='robots_txt'),

Enjoy.
