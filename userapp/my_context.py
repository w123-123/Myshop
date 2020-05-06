#coding=utf-8

def get_user(request):

    if request.session.has_key('user'):
        return {'user':request.session['user']}
    return {'user':''}