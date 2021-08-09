# manim_express
[![image](https://img.shields.io/badge/Pypi-0.4.0-green.svg)](https://pypi.org/project/manim_express)
[![image](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![image](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![image](https://img.shields.io/badge/author-kunyuan-orange.svg?style=flat-square&logo=appveyor)](https://github.com/beidongjiedeguang)

## Requirements
```python
manim_kunyuan >= 0.27
sparrow_tool
fake_headers
requests
# helium
# pyperclip
```

------------------------
[**中文说明**](https://github.com/beidongjiedeguang/manim-express/blob/dev/README_zh.md) | [**English**](https://github.com/beidongjiedeguang/manim-express/blob/dev/README.md)
## Install

```bash
pip install manim_express
```

The above steps will automatically install packages `manim_express` and  [`manimlib`](https://github.com/beidongjiedeguang/manimlib) for you. Then you can code with them anywhere.  


# Quick start

* Render an animation: [3b1b:SquareToCircle](https://3b1b.github.io/manim/getting_started/quickstart.html#add-animations)

  ```python
  from manimlib import *
  from manim_express import EagerModeScene
  
  scene = EagerModeScene()
  circle = Circle()
  circle.set_fill(BLUE, opacity=0.5)
  circle.set_stroke(BLUE_E, width=4)
  
  square = Square()
  scene.play(ShowCreation(square))
  scene.play(ReplacementTransform(square, circle))
  
  scene.hold_on()
  ```
  
  Operating graphics:
  * hold down the `d` key on the keyboard and move the mouse to change the three-dimensional perspective.
  * hold down the `s` key on the keyboard and move the mouse to pan the screen
  * hold down the `z` on the keyboard while scrolling the middle mouse button to zoom the screen
  * scroll the middle mouse button to move the screen up and down
  * reset camera view by pressing `r`
  * close the window and exit the program by pressing `q` or `tab`
  * pause the animation by pressing `space` or `ctrl`
  * previews animation clip by pressing `LEFT`
  * next animation clip: `RIGHT`
  * replay current animation clip: `DOWN`
  

* `manim_express` vs `Matplotlib`:  
  In some cases, you may need to install [LaTeX](https://www.latex-project.org/get/#tex-distributions) to render `tex` fonts.  
  Fortunately, online latex compilation option is available. Just set `SceneArgs.use_online_tex=True`

  ```python
  from manimlib import *
  from manim_express import *
  import numpy as np
  SceneArgs.use_online_tex = True # Use online latex compiler
  
  theta = np.linspace(0, 2*np.pi, 200)
  x = np.cos(theta)
  y = np.sin(theta)
  
  # matplotlib
  # import matplotlib.pyplot as plt
  # plt.plot(x, y, color='green', linewidth=2)
  # plt.axis("equal")
  # plt.show()
  
  # manim_express
  scene = EagerModeScene()
  scene.plot(x, y, color=GREEN, width=2, scale_ratio=1)
  scene.show_plot()
  
  scene.hold_on()
  ```
  
  



# Resources

* Wiki  
  https://flyingframes.readthedocs.io/en/latest/index.html  
  https://3b1b.github.io/manim/  
  https://docs.manim.org.cn/  
  https://docs.manim.org.cn/shaders/
  
* 3B1B videos:  
  https://github.com/3b1b/videos





# Examples
* GOA model
  <img src="data/pic/GOA.PNG" width = "900"/>