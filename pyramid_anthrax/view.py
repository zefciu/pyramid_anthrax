import sys
from decorator import decorator

def form_post(Form, on_invalid, form_mode):
    def form_post_(view, *view_args):
        request = view_args[1] if len(view_args) == 2 else view_args[0]
        form = Form(form_mode)
        form.__raw__ = request.POST
        request.form = form
        if not form.__valid__ and on_invalid is not None:
            return pyramid.view.render_view_to_response(
                context=request.context, request=request, name=on_invalid)
        else: 
            return view(*view_args)
    return decorator(form_post_)
