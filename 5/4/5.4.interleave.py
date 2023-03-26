def interleave(*args):
    lst = []
    for seq in zip(*args):
        lst.extend(seq)

    return lst


def interleave_generator(*args):
    iters = [iter(arg) for arg in args]
    while True:
        try:
            for itr in iters:
                yield next(itr)
        except StopIteration:
            return


def interleave_generator(*args):
    # Flatten all arguments into a single iterable
    interleaved = (elem for seq in zip(*args) for elem in seq)
    yield from interleaved


print(interleave('abc', [1, 2, 3], ('!', '@', '#')))


a = 'abc'
b = [1, 2, 3]
c = ('!', '@', '#')

interleaved = interleave_generator(a, b, c)
lst = []
for element in interleaved:
    lst.append(element)

print(lst)
