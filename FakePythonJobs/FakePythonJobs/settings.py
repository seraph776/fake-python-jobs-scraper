BOT_NAME = 'FakePythonJobs'

SPIDER_MODULES = ['FakePythonJobs.spiders']
NEWSPIDER_MODULE = 'FakePythonJobs.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'FakePythonJobs.pipelines.SQLiteDatabasePipeline': 300,
}

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
