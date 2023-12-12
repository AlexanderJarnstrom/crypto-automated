# Math operations crypto

## ord_table.py

Gives all exponents a^k modulo n in a table

### Usage

Print whole table:

    ord_table.py n

Print row *a*:

    ord_table.py n a

## calc_prim.py

Worse *ord_table.py*, prints all exponents *a^k_i* modulo *n* in a list to element *k*.

### Usage

    calc_prim_root.py a n k

## gen_rel_prim.py

generates all relative prim numbers to the element *n*.

### Usage

    gen_rel_prim.py n

## gen_primitiv_root.py

generates all primitiv roots to *n* using an already found root *a*

### Usage

    gen_primitiv_root.py n a