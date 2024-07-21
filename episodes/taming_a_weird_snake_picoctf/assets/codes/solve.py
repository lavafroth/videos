input_list = [ 4, 54, 41, 0, 112, 32, 25, 49, 33, 3, 0, 0,
57, 32, 108, 23, 48, 4, 9, 70, 7, 110, 36, 8, 108, 7, 49,
10, 4, 86, 43, 102, 126, 92, 0, 16, 58, 41, 89, 78 ]

key_str = 'J'
key_str = '_' + key_str
key_str = key_str + 'o'
key_str = key_str + '3'
key_str = 't' + key_str
# key_str = 't_Jo3'
key_list = [ord(char) for char in key_str]
# key_list = [116, 95, 74, 111, 51]
while len(key_list) < len(input_list):
    key_list.extend(key_list)
# key_list = [116, 95, 74, 111, 51, 116, 95, 74, 111, 51, ...
result = [a ^ b for a, b in zip(input_list, key_list)]
text = ''.join(map(chr, result))
print(text)
