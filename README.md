##  Материалы курса "Анализ изображений"

| № |Темы| Лекции | Практика |
|:-:|:------:|:------:|:---------:|
| 1  |Цветовые и геометрические операции над изображениями|[lecture_01.pdf](lectures/lecture_01.pdf)| [notebook_01.ipynb](notebooks/notebook_01.ipynb)|
| 2  |Пространственная и частотная фильтрация изображений|[lecture_02.pdf](lectures/lecture_02.pdf)| [notebook_02.ipynb](notebooks/notebook_02.ipynb)|
| 3  |Методы улучшения качества изображений|[lecture_03.pdf](lectures/lecture_03.pdf)|[notebook_03.ipynb](notebooks/notebook_03.ipynb)|
| 4  |Детекция границ и линий на изображениях|[lecture_04.pdf](lectures/lecture_04.pdf)|[notebook_04.ipynb](notebooks/notebook_04.ipynb)|
| 5  |Детекция и сопоставление ключевых точек на изображениях|[lecture_notes_05.pdf](lectures/lecture_notes_05.pdf)|[notebook_05.ipynb](notebooks/notebook_05.ipynb)|
| 6  |Сегментация изображений|[lecture_06.ipynb](lectures/lecture_06.ipynb)|[lecture_06.ipynb](lectures/lecture_06.ipynb)|
| 7  |Гомография. Сшивка изображений|||
| 8  |Проективная модель камеры. Калибровка камеры|||
| 9  |Эпиполярная геометрия. Относительное положение камер|||
| 10 |Реконструкция 3D сцены|||
| 11 |Методы понижения размерности многомерных данных. Классификация изображений|||


### Установка Python окружения

- Установить [miniconda](https://anaconda.com/docs/getting-started/miniconda/install) для вашей [системы](https://repo.anaconda.com/miniconda)

    ```bash
    curl -O https://repo.anaconda.com/miniconda/Miniconda3-py312_24.9.2-0-MacOSX-arm64.sh

    sh Miniconda3-py312_24.9.2-0-MacOSX-arm64.sh -b

    ~/miniconda3/bin/conda init --all

    # restart terminal
    ```
- Создать и активировать окружение 
    ```bash
        conda create --name env python=3.12 ffmpeg -y
        conda activate env
    ```
- Установить зависимости
    ```bash
        git clone git@github.com:alextanch/image-processing.git
        cd image-processing
        pip install -r requirements.txt
    ```

- Удаление окружения при необходимости
    ```bash
        conda deactivate
        conda remove -n env --all
    ```



