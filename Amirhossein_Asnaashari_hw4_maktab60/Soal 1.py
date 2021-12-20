import pickle


class Person:
    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender

    def __str__(self):
        return f'Name: {self.name} + Email: {self.email} + Gender: {self.gender}'


class Author(Person):
    def __init__(self, name, email, gender, writing_code, genre):
        super().__init__(name, email, gender)
        self.writing_code = writing_code
        self.genre = genre

    def __str__(self):
        return f'Writing Code: {self.writing_code} + Genre: {self.genre}'


class Poet(Person):
    def __init__(self, name, email, gender, style):
        super().__init__(name, email, gender)
        self.style = style

    def __str__(self):
        return f'Style: {self.style}'


class Researcher(Person):
    def __init__(self, name, email, gender, field, university):
        super().__init__(name, email, gender)
        self.field = field
        self.university = university

    def __str__(self):
        return f'Field: {self.field} + University: {self.university}'


class Work:
    def __init__(self, title, owner):
        self.title = title
        self.owner = owner
        self.writers = input(str()).split()

    def __str__(self):
        return f'Title: {self.title} + Owner: {self.owner}'


class Book(Work):
    def __init__(self, title, owner, ISBN, publication):
        super().__init__(title, owner)
        self.ISBN = ISBN
        self.publication = publication

    def __str__(self):
        return f'ISBN: {self.ISBN} + Publication: {self.publication}'

    def number_of_owners(self):
        return print(len(self.title))


class Poem(Work):
    def __init__(self, title, owner, literature_style):
        super().__init__(title, owner)
        self.literature_style = literature_style

    def __str__(self):
        return f'Literature Style: {self.literature_style}'


class Article(Work):
    def __init__(self, title, owner, magazine_name, publish_year):
        super().__init__(title, owner)
        self.magazine_name = magazine_name
        self.publish_year = publish_year

    def __str__(self):
        return f'Magazine Name: {self.magazine_name} + Publish Year: {self.publish_year}'

    def number_of_owners_articles(self):
        return print((len(self.magazine_name)))


person_object = Person('ahmad', 'ahmadiii90', 'male')
author_object = Author('ali', 'alipoor95', 'male', '22658', 'thriller')
poet_object = Poet('ahmad', 'ahmadiii90', 'male', 'robaee')
researcher_object = Researcher('ahmad', 'ahmadiii90', 'male', )
work_object = Work('shirin o farhad', 'nezami')
book_object = Book()
poem_object = Poem()
article_object = Article()