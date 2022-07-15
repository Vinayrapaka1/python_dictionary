# a={}
# print(type(a))  #an empty curly brackets represented as dictionary(dict)

# b={1:'vinnu',2:'nani',3:'python'}  #dict is having keys like, 1,2,3
# print(b[3])

# rvk={
# 12:'kazipet is my home town',
# 13:'i like green colour',
# 14:'am learning python'
# }
# print(rvk[12])
# print(rvk[15]) #key error

# v={
#     1:37,
#     2:4.9,
#     3:'begumpet',
#     4:[1,2],
#     5:(3,5),
#     6:{2,4},
#     7:{12:'blackknight'}
#     }
# print(v[1],type(v[1]))
# print(v[2],type(v[2]))
# print(v[3],type(v[3]))
# print(v[4],type(v[4]))
# print(v,type(v))
# print(v.keys())
# print(v.values())
# print(v.items())

# a={1:'vinnu',2:'hi',3:'hello'}
# a.clear()
# print(a)

# a=[11,12,13,14,15]
# b=dict.fromkeys(a)
# print(b,type(b))
# print(dict.fromkeys(a,17))

# v={
#     1:37,
#     2:4.9,
#     3:'begumpet',
#     4:[1,2],
#     5:(3,5),
#     6:{2,4},
#     7:{12:'blackknight'}
# }
# print(v.get(3))
# print(v[5])
# print(v[23]) #key error
# v.pop(4)
# print(v)
# v.popitem()
# print(v)

# a={1:'hi',2:'hello',3:'hyderabad'}
# a.update({3:'warangal'})
# print(a)

# a={1:'hi',2:'hello',3:'hyderabad'}
# a.setdefault(2,'who')
# a.setdefault(4,'who')
# print(a) 

print(dir(dict))