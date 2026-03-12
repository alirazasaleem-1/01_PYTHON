# Importing my own created module
import mymodule
# Two ways to use function insde my module
# First Way:
mymodule.greet("Ali")

# Second way
# This one is more clean

from mymodule import greet
greet("Ali") 