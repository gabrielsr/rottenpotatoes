from functools import wraps
from flask import flash
from flask_wtf import FlaskForm



def form_view(form_class):
    """"
    Decorator for views that have forms.
    If the view is called with a form it will call the view with the exiting form
    else it will call the view with a new form.

    :param form_class: The form class to use.
    """
    def decorated_view(func, *args, **kwargs):
        @wraps(func)
        def wrapper(form=None, *wrargs, **wrkwargs):
            if form:
                return func(form, *wrargs, **wrkwargs)
            else:
                form = form_class(**wrkwargs)
                return func(form, *wrargs, **wrkwargs)
        return wrapper

    return decorated_view

def form_edit_view(form_class, entitycls, id_key='id', *aargs, **akwargs):
    # """"
    # Decorator for views that have forms.
    # If the view is called with a form it will call the view with the exiting form
    # else it will call the view with a new form.

    # :param form_class: The form class to use.
    # """
    def decorated_view(func):
        @wraps(func)
        def wrapper(form=None, *wargs, **wkwargs):
            if form:
                return func(form, *wargs, **wkwargs)
            else:
                from ..webapp import db
                id = wkwargs.get(id_key, None)
                if not id:
                    raise Exception(f"Error using @form_edit_view. Missing {id_key} parameter")
                entity = db.get_or_404(entitycls, id)
                form = form_class(obj=entity)
                return func(form, *wargs, **wkwargs)
        return wrapper

    return decorated_view


def form_validated(form_class, form_view):
    
    """
    Decorator for views that user submitted form data.
    If the form is valid it will call the view with the form
    else it will call the view with the form and the errors.

    :param form_class: The form class to use.
    :param form_view: The view to call if the form is not valid.
    """
    def decorated_view(func):
        @wraps(func)
        def wrapper(*wargs, **wkwargs):
            
            form = form_class()
            if form.validate_on_submit():
                try:
                    return func(form, *wargs, **wkwargs)
                except ValueError as e:
                    flash(str(e), "danger")
                except FormGeneralError as e:
                    flash(str(e), "danger")
                except Exception as e:
                    from app.webapp import app
                    flash('Internal Error. Please try later', "danger")
                    app.logger.error(e)
                return form_view(form, *wargs, **wkwargs)
            else:
                return form_view(form, *wargs, **wkwargs)
        return wrapper
    return decorated_view

def get_form_data(form, *fields):
    return dict((field, getattr(form, field).data) for field in fields)


def load_parent_resource_factory(modelcls, id_field:int):
    def decorated_view(func):
        @wraps(func)
        def wrapper(*wargs, **wkwargs):
            from ..webapp import db
            id = wkwargs.pop(id_field)
            if id:
                resource = db.get_or_404(modelcls, id)
                return func(resource, *wargs, **wkwargs)
            else:
                return func(*wargs, **wkwargs)
        return wrapper
    return decorated_view


class FormGeneralError(Exception):
    pass