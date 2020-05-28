# web-scraping-challenge

A Mars dashboard that updates to the latest planet Mars data from various websites. 

Uses Python Beautiful Soup to scrape data on Mars from various websites. All test code is done on the ipynb notebook file. 

Then the scrape.py file is created that contains all scrape data that was tested in the ipynb notebook.

An app is created called app.py used to create a NoSQL MongoDB database and collection to store latest data. There is also an app route in the app.py that calls a scrape function that is referenced in the index.html as a button that can be clicked to get an update on the latest Mars data. 

First run the app.py followed by the index.html
