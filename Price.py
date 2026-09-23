class Product:
    count=0
    
    
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count+=1
    
    @classmethod
    def get_count(cls):
        print(f"total product i store is = {cls.count}")
    
    @staticmethod
    def calc_discount(price,discount):
        print(f"discounted price = {price-(price*discount/100)}")
    
    def display(self):
        print(f"{self.name} has price {self.price}")


p1=Product("phone",12000)
p2=Product("laptop",120000)



p1.display()
p2.display()
Product.get_count()
p1.calc_discount(12000,12)