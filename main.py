import matplotlib.pyplot as plt
from Projects.PA2.imagepro import *

if __name__ == '__main__':
    # read image
    fname = '/Users/andrewyinschool/Desktop/plant.jpg'
    img = plt.imread(fname)
    
    # resize image
    scale = 0.4
    img2 = resize(img, scale)
    print(img.shape, img2.shape)
    
    # resize image
    scale = 2.5
    img3 = resize(img, scale)
    print(img.shape, img3.shape)
    
    # crop image
    region = (0, 50, 116, 150)
    img4 = crop(img, region)
    print(img.shape, img4.shape)
    
    # blur image
    factor = 5
    red = blur(img[:, :, 0], factor)  # use one channel: red
    green = blur(img[:, :, 1], factor)
    blue = blur(img[:, :, 2], factor)
    img5 = np.stack((red, green, blue), axis=2)  # combine three channels
    print(img.shape, img5.shape)
    
    # convolve image
    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    img6 = convolve(img[:, :, 1], kernel)  # use one channel: green
    print(img.shape, img6.shape)
    
    # show images
    fig = plt.figure()
    
    fig.add_subplot(2, 3, 1)
    plt.imshow(img)
    
    fig.add_subplot(2, 3, 2)
    plt.imshow(img2 / 255)
    
    fig.add_subplot(2, 3, 3)
    plt.imshow(img3 / 255)
    
    fig.add_subplot(2, 3, 4)
    plt.imshow(img4 / 255)
    
    fig.add_subplot(2, 3, 5)
    plt.imshow(img5 / 255)
    
    fig.add_subplot(2, 3, 6)
    plt.imshow(img6 / 255, cmap='Greys')  # use a gray scale
    
    plt.show()
    
    
    