import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

portfolio = {}

while True:

    print("""
====== AI STOCK PORTFOLIO TRACKER ======

1. Buy Stock
2. View Portfolio
3. Save Portfolio
4. Portfolio Chart
5. AI Suggestions
6. Exit
""")

    choice = input("Enter choice: ")

    # BUY STOCK
    if choice == "1":

        stock = input(
            "\nEnter Stock Symbol (AAPL, TSLA, MSFT, AMZN): "
        ).upper()

        qty = int(input("Enter Quantity: "))

        try:
            ticker = yf.Ticker(stock)

            current_price = (
                ticker.history(period="1d")
                ["Close"]
                .iloc[-1]
            )

        except:
            print("Invalid Stock Symbol!")
            continue

        investment = current_price * qty

        if stock in portfolio:
            portfolio[stock]["quantity"] += qty
            portfolio[stock]["investment"] += investment

        else:
            portfolio[stock] = {
                "price": current_price,
                "quantity": qty,
                "investment": investment
            }

        print(f"\n{stock} added successfully!")
        print(f"Current Price: ${current_price:.2f}")

    # VIEW PORTFOLIO
    elif choice == "2":

        if not portfolio:
            print("Portfolio is empty.")
            continue

        total = 0

        print("\n====== PORTFOLIO ======")

        for stock, details in portfolio.items():

            print(f"""
Stock: {stock}
Price: ${details['price']:.2f}
Quantity: {details['quantity']}
Investment: ${details['investment']:.2f}
""")

            total += details["investment"]

        print(f"Total Portfolio Value: ${total:.2f}")

    # SAVE CSV
    elif choice == "3":

        if not portfolio:
            print("Portfolio is empty.")
            continue

        rows = []

        for stock, details in portfolio.items():

            rows.append({
                "Stock": stock,
                "Price": details["price"],
                "Quantity": details["quantity"],
                "Investment": details["investment"]
            })

        df = pd.DataFrame(rows)

        df.to_csv(
            "portfolio.csv",
            index=False
        )

        print("Portfolio saved successfully!")

    # PIE CHART
    elif choice == "4":

        if not portfolio:
            print("Portfolio is empty.")
            continue

        labels = []
        values = []

        for stock, details in portfolio.items():
            labels.append(stock)
            values.append(details["investment"])

        plt.figure(figsize=(7, 7))

        plt.pie(
            values,
            labels=labels,
            autopct="%1.1f%%"
        )

        plt.title("Portfolio Distribution")
        plt.show()

    # AI SUGGESTIONS
    elif choice == "5":

        if not portfolio:
            print("Portfolio is empty.")
            continue

        print("\n====== AI SUGGESTIONS ======")

        if len(portfolio) < 3:
            print(
                "Diversify your portfolio by adding more stocks."
            )

        if "TSLA" in portfolio:
            print(
                "TSLA can be volatile. Monitor risk carefully."
            )

        if "AAPL" in portfolio:
            print(
                "AAPL is generally considered a stable long-term stock."
            )

        print(
            f"You currently own {len(portfolio)} stocks."
        )

    # EXIT
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")