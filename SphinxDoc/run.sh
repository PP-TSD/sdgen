mkdir -p source/examples
cp ../examples/*.py source/examples

touch source/examples.txt
echo "========
Examples
========
   
Below there are some examples of using Syntax Diagram Generator to generate images.

" > source/examples.txt

echo "Terminal example
================

.. include:: examples/ex01.py
   :literal:

" >> source/examples.txt

python ../examples/ex01.py source/images > /dev/null

echo "
.. image:: images/Simple_A->B.png

" >> source/examples.txt

echo "Sequence example
================

.. include:: examples/ex05.py
   :literal:

" >> source/examples.txt

python ../examples/ex05.py source/images > /dev/null

echo "
.. image:: images/Example_of_Sequence.png

" >> source/examples.txt

echo "Return example
==============

.. include:: examples/ex07.py
   :literal:

" >> source/examples.txt

python ../examples/ex07.py source/images > /dev/null

echo "
.. image:: images/Example_of_Return.png

" >> source/examples.txt

echo "Alternation example
===================

.. include:: examples/ex06.py
   :literal:

" >> source/examples.txt

python ../examples/ex06.py source/images > /dev/null

echo "
.. image:: images/Example_of_Alternation.png

" >> source/examples.txt

echo "Detour example
==============

.. include:: examples/ex02.py
   :literal:

" >> source/examples.txt

python ../examples/ex02.py source/images > /dev/null

echo "
.. image:: images/Example_of_Detour_element.png

" >> source/examples.txt

echo "Inverse Terminal example
========================

.. include:: examples/ex04.py
   :literal:

" >> source/examples.txt

python ../examples/ex04.py source/images > /dev/null

echo "
.. image:: images/Example_of_Inverse_Terminal.png

" >> source/examples.txt

echo "Nonterminal example
===================

.. include:: examples/ex03.py
   :literal:

" >> source/examples.txt

python ../examples/ex03.py source/images > /dev/null

echo "
.. image:: images/Example_of_NonTerminal.png

.. image:: images/Non_Terminal_C.png

" >> source/examples.txt

echo "Nested groups example
=====================

.. include:: examples/ex09.py
   :literal:

" >> source/examples.txt

python ../examples/ex09.py source/images > /dev/null

echo "
.. image:: images/Example_of_nested_groups.png

" >> source/examples.txt

