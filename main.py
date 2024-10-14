from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title' : 'Title 1', 'author': 'Author 1', 'category': 'Science'},
    {'title' : 'Title 6', 'author': 'Author 1', 'category': 'Science'},
    {'title' : 'Title 7', 'author': 'Author 1', 'category': 'Science'},
    {'title' : 'Title 2', 'author': 'Author 2', 'category': 'Math'},
    {'title' : 'Title 3', 'author': 'Author 3', 'category': 'Science'},
    {'title' : 'Title 4', 'author': 'Author 4', 'category': 'Eco'},
    {'title' : 'Title 5', 'author': 'Author 5', 'category': 'Math'}
]
@app.get("/books")
async def read_all_boks():
    return BOOKS


@app.get("/books/mybook")
async def read_mybook():
    return {'book_title': 'My favourite book!'}
# @app.get("/books/{dynamic_param}")
# async def read_param(dynamic_param: str):
#     return {'dynamic_param': dynamic_param}

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if(book.get('title').casefold() == book_title.casefold()):
            return book
        

@app.get("/books/")
async def read_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if(book.get('category').casefold() == category.casefold()):
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_by_category(book_author, category):
    book_to_return = []
    for book in BOOKS:
        if(book.get('author').casefold() == book_author.casefold() 
           and book.get('category').casefold() == category.casefold()):
            book_to_return.append(book)
    return book_to_return


@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if( BOOKS[i].get('title').casefold() == updated_book.get('title').casefold()):
            BOOKS[i] = updated_book


@app.delete("/books/delete/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if(BOOKS[i].get('title').casefold() == book_title.casefold()):
            BOOKS.pop(i)
            break


@app.get("/books/getBooks/{author_name}")
async def book_by_author(author_name):
    books_to_return = []
    for book in BOOKS:
        if(book.get('author').casefold() == author_name.casefold()):
            books_to_return.append(book)
    return books_to_return
        