import match
import numpy as np
import cv2


# main programme
def main(file1, file2, color, dispMin, dispMax):
    # load two images
    imgLeft = cv2.imread(file1)
    imgRight = cv2.imread(file2)
 

    # Default parameters
    K = 500
    lambda_ = 100
    lambda1 = 300  # 3 time of base lamdha
    lambda2 = 100  # 1 time of base lamdha
    params = match.Parameters(is_L2=True,
                              denominator=1,
                              edgeThresh=8,
                              lambda1=lambda1,
                              lambda2=lambda2,
                              K=K,
                              maxIter=4)

    # create match instance
    m = match.Match(imgLeft, imgRight, color)

    m.SetDispRange(dispMin, dispMax)
    m = match.fix_parameters(m, params, K, lambda_, lambda1, lambda2)
    m.kolmogorov_zabih()
    m.saveDisparity("./results/disparity_map.png")


if __name__ == '__main__':
    ## For corridor 
    filename_left = "./images/corridorl.jpg"
    filename_right = "./images/corridorr.jpg"
    is_color = True
    disMin = -16
    disMax = 16
    main(filename_left, filename_right, is_color, disMin, disMax)
    
    ## For triclopsi2
    #filename_left = "./images/triclopsi2l.jpg"
    #filename_right = "./images/triclopsi2r.jpg"
    #is_color = True
    #disMin = -16
    #disMax = 16
    #main(filename_left, filename_right, is_color, disMin, disMax)
