from datetime import datetime as dt, timedelta as td
from Stock_Scraper import read_current_stock_price
from Portfolio import Portfolio
import random

class Simulator:
    def __init__(self, portfolio = Portfolio(10000)):
        self.portfolio = portfolio

    def simulate(self, start_date="2023-01-04", end_date=dt.now()):
        current_date = dt.strptime(start_date, "%Y-%m-%d")
        while (current_date.date() != end_date.date()):
            if current_date.weekday() < 5:
                random_decider = random.randint(1,3)
                match random_decider:
                    case 1 | 3: #Buys Stock
                        price = read_current_stock_price(current_date, 'F')
                        if not price:
                            continue
                        quantity = int((self.portfolio.balance * 0.1) / price) # 10% of balance can be used to buy
                        self.portfolio.buy_stock('F', price, quantity)
                    case 2: #Sells Stock whole stock
                        stock_info = self.portfolio.get_stock_info('F')
                        if stock_info:
                            price = read_current_stock_price(current_date, 'F')
                            if not price:
                                continue
                            self.portfolio.sell_stock('F', price, stock_info['quantity'])
                        else:
                            current_date -= td(days=1)
                self.portfolio.evaluate(current_date, 'F', True)
            current_date += td(days=1)
            print(current_date.date())
            print("--------------------------------------------")
        self.portfolio.evaluate(current_date, 'F', True)
            