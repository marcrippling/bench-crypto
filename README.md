# bench-crypto
Benchmarking of cryptography library in python

### Benchmarking dimensions:
1. modulo bits: RSA 1024, RSA 2048, RSA 4096 
1. message bits: 2, 256, 512, 1024(128 bytes/characters) 

### Steps on how-to run this script in a linux box
```
# 0. make sure you have venv installed in your box, if not:
$ pip install virtualenv

# 1. create a venv named crypt-curr 
$ python -m venv crypt-curr

# 2. activate venv crypt-curr 
$ source ./crypt-curr/bin/activate

# 3. install deps for venv crypt-curr 
$ pip install -r ./curr/requirements.txt

# 4. run benchmark.py for venv crypt-curr 
$ python benchmark.py

# 5. create a venv named crypt-latest 
$ python -m venv crypt-latest

# 6. activate venv crypt-latest 
$ source ./crypt-latest/bin/activate

# 7. install deps for venv crypt-latest 
$ pip install -r ./latest/requirements.txt

# 8. run benchmark.py for venv crypt-latest
$ python benchmark.py

```

### Sample venv deps
- crypt-curr
```
$ pip list

Package      Version
------------ -------
cffi         1.16.0
cryptography 3.4.8
pip          22.0.4
pycparser    2.21
pycryptodome 3.10.1
setuptools   58.1.0

```
- crypt-latest 
```
$ pip list

Package      Version
------------ -------
cffi         1.16.0
cryptography 41.0.7
pip          22.0.4
pycparser    2.21
pycryptodome 3.19.0
setuptools   58.1.0
```

### Sample benchmarking results
```
(crypt-latest) admin@ip-10-201-1-60:~/bench-crypto$ python benchmark.py
    9200 iter in   1.0074 sec :     9132.5 iter/sec:  cryptography.rsa:1024/2
    9200 iter in   1.0192 sec :     9026.8 iter/sec:  cryptography.rsa:1024/256
    9200 iter in   1.0074 sec :     9132.5 iter/sec:  cryptography.rsa:1024/512
    9200 iter in   1.0084 sec :     9123.5 iter/sec:  cryptography.rsa:1024/1024
    1800 iter in   1.1103 sec :     1621.2 iter/sec:  cryptography.rsa:2048/2
    1600 iter in   0.9863 sec :     1622.3 iter/sec:  cryptography.rsa:2048/256
    1800 iter in   1.1114 sec :     1619.6 iter/sec:  cryptography.rsa:2048/512
    1600 iter in   0.9879 sec :     1619.5 iter/sec:  cryptography.rsa:2048/1024
     400 iter in   1.6480 sec :      242.7 iter/sec:  cryptography.rsa:4096/2
     400 iter in   1.6498 sec :      242.5 iter/sec:  cryptography.rsa:4096/256
     400 iter in   1.6536 sec :      241.9 iter/sec:  cryptography.rsa:4096/512
     400 iter in   1.6556 sec :      241.6 iter/sec:  cryptography.rsa:4096/1024
```

```
(crypt-curr) admin@ip-10-201-1-60:~/bench-crypto$ python benchmark.py
    9200 iter in   0.9888 sec :     9304.3 iter/sec:  cryptography.rsa:1024/2
    9400 iter in   1.0083 sec :     9322.6 iter/sec:  cryptography.rsa:1024/256
    9400 iter in   1.0110 sec :     9297.7 iter/sec:  cryptography.rsa:1024/512
    9000 iter in   0.9675 sec :     9302.4 iter/sec:  cryptography.rsa:1024/1024
    1800 iter in   1.1234 sec :     1602.3 iter/sec:  cryptography.rsa:2048/2
    1600 iter in   0.9990 sec :     1601.7 iter/sec:  cryptography.rsa:2048/256
    1800 iter in   1.1244 sec :     1600.9 iter/sec:  cryptography.rsa:2048/512
    1600 iter in   0.9960 sec :     1606.5 iter/sec:  cryptography.rsa:2048/1024
     400 iter in   1.6531 sec :      242.0 iter/sec:  cryptography.rsa:4096/2
     400 iter in   1.6542 sec :      241.8 iter/sec:  cryptography.rsa:4096/256
     400 iter in   1.6610 sec :      240.8 iter/sec:  cryptography.rsa:4096/512
     400 iter in   1.6555 sec :      241.6 iter/sec:  cryptography.rsa:4096/1024
```