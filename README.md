###A simple Scrapy Crawler to fetch all content from listed URLs + Pagination using python urljoin

#### To Run From Root
>> scrapy crawl manual
>> 
>> or
>> 
>> scrapy crawl manual -s CLOSESPIDER_ITEMCOUNT=90 #to Limit Crawler
>> 
>> 
>> or
>> 
>> scrapy crawl manual -o manual.json #to export data to json


Sample Scraped Data of First Link 

`[
{"title": ["lancaster fast westfields"], "price": [852.39], "description": ["elephant follow boasting all perfect send corner\r\nwhole coming borough broadband walk ready months near present\r\ncurrently move sociable king length"], "image_urls": ["http://scrapybook.s3.amazonaws.com/images/i13.jpg"], "url": ["http://scrapybook.s3.amazonaws.com/properties/property_000011.html"], "project": ["properties"], "spider": ["manual"], "server": ["Rahuls-MacBook-Pro.local"], "date": ["2017-02-16 12:12:51"]},
]`

This Crawler is Inspired by 

**Learning Scrapy Book From Dimitrios Kouzis-Loukas** 

**@CH03** Named **Properties**.

**Buy Book** From [www.packtpub.com](https://www.packtpub.com/big-data-and-business-intelligence/learning-scrapy)