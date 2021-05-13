from lithops import Storage

#storage = Storage()
#storage.put_object('my_bucket', 'test.txt', 'Hello World')
storage = Storage()
print(storage.list_objects('test-bythepego', prefix=''))
