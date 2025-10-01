import redis
r = redis.Redis(host='10.1.68.172', port=6379, db=0)
r.ping()

# # True

# # ### Inserindo Dados ###
# # 
# r.set('otavio_mykey', 'myvalue')
# # True

# # ### Obtendo Dados ###,


# name = r.get('otavio_mykey')
# print(name.decode())
# # myvalue

# # ### Removendo Dados ###

# #r.delete('otavio_mykey')

# name = r.get('otavio_mykey')
# print(name.decode())
# # Traceback (most recent call last):
# # File "", line 1, in print(name.decode())
# # ^^^^^^^^^^^
# # AttributeError: 'NoneType' object has no attribute 'decode'

# r.hset("8888", "p1", "")
r.hset("8888", "p2", "3")



