from datetime import date

from ariadne import convert_kwargs_to_snake_case
from flask_login import login_required

from api import db
from api.review.models import Review


@convert_kwargs_to_snake_case
@login_required
def create_review_resolver(obj, info, book_id, rating, review):
    today = date.today()
    rev = Review(book_id=book_id, rating=rating, review=review, created_at=today)
    db.session.add(rev)
    db.session.commit()
    payload = {"success": True, "review": rev.to_dict()}
    return payload


@convert_kwargs_to_snake_case
@login_required
def update_review_resolver(obj, info, id, book_id, rating, review):
    try:
        rev = Review.query.get(id)
        if rev:
            rev.book_id = book_id
            rev.review = review
            rev.rating = rating
        db.session.add(rev)
        db.session.commit()
        payload = {"success": True, "post": rev.to_dict()}
    except AttributeError:
        payload = {"success": False, "errors": [f"item matching id {id} not found"]}
    return payload


@convert_kwargs_to_snake_case
@login_required
def delete_review_resolver(obj, info, id):
    try:
        review = Review.query.get(id)
        db.session.delete(review)
        db.session.commit()
        payload = {"success": True, "post": review.to_dict()}
    except AttributeError:
        payload = {"success": False, "errors": ["Not found"]}
    return payload
