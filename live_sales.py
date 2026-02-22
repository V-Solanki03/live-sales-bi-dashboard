import random
import time
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# connect to google sheets
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\solan\OneDrive\Documents\PROJECTS\live sales data\credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Live_Sales_Data").sheet1

products = ["Laptop", "Phone", "Headphones", "Shoes", "Watch"]
cities = ["Delhi", "Mumbai", "Bangalore", "Hyderabad", "Pune"]
payments = ["UPI", "Credit Card", "Cash on Delivery"]

order_id = 1000

while True:
    order_id += 1

    row = [
        order_id,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        random.choice(products),
        random.randint(500, 50000),
        random.choice(cities),
        random.choice(payments)
    ]

    sheet.append_row(row)

    print("New Order Added:", row)

    time.sleep(60)