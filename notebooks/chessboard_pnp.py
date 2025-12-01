from dataclasses import dataclass

import cv2
import numpy as np
import rootutils

root = rootutils.setup_root(".", indicator="data", pythonpath=True)

DATA_DIR = root / "data"

@dataclass
class Config:
    video_file = DATA_DIR / "uncalib_chessboard.avi"

    board_pattern = [10, 7] # число точек в калибровочном шаблоне
    cell_size = 0.025       # размер клетки в метрах

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

    box_lower = cfg.cell_size * np.array([
        [4, 2,  0], 
        [5, 2,  0], 
        [5, 4,  0], 
        [4, 4,  0]
    ])

    box_upper = cfg.cell_size * np.array([
        [4, 2, -1], 
        [5, 2, -1], 
        [5, 4, -1], 
        [4, 4, -1]
    ])

    num_cols, num_rows = cfg.board_pattern

    object_points = cfg.cell_size * np.array([
        [c, r, 0] 
        for r in range(num_rows) for c in range(num_cols)
    ])

    while True:
        ok, image = cap.read()

        if not ok:
            break
        
        ok, image_points = cv2.findChessboardCorners(image, cfg.board_pattern)

        if not ok:
            continue

        ok, rvec, tvec = cv2.solvePnP(
            object_points, 
            image_points, 
            cfg.K, 
            cfg.dist_coeff
        )

        if not ok:
            continue
        
        image_box_lower, _ = cv2.projectPoints(
            box_lower, 
            rvec, tvec, 
            cfg.K, cfg.dist_coeff
        )

        image_box_upper, _ = cv2.projectPoints(
            box_upper, 
            rvec, tvec, 
            cfg.K, cfg.dist_coeff
        )

        show_image = image.copy()

        cv2.polylines(
            show_image, 
            [np.int32(image_box_lower)], 
            True, 
            (255, 0, 0), 
            2
        )

        cv2.polylines(
            show_image, 
            [np.int32(image_box_upper)], 
            True, 
            (0, 0, 255), 
            2
        )
        
        pts_lower = image_box_lower[:, 0].astype(int)
        pts_upper = image_box_upper[:, 0].astype(int)

        for (x1, y1), (x2, y2) in zip(pts_lower, pts_upper):
            cv2.line(
                show_image, 
                (int(x1), int(y1)), 
                (int(x2), int(y2)), 
                (0, 255, 0), 
                2
            )

        cv2.imshow("Chessboard PnP", show_image)
        
        key = cv2.waitKey(10)

        if key == ord("q"):
            break
        elif key == ord(" "):
            cv2.waitKey(0)


if __name__ == "__main__":
    cfg = Config()

    main(cfg)