from dataclasses import dataclass

import cv2
import numpy as np
import rootutils

root = rootutils.setup_root(".", indicator="data", pythonpath=True)

DATA_DIR = root / "data"


@dataclass
class Config:
    video_file = DATA_DIR / "uncalib_chessboard.avi"
    num_calib_samples = 10  # число изображений для калибровки
    board_pattern = [10, 7] # число точек в калибровочном шаблоне
    cell_size = 0.025       # размер клетки в метрах


def main(cfg):
    cap = cv2.VideoCapture(cfg.video_file)

    image_points = []

    while True:
        num_selected_samples = len(image_points)

        if num_selected_samples == cfg.num_calib_samples:
            break
        
        ok, image = cap.read()

        if not ok:
            break

        ok, points = cv2.findChessboardCorners(image, cfg.board_pattern)

        if not ok:
            continue

        show_image = image.copy()
        
        cv2.drawChessboardCorners(show_image, cfg.board_pattern, points, ok)

        cv2.putText(
            show_image, 
            f"Num. Samples: {num_selected_samples}", 
            (15, 30), 
            cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255)
        )

        cv2.imshow("Calibration", show_image)

        key = cv2.waitKey(10)

        if key == ord("q"):
            break
        elif key == ord(" "):
            cv2.waitKey(0)
        elif key == ord("s"):
            image_points.append(points)

    cap.release()
    cv2.destroyAllWindows()

    assert len(image_points) == cfg.num_calib_samples

    num_cols, num_rows = cfg.board_pattern
    cell_size = cfg.cell_size

    object_points = []

    for r in range(num_rows):
        for c in range(num_cols):
            object_points.append((c * cell_size, r * cell_size, 0))

    object_points = np.float32(object_points)
    object_points = [object_points] * cfg.num_calib_samples

    image_height, image_width = image.shape[:2]

    rms, K, dist_coeff, rvecs, tvecs = cv2.calibrateCamera(
        object_points, 
        image_points, 
        (image_width, image_height), 
        None, None, flags=None
    )

    return rms, K, dist_coeff, rvecs, tvecs


if __name__ == "__main__":
    cfg = Config()

    rms, K, dist_coeff, rvecs, tvecs = main(cfg)

    print("# Camera Calibration Results")
    print(f"* RMS error = {rms}")
    print(f"* Camera matrix (K) = \n{K}")
    print(f"* Distortion coefficients (k1, k2, p1, p2, k3) = {dist_coeff}")




