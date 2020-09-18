class Book:
    
    def __init__(self, author, title, year, genre, reviews=[]):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.reviews = reviews
        
    def __str__(self):
        return ('Book ( ' + self.author + '. ' + self.title + '. ' + 
                str(self.year) + '. genre: ' + self.genre + '). ' +
                'Reviews: ' + str(self.reviews))
    
    def __repr__(self):
        return '{Book: %s, %s, %d, %s}' % (self.author, self.title, 
                                           self.year, self.genre)
        
    def __eq__(self, o):
        return (self.author == o.author and 
               self.title == o.title and
               self.year == o.year and
               self.genre == o.genre)
    
    def set_reviews(self, new_review):
        self.reviews.append(new_review)
        
class Review:
    
    def __init__(self, text):
        self.text = text
    
    def __str__(self):
        return self.text
    
    def __repr__(self):
        return str(self)


book1 = Book('Bulgakov', 'Heart of a Dog', 1925, 'satire')

print(book1)

book1.set_reviews(Review('Great'))

print(book1)