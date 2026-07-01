# Lights Out
---

## About 
---

Lights Out is an electronic puzzle game released by Tiger Electronics in 1995. The game starts with an N x N grid, usually 5x5, of lights in a randomly configured state: on or off. The goal is to turn off all the lights by pressing a sequence of lights that will toggle its direct neighbors.

### Built With

* [![Python][Python-shield]][Python-url]
* [![Pytorch][Pytorch-shield]][Pytorch-url]
* [![Pytorch][PyQt6-shield]][PyQt6-url]

## Getting Started
---

### Prerequisites

* Python/pip
  ```sh
  py -m pip install --upgrade pip
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Implycitt/LightsOut.git

   cd LightsOut
   ```
2. Create a venv 
   ```sh
   python3 -m venv .venv

   source .venv/bin/activate
   ```
3. run the main .py file
    ```sh
    python3 src/main.py 
    ```

## Resources
---

* [Physics for the birds](https://www.youtube.com/watch?v=0fHkKcy0x_U) - original video inspiration 
* [MAA](https://people.sc.fsu.edu/~jburkardt/classes/imps_2017/11_28/2690705.pdf)

## License
---

Distributed under the MIT license. See `LICENSE.txt` for more information.

[forks-shield]: https://img.shields.io/github/forks/Implycitt/LightsOn.svg?style=for-the-badge
[forks-url]: https://github.com/Implycitt/LightsOn/network/members
[stars-shield]: https://img.shields.io/github/stars/Implycitt/LightsOn.svg?style=for-the-badge
[stars-url]: https://github.com/Implycitt/LightsOn/stargazers
[issues-shield]: https://img.shields.io/github/issues/Implycitt/LightsOn.svg?style=for-the-badge
[issues-url]: https://github.com/Implycitt/LightsOn/issues
[license-shield]: https://img.shields.io/github/license/Implycitt/LightsOn.svg?style=for-the-badge
[license-url]: https://github.com/Implycitt/LightsOn/blob/master/LICENSE.txt
[Python-shield]: https://img.shields.io/badge/Python-0769AD?style=for-the-badge&logo=python&logoColor=yellow
[Python-url]: https://python.org 
[Pytorch-shield]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white
[Pytorch-url]: https://pytorch.org 
[PyQt6-shield]: https://img.shields.io/badge/PyQt6-FFD43B?style=for-the-badge&logo=Python&logoColor=blue
[PyQt6-url]: https://pypi.org/project/PyQt6/
