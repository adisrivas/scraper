This project demonstrates a web scraper built using Scrapy.

### 1. Clone the repository
```
git clone https://github.com/adisrivas/scraper.git

cd scraper/
```

### 2. Create and activate a virtual environment
It’s best practice to isolate dependencies.

- #### Move into scraper
  ``` cd scraper/ ```

- #### Create venv
  ```python3 -m venv venv```

- #### Activate (Linux/Mac)
  ```source venv/bin/activate```

- #### Activate (Windows)
  ```venv\Scripts\activate```


#### To run the spider:<br>

```scrapy crawl item -o output.json```
