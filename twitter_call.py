from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_1iY9IFnf6GSNO0SRqXZghRKxk700ET2va3YS")

# Prepare the actor input
run_input = {
    "searchTerms": [
    "formula 1",
    "BahrainGP",
    "F1",
    "f1",
    "FORMULA1"
  ], #Finds these terms in Hashtags, usernames, tweet bodies, 
    "searchMode": "",
    "mode": "replies",
    "tweetsDesired": 1000,
    "proxyConfig": { "useApifyProxy": True },
    "extendOutputFunction": """async ({ data, item, page, request, customData, Apify }) => {
  return item;
}""",
    "extendScraperFunction": """async ({ page, request, addSearch, addProfile, _, addThread, addEvent, customData, Apify, signal, label }) => {
 
}""",
    "customData": {},
    "handlePageTimeoutSecs": 5000,
    "maxRequestRetries": 3,
    "maxIdleTimeoutSecs": 30,
    "initialCookies": [],
}

# Run the actor and wait for it to finish
run = client.actor("vdrmota/twitter-scraper").call(run_input=run_input)

# Fetch and print actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)