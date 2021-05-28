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
