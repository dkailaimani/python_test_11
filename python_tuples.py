# Task 1: Formatting Flight Itineraries
# Create a Python function that takes a list of tuples as an argument. 
# Each tuple contains information about a flight itinerary: 
# (name, start, finish). The function should format and
#  return a string that lists each itinerary. For example, if the input 
# is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")],
#  the output should be a string formatted as:

# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"

def formatItenerary(itineraries):
    result = ""
    for i, itinerary in enumerate(itineraries, 1):
        name, start, finish = itinerary
        result += f"Itinerary {i}: {name} - From {start} to {finish}\n"
    return result.strip()


itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formItenararies = formatItenerary(itineraries)
print(formItenararies)

# You are maintaining a library system where each bookTitle is stored as a tuple within a list.
# Your task is to update this system by adding new books and ensuring no duplicates.
# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def insertBook(library, bookTitle, author):
    addBook = (bookTitle, author)
    if addBook in library:
        print(f"ERROR: The bookTitle '{bookTitle}' by {author} already exists in collection!")
    else:
        library.append(addBook)
        print(f"'{bookTitle}' by {author} has been successfully added to the library.")

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

insertBook(library, "Brave New World", "Aldous Huxley") 
insertBook(library, "Harry Potter", "J.K. Rowling")

print(library)

# You have been provided with stock market data, where each data point 
# is a tuple containing a company's stock name, the date, and the closing 
# price. Your task is to analyze this data to find the average closing price 
# of a specified stock over a given period.

def averagePrice(stockData, stockName, startDate, closingDate):
    totalClosingPrice = 0
    numOfEntries = 0
    for name, date, closingPrice in stockData:
        if name == stockName and startDate <= date <= closingDate:
            totalClosingPrice += closingPrice
            numOfEntries += 1
    if numOfEntries == 0:
        return f"ERROR: {stockName} between {startDate} and {closingDate} NOT FOUND!"
    else:
        return totalClosingPrice / numOfEntries

stockData = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

msftAvgPrice = averagePrice(stockData, "MSFT", "2021-01-01", "2021-01-02")
print("MSFT between 2021-01-01 and 2021-01-02:", f"${msftAvgPrice}")

aaplAvgPrice = averagePrice(stockData, "AAPL", "2021-01-01", "2021-01-02")
print("AAPL between 2021-01-01 and 2021-01-02:", f"${aaplAvgPrice}")

# You are given a list of tuples, each representing a customer's listOfOrders.
# Each tuple contains the customer's name, the product ordered, 
# and the quantity. Your task is to unpack each tuple and print the listOfOrders
# details in a user-friendly format.

def listOfOrders(orders):
    for i, (customer, product, quantity) in enumerate(orders, 1):
        print(f"Order #{i}:")
        print(f"\tCustomer: {customer}")
        print(f"\tProduct: {product}")
        print(f"\tQuantity: {quantity}")
        print()

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More listOfOrders...
]

listOfOrders(orders)

# You are managing the product catalogs for an online store. 
# Each catalog is a tuple of products, and each product is a tuple 
# containing the product name and price. Merge multiple catalogs into a single tuple.

# Write a function to join two or more product catalogs into one.
# Display the combined catalog, ensuring that it maintains the order 
# of products as they were in their original catalogs.

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

def extendCatalog(*catalogs):
    completeCatalog = ()
    for catalog in catalogs:
        completeCatalog += catalog
    return completeCatalog

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

completeCatalog = extendCatalog(catalog1, catalog2)

print("COMPLETE CATALOG:")
for product, price in completeCatalog:
    print(f"\t{product} : ${price:.2f}")



