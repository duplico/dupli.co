AUTHOR = 'george | duplico'
SITENAME = 'George Louthan | duplico'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

STATIC_PATHS = [
    "images",
    "_meta",
]

EXTRA_PATH_METADATA = {
    "_meta/favicon.ico": {"path": "favicon.ico"},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Starlight Concerts", "https://www.starlightconcerts.org/"),
    ("Southwest CCDC", "https://www.southwestccdc.com/"),
    ("Queercon", "https://queercon.org/"),
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("Bluesky", "https://bsky.app/profile/dupli.co"),
    ("Instagram", "https://www.instagram.com/louthage"),
    ("GitHub", "https://github.com/duplico"),
    ("LinkedIn", "https://www.linkedin.com/in/georgelouthan/"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
