USER: Generate the contents of the file: /aws-amplify-scrapy-app/aws-amplify-scrapy-app/src/scraper/settings.py 

CONTENTS:
BOT_NAME = 'aws_amplify_scrapy_app'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

USER_AGENT = 'aws_amplify_scrapy_app (+http://www.yourdomain.com)'

ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 1

ITEM_PIPELINES = {
    'scraper.pipelines.YourPipeline': 300,
}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See autothrottle settings and docs
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Enable HTTP caching (default: False)
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'