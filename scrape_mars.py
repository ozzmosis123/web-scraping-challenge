# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import time
timeout = 4

def init_browser():
    executable_path = {'executable_path': 'C:/Users/Ozzmo/Downloads/chromedriver_win32/chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(timeout)

    # Empty dictionary for all scraped data
    scraped_dict = {}

    # Get the news title
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    title_slide = soup.find('li', class_='slide')

    news_title = title_slide.find('div', class_='content_title').text
    

    # Get the news headline
    headline = title_slide.find('div', class_='article_teaser_body').text
    
    # create a dictionary to append to scrap dictionary at end of function
    news_dict = {'headline': headline, 'title': news_title}

    # Nasa Space images website
    url_2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_2)

    # Grab the latest full size mars image
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    images = soup.find_all('a', class_='button fancybox')
    for image in images:
        href = image.get('data-link')
        href = 'https://www.jpl.nasa.gov' + href
    
    browser.visit(href)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    main_image = soup.find_all('img', class_='main_image')
    for image in main_image:
        src = image.get('src')
        featured_image_url = 'https://www.jpl.nasa.gov' + src
        print(featured_image_url)

    featured_image_url = {'featured_image': featured_image_url}

    # Get the latest Mars weather from Twitter
    url_3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_3)
    time.sleep(timeout)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # weather data is under the article tag
    all_tweets = soup.find_all('article')

    # loop through the span tags to get the 5th span tag which holds the weather text
    for tweet in all_tweets:
        message = tweet.find_all('span')
        if 'InSight' in message[4].text:
            mars_weather = message[4].text
            

    print(mars_weather)
    weather = {'mars_weather': mars_weather}

    # Scrape the table facts from the Mars Facts webpage
    import pandas as pd
    url = "https://space-facts.com/mars/"
    mars_facts = pd.read_html(url)
    mars_facts = mars_facts[0]
    mars_facts.set_index(0, inplace=True)
    
    # Turn table to HTML
    mars_facts = mars_facts.to_html()

    facts = {'mars_facts' : mars_facts}

    
    # The astrogeology site used to obtain 4 images of Mar's Hemispheres
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # The Python list to store the 4 dictionaries of the image urls
    hemisphere_image_urls = []

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    soup.find('div', class_='description')

    # Clicking to new page
    browser.click_link_by_partial_text('Hemisphere Enhanced')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars = soup.find('div', class_='downloads')
    image_url = mars.find('a', {'href': True})
    image_url = image_url.get('href')

    # Appending to dictionary and add to list of dictionaries
    cerberus_dict = {'title': 'Cerberus Hemisphere', 'img_url': image_url}
    hemisphere_image_urls.append(cerberus_dict)

    # 2nd IMAGE
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    soup.find('div', class_='description')

    # Clicking to the next page
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars = soup.find('div', class_='downloads')
    image_url = mars.find('a', {'href': True})
    image_url = image_url.get('href')

    # Appending to dictionary and add to list of dictionaries
    schiaparrelli_dict = {'title': 'Schiaparelli Hemisphere', 'img_url': image_url}
    hemisphere_image_urls.append(schiaparrelli_dict)

    # 3rd IMAGE
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    soup.find('div', class_='description')

    # Clicking to new page
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars = soup.find('div', class_='downloads')
    image_url = mars.find('a', {'href': True})
    image_url = image_url.get('href')

    # Appending to dictionary and add to list of dictionaries
    syrtis_major_dict = {'title': 'Syrtis Major Hemisphere', 'img_url': image_url}
    hemisphere_image_urls.append(syrtis_major_dict)

    # 4th IMAGE
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    soup.find('div', class_='description')

    # Clicking to new page
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars = soup.find('div', class_='downloads')
    image_url = mars.find('a', {'href': True})
    image_url = image_url.get('href')

    # Appending to dictionary and add to list of dictionaries
    valles_marineris_dict = {'title': 'Valles Marineris Hemisphere', 'img_url': image_url}
    hemisphere_image_urls.append(valles_marineris_dict)


   
    # Gathering all the dictionaries into one final dictinary of all scraped data
    scraped_dict = {'news' : news_dict,
                    'featured_image_url' : featured_image_url,
                    'mars_weather' : weather,
                    'mars_facts' : facts,
                    'hemisphere_image_urls' : hemisphere_image_urls}




    browser.quit()

    return scraped_dict