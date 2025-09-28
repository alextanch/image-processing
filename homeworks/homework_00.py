from pathlib import Path

import cv2
from omegaconf import OmegaConf


def main(cfg):
    image = cv2.imread(cfg.image)

    cv2.circle(image, cfg.point, cfg.radius, cfg.color, thickness=-1)
    cv2.imshow("Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    task = Path(__file__).stem
    cfg = OmegaConf.load("params.yaml")[task]

    main(cfg)
