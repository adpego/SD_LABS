# Pràctica 1 - Communication models and Middleware

**Middelware utilitzats:** gRPC i Reddis

**Funcions RPC:**
```python
create_worker(Empty) returns (Int)
delete_worker(Int) returns (Int)
list_workers(Empty) returns (String)
job_worker(Operation) returns (String)
```

**Operacions:**
```python
wordCount(list_urls) # Counts the total number of words in different text files or text entries.
countingWords(list_urls) # Counts the number of occurrences of each word in a text file.
```

**Passos per executar-ho:**
```bash
# Engegar reddis (port 50051)
> redis-server

# Engegar el servidor RPC
> python3 server.py

# Engegar el servidor web (port 8000)
> cd files; python3 -m http.server

# Executar el client
> python3 client.py
```
