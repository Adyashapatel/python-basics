'''class product():

    count = 0
    def __init__(self,name , price):
        self.name = name
        self.price = price
        product.count += 1
    def display(self):
        print("Product Name :",self.name)
        print("Product Price :",self.price)
    @classmethod
    def total_products(cls):
        print("Total products are :",cls.count)



p1 = product("laptop",45000)
p1.display()        
p2 = product("mobile",25000)
p2.display()
product.total_products() '''

#q1
'''class Bankaccount():
    def __init__(self, accountnumber,ownername,balanace):
        self.accountnumber = accountnumber
        self.ownername = ownername
        self.balanace = balanace
    def deposit(self, amount):
        self.balanace += amount
        print("Deposited :",amount)
    def withdraw(self, amount):
        if amount > self.balanace:
            print("Insufficient balance")
        else:
            self.balanace -= amount
            print("Withdrawn :",amount)
    def display(self):
        print("Account Number :",self.accountnumber)
        print("Owner Name :",self.ownername)
        print("Balance :",self.balanace)

acc1 = Bankaccount("123456","John Doe",5000)
acc1.display()
acc1.deposit(2000)
acc1.withdraw(1000)
acc1.display() '''

#q2
'''class Book()
  count = 0
  def __init__(self , author , list of review ):
    self.author = author
    self.list of review = list of review
    self.reviews = [] #created empty list to store the reviw 
    def new_review(self, review):
        self.reviews.append(review)
        Book.count += 1
    def display_reviews(self):
        print("new reviwes :"self.reviews)
    @classmethod
    def total_reviews(cls):
        print("Total reviews are :",Book.count)

b1 = Book("Author Name",[])
b1.new_review("Great book!")
b1.total_reviews()
b1.display_reviews()'''

#3
class vachile():  
   def __init__(self, brand, model):
         self.brand = brand
         self.model = model
class car(vachile):
        def __init__(self, brand, model, num_doors):
            super().__init__(brand, model)
            self.num_doors = num_doors
        def display_info(self):
            print("Brand:", self.brand)
            print("Model:", self.model)
            print("Number of doors:", self.num_doors)
v1 = vachile("Toyota", "Camry",)
v1.display_info()

