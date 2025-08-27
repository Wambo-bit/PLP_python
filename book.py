                    #ACTIVITY 1
# #Base Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def show_author(self):
        print(f"Author is {self.author}")
        
    def show_title(self):
        print(f"Title: {self.title}")

#Derived Class*(inheritance)
class TheRiverBetween(Book):
    def __init__(self,title,author, publication_year):

        #Calling parent constructor
        super().__init__(title, author)
        self.publication_year = publication_year
        #Polymorphism--override method
    def show_author(self):
        print(f"This book was written by {self.author} in {self.publication_year}")

book1=Book("A Grain of Wheat", "Ngugi wa Thiong'o")
book1.show_title()
book1.show_author()

river_between=TheRiverBetween("The River Between", "Ngugi wa Thiong'o", "1965")
river_between.show_title()
river_between.show_author()

                        