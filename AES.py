import codecs, random
key=input("input the key: ")
def array_from_string(key):
    byte_array=key.encode()
    hex=codecs.encode(byte_array, "hex")
    string=str(hex)
    hex=string[2:-1]
    print(hex)
    array=[]
    astr=str(hex)
    length=len(astr)
    for i in range(int(length/2)):
            array.append(hex[2*i:2*i+2])
    return array

def decode(key,encode_string):
    useful_array=[]
    encode_array=[]
    for i in range(int(len(encode_string)/2)):
            encode_array.append(encode_string[2*i:2*i+2])
    key_array=array_from_string(key)
    
    for i in range(len(encode_array)):
        object=encode_array[i]
        if object not in key_array:
            bytes_object = bytes.fromhex(object)
            ascii_string = bytes_object.decode("ASCII")
            useful_array.append(ascii_string)
    useful_string=''.join(useful_array)
    print(useful_string)
    return useful_string
    
def encode(key,string):
    key_array=array_from_string(key)
    length_key=int(len(key_array))
    undecoded_array= array_from_string(string)
    level=len(undecoded_array)
    for i in range(int(2*level)):
        random_insert=key_array[random.randrange(0,length_key)]
        for k in range(length_key):
            undecoded_array.insert(i,random_insert)
    encoded_array=undecoded_array
    encoded_string=''.join(encoded_array)
    print(encoded_string)
    return encoded_string
        
while True:
    Choice=input("decode or encode")
    while Choice!='decode' and Choice!='encode':
        Choice=input("decode or encode")
    if Choice=="decode":
        encoded_string=input("input decode array: ")
        decode(key, encoded_string)
    else:
        string=input("input array to be encoded")
        encode(key, string)
