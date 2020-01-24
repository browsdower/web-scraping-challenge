from splinter import Browser
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd

#executable path for windows
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)

#url
url = "https://mars.nasa.gov/news/"
browser.visit(url)

#using bs to write it into html
html = browser.html
soup = bs(html,"html.parser")

#drill into title and paragraphs
news_title = soup.find("div",class_="content_title").text
news_para = soup.find("div", class_="article_teaser_body").text

print(news_title)
print(news_para)

# Parse HTML
html_image = browser.html
soup = bs(html_image, 'html.parser')

#find style tag 
featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

# url 
main_url = 'https://www.jpl.nasa.gov'

# combine all urls
featured_image_url = main_url + featured_image_url

# Display image
featured_image_url

# Visit Mars Weather Twitter
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)

url_weather = "https://twitter.com/marswxreport?lang=en"
browser.visit(url_weather)

#set up new parser up
html_weather = browser.html
soup = bs(html_weather, "html.parser")

# Find a weather tweet 
mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
print(mars_weather)

#Mars facts url 
mars_facts_url = 'http://space-facts.com/mars/'

#prepare df
mars_facts = pd.read_html(mars_facts_url)

#prepare facts to be entered into df
mars_df = mars_facts[0]

#create columns 
mars_df.columns = ['Item','Value']

# Set index
mars_df.set_index('Item', inplace=True)

# Save html to Assets
mars_df.to_html()

mars_df

#Visit hemispheres url 
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)

hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemispheres_url)

html_hemispheres = browser.html

# Parse HTML with bs
soup = bs(html_hemispheres, 'html.parser')

# Retreive items realated to hemispheres 
hemispheres = soup.find_all('div', class_='item')

# Create list for new urls 
hemisphere_image_urls = []

# Store the main_ul 
hemispheres_main_url = 'https://astrogeology.usgs.gov'

# Loop through the items
for h in hemispheres: 
    # Store title
    title = h.find('h3').text
    
    # Store link to image website
    partial_img_url = h.find('a', class_='itemLink product-item')['href']
    
    # go to link that contains the full image site 
    browser.visit(hemispheres_main_url + partial_img_url)
    
    # create object of individual hemisphere info 
    partial_img_html = browser.html
    
    # Parse HTML with bs
    soup = bs( partial_img_html, 'html.parser')
    
    #create image source 
    img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
    
    #append the information into dictionaries 
    hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
    

#show urls
hemisphere_image_urls

mars_data = {
     "News_Title": news_title,
     "Paragraph_Text": news_para,
     "Most_Recent_Mars_Image": featured_image_url,
     "Mars_Weather": mars_weather,
     "mars_h": hemisphere_image_urls
     }

print(mars_data)