class Book:
    r_count=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.reviews=[]
        
        
    def new_review(self,new):
        self.reviews.append(new)
    
    def review_count(self):
        return len(self.reviews)
        
    def d_review(self):
        for r in self.reviews:
            print(r)
b1=Book("ego is the enemy","unknown")
b1.new_review("very good")
b1.new_review("interesting")
b1.new_review("worth reading")

print("Number of reviews:", b1.review_count())
b1.d_review()