import numpy as np

index = np.abs(A-z).argmin()
def number_aproximation(A, z):
    print(A[index])


def creatArray():
    A = np.random.randint(0, 500, (208,30))
    print(A)
    z=float(input("Input z: "))
    number_aproximation(A, z)


if __name__ == "__main__":
    creatArray()
