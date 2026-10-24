class CartModule:
    def __init__(self):
        self.external_discount_service = "Active"

    def calculate_total(self, items_prices, promo_code=None):
        if not items_prices:
            return 0.0
        total = sum(items_prices)
        if promo_code == "STUDENT2024":
            total *= 0.9
        return max(0.0, total)
