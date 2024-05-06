def compute_brand_frequency(items):
    brands = {}
    for item in items:
        for brand in item.brands:
            if brand in brands:
                brands[brand] += 1
            else:
                brands[brand] = 1
    return brands

def compute_average_price(items):
    total_price = 0
    for item in items:
        total_price += item.price
    return total_price / len(items)

def compute_average_discount(items):
    total_discount = 0
    for item in items:
        total_discount += item.discount_percent
    return total_discount / len(items)

def compute_position_to_likes_per_hour_ratio(items):
    position_frequency = {}
    for item in items:
        if item.trending_position in position_frequency:
            position_frequency[item.trending_position] += 1
        else:
            position_frequency[item.trending_position] = 1
            
    position_to_likes_per_hour = {}
    for item in items:
        if item.trending_position in position_to_likes_per_hour:
            position_to_likes_per_hour[item.trending_position] += item.likes_per_hour/position_frequency[item.trending_position]
        else:
            position_to_likes_per_hour[item.trending_position] = item.likes_per_hour/position_frequency[item.trending_position]
    
    return position_to_likes_per_hour

def compute_title_keyword_frequency(items):
    keywords = {}
    for item in items:
        title = item.title
        title = title.split(" ")
        for word in title:
            if word in keywords:
                keywords[word] += 1
            else:
                keywords[word] = 1
    return keywords

def compute_subcategory_frequency(items):
    subcategories = {}
    for item in items:
        subcategory = item.specific_subcategory
        if subcategory in subcategories:
            subcategories[subcategory] += 1
        else:
            subcategories[subcategory] = 1
    return subcategories