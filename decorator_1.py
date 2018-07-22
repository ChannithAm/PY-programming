def p_decorator(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format((func(name)))

    return func_wrapper

def strong_decorator(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorator(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper


@p_decorator
@strong_decorator
@div_decorator
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

print(get_text("John"))