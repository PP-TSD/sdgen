#!/bin/bash

SOURCEDIR=source
EXAMPLES=../examples

GENERATED=${SOURCEDIR}/generated

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
.. image:: generated/Terminal_example.png

" >> ${SOURCEDIR}/examples.txt

echo "Sequence example
================

.. include:: examples/ex05.py
   :literal:

" >> ${SOURCEDIR}/examples.txt

python ${EXAMPLES}/ex05.py ${GENERATED} > /dev/null

echo "
.. image:: generated/Sequence_example.png

" >> ${SOURCEDIR}/examples.txt

echo "Return example
==============

.. include:: examples/ex07.py
   :literal:

" >> ${SOURCEDIR}/examples.txt

python ${EXAMPLES}/ex07.py ${GENERATED} > /dev/null

echo "
.. image:: generated/Return_example.png

" >> ${SOURCEDIR}/examples.txt

echo "Alternation example
===================

.. include:: examples/ex06.py
   :literal:

" >> ${SOURCEDIR}/examples.txt

python ${EXAMPLES}/ex06.py ${GENERATED} > /dev/null

echo "
.. image:: generated/Alternation_example.png

" >> ${SOURCEDIR}/examples.txt

echo "Detour example
==============

.. include:: examples/ex02.py
   :literal:

" >> ${SOURCEDIR}/examples.txt

python ${EXAMPLES}/ex02.py ${GENERATED} > /dev/null

echo "
.. image:: generated/Detour_example.png

" >> ${SOURCEDIR}/examples.txt

echo "Inverse Terminal example
========================

.. include:: examples/ex04.py
   :literal:

" >> ${SOURCEDIR}/examples.txt

python ${EXAMPLES}/ex04.py ${GENERATED} > /dev/null

echo "
.. image:: generated/Inverse_example.png

" >> ${SOURCEDIR}/examples.txt

echo "Nonterminal example
===================

.. include:: examples/ex03.py
   :literal:

" >> ${SOURCEDIR}/examples.txt

python ${EXAMPLES}/ex03.py ${GENERATED} > /dev/null

echo "
.. image:: generated/Nonterminal_example.png

.. image:: generated/Non_Terminal_C.png

" >> ${SOURCEDIR}/examples.txt

echo "Nested groups example
=====================

.. include:: examples/ex09.py
   :literal:

" >> ${SOURCEDIR}/examples.txt

python ${EXAMPLES}/ex09.py ${GENERATED} > /dev/null

echo "
.. image:: generated/Nested_groups_example.png

" >> ${SOURCEDIR}/examples.txt
