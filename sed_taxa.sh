#!/usr/bin/bash

# sed D_X__ by k p c o f g s
# 0 1 2 3 4 5 6
# k p c o f g s

file=$1
out=$2

cp $file $out
cat $out | sed -i -e "s/D_0__/k__" | sed -i -e "s/D_1__/p__" | sed -i -e "s/D_2__/c__" | sed -i -e "s/D_3__/o__" | sed -i -e "s/D_4__/f__" | sed -i -e "s/D_5__/g__" | sed -i -e "s/D_6__/s__"
