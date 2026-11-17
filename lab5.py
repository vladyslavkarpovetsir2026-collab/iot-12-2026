class Flower:
    def __init__(self, name, height, size, color, price, quantity,
                 delivery_rate):
        self._name = name
        self._height = height
        self._size = size
        self._color = color
        self._price = price
        self._quantity = quantity
        self._delivery_rate = delivery_rate

    def __del__(self):
        print(f"[Деструктор] Квітку «{self._name}» видалено")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def delivery_rate(self):
        return self._delivery_rate

    @delivery_rate.setter
    def delivery_rate(self, value):
        self._delivery_rate = value

    def show(self):
        print(f"{self._name}, {self._color}, висота {self._height} см, "
              f"розмір {self._size} см, ціна {self._price} грн, "
              f"кількість {self._quantity}, "
              f"доставка {self._delivery_rate} грн")


class FlowerShop:
    def __init__(self, name):
        self.name = name
        self._flowers = []

    def __del__(self):
        print(f"[Деструктор] Магазин «{self.name}» закрито")

    def add_flower(self, flower):
        self._flowers.append(flower)

    def remove_flower(self, flower):
        self._flowers.remove(flower)

    def top_expensive(self, count):
        ordered = sorted(self._flowers, key=lambda f: f.price, reverse=True)
        return ordered[:count]

    def show_top_expensive(self, count):
        print(f"Топ-{count} найдорожчих квітів:")
        for number, flower in enumerate(self.top_expensive(count), start=1):
            print(f"{number}. ", end="")
            flower.show()

    def show(self):
        print(f"Асортимент магазину «{self.name}»:")
        for flower in self._flowers:
            print(flower)
            flower.show()


class Bouquet:
    def __init__(self):
        self._items = []

    def __del__(self):
        print("[Деструктор] Букет розібрано")

    def add_flower(self, flower, count=1):
        self._items.append((flower, count))

    def total_cost(self):
        total = 0
        for flower, count in self._items:
            total += flower.price * count
        return total

    def show(self):
        print("Букет:")
        for flower, count in self._items:
            print(f"{flower.name}: {count} шт. x {flower.price} грн")
        print(f"Вартість букета: {self.total_cost()} грн")


def main():
    rose = Flower("Троянда", 60, 6, "червона", 55, 100, 5)
    tulip = Flower("Тюльпан", 40, 4, "жовтий", 25, 150, 3)
    lily = Flower("Лілія", 70, 10, "біла", 90, 40, 8)
    orchid = Flower("Орхідея", 50, 8, "фіолетова", 150, 15, 12)

    rose.show()
    rose.price = 60
    print(f"Нова ціна троянди: {rose.price} грн")
    print()

    shop = FlowerShop("Флора")
    shop.add_flower(rose)
    shop.add_flower(tulip)
    shop.add_flower(lily)
    shop.add_flower(orchid)
    shop.show()
    print()

    shop.show_top_expensive(3)
    print()

    shop.remove_flower(tulip)
    shop.show()
    print()

    bouquet = Bouquet()
    bouquet.add_flower(rose, 5)
    bouquet.add_flower(lily, 3)
    bouquet.show()
    print()

    shop.add_flower(bouquet)
    shop.add_flower('bbb')
    shop.show()



    del bouquet
    del shop


if __name__ == "__main__":
    main()