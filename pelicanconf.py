AUTHOR = 'Cyberwildcats'
SITENAME = 'Cyberwildcats'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
FEED_MAX_ITEMS = 10
# Enable RSS feed generation
FEED_ALL_RSS = 'feeds/all.rss.xml'  # Generates a site-wide RSS feed
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'  # Generates category-specific RSS feeds
# Optional: Limit the number of items in the RSS feed
FEED_MAX_ITEMS = 10
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = "atom.xml"
#AUTHOR_FEED_RSS = None
THEME = "/Users/earnoth/src/cyberwildcats/pelican-themes/bootstrap2-dark"

# Links
LINKS = (('Cyberwildcats Calendar', 'https://calendar.google.com/calendar/embed?src=cyberwildcats%40gmail.com&ctz=America%2FNew_York'),
         ('Proxmox (needs VPN)', 'https://10.1.11.33:8006'),
         ('Cyberwildcats Github', 'https://github.com/Cyberwildcats'),
         ('Google Drive', 'https://drive.google.com/drive/folders/1bBJfnMvM-af_80J7JxpGMyXZ602dkWER'))

# Social widget
SOCIAL = (('Cyberwildcats Slack', 'https://cyberwildcats.slack.com'),
          ('Cyberwildcats Google Group', 'https://groups.google.com/g/cyberwildcats'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True