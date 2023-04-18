import sys
import numpy
import matplotlib.pyplot as plt

if __name__ == "__main__":
   
    # initial values
    Nexp = 100

    # read the user-provided seed from the command line (if there)
	#figure out if you have to have -- flags before - flags or not
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Nexp = int(sys.argv[p+1])
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-res] resolution of graph" % sys.argv[0])
        print
        sys.exit(1)

    N = 1000

    # number of samples
    num = [1, 2, int(0.5*N), int(N)]
    # list of sample means
    means = []

    # Generating random numbers from -40 to 40 using the num list
    for j in num:
    # Generating seed so that we can get same result
    # every time the loop is run...
        numpy.random.seed(1)
        x = [numpy.mean(
            numpy.random.randint(
                -40, 40, j)) for _i in range(1000)]
        means.append(x)
    k = 0

    # plotting all the means in one figure
    fig, ax = plt.subplots(2, 2, figsize =(8, 8))
    for i in range(0, 2):
        for j in range(0, 2):
            # Histogram for each x stored in means
            ax[i, j].hist(means[k], 75, density = True)
            ax[i, j].set_title(label = num[k])
            k = k + 1
    plt.show() 

