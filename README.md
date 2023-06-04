<a name="readme-top"></a>

# RSA Factoring Challenge
Factoring as many numbers as possible into a product of two smaller numbers.

## Table of Contents
- [Introduction](#introduction)
  - [What is the RSA algorithm](#What-is-the-RSA-algorithm)
  - [What is the RSA factoring challenge](#What-is-the-RSA-factoring-challenge)
- [Compilation](#compilation)
- [Usage](#usage)
  - [Run factors](#run-factors)
  - [Run rsa](#run-rsa)
- [Output](#output)
  - [Factors output](#factors-output)
  - [Rsa output](#rsa-output)
- [Files](#files)

## Introduction

### What is the RSA algorithm
The RSA algorithm is a widely used public-key cryptosystem that is used for secure data transmission. It is an asymmetric encryption algorithm that uses a key pair to encrypt and decrypt data. The key pair consists of a public key that is accessible to anyone and a private key that is kept secret by the key pair creator.

The RSA algorithm involves four steps: key generation, key distribution, encryption, and decryption. The RSA algorithm is based on the principle that it is easy to multiply large numbers, but factoring large numbers is very difficult.

The public key consists of two numbers where one number is a multiplication of two large prime numbers, and the private key is also derived from the same two prime numbers. The client receives this data and decrypts it, and nobody else except the browser can decrypt the data even if a third party has the public key of the browser.

### What is the RSA factoring challenge
The RSA Factoring Challenge was a public challenge issued by RSA Security on March 18, 1991 to encourage the academic community to find more efficient ways of factoring large prime numbers.

The challenge was to factorize two large numbers that were the product of two prime numbers each. The first number was a 129-digit integer, and the second number was a 130-digit integer. The challenge lasted for over a decade, and the first successful factorization of the 129-digit number was achieved in 1994 by a team of researchers using a special-purpose computer. Finally, in 2009, the 130-digit integer was factored using a general number field sieve algorithm. The RSA Factoring Challenge contributed significantly to the development of modern cryptography.

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

### Factors output

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

### Rsa output

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
|[factors](factors)|Factorize as many numbers as possible into a product of two smaller numbers.|
|[factors.c](factors.c)|Finds the smallest divisor of a given number.|
|[lib_factors.so](lib_factors.so)|A shared object library file of the [factors.c](factors.c) file that can be used in the [rsa](rsa) file.|
|[rsa](rsa)|Factorize as many numbers as possible into a product of two smaller prime numbers.|

<p align="right"><a href="#readme-top">Back to Top</a></p>
