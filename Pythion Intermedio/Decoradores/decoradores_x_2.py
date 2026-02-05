user_logged_in = False

def requires_login(func):
    def wrapper():
        try:
            global user_logged_in
            if user_logged_in is False:
                raise
            func()
        except:
            print("Usuario no autenticado\n")
    return wrapper


@requires_login
def view_profile():
    print("Mostrando perfil del usuario\n")


view_profile()