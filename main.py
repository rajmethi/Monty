from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from item import Item
from time import sleep
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from db import insert_item_into_sqlite, get_all_items_from_sqlite
from analysis import compute_brand_frequency, compute_average_price, compute_average_discount, compute_position_to_likes_per_hour_ratio
def createItem(browser, anchor_href, trending_position):
    print("inside createItem")
    try:
        price = browser.find_element(By.XPATH, "//div[contains(@class, 'Price_large')]/span[contains(@class, 'Money_root')]").text
        price = int(price[1:])
    except Exception as e:
        price = 0
    
    brands = []
    brand_spans = browser.find_elements(By.XPATH, "//a[contains(@class, 'Designers_designer')]")
    
    for brand in brand_spans:
        print(brand.text)
        brands.append(brand.text)
        
    title = browser.find_element(By.XPATH, "//h1[contains(@class, 'Details_title')]").text  
    discount_percent = 0
    try:
        discount = browser.find_element(By.XPATH, "//span[contains(@class, 'percentOff')]")
        discount = discount.split(" ")[0][:-1]
    except Exception as e:
        discount = None
        
    if discount:
        discount_percent = discount.text
        
    
    dating_spans = browser.find_elements(By.XPATH, "//div[contains(@class, 'Metadata_metadata')]/span[contains(@class, 'Metadata_')]")

    original_list_date = f'{dating_spans[1].text} from {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    last_bump = f'not bumped as of {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    
    if len(dating_spans) == 4:
        last_bump = f'{dating_spans[3].text} from {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'

    
    size = browser.find_element(By.XPATH, "//p[contains(text(), 'Size ')]/span").text
    
    condition = browser.find_element(By.XPATH, "//p[contains(text(), 'Condition ')]/span").text
    
    color = browser.find_element(By.XPATH, "//p[contains(text(), 'Color ')]/span").text
    
    like_count = int(browser.find_element(By.XPATH, "//span[contains(@class, 'Likes_count')]").text)
    
    seller_stars = "n/a"
    
    seller_transaction_count = browser.find_element(By.XPATH, "//div[contains(@class, 'transactionsAndForSale')]/span[contains(@class, Footnote_footnote)]").text
    seller_transaction_count = int(seller_transaction_count.split(" ")[0])
    
    
    seller_listing_count = browser.find_element(By.XPATH, "//a[contains(@class, 'forSaleCount')]/span[contains(@class, Footnote_footnote)]").text
    seller_listing_count = int(seller_listing_count.split(" ")[0])
    
    tags = ""
    tag_spans = browser.find_elements(By.XPATH, "//a[contains(@class, 'Hashtag_link')]")
    for tag in tag_spans:
        tags += tag.text
    
    description = ""
    description_ps = browser.find_elements(By.XPATH, "//p[contains(@class, 'Description_paragraph')]")
    for paragraph in description_ps:
        if paragraph:
            try:
                description += paragraph.text
            except Exception as e:
                print(e)
                description += "error getting this line."
            description += "\n"
    shipping_cost = "0"
    try:
        shipping = browser.find_element(By.XPATH, "//span[contains(@class, 'Shipping_cost')]")
        shipping_cost = shipping.text
    except Exception as e:
        print(e)
        
    breadcrumbs = browser.find_elements(By.XPATH, "//a[contains(@class, 'Breadcrumbs_link')]")
    specifc_subcategory = "n/a"
    for i in range(len(breadcrumbs)-1, -1, -1):
        print(breadcrumbs[i].text)
        if breadcrumbs[i].text != "":
            specifc_subcategory = breadcrumbs[i].text
            break
        
    item = Item(price, brands, title, discount_percent, last_bump, original_list_date, size, condition, color, like_count, seller_stars, seller_transaction_count, seller_listing_count, tags, description, shipping_cost, anchor_href, trending_position, specifc_subcategory)
    
    
    return item

def createItemList(browser, listing_anchor_elements):
    items = []
    for i, anchor_href in enumerate(listing_anchor_elements):
        browser.get(anchor_href)
        item = createItem(browser, anchor_href, i)
        items.append(item)
            
    return items

def getListingAnchorElements(browser, item_count):
    
    visible_elements = []
    
    while len(visible_elements) < item_count:
        visible_elements = browser.find_elements(By.XPATH, "//a[contains(@class, 'listing-item-link')]")
        print(f'visible elements: {len(visible_elements)}')
        
        browser.execute_script('window.scrollBy(0, document.body.scrollHeight);') 
    # Assuming 'visible_elements' is a list of Selenium WebElements
    
        

    return [element.get_attribute('href') for element in visible_elements][:item_count]


if __name__ == "__main__":
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--start-maximized')
    
    browser = webdriver.Chrome()
    
    browser.get('https://www.grailed.com/shop')
    
    items = []
    listing_anchor_elements = getListingAnchorElements(browser, 1)
    items = createItemList(browser, listing_anchor_elements)

    browser.quit()
    print(items[0])
    
    # for item in items:
    #     insert_item_into_sqlite(item)
    
    # x = get_all_items_from_sqlite()
    # print(x[0])
    # print(compute_position_to_likes_per_hour_ratio(x))
    
    # print(compute_brand_frequency(x))