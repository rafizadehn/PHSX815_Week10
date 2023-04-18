# PHSX 815: Week 10
## Central Limit Theorem

This repository includes a script that demonstrates the Central Limit Theorem, showing a random distribution of average values tending toward a Gaussian distribution. 

---

### Homework 11:

### Running the Code
The construction plots are made by the `CentralLimit.py` python file. This file requires python3 to run, and includes the following packages listed at the top of the script:

```
    import sys
    import numpy
    import matplotlib.pyplot as plt
```

To run this script from the terminal in linux, run:

> $ python3 CentralLimit.py

This runs the file with the default parameters which is 100 number of experiements. This can be changed from the terminal.

For example, it may looks something like this in linux:

> $ python3 Minimization.py -Nexp 50

which would run through 50 iterations of this average calculation.

### The Output

The shows the asymptotic tend to Gaussian distribution as the number of experiments increases from 1.

![Figure_111](https://user-images.githubusercontent.com/76142511/232670497-baeb6d48-dba2-4d01-81fd-e0efbea6fd81.png)

SOURCES: Code was taken and adpated from [this GeekforGeek page.](https://www.geeksforgeeks.org/python-central-limit-theorem/)




