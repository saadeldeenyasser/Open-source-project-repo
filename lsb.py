def encode2(im_path,secret):
    image = Image.open(im_path, 'r')
    if (len(secret) == 0):
        raise ValueError('Data is empty')
    newimg = image.copy()
    encode_enc(newimg, secret)
    new_img_name = im_path[:im_path.find(".")]+"steg"+im_path[im_path.find("."):]
    newimg.save(new_img_name)
    newimg.show()