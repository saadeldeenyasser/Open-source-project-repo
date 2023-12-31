from PIL import Image

end_bits=b"\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"
end_bits2=b"\xff\xd9"

def encode(path,secret):
    fhand= open(path,'rb')
    path=path[:path.find(".")] + "steg" + path[path.find("."):]
    if secret=="":
        exit("error")
    y=fhand.read()
    if y.endswith(end_bits)==1:
        newI=open(path,"wb")
        newI.write(y+secret.encode()+end_bits)
        img = Image.open(path)
        img.show()
    elif y.endswith(end_bits2)==1:
        newI=open(path,"wb")
        newI.write(y+secret.encode()+end_bits2)
        # img=Image.open(path)
        # img.show()
    else:
        exit("unsupported image type")

def decode(path):
    fhand=open(path,"rb")
    data = fhand.read()
    if data.endswith(end_bits) == 1 :
        data=data[data.find(end_bits)+len(end_bits):]
        data=data[:data.find(end_bits)]
    elif data.endswith(end_bits2) == 1:
        data=data[data.find(end_bits2)+len(end_bits2):]
        data = data[:data.find(end_bits2)]
    else:
        exit("unsupported image type")
    print("your secret message is:"+data.decode())

