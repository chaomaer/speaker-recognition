import os


def test(*args, **kwargs):
    for i in args:
        print(i)
    print("===============")
    for key, val in kwargs.items():
        print(key +':'+ val)


if __name__ == '__main__':
    test('-a', '-b', '-c', '-c', 'songsdfasdf', hello='hello', way='way')
