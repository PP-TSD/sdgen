#!/bin/bash

SOURCEDIR=source
EXAMPLES=../examples

GENERATED=${SOURCEDIR}/_generated

mkdir -p ${GENERATED}
mkdir -p ${SOURCEDIR}/examples
cp ${EXAMPLES}/*.py ${SOURCEDIR}/examples

touch ${SOURCEDIR}/examples.txt
echo "========
Examples
========

Below there are some examples of using Syntax Diagram Generator to generate images.

" > ${SOURCEDIR}/examples.txt

echo "Terminal example
================

.. include:: examples/ex01.py
   :literal:

" >> ${SOURCEDIR}/examples.txt

python ${EXAMPLES}/ex01.py ${GENERATED} > /dev/null

echo "
.. image:: _generated/Terminal_Terminal_example.png

" >> ${SOURCEDIR}/examples.txt

echo "Sequence example
================

.. include:: examples/ex05.py
   :literal:

" >> ${SOURCEDIR}/examples.txt

python ${EXAMPLES}/ex05.py ${GENERATED} > /dev/null

echo "
.. image:: _generated/Sequence_example.png

" >> ${SOURCEDIR}/examples.txt

echo "Return example
==============

.. include:: examples/ex07.py
   :literal:

" >> ${SOURCEDIR}/examples.txt

python ${EXAMPLES}/ex07.py ${GENERATED} > /dev/null

echo "
.. image:: _generated/Return_example.png

" >> ${SOURCEDIR}/examples.txt

echo "Alternation example
===================

.. include:: examples/ex06.py
   :literal:

" >> ${SOURCEDIR}/examples.txt

python ${EXAMPLES}/ex06.py ${GENERATED} > /dev/null

echo "
.. image:: _generated/Alternation_example.png

" >> ${SOURCEDIR}/examples.txt

echo "Detour example
==============

.. include:: examples/ex02.py
   :literal:

" >> ${SOURCEDIR}/examples.txt

python ${EXAMPLES}/ex02.py ${GENERATED} > /dev/null

echo "
.. image:: _generated/Detour_example.png

" >> ${SOURCEDIR}/examples.txt

echo "Complex detour diagram
======================

.. include:: examples/ex10.py
   :literal:

" >> source/examples.txt

cp ../examples/ex10.py ../src/
python ../src/ex10.py source/_generated > /dev/null

echo "
.. image:: _generated/Complex_detour_diagram.png

.. image:: _generated/B_C.png

" >> source/examples.txt

rm ../src/ex10.py

echo "Inverse Terminal example
========================

.. include:: examples/ex04.py
   :literal:

" >> ${SOURCEDIR}/examples.txt

python ${EXAMPLES}/ex04.py ${GENERATED} > /dev/null

echo "
.. image:: _generated/Inverse_example.png

" >> ${SOURCEDIR}/examples.txt

echo "Nonterminal example
===================

.. include:: examples/ex03.py
   :literal:

" >> ${SOURCEDIR}/examples.txt

python ${EXAMPLES}/ex03.py ${GENERATED} > /dev/null

echo "
.. image:: _generated/Nonterminal_example.png

.. image:: _generated/Non_Terminal_C.png

" >> ${SOURCEDIR}/examples.txt

echo "Nested groups example
=====================

.. include:: examples/ex09.py
   :literal:

" >> ${SOURCEDIR}/examples.txt

python ${EXAMPLES}/ex09.py ${GENERATED} > /dev/null

echo "
.. image:: _generated/Nested_groups_example.png

" >> ${SOURCEDIR}/examples.txt
