<div id="top" align="center">
  
# Web Scraping Template

  _Show your support and give this repo a_ ⭐



![made-with-Python](https://img.shields.io/badge/Python-blue?&logo=python&logoColor=yellow&label=Built%20with&style=flat&labelColor=black)
![GitHub](https://img.shields.io/github/license/seraph776/seraph776?color=green&style=flat&labelColor=black&label=License)
[![Contribute](https://img.shields.io/badge/Contribute-black?&logo=github&logoColor=black&label=&flat&labelColor=yellow)](https://github.com/seraph776/QuickStartTemplate/blob/main/contributing.md) [![Report Bugs](https://img.shields.io/badge/Report%20Bugz-black?&logo=github&logoColor=black&label=&flat&labelColor=red)](https://github.com/seraph776/QuickStartTemplate/issues/new/choose)


<img src="https://user-images.githubusercontent.com/72005563/193153931-1d4aec4f-f7ab-4b30-95fb-635ca3e7333c.png" width=250>


_Eat, Sleep, Code, Repeat!_ - Sun Tzu

</div>  


## ℹ️ About this Repo



**_Web Scraping_** is the art of extracting and parsing data from websites in an automated fashion using a computer program. 
This repo will teach you how to build a web scraper using Python Scrapy that will collect and store data from https://example.com




- **Objective**: The objective for this scraping system is to monitor product rankings for our target keywords and monitor the individual products every day.
- **Target Data**: We want to store the product rankings for each keyword and the essential product data (price, reviews, etc.)
- **Scale**: This will be a relatively small scale scraping process (handful of keywords), so no need to design a more sophisticated infrastructure.
- **Data Storage**: We will store the data to a `CSV` file, and to `SQLite3` database.


## Screenshots

![image](https://user-images.githubusercontent.com/72005563/181623334-d74b5712-2709-4ccb-925b-f82cab72d8e1.png)
![image](https://user-images.githubusercontent.com/72005563/181623334-d74b5712-2709-4ccb-925b-f82cab72d8e1.png)



## Project Requirements

This project was built using the `Python 3.10.1` and the following modules: 

| Required                 | Version | Purpose                                        |
|--------------------------|:-------:|------------------------------------------------|
| `Scrapy `                |  2.6.3  | A web-crawling framework.                      | 
| `beautifulsoup4`         |  4.9 3  | HTML/XMl processing library.                   | 
| `requests`               |  2.7.0  | A simple, yet elegant, HTTP library.           | 
| `request-html`           | 0.10.0  | HTTP library, and HTML/XMl processing library. | 
| `mysql-connector-python` | 8.0.31  | MySQL driver written in Python                 | 
| `openpyxl`               | 3.0.10  | Reads and writes Excel 2010 files              | 
| `sqlite3`                |    _    | Lightweight database for storing results.      | 
| `csv`                    |    _    | Reads and writes tabular data in CSV format.   | 
| `json`                   |    _    | Simple JSON decoder.                           | 




## Setup Instructions

Instructions on how to create a `pipenv` virtual environment.

<details>

<summary>⚙️  Click to View </summary>

1. Download [zip file](https://github.com/seraph776/webscrape_template/archive/refs/heads/main.zip) 
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
>>> scrapy crawl spidername -o output.csv
```


For more information read [documentation](https://github.com/seraph776/QuickStartTemplate).



## Project Walk Through

<details>
<summary> 📚 Click to View </summary>
  
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
</details>



## How to Contribute


Contributions are Welcome! For instructions on how to contribute please read our [Contributing Guidelines](https://github.com/seraph776/webscrape_template/blob/main/CONTRIBUTING.md). 


## Discussions

Have any Questions? Visit [Discussions](https://github.com/seraph776/webscrape_template/discussions) which is a space for our community to have conversations, ask questions and post answers without opening issues. Please read our [Code of Conduct](https://github.com/seraph776/webscrape_template/blob/main/CODE-OF-CONDUCT.md) which defines the  standards for engaging with the community!


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

All code in this repository is available under the [MIT License](https://github.com/seraph776/webscrape_template/blob/main/LICENSE) © [Seraph★776](https://github.com/seraph776)



<div align="right">

[[↑] Back to top](#top)

</div>  


