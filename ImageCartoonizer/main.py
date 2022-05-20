import cv2
def convert(img):
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Gray Image", grayImg)
    noiseReducedImg = cv2.medianBlur(grayImg,7)

    laplacedge = cv2.Laplacian(noiseReducedImg, cv2.CV_8U, ksize=5)
    #cv2.imshow("Laplace edge detection", laplacedge)
    thresholdedges = cv2.threshold(laplacedge, 125, 255, cv2.THRESH_BINARY_INV)
    #cv2.imshow("Sketch image", thresholdedges[1])
    height=img.shape[0]
    width=img.shape[1]
    dim=(200,200)
    # image downsizing
    imgresize=cv2.resize(img, dim, interpolation= cv2.INTER_AREA)

    for i in range (7):
        bilateralimg=cv2.bilateralFilter(imgresize, 9, 9, 7)

    dim= (width, height)
    #image upsizing
    resizedimg=cv2.resize(bilateralimg,dim,interpolation= cv2.INTER_AREA)
    #cv2.imshow("Painting image", resizedimg)
    output=cv2.bitwise_and(resizedimg, resizedimg, mask=thresholdedges[1])

    cv2.imshow("Original Image", img)
    cv2.imshow("Cartoon Image", output)
    cv2.waitKey(0)

img = cv2.imread("C:/Users/Eng Ahmed/Music/dog.jpg")
convert(img)
