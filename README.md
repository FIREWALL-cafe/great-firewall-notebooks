## Setup

If you want to run these notebooks, you'll need to set up some credentials with [Google Cloud Translation](https://cloud.google.com/translate/docs/quickstarts) and you'll need to download the appropriate [Chrome webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for your version of Chrome.

Install these packages at a minimum:
 - Jupyter Notebooks (or the Anaconda stack)
 - Selenium
 - Google Cloud Translate
 - ipyplot

## Prototyping a scraper

[1_requests-google-baidu](https://nbviewer.jupyter.org/github/FIREWALL-cafe/great-firewall-notebooks/blob/master/1_requests-google-baidu.ipynb). Reverse-engineering search results.

[2_using-google-cloud-translation](https://nbviewer.jupyter.org/github/FIREWALL-cafe/great-firewall-notebooks/blob/master/2_using-google-cloud-translation.ipynb). Getting some basic automatic translation with Google Translate.

[3_compare-languages-Google](https://nbviewer.jupyter.org/github/FIREWALL-cafe/great-firewall-notebooks/blob/master/3_compare-languages-Google.ipynb). Comparing what search results look like in different languages on Google.

[4_compare-languages-Baidu](https://nbviewer.jupyter.org/github/FIREWALL-cafe/great-firewall-notebooks/blob/master/4_compare-languages-Baidu.ipynb). Comparing what search results look like in different languages on Baidu.

[5_querying-many-sensitive-words-archive](https://nbviewer.jupyter.org/github/FIREWALL-cafe/great-firewall-notebooks/blob/master/5_querying-many-sensitive-words-archive.ipynb). Testing rate limits to see if Google or Baidu have automatic ban-hammers at a certain rate.

## API integration

[6_firewall-api](https://nbviewer.jupyter.org/github/FIREWALL-cafe/great-firewall-notebooks/blob/master/6_firewall-api.ipynb). Testing Firewall Cafe API endpoints and demonstrating their use.

[7_firewall-babelfish](https://nbviewer.jupyter.org/github/FIREWALL-cafe/great-firewall-notebooks/blob/master/7_firewall-babelfish.ipynb). Demonstrating how to use the Babelfish translate API (if you have a key).

[8_image-hashing](https://nbviewer.jupyter.org/github/FIREWALL-cafe/great-firewall-notebooks/blob/master/8_image-hashing.ipynb). Testing different image hashing algorithms.

[9_wordpress-node-APIs](https://nbviewer.jupyter.org/github/FIREWALL-cafe/great-firewall-notebooks/blob/master/9_wordpress-node-APIs.ipynb). Looking at similarities between the old and new Firewall Cafe APIs.

## Migrations

[10_transfer-images-http](https://nbviewer.jupyter.org/github/FIREWALL-cafe/great-firewall-notebooks/blob/master/10_transfer-images-http.ipynb). A first attempt at getting 10k images from one place to another.

[11_extract-images-postgres-dump](https://nbviewer.jupyter.org/github/FIREWALL-cafe/great-firewall-notebooks/blob/master/11_extract-images-postgres-dump.ipynb). Extracting images from a postgresql dump; never got it working.

## Data integrity checks

[12_data-integrity](https://nbviewer.jupyter.org/github/FIREWALL-cafe/great-firewall-notebooks/blob/master/12_data-integrity.ipynb). Checking that search results are getting entered correctly into the API, and returning as expected when we ask for them.

[13_clean-up-searches-API](https://nbviewer.jupyter.org/github/FIREWALL-cafe/great-firewall-notebooks/blob/master/13_clean-up-searches-API.ipynb). Delete searches that incorrectly stored way too many images.

[14_wordpress-and-db-check](https://nbviewer.jupyter.org/github/FIREWALL-cafe/great-firewall-notebooks/blob/master/14_wordpress-and-db-check.ipynb). Take a closer look at Wordpress API vs new API to see if there are discrepencies in image results (they all seem to match).
