# Pràctica 1 - Communication models and Middleware
**Programadors:** Joel Panisello Lozano i Adrià Pérez Gondolbeu

**Middelware utilitzats:** gRPC (Comunicació directa) i Redis (Comunicació indirecta)

**Funcions gRPC:**
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
# Instalar llibreries
> pip3 install -r requirements.txt

# Engegar redis (port 50051)
> redis-server

# Engegar el servidor RPC
> python3 server.py

# Engegar el servidor web (port 8000)
> cd files; python3 -m http.server

# Executar el client
> python3 client.py
```

**Exemples client:**
```bash
# Crear worker
> python3 client.py createworker

# Llistar fitxers
> python3 client.py listfiles

# Executar countingWords d'un fitxer
> python3 client.py countingwords fitxer1.txt

# Executar wordcount de dos fitxers
> python3 client.py createworker # s'ha de tindre minim 2 workers
> python3 client.py wordcount fitxer1.txt

# Llistar workers
> python3 client.py listworkers

# Eliminar worker
> python3 client.py deleteworker 1
```
