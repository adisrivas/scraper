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
  ```python3 -m venv scraper```

- #### Activate (Linux/Mac)
  ```source scraper/bin/activate```

- #### Activate (Windows)
  ```scraper\Scripts\activate```


#### To run the spider:<br>

```scrapy crawl item -o output.json```
