#!/bin/bash
for A in $@; do
 echo Arg A: $A + 1
done
for A; do
 echo Arg B: $A
done



S = 0; for F in ./*.c; do N = 'grep -v "^[ \t{}]*$\|^[ \t]*//" $F | wc -l; S = 'expr $S + $N'; done; echo $S (nu merge)