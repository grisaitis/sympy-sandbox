# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# referencing:
# http://zulko.wordpress.com/2012/04/15/symbolic-matrix-differentiation-with-sympy/

# <codecell>

import sympy

# <codecell>

A = sympy.symbols('A', commutative=False)

# <codecell>

d = sympy.Function('d', commutative=False)

# <codecell>


