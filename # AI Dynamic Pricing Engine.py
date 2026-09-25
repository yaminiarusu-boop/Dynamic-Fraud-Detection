# AI Dynamic Pricing Engine
print("===================================")
print("       AI DYNAMIC PRICING ENGINE")
print("===================================")

# Product details
base_price = 1000
demand = 85
inventory = 15
competitor_price = 950

# Dynamic pricing calculation
price = base_price

if demand > 80 and inventory < 20:
    price = base_price * 1.20
elif demand < 40 and inventory > 60:
    price = base_price * 0.90
else:
    price = base_price

# Compare with competitor price
if price > competitor_price:
    price = price
else:
    price = competitor_price

# Pricing result
print("\n===================================")
print("          PRICING RESULT")
print("===================================")

print("Demand:", demand)
print("Inventory:", inventory)
print("Competitor Price: Rs.", competitor_price)
print("Recommended Price: Rs.", round(price, 2))

# Pricing strategy
if demand > 80 and inventory < 20:
    print("Strategy: HIGH DEMAND - LOW INVENTORY")
elif demand < 40 and inventory > 60:
    print("Strategy: LOW DEMAND - HIGH INVENTORY")
else:
    print("Strategy: NORMAL PRICING")

print("===================================")
print("AI Dynamic Pricing Completed")