#! /usr/bin/env python3
##
# Script for PicoCTF weirderRSA challenge
# Created by Amos (LFlare) Ng
##
import binascii
import gmpy2

# Default public key?
e = 65537
n = 248501410365662412791489552646042256782092770118253438700194718631291036762726489658495565276550205113648626040596191969135846656414394584577305526761671104277390765264806022908497647300596494542202565022133435383403344333672279722534625284520459706609569974491538689429548817677759350947931780871046796607829
c = 194048013822218245260658018019940874060627700835842604475987702337533801266490182061968998210807564778328557627772974110046885380635225974269865976518335375789734689098164529086561756412074742698644530189076800227300946408167039318949544794351233987752575608106800908043533012088081995031010618521695843625062

# Interesting dp
dp = 13026685992320376966900872608865420374627539408788613307094830638345728123427345410810495082016593339528583880478309351125854158459979947140005048595481921

# Random R
r = 123456

# n = pq
p = gmpy2.gcd(n, pow(r, (e*dp), n) - r)
q = gmpy2.div(n, p)
print("p: %d" % p)
print("q: %d" % q)

# calculate d
phi = (p-1) * (q-1)
d = gmpy2.invert(e, phi)
print("phi: %d" % phi)
print("d: %d" % d)

# Calculate message
m = int(pow(c, d, n))
print("m: %d" % m)

# Convert int message to string
mHex = format(m, 'x')
print(mHex)
message = binascii.unhexlify(mHex).decode("utf-8")
print(message)