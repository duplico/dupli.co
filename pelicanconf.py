AUTHOR = 'george | duplico'
SITENAME = 'George Louthan | duplico'
SITEURL = ""
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'
THEME = "notmyidea"

PATH = "content"
STATIC_PATHS = [
    "images",
    "_meta",
]
EXTRA_PATH_METADATA = {
    "_meta/favicon.ico": {"path": "favicon.ico"},
}

PLUGINS = [
    "photos",
]

PHOTO_LIBRARY = "/home/george/project/dupli.co/photos"
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_THUMB = (192, 144, 60)
PHOTO_SQUARE_THUMB = True # Crop to square
PHOTO_RESIZE_JOBS = 0 # Try to detect CPU count and start CPU_COUNT+1 jobs
PHOTO_WATERMARK = True
PHOTO_WATERMARK_TEXT = "@dupli.co"
PHOTO_INLINE_GALLERY_ENABLED = True
PHOTO_INLINE_GALLERY_TEMPLATE = "inline_gallery"

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
    ("badge.lgbt", "https://badge.lgbt/"),
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
