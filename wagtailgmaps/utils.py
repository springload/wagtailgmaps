import random
import string


def random_string(length=6, chars=string.ascii_lowercase):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))
