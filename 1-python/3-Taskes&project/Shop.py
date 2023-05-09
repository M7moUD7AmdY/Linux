# Sample grocery items
items = (
    ('apple', 10),
    ('banana', 12),
    ('orange', 13),
    
)

# Function to display available items
def display_items():
    print('Available items:')
    for item in items:
        print(f'{item[0]} (EP{item[1]})')

# Function to calculate total cost of items
def calculate_total(items_list):
    total = 0
    for item in items_list:
        found_item = None
        for available_item in items:
            if available_item[0] == item:
                found_item = available_item
                break
        if found_item is None:
            print(f'Error: {item} not found in available items')
        else:
            total += found_item[1]
    return total

# Display available items
display_items()

# Prompt user for items to purchase
items_list = input('Enter items to purchase ): ').split(',')

# Calculate total cost of items
total = calculate_total(items_list)

# Display total cost
print(f'Total cost: EP{total}')