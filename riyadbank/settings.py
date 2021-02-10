BOT_NAME = 'riyadbank'
SPIDER_MODULES = ['riyadbank.spiders']
NEWSPIDER_MODULE = 'riyadbank.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
ITEM_PIPELINES = {
   'riyadbank.pipelines.DatabasePipeline': 300,
}
