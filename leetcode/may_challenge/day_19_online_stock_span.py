class StockSpanner:

    def __init__(self):
        self.price_list = []

    def next(self, price: int) -> int:
        self.price_list.append(price)
        idx = len(self.price_list) - 1
        count_days = 0
        while idx >= 0:
            if self.price_list[idx] <= price:
                count_days += 1
            if self.price_list[idx] > price:
                break
            idx -= 1
        return count_days
