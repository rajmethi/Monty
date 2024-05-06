

# Define a simple class named Person
class Item:
    # Constructor method (__init__) to initialize object attributes
    def __init__(self, price, brands, title, discount_percent, last_bump, original_list_date, size, condition, color, like_count, seller_stars, seller_transaction_count, seller_listing_count, tags, description, shipping_cost, href, trending_position, specific_subcategory):
        self.price = price
        self.brands = brands
        self.title = title
        self.discount_percent = discount_percent
        self.last_bump = last_bump
        self.original_list_date = original_list_date
        self.size = size
        self.condition = condition
        self.like_count = like_count
        self.seller_stars = seller_stars
        self.seller_transaction_count = seller_transaction_count
        self.seller_listing_count = seller_listing_count
        self.tags = tags
        self.description = description
        self.shipping_cost = shipping_cost
        self.color = color
        self.href = href
        self.trending_position = trending_position
        self.likes_per_hour = self.calculate_likes_per_hour()
        self.specific_subcategory = specific_subcategory
        
        
    def calculate_likes_per_hour(self):
        split = self.original_list_date.split(" ")
        hours_elapsed = 0
        if split[0] == "about":
            time_unit_index = 2
        else:
            time_unit_index = 1
        if split[time_unit_index][0:3] == "min":
            hours_elapsed = int(split[time_unit_index-1]) / 60
        elif split[time_unit_index][0] == "h":
            hours_elapsed = int(split[time_unit_index-1])
            
        elif split[time_unit_index][0] == "d":
            hours_elapsed = int(split[time_unit_index-1]) * 24
        
        elif split[time_unit_index][0] == "w":
            hours_elapsed = int(split[time_unit_index-1]) * 24 * 7
            
        elif split[time_unit_index][0:3] == "mon":
            hours_elapsed = int(split[time_unit_index-1]) * 24 * 30
            
        elif split[time_unit_index][0] == "y":
            hours_elapsed = int(split[time_unit_index-1]) * 24 * 365
        
        return int(self.like_count) / hours_elapsed

    def __str__(self):
        return (
                f"  Title: {self.title}\n"
                f"  Price: {self.price}\n"
                f"  Brand: {self.brands}\n"
                f"  Discount Percent: {self.discount_percent}%\n"
                f"  Last Bump: {self.last_bump}\n"
                f"  Original List Date: {self.original_list_date}\n"
                f"  Size: {self.size}\n"
                f"  Condition: {self.condition}\n"
                f"  Like Count: {self.like_count}\n"
                f"  Seller Stars: {self.seller_stars}\n"
                f"  Seller Transaction Count: {self.seller_transaction_count}\n"
                f"  Seller Listing Count: {self.seller_listing_count}\n"
                f"  Tags: {', '.join(self.tags)}\n"
                f"  Description: {self.description}\n"
                f"  Shipping Cost: {self.shipping_cost}\n"
                f"  Color: {self.color}\n"
                f"  Link: {self.href}\n"
                f"  Likes Per Hour: {self.likes_per_hour:.10f}\n"
                f"  Trending Position: {self.trending_position}\n"
                f"  Specific Subcategory: {self.specific_subcategory}\n"
                )
        

