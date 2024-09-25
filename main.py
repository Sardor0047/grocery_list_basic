

# Define function to retrieve prices colum in to a list
def get_prices(data):
    """
    Retrieves prices column in to a list

    Args:
        data (str): CSV format data

    Returns:
        list: list of prices
    """

    x = data.split('\n')
    maxsulot = ''

    i = 0
    while i < len(x):

        narx = x[i].split(',')
        maxsulot += f"{i+1} {narx[2]} \n"
        i += 1

    return maxsulot

def get_products(data):
    """
    Retrieves products column in to a list

    Args:
        data (str): CSV format data

    Returns:
        list: list of products
    """

    x = data.split('\n')
    maxsulot = ''

    i = 0
    while i < len(x):

        lst = x[i].split(',')
        maxsulot += f"{i+1} {lst[0]} \n"
        i +=1

    return maxsulot
def get_expensive(prices):
    """
    Finds the most expensive product of index

    Args:
        prices (list): list of prices

    Returns:
        int: index of most expensive product
    """

    x = data.split('\n')
    maxsulot = []

    i = 1
    while i < len(x):

        narx = x[i].split(',')
        maxsulot.append((narx[2]))
        i += 1

    price = []

    y = 0
    while y < len(maxsulot):
        
        just = maxsulot[y]
        price.append(float(just[1:]))
        y += 1

    top_price = (price[0])
    n = 0
    while n < len(price):
        if top_price < price[n]:
            top_price =(price[n])
        n += 1
    return f"${top_price}"
    

# Read data from file
f = open("grocery_list_basic/data.csv")
data = f.read()
print(get_products(data))
