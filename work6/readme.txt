https://github.com/amueller/word_cloud/blob/master/examples/masked.py
用的是这个例子，只修改了2行
text = open(path.join(d, 'Aesops\' Fables.txt')).read()
alice_mask = np.array(Image.open(path.join(d, "anne.png")))
