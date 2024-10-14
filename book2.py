from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    rating: int
    description: str

    def __init__(self, id, title, author, rating, description):
        self.author = author
        self.description = description
        self.title = title
        self.rating = rating
        self.id = id


class BookRequest(BaseModel):
    id: Optional[int] = Field(description='Id is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    rating: int = Field(gt=0, lt=6)
    description: str = Field(min_length=1, max_length=100)

    class Config: 
        schema_extra = {
            "example": {
                "title": "a new book",
                "author": "John Doe",
                "rating" : 5,
                "description" : "A new description"
            }
        }



BOOKS = [
    Book(1, "Book 1", "Author 1", 5, "This is book 1"),
    Book(2, "Book 2", "Author 2", 5, "This is book 2"),
    Book(3, "Book 3", "Author 3", 5, "This is book 3"),
    Book(4, "Book 4", "Author 4", 5, "This is book 4"),
    Book(5, "Book 4", "Author 4", 5, "This is book 5"),
    Book(6, "Book 4", "Author 4", 5, "This is book 6"),
]

@app.get("/")
async def root():
    return BOOKS


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book
        
@app.get("/books/")
async def read_book_by_rating(rating: int):
    book_to_return = []
    for book in BOOKS:
        if book.rating == rating:
            book_to_return.append(book)
    return book_to_return


@app.post("/create-book")
async def create_book(book_request :BookRequest):
    #print(type(book_request)) #BookRequest
    new_book = Book(**book_request.model_dump())  #** -> allows us to convert into key-value 
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    # if(len(BOOKS) > 0):
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1

    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book

@app.delete("/book/{book_id}")
async def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            del BOOKS[i]