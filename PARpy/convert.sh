#!/bin/bash
 
for i in *.hdf; do
   echo "Converting to hdf5 $i ..."
   h4toh5 $i $i.h5
done
