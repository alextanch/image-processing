from dataclasses import dataclass

import cv2
import numpy as np
import rootutils

root = rootutils.setup_root(".", indicator="data", pythonpath=True)

DATA_DIR = root / "data"

@dataclass
class Config:
    video_file = DATA_DIR / "uncalib_chessboard.avi"

    # коэффициенты дисторсии (k1, k2, p1, p2, k3)
    dist_coeff = np.array([ 
        -2.88814430e-01,  
        1.05033744e-01, 
        -2.08082860e-04,  
        3.38327238e-05,
        -1.89933951e-02
    ])

    # внутренние параметры камеры
    K = np.array([
        [433.44653214, 0, 475.52431698],
        [0, 432.10692526,  289.09156331],
        [0, 0, 1]
    ])
    

def main(cfg):
    cap = cv2.VideoCapture(cfg.video_file)

    rect_map = None

    while True:
        ok, src_image = cap.read()

        if not ok:
            break
        
        if rect_map is None:
            image_height, image_width = src_image.shape[:2]

            rect_map = cv2.initUndistortRectifyMap(
                cfg.K, 
                cfg.dist_coeff, 
                None, None, 
                (image_width, image_height), 
                cv2.CV_32FC1
            )

        mx, my = rect_map

        dst_image = cv2.remap(
            src_image, 
            mx, my, 
            interpolation=cv2.INTER_LINEAR
        )

        cv2.imshow("Distorted", src_image)
        cv2.imshow("Rectified", dst_image)

        key = cv2.waitKey(10)

        if key == ord("q"):
            break
        elif key == ord(" "):
            cv2.waitKey(0)


if __name__ == "__main__":
    cfg = Config()

    main(cfg)
