# Ömer Malik Kalembaşı 150180112

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

img = plt.imread("clown.bmp")

u, s, v = np.linalg.svd(img)


zeros = np.zeros((200, 320))
for i in range(200):
    zeros[i, i] = s[i]

for n in range(1, 7):
    r = 2**i
    p = np.dot(u, zeros[:, :r])
    svd = np.dot(p, v[:r, :])
    fig.add_subplot(3, 2, n)
    plt.imshow(svd, "gray")

plt.show()
