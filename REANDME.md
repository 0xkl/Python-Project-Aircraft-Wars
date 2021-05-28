# 武装飞船
## 1.0 规划项目
## 2.0 安装Pygame
### 2.1 使用pip安装Pygame包
1. 在Linux和OS X系统中检查是否安装了pip
2. 在Windows系统中检查是否安装了pip
3. 安装pip
4. 在Linux和OS X系统中安装pip
5. 在Windows系统中安装pip

### 2.2 在Linux系统中安装Pygame
### 2.3 在OS X系统中安装Pygame
### 2.4 在Windows系统中安装Pygame
## 3.0 开始游戏项目
### 3.1 创建Pygame窗口以及响应用户的输出
首先，创建一个空的Pygame窗口。使用Pygame编写游戏的基本结构，如下：
- alien_invasion.py
```python
import sys

import pygame

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('飞机大战')

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()

```
首先，我们导入了模块**sys**和**pygame**。模块**pygame**包含开发游戏所需的功能。玩家退出时，我们将使用**sys**来
退出游戏。
游戏《飞机大战》的开头函数**run_game()**中**pygame.init()**初始化背景设置，让**Pygame**能够正常工作，**run_game()**中调用
**pygame.display.set_mode()**来创建 一个名为**screen**的显示窗口，这个游戏的所有图形元素都将在其中绘制，实参
**(1200, 800)**是一个元组，制定了游戏窗口的尺寸，通过将这些尺寸传递给**pygame.display.set_mode()**，我们创建了一个
宽1200像素、高200像素的游戏窗口（你可以根据自己的显示器尺寸调整这些值）。

对象**screen**是一个**surface**。在**Pygame**中，**surface**是屏幕的一部分，用于显示游戏元素，在这个游戏中，每个元素（如敌军和
或飞船）都是一个**surface**。**display.set_mode()**返回的**surface**表示整个游戏窗口。我们激活游戏的动画循环后，每经过一次
循环将自动重新绘制这个**surface**。

这个游戏由一个**while**循环控制，其中包含一个事件循环以及管理屏幕更新的代码。事件是用户玩游戏时执行的操作，如按键或
移动鼠标。为让程序向应事件。我们编写一个事件循环，以侦听事件，并根据发生的事件执行相应的任务，**while**中的**for**循环
就是一个事件循环。

为访问**Pygame**检测到的事件，我们使用方法**pygame.event.get()**。所有键盘和鼠标事件都将促使**for**循环运行。在这个循环中，
我们编写一些列的**if**语句来检测并向应特定事件。例如：玩家单击游戏窗口的关闭按钮时，将检测到**pygame.QUIT**事件，而我们调用
**sys.exit()**来退出游戏。

**pygame.display.flip()**，命令**Pygame**让最近绘制的屏幕可见，在这里，它在每次执行**while**循环时都绘制一个空屏幕，并
擦去旧屏幕，使得只有新屏幕可见。在我们移动游戏结构中，最后一行调用**run_game()**，这将初始化游戏并开始主循环。

编写完**alien_invasion.py**并且执行之后你将看到一个空的**Pygame**窗口。