Tips and tricks for python competition algorithms
=================================================

# Python and floating-point variables

- When comparing float variables to float literals, e.g. 'if somevar == 1.0', remember to round off the value of 'somevar', as floating point error accumulation might result in var being '1.00000000017' instead of exactly '1.0'. One should therefore check with 'if round(var, 10) == 1.0' instead.
