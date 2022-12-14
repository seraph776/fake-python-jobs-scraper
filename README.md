<div id="top" align="center">
  
# Fake Python Jobs Scraper

  _Show your support and give this repo a_ ⭐



![made-with-Python](https://img.shields.io/badge/Python-blue?&logo=python&logoColor=yellow&label=Built%20with&style=flat&labelColor=black)
![GitHub](https://img.shields.io/github/license/seraph776/seraph776?color=green&style=flat&labelColor=black&label=License)
[![Contribute](https://img.shields.io/badge/Contribute-black?&logo=github&logoColor=black&label=&flat&labelColor=yellow)](https://github.com/seraph776/QuickStartTemplate/blob/main/contributing.md) [![Report Bugs](https://img.shields.io/badge/Report%20Bugz-black?&logo=github&logoColor=black&label=&flat&labelColor=red)](https://github.com/seraph776/QuickStartTemplate/issues/new/choose)


<img src="https://user-images.githubusercontent.com/72005563/193153931-1d4aec4f-f7ab-4b30-95fb-635ca3e7333c.png" width=250>


_Eat, Sleep, Code, Repeat!_ - Sun Tzu

</div>  


## ℹ️ About this Repo



**_Web Scraping_** is the art of extracting and parsing data from websites in an automated fashion using a computer program. 
This repo will teach you how to build a web scraper using Python Scrapy that will collect and store data from https://realpython.github.io/fake-jobs/




- **Objective**: The objective for this scraping system is to scrape job details from our target site.
- **Target Data**: We want to store the essential job detail information (`post_date`, `job_name`, `company`, `location`, and `apply_link`)
- **Scale**: This will be a small scale scraping project, so no need to design a more sophisticated infrastructure.
- **Data Storage**: To keep things simple for the example we will store to `CSV` and `JSON` file, and `SQLite3` database.


## Screenshots

First 10 records.

![image](https://user-images.githubusercontent.com/72005563/207714195-3b01d55d-6281-4ac8-8171-f10371513d70.png)


## Project Requirements

This project was built using the `Python 3.10.1` and the following modules: 

| Required                 | Version | Purpose                                        |
|--------------------------|:-------:|------------------------------------------------|
| `Scrapy `                |  2.6.3  | A web-crawling framework.                      | 
| `sqlite3`                |    _    | Lightweight database for storing results.      | 
| `csv`                    |    _    | Reads and writes tabular data in CSV format.   | 
| `json`                   |    _    | Simple JSON decoder.                           | 




## Setup Instructions

Instructions on how to create a `pipenv` virtual environment.

<details>

<summary>⚙️  Click to View </summary>

1. Download [zip file](https://github.com/seraph776/fake-python-jobs-scraper/archive/refs/heads/main.zip) 
2. Extract zip files
3. Change directory into projectFolder:

```python
>>> cd projectFolder
```

4. Install from Pipfile:

```python
>>> pipenv install  
```

5. Activate virtual environment

```python
>>> pipenv shell
```

6. CD into project app directory

```python
>>> cd projectName/projectName
```


</details>


## Usage



```python
>>> scrapy crawl jobs -o output.csv
```




##  Project Walk Through

<details>
<summary> 📚 Click to View </summary>
  

Here are instructions on how to duplicate this project.

#### STEP 1: Create Project folder and Install Scrapy 

```commandline
>>> mkdir FakePythonJobs
>>> cd FakePythonJobs
>>> pipenv install scrapy
```
#### STEP 2: Create Scrapy Project 
```commandline
>>> scrapy startproject FakePythonJobs
>>> cd FakePythonJobs
```
#### STEP 3: Create Scrapy Spider 

```commandline
>>> scrapy genspider jobs
```
#### STEP 4: Modify Jobs Spider

```python
# jobs.py

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    start_urls = ['https://realpython.github.io/fake-jobs/']

    def parse(self, response):
        jobs = response.xpath('//div[@class="card"]')
        for job in jobs:          
            job_name = job.xpath('//h2/text()').get()
            company = job.xpath('//h3/text()').get()
            location = job.xpath('//p[@class="location"]/text()').get()
            date_posted = job.xpath('//time/text()').get()
            apply_link = job.xpath('//footer//a[2]/@href').get()
            yield {
                'job_name': job_name,
                'company': company,
                'location': location,
                'date_posted': date_posted,
                'apply_link': apply_link
            }
```
#### STEP 5: Create Custom Item and, ItemLoader

```python
# items.py

import scrapy
from scrapy.loader import Item, ItemLoader
from itemloaders.processors import TakeFirst, MapCompose

class FakePythonjobsItem(Item):
    # define the fields for your item here like:
    job_name = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    date_posted = scrapy.Field()
    apply_link = scrapy.Field()


class FakePythonjobsItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    job_name_in = MapCompose(str.strip)
    company_in = MapCompose(str.strip)
    location_in = MapCompose(str.strip)
    date_posted_in = MapCompose(str.strip)
    apply_link_in = MapCompose(str.strip)
```
#### STEP 6: Modify Jobs Spider... again

```python
# jobs.py

import scrapy
from ..items import FakePythonjobsItem, FakePythonjobsItemLoader


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    start_urls = ['https://realpython.github.io/fake-jobs/']

    def parse(self, response):
        jobs = response.xpath('//div[@class="card"]')
        for job in jobs:
            fake_job_item = FakePythonjobsItemLoader(item=FakePythonjobsItem(), 
                                                     selector=job)
            fake_job_item.add_xpath('job_name', '//h2/text()')
            fake_job_item.add_xpath('company', '//h3/text()')
            fake_job_item.add_xpath('location', '//p[@class="location"]/text()')
            fake_job_item.add_xpath('date_posted', '//time/text()')
            fake_job_item.add_xpath('apply_link', '//footer//a[2]/@href')

            yield fake_job_item.load_item()
```
#### STEP 7: Create SQLite DataBase Pipeline

```python
# pipelines.py

import sqlite3


class SQLiteDatabasePipeline:

    def __init__(self):
        self.conn = sqlite3.connect('jobs.db')
        self.curr = self.conn.cursor()
        self.create_table()

    def create_table(self):
        SQL = """CREATE TABLE IF NOT EXISTS jobs_tb(
                    date_posted TEXT,
                    job_name TEXT,
                    company TEXT,
                    location TEXT,                    
                    apply_link TEXT        
        )"""
        self.curr.execute(SQL)

    def store_db(self, item):
        SQL = """INSERT INTO jobs_tb VALUES (?,?,?,?,?)"""
        self.curr.execute(SQL, (item['date_posted'],
                                item['job_name'],
                                item['company'],
                                item['location'],
                                item['apply_link']))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
```
#### STEP 8: Activate SQLite DataBase Pipeline
```python
# settings.py

ITEM_PIPELINES = {
   'FakePythonJobs.pipelines.SQLiteDatabasePipeline': 300,
}
```

#### STEP 9: Run Spider

```commandline
>>> scrapy crawl jobs -o jobs.csv -o jobs.json
```


</details>



## How to Contribute


Contributions are Welcome! For instructions on how to contribute please read our [Contributing Guidelines](https://github.com/seraph776/fake-python-jobs-scraper/blob/main/CONTRIBUTING.md). 


## Discussions

Have any Questions? Visit [Discussions](https://github.com/seraph776/fake-python-jobs-scraper/discussions) which is a space for our community to have conversations, ask questions and post answers without opening issues. Please read our [Code of Conduct](https://github.com/seraph776/webscrape_template/blob/main/CODE-OF-CONDUCT.md) which defines the  standards for engaging with the community!


## Feedback / Questions?

If you have any feedback or questions please contact me at [seraph776@gmail.com](mailto:seraph776@gmail.com)



## Donate


<details>
<summary> Support my work </summary>


All donations help fund the continued development of new content.


| Coin                                                                                                                        | Address                                                     |
|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <img src="https://user-images.githubusercontent.com/72005563/206338569-a607c171-5dfe-47c4-abed-a7e3beeab5bf.png" width=150> | 3GhUQkT7jJcfu6xuqrAh8E9PR5hwQhTXsC                          |
| <img src="https://user-images.githubusercontent.com/72005563/206338723-44e6f026-01fd-41dd-ab31-0c184c78a896.png" width=150> | 0x6fA9A81b7e6373Ca5C55A265dFeAa0d438c91D81                  |
| <img src="https://user-images.githubusercontent.com/72005563/206338886-1a07e215-0664-472a-a2a9-2a6d4e38b694.png" width=150> | 0x9a5C640a853B8E759111A28C4D43224a090E53d9                  |
| <img src="https://user-images.githubusercontent.com/72005563/206338998-9819976d-622a-462c-8d88-897a8d5880f4.png" width=150> | [Buy me a Coffee](https://www.buymeacoffee.com/codecrypt76) |       

</details>

## License 

All code in this repository is available under the [MIT License](https://github.com/seraph776/fake-python-jobs-scraper/blob/main/LICENSE) © [Seraph★776](https://github.com/seraph776)



<div align="right">

[[↑] Back to top](#top)

</div>  


