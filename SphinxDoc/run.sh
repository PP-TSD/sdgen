mkdir -p source/_generated
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

cp ../examples/ex01.py ../src/
python ../src/ex01.py source/_generated > /dev/null

echo "
.. image:: _generated/Simple_A->B.png

" >> source/examples.txt

rm ../src/ex01.py

echo "Sequence example
================

.. include:: examples/ex05.py
   :literal:

" >> source/examples.txt

cp ../examples/ex05.py ../src/
python ../src/ex05.py source/_generated > /dev/null

echo "
.. image:: _generated/Example_of_Sequence.png

" >> source/examples.txt

rm ../src/ex05.py

echo "Return example
==============

.. include:: examples/ex07.py
   :literal:

" >> source/examples.txt

cp ../examples/ex07.py ../src/
python ../src/ex07.py source/_generated > /dev/null

echo "
.. image:: _generated/Example_of_Return.png

" >> source/examples.txt

rm ../src/ex07.py

echo "Alternation example
===================

.. include:: examples/ex06.py
   :literal:

" >> source/examples.txt

cp ../examples/ex06.py ../src/
python ../src/ex06.py source/_generated > /dev/null

echo "
.. image:: _generated/Example_of_Alternation.png

" >> source/examples.txt

rm ../src/ex06.py

echo "Detour example
==============

.. include:: examples/ex02.py
   :literal:

" >> source/examples.txt

cp ../examples/ex02.py ../src/
python ../src/ex02.py source/_generated > /dev/null

echo "
.. image:: _generated/Example_of_Detour_element.png

" >> source/examples.txt

rm ../src/ex02.py

echo "Another detour example
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

" >> source/examples.txt

cp ../examples/ex04.py ../src/
python ../src/ex04.py source/_generated > /dev/null

echo "
.. image:: _generated/Example_of_Inverse_Terminal.png

" >> source/examples.txt

rm ../src/ex04.py

echo "Nonterminal example
===================

.. include:: examples/ex03.py
   :literal:

" >> source/examples.txt

cp ../examples/ex03.py ../src/
python ../src/ex03.py source/_generated > /dev/null

echo "
.. image:: _generated/Example_of_NonTerminal.png

.. image:: _generated/Non_Terminal_C.png

" >> source/examples.txt

rm ../src/ex03.py

echo "Nested groups example
=====================

.. include:: examples/ex09.py
   :literal:

" >> source/examples.txt

cp ../examples/ex09.py ../src/
python ../src/ex09.py source/_generated > /dev/null

echo "
.. image:: _generated/Example_of_nested_groups.png

" >> source/examples.txt

rm ../src/ex09.py
