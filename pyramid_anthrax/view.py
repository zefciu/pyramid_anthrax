import pyramid.view 

def view_config(*args, **kwargs):
    Form = kwargs.pop('Form', None)
    on_invalid = kwargs.pop('on_invalid', None)
    form_mode = kwargs.pop('form_mode', '')
    if Form is None:
        return pyramid.view.view_config(*args, **kwargs)

    def view_config(orig_view):

        def view(*view_args):
            request = view_args[1] if len(view_args) == 2 else view_args[0]
            form = Form(form_mode)
            form.__raw__ = request.POST
            request.form = form
            if not form.__valid__ and on_invalid is not None:
                import pdb; pdb.set_trace()
                return pyramid.view.render_view_to_response(
                    context=request.context, request=request, name=on_invalid)
            else: 
                return orig_view(*view_args)

        return pyramid.view.view_config(*args, **kwargs)(view)
    return view_config