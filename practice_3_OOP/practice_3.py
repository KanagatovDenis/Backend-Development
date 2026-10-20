class Product:
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def is_available(self, quantity=1):
        return self.stock >= quantity

    def reduce_stock(self, quantity):
        if not self.is_available(quantity):
            raise ValueError(f'Недостаточно товара «{self.name}» на складе')

        self.stock -= quantity

    def __str__(self):
        return f'{self.name} ({self.category}) стоит {self.price:.2f} руб. (на складе: {self.stock})'


class ShoppingCart:
    def __init__(self):
        self._items = {}

    def add(self, product, quantity=1):
        if quantity <= 0:
            raise ValueError('Количество должно быть положительным')

        new_qty = self._items.get(product, 0) + quantity

        if not product.is_available(new_qty):
            raise ValueError(f'Нельзя добавить {new_qty} шт. товара «{product.name}»: на складе {product.stock} шт.')

        self._items[product] = new_qty

    def remove(self, product):
        if product not in self._items:
            raise KeyError(f"Товара «{product.name}» нет в корзине")

        del self._items[product]

    def update_quantity(self, product, quantity):
        if product not in self._items:
            raise KeyError(f"Товара «{product.name}» нет в корзине")

        if quantity <= 0:
            self.remove(product)
            return

        if not product.is_available(quantity):
            raise ValueError(f"Нельзя установить {quantity} шт. товара «{product.name}»: на складе {product.stock}")

        self._items[product] = quantity

    @property
    def items(self):
        return dict(self._items)

    def subtotal(self):
        return sum(item.price * quantity for item, quantity in self._items.items())

    def is_empty(self):
        return not self._items

    def clear(self):
        self._items.clear()

    def __str__(self):
        if self.is_empty():
            return "Корзина пуста"

        lines = [f"  {price.name} x{quantity} = {price.price * quantity:.2f} руб."
                 for price, quantity in self._items.items()]

        return "Корзина:\n" + "\n".join(lines) + f"\n  Итого без скидок и налогов: {self.subtotal():.2f} руб."


class Order:
    TAX_RATE = 0.13
    DISCOUNT_THRESHOLD = 15000
    DISCOUNT_RATE = 0.2

    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.processed = False

    def subtotal(self):
        return sum(price.price * quantity for price, quantity in self.items.items())

    def discount(self):
        if self.subtotal() >= self.DISCOUNT_THRESHOLD:
            return self.subtotal() * self.DISCOUNT_RATE

        return 0.0

    def tax(self):
        return (self.subtotal() - self.discount()) * self.TAX_RATE

    def total(self):
        return self.subtotal() - self.discount() + self.tax()

    def process(self):
        if self.processed:
            raise RuntimeError("Заказ уже оформлен")

        if not self.items:
            raise ValueError("Нельзя оформить пустой заказ")

        for product, qty in self.items.items():
            if not product.is_available(qty):
                raise ValueError(f"Недостаточно товара «{product.name}» на складе")

        for product, qty in self.items.items():
            product.reduce_stock(qty)

        self.processed = True
        self.customer.order_history.append(self)

    def __str__(self):
        return (f"Заказ ({self.customer.name}): товары {self.subtotal():.2f}, "
                f"скидка -{self.discount():.2f}, налог +{self.tax():.2f}, "
                f"итого к оплате {self.total():.2f} руб.")


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = ShoppingCart()
        self.order_history = []

    def checkout(self):
        order = Order(self, self.cart.items)
        order.process()
        self.cart.clear()
        return order

    def total_spent(self):
        return sum(o.total() for o in self.order_history)

    def __str__(self):
        return f"{self.name} <{self.email}>, заказов: {len(self.order_history)}"
