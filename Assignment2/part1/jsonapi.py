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
    
    def encode_range(self, obj):
        return {"start":obj.start, "stop": obj.stop, "step": obj.step}

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
    
    def decode_range(self, dct):
        return range(dct["start"], dct["stop"], dct["step"])

def dumps(obj, *args, **kwargs):
    return json.dumps(obj, cls=ExtendedEncoder, *args, **kwargs)

def loads(s, *args, **kwargs):
    return json.loads(s, cls=ExtendedDecoder, *args, **kwargs)


