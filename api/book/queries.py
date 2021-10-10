from ariadne import convert_kwargs_to_snake_case

from api.book.models import Book


def listBooks_resolver(obj, info):
    try:
        posts = [post.to_dict() for post in Book.query.all()]
        payload = {"success": True, "posts": posts}
    except Exception as error:
        payload = {"success": False, "errors": [str(error)]}
    return payload


@convert_kwargs_to_snake_case
def getBook_resolver(obj, info, id):
    try:
        post = Book.query.get(id)
        payload = {"success": True, "post": post.to_dict()}
    except AttributeError:
        payload = {"success": False, "errors": [f"Book with id {id} not found"]}
    return payload
