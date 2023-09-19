from jsonapi import *

# Test the extended library
# Test complex
def test_complex_encode(complex_num):
    encoded_data = dumps(complex_num)
    if encoded_data == '{"real": 3.0, "imag": 4.0, "__extended_json_type__": "complex"}':
        print("Test complex encode passed") 
    else:
        print("Test complex encode failed")

test_complex_encode(3 + 4j)

def test_complex_decode(encoded_data):
    decoded_data = loads(encoded_data)
    if decoded_data == complex(3+4j):
        print("Test complex decode passed")
    else:
        print("Test complex decode failed")

test_complex_decode('{"real": 3.0, "imag": 4.0, "__extended_json_type__": "complex"}')

# Test range
def test_range_encode(range_num):
    encoded_data = dumps(range_num)
    if encoded_data == '{"start": 1, "stop": 10, "step": 3, "__extended_json_type__": "range"}':
        print("Test range encode passed") 
    else:
        print("Test range encode failed")

test_range_encode(range(1, 10, 3))

def test_range_decode(encoded_data):
    decoded_data = loads(encoded_data)
    if decoded_data == range(1, 10, 3):
        print("Test range decode passed")
    else:
        print("Test range decode failed")

test_range_decode('{"start": 1, "stop": 10, "step": 3, "__extended_json_type__": "range"}')

