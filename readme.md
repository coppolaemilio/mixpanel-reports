# Mixpanel Reports
-----
## Config
When you run the `main.py` file you will be prompted with the Mixpanel's API Key and secret, if you don't want to keep typing this you can create a config.ini file:
```
[mixpanel]
api_key = yourapikeylongthingwithnumbersandletters
api_secret = yourapisecretlongthingwithnumbersandletters
```

## Downloading data
The function `get_data(event)` will download all the events related with the name of your `event` argument. Once downloaded this file will be located at `./data/file.json`