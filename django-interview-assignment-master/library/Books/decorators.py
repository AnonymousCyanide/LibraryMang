from django.http import HttpResponse
from django.shortcuts import redirect

def check_grp(names,roles):
    for name in names:
        if name in roles:
            return True
    return False

def allowed_users(allowed_roles= []):
    def decorator(view_func):
        def wrapper(request , *args, **kwargs):
            print(allowed_roles)
            group = None
            if request.user.groups.exists():
                groups = list(request.user.groups.all())
                names = []
                for group in groups:
                    names.append(group.name)
                print(names)
                if check_grp(names , allowed_roles):
                    return view_func(request , *args, **kwargs)
                else :
                    print('I am here')
                    return redirect('home_page')
            else :
                return redirect('home_page')
    
        return wrapper
    return decorator