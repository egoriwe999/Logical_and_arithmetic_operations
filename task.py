def add_hex(a, b):
    data1 = int(a, 16)
    data2 = int(b, 16)
    result = data1 + data2
    return hex(result)[2:]    

def sub(a, b):
    data1 = int(a, 16)
    data2 = int(b, 16)
    result = data1 - data2
    return hex(result)[2:] 

def shiftR(a,n):
    data1 = int(a, 16)
    result = data1 >> n
    return hex(result)[2:] 

def shiftL(a,n):
    data1 = int(a, 16)
    result = data1 << n
    return hex(result)[2:] 

def mod(a):
    data1 = int(a, 16)
    if data1 < 0:
        data1 *= -1
    result = data1
    return hex(result)[2:] 

def inv(a):
    data1 = int(a, 16)
    result = ~data1
    return hex(result)[2:] 
    
def xor(hex_str1, hex_str2):

    data1 = bytes.fromhex(hex_str1)
    data2 = bytes.fromhex(hex_str2)

    result = bytes( a ^ b for a, b in zip(data1, data2))
    
    result_hex = result.hex()
    
    return result_hex

def or_hex(hex_str1, hex_str2):
    data1 = bytes.fromhex(hex_str1)
    data2 = bytes.fromhex(hex_str2)

    result = bytes( a | b for a, b in zip(data1, data2))
    
    result_hex = result.hex()
    
    return result_hex

def and_hex(hex_str1, hex_str2):
    # Converting hex strings to binary data
    data1 = bytes.fromhex(hex_str1)
    data2 = bytes.fromhex(hex_str2)
    
    result = bytes( a & b for a, b in zip(data1, data2))
    
    # Convert result to hexadecimal string
    result_hex = result.hex()
    
    return result_hex


hex_str1 = '33ced2c76b26cae94e162c4c0d2c0ff7c13094b0185a3c122e732d5ba77efebc' # you may change this
hex_str2 = '22e962951cb6cd2ce279ab0e2095825c141d48ef3ca9dabf253e38760b57fe03' # you may change this

n = 1 # you may change this
results = shiftL(hex_str1,n) # now i use shiftL function , but you can use other function above
print(results)

# created by egoriwe999