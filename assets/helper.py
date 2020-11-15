from uuid import uuid4


def generate_key(length, model):
    key = uuid4().hex[:length]
    while model.objects.filter(key=key).exists():
        key = uuid4().hex[:length]
    return key
