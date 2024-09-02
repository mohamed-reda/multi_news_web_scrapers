# Multi News Web Scrapers (Yahoo, CNN, Associated Press)

## Overview

This repository contains web scrapers designed to extract news articles from three major sources: **Yahoo News**, **CNN
**, and the **Associated Press**. Built using the **Scrapy** framework, these spiders crawl news websites and collect
essential data such as article titles, descriptions, publication dates, authors, and full article texts.

## Projects

### 1. CNN Spider

- **Target website**: [CNN News](https://edition.cnn.com/)
- **Purpose**: Scrapes news articles from CNN's dynamically loaded pages.
- **Extracted fields**:
    - URL
    - Title
    - Description
    - Publication Date
    - Author
    - Article Text

### 2. apnews Spider

- **Target website**: [apnews News](https://apnews.com/)
- **Purpose**: Collects news articles from AP's website using JSON-structured data.
- **Extracted fields**:
    - URL
    - Title
    - Description
    - Publication Date
    - Author
    - Article Text

### 3. Yahoo Spider

- **Target website**: [Yahoo News](https://news.yahoo.com/)
- **Purpose**: Extracts news articles from Yahoo News, using structured JSON data.
- **Extracted fields**:
    - URL
    - Title
    - Description
    - Publication Date
    - Author
    - Article Text

## Requirements

- Python 3.x
- Scrapy framework

## Installation

1. Clone this repository.
2. Install the required dependencies with `pip install -r requirements.txt`.

## Usage

1. Run the spiders individually from the command line using the Scrapy command.
2. Each spider saves the extracted data in the specified format (e.g., JSON, CSV).

## Scrapy Command Line Fundamentals - README

### **Run a Project:**

   ```bash
   scrapy runspider <project_name>
   ```

### **Extract Data:**

   ```bash
   scrapy runspider cnn.py -o articles.csv -t csv -s CLOSESPIDER_PAGECOUNT=10

   ```

------------

## Here are some key points about Scrapy:

Scrapy is built on top of other libraries such as curl and select, which makes it a good choice for web scraping tasks.
Scrapy provides a flexible and efficient way to extract data from websites.
Scrapy has a lot of built-in features that make it a good choice for web scraping tasks.
Scrapy can be used for a variety of web scraping tasks, including extracting data from websites and storing it in
formats such as Json or CSV.
Scrapy is a good choice for beginners and professionals alike, as it provides a lot of built-in features and is easy to
use.
Scrapy can be used in conjunction with other libraries such as Scrape and playwright to provide a more comprehensive web
scraping solution.