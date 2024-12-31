# Shipping Cost Calculator

## Input Package weight and shipping weight
weight = float(input("Enter the package weight in kilograms"))
rate = float(input("Enter the shipping rate in kilograms"))

# Calculate Shipping Cost
shipping_cost = weight * rate

## Display the results
print(f"Shipping Cost: {shipping_cost} USD")
