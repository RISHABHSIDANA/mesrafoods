from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
       # print(request.session.get('customer'))
        print( request.user.is_authenticated)
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('customer'):
           return redirect('index')

        response = get_response(request)
        return response

    return middleware