#!/bin/bash
:<<'A'
echo "The postion $1 and the postion ${22} "
echo "The script is $0"

#Indirection 
x=abc
abc=Start of the alphabet
echo "The value of x is $x"
echo "The value of abc is $abc"
A

m = ${p:-hotdog}
echo $m
echo $p

