class Portfolio:
    def __init__(self, starting_balance):
        self.balance = starting_balance
        self.stocks = {}
        self.logs = []

    def buy_stock(self, symbol, price, quantity):
        cost = price * quantity

        if cost > self.balance:
            return False

        self.balance -= cost

        if symbol in self.stocks:
            prev_qty = self.stocks[symbol]['quantity']
            prev_avg = self.stocks[symbol]['avg_price']

            new_qty = prev_qty + quantity
            new_avg = (prev_qty * prev_avg + quantity * price) / new_qty
            
            self.stocks[symbol]['quantity'] = new_qty
            self.stocks[symbol]['avg_price'] = new_avg
        else:
            self.stocks[symbol] = {'quantity': quantity, 'avg_price': price}

        self.logs.append(f"Bought {quantity} of {symbol} at {price:.2f}")
        return True
    
    def sell_stock(self, symbol, price, quantity):
        if symbol not in self.stocks or self.stocks[symbol]['quantity'] < quantity:
            return False

        self.stocks[symbol]['quantity'] -= quantity
        proceeds = price * quantity
        self.balance += proceeds

        if self.stocks[symbol]['quantity'] == 0:
            del self.stocks[symbol]

        self.logs.append(f"Sold {quantity} of {symbol} at {price:.2f}")
        return True
    
    def reset_portfolio(self, starting_balance):
        self.balance = starting_balance
        self.stocks = {}
        self.logs = []

    def evaluate(self, current_prices, print=False):
        total_stock_value = 0

        for symbol, data in self.stocks.items():
            quantity = data['quantity']
            if symbol in current_prices:
                price = current_prices[symbol]
                total_stock_value += quantity * price

        total_value = self.balance + total_stock_value

        if print:
            print(f"Cash: £{self.balance:.2f}")
            print(f"Stock value: £{total_stock_value:.2f}")
            print(f"Total portfolio value: £{total_value:.2f}")

        return total_value