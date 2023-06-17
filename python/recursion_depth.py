def foobar(i: int):
    try:
        return foobar(i + 1)
    except RecursionError:
        return i + 1


def foo(i: int):
    try:
        return bar(i + 1)
    except RecursionError:
        return i + 1


def bar(i: int):
    try:
        return foo(i + 1)
    except RecursionError:
        return i + 1


if __name__ == "__main__":
    calls = foobar(1)
    print("Got a RecursionError after {} recursive calls.".format(calls))
    calls = foo(1)
    print("Got a RecursionError after {} interleaved recursive calls.".format(calls))
