from ariadne import convert_kwargs_to_snake_case

from api.review.models import Review


def listReviews_resolver(obj, info):
    try:
        revs = [rev.to_dict() for rev in Review.query.all()]
        payload = {"success": True, "posts": revs}
    except Exception as error:
        payload = {"success": False, "errors": [str(error)]}
    return payload


@convert_kwargs_to_snake_case
def getReview_resolver(obj, info, id):
    try:
        rev = Review.query.get(id)
        payload = {"success": True, "post": rev.to_dict()}
    except AttributeError:
        payload = {"success": False, "errors": [f"Review with id {id} not found"]}
    return payload


@convert_kwargs_to_snake_case
def getBookReviews_resolver(obj, info, book_id):
    try:
        revs = Review.query.filter_by(book_id=book_id)
        payload = {"success": True, "post": [rev.to_dict() for rev in revs]}
    except AttributeError:
        payload = {"success": False, "errors": [f"Book with id {id} not found"]}
    return payload
