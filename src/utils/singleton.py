""" Singleton decorator """

def singleton(func):
    """ Make the only one instance """
    instance = None
    def get_instance(*args, **kwargs):
        """ Wrapper """
        nonlocal instance
        if instance is None:
            instance = func(*args, **kwargs)
        return instance
    return get_instance
