import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
    # First create lists of dictionaries containing the pages we want to add into each category
    # Then create dict of dicts for categories

    python_pages = [{'title': 'Official Python Tutorial',
                     'url':'http://docs.python.org/3/tutorial/',
                     'views': 1},
                    {'title':'How to Think like a Computer Scientist',
                     'url':'http://www.greenteapress.com/thinkpython/',
                     'views': 100},
                    {'title':'Learn Python in 10 Minutes',
                     'url':'http://www.korokithakis.net/tutorials/python/',
                     'views': 10} ]

    django_pages = [{'title':'Official Django Tutorial',
                     'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
                     'views': 5},
                    {'title':'Django Rocks',
                     'url':'http://www.djangorocks.com/',
                     'views': 3},
                    {'title':'How to Tango with Django',
                     'url':'http://www.tangowithdjango.com/',
                     'views': 9} ]

    other_pages = [{'title':'Bottle',
                    'url':'http://bottlepy.org/docs/dev/',
                     'views': 69},
                   {'title':'Flask',
                    'url':'http://flask.pocoo.org',
                    'views': 420} ]

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16} }


    # Iterate through the cats pages, add each category, and add all associated pages
    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views=p['views'])
                     

    # Print out added categories
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f"- {c}: {p}")


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c


# Start execution here
if __name__ == '__main__':
    print("Starting Rango population script")
    populate()
