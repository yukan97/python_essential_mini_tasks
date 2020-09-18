class Book:
    
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        
    def __str__(self):
        return ('Book ( ' + self.author + '. ' + self.title + '. ' + 
                str(self.year) + '. genre: ' + self.genre + ').')
    
    def __repr__(self):
        return '{Book: %s, %s, %d, %s}' % (self.author, self.title, 
                                           self.year, self.genre)
        
    def __eq__(self, o):
        return (self.author == o.author and 
               self.title == o.title and
               self.year == o.year and
               self.genre == o.genre)
               

book1 = Book('Bulgakov', 'Heart of a Dog', 1925, 'satire')
book2 = Book('Rowling', 'Harry Potter', 1997, 'fantasy')
book3 = Book('Johnes', 'Moving Castle', 1986, 'fantasy')
book4 = Book('Johnes', 'Moving Castle', 1986, 'fantasy')
    
print(book1)
print(book2)
print(book3)
print(book4)
    

print(repr(book1))
print(repr(book2))
print(repr(book3))
print(repr(book4))

print(book1==book2)
print(book2==book3)
print(book3==book1)
print(book4==book3)