import redis
    r = redis.Redis()
    r.mset({'Croatia': 'Zagreb'})
    print(r.get('Croatia'))

if __name__ == '__main__':
    
    import sys
    sys.exit(int(main() or 0))