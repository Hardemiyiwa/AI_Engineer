# Daily market report
# collecting input 
try:
    market_name = input("Enter the market name: ")
    no_of_trader = int(input("Enter the number trader: "))
    daily_revenue = float(input("Enter the daily revenue: "))

    # Output
    print(f"\nMarket name: {market_name}\nNumber of trader: {no_of_trader:,}\nDaily revenue: #{daily_revenue:,}")
except ValueError as e:
    print("\nError:", e)
finally:
    print("Report closed")
