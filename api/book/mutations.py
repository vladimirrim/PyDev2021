from datetime import date

from ariadne import convert_kwargs_to_snake_case
from flask_login import login_required

from api import db
from api.book.models import Book


@convert_kwargs_to_snake_case
@login_required
def create_book_resolver(obj, info, title, author, description):
    today = date.today()
    book = Book(title=title, author=author, description=description, created_at=today)
    db.session.add(book)
    db.session.commit()
    payload = {"success": True, "book": book.to_dict()}
    return payload


@convert_kwargs_to_snake_case
@login_required
def update_book_resolver(obj, info, id, title, author, description):
    try:
        book = Book.query.get(id)
        if book:
            book.title = title
            book.author = author
            book.description = description
        db.session.add(book)
        db.session.commit()
        payload = {"success": True, "post": book.to_dict()}
    except AttributeError:
        payload = {"success": False, "errors": [f"item matching id {id} not found"]}
    return payload


@convert_kwargs_to_snake_case
@login_required
def delete_book_resolver(obj, info, id):
    try:
        book = Book.query.get(id)
        db.session.delete(book)
        db.session.commit()
        payload = {"success": True, "post": book.to_dict()}

    except AttributeError:
        payload = {"success": False, "errors": ["Not found"]}

    return payload
