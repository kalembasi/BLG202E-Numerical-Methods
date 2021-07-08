import numpy

def normalize(vector):
    v_n = vector / vector.max()
    return v_n

def find_lambda(vector):
    lambda_ = abs(vector).max()
    return lambda_


# v0 = (1,2,-1)^T
eigen1 = numpy.array([1, 2, -1])
mtx = numpy.array([[-2, 1, 4],
                   [1,1,1],
                   [4,1,-2]])

for i in range(5):
    print("Iteration",i+1,":")
    eigen1 = numpy.dot(mtx, eigen1)
    lambda_x = find_lambda(eigen1)
    eigen1 = normalize(eigen1)
    print("Eigenvalue 1 :", lambda_x)
    print("Eigenvector 1 :", eigen1)

print("\n")
# v0 = (1,2,1)^T

eigen2 = numpy.array([1, 2, 1])
mtx = numpy.array([[-2, 1, 4],
                   [1,1,1],
                   [4,1,-2]])

for i in range(5):
    print("Iteration", i + 1,":")
    eigen2 = numpy.dot(mtx, eigen2)
    lambda_x = find_lambda(eigen2)
    eigen2 = normalize(eigen2)
    print('Eigenvalue 2 :', lambda_x)
    print('Eigenvector 2 :', eigen2)