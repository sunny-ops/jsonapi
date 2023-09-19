import json

class ExtendedEncoder(json.JSONEncoder):
    def default(self, obj):
        name = type(obj).__name__
        try:
            encoder = getattr(self, f"encode_{name}")
        except AttributeError:
            return super().default(obj)
        else:
            encoded = encoder(obj)
            encoded["__extended_json_type__"] = name
            return encoded

    def encode_complex(self, obj):
        return {"real": obj.real, "imag": obj.imag}

class ExtendedDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        extended_type = dct.pop("__extended_json_type__", None)
        if extended_type:
            decoder = getattr(self, f"decode_{extended_type}", None)
            if decoder:
                return decoder(dct)
        return dct

    def decode_complex(self, dct):
        return complex(dct["real"], dct["imag"])

def dumps(obj, *args, **kwargs):
    return json.dumps(obj, cls=ExtendedEncoder, *args, **kwargs)

def loads(s, *args, **kwargs):
    return json.loads(s, cls=ExtendedDecoder, *args, **kwargs)

# Test the extended library
if __name__ == '__main__':
    complex_num = 3 + 4j
    print(dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
    encoded_data = dumps(complex_num)
    print(encoded_data)
    decoded_data = loads(encoded_data)
    print(decoded_data)
