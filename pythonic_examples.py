# tuple unpacking
(a, b) = (1, 2)
print(f'a = {a}, b = {b}')
(a, b) = (3, 4)
print(f'a = {a}, b = {b}')

def return_tuple(a, b, c):
    return (a, b, c)

(d, e, f) = return_tuple(4, 5, 6)
# print(f'd = {d}, e = {e}, f = {f}')

# args, **kwargs
def use_args_and_kwargs(number, another_number, *others , **favorites):
# first parameter is the positional argument, 2nd if arg, 3rd kwarg
# if you want a 2nd positional argument, you can make another one (right after "number" in this example)
    print(f'positional arguments (required) = {number}, {another_number}')
    print(f'args = {others}')
    print(f'kwargs = {favorites}')
    return "This is fine"

print(use_args_and_kwargs(3, 8))
print(use_args_and_kwargs(3, 4, 5, favorite=7))
print(use_args_and_kwargs(6, 'red', 'yellow', 'purple', favorite='green'))

