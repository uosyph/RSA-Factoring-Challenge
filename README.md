<a name="readme-top"></a>

# RSA Factoring Challenge


## Table of Contents
- [Compilation](#compilation)
- [Usage](#usage)
  - [Run factors](#run-factors)
  - [Run rsa](#run-rsa)
- [Output](#output)
  - [Factors](#factors)
  - [Rsa](#rsa)
- [Files](#files)

## Compilation
Compile the C source code into a shared object library:

```bash
gcc -fPIC -shared -o lib_factors.so factors.c
```

## Usage

### Run factors:

```bash
./factors <file>
```

Where `file` is a file containing natural numbers to factor.
One number per line.

### Run rsa:

```bash
./rsa <file>
```

Where `file` is a file containing one natural number to factor.

## Output

### Factors

Output format: **n=p*q**
- One factorization per line.
- `p` and `q` are not always prime numbers.

```bash
$ cat tests/test00
4
12
34
128
1024
4958
1718944270642558716715
9
99
999
9999
9797973
49
$ ./factos tests/test00
4=2*2
12=6*2
34=17*2
128=64*2
1024=512*2
4958=2479*2
1718944270642558716715=343788854128511743343*5
9=3*3
99=33*3
999=333*3
9999=3333*3
9797973=3265991*3
49=7*7
239809320265259=15485783*15485773
$
```

### Rsa

Output format: **n=p*q**
- `p` and `q` are always prime numbers.

```bash
$ cat tests/rsa-*
$ ./rsa tests/rsa-0
6=3*2
$ ./rsa tests/rsa-1
77=11*7
$ ./rsa tests/rsa-2
239821585064027=15486481*15485867
$ ./rsa tests/rsa-3
2497885147362973=49979141*49978553
$
```

## Files
|File|Description|
|---|---|
|[factors](factors)||
|[factors.c](factors.c)||
|[lib_factors.so](lib_factors.so)||
|[rsa](rsa)||

<p align="right"><a href="#readme-top">Back to Top</a></p>
