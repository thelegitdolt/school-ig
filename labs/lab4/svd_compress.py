import matplotlib.pyplot as plt
from numpy import linalg as la
import numpy as np
import matplotlib.image as mpimg

def compress(img, k, debug=False):
    img_transposed = np.transpose(img, (2, 0, 1))
    U, s, Vt = la.svd(img_transposed)
    if debug:
        print("The shapes of three the decomposed matrices:", U.shape, s.shape, Vt.shape)

    Sigma = np.zeros(U.shape)

    if debug:
        print("Sigma after decomposition:", Sigma)

    for j in range(3):
        np.fill_diagonal(Sigma[j, :, :], s[j, :])

    img_approx = U @ Sigma[..., :k] @ Vt[..., :k, :]
    img_approx = np.transpose(img_approx, (1, 2, 0))
    img_approx = img_approx - img_approx.min()
    img_approx = img_approx / img_approx.max()
    plt.imshow(img_approx)
    plt.show()


