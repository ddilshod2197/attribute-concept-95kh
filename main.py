class Attribute:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name}: {self.value}"

class Object:
    def __init__(self):
        self.attributes = []

    def add_attribute(self, attribute):
        self.attributes.append(attribute)

    def __str__(self):
        attributes_str = "\n".join([str(attr) for attr in self.attributes])
        return f"Attributes:\n{attributes_str}"

# Misol
obj = Object()
attr1 = Attribute("name", "John")
attr2 = Attribute("age", 30)

obj.add_attribute(attr1)
obj.add_attribute(attr2)

print(obj)
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. `Attribute` klassi yaratib, `name` va `value` parametrini qabul qilib, ularni `self.name` va `self.value` atributlariga saqlab oling.
2. `Object` klassi yaratib, `attributes` ro'yxatini qabul qilib, uga `add_attribute` metodi orqali `Attribute` klassidan ob'ekt qo'shish imkonini berib oling.
3. `Object` klassidan ob'ekt yaratib, unda `Attribute` klassidan ob'ektlarni qo'shing.
4. `print` funksiyasidan foydalanib, `Object` klassidan ob'ektning `attributes` ro'yxatini chiqaring.
