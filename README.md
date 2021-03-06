# 武装飞船
## 1.0 规划项目
在开始编写代码之前，我们要安装Pygame库。话不多说，我们来介绍一下如何在Linux、Mac_OS、Windows中安装Pygame。
## 2.0 安装Pygame
### 2.1 使用pip安装Pygame包
2021年了现在大多数比较新的Python版本都会自带pip，因此我们可以先简单来检查一下我们的系统是否安装了pip。在Python3中，pip有时候经常被称为pip3。
1. 在Linux和OS X系统中检查是否安装了pip

打开一个命令行窗口，执行一下命令：
```bash
$ pip --version
pip 20.3.4 from /usr/lib/python3/dist-packages/pip (python 3.8)
$
```
输入命令且到你按下回车键的那一刻，出现此消息证明你的电脑安装了Python Pip。如果出现类似的输出，则证明你安装了pip。如果没有或者有错误的消息接下来我们将研究如何安装。

2. 在Windows系统中检查是否安装了pip
```bash
C:/> python -m pip --version
pip 21.0.1 from C:\Users\ASUS\AppData\Local\Programs\Python\Python37\lib\site-packages\pip (python 3.7)
C:/> 
```
输入命令且到你按下回车键的那一刻，出现此消息证明你的电脑安装了Python Pip。
如果出现类似的输出，则证明你安装了pip。如果没有或者有错误的消息接下来我们将研究如何安装。

3. 安装pip
```bash
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
首先先下载pip安装脚本，不同的系统都适用这条命令。

4. 在Linux和OS X系统中安装pip
以管理员的身份运行这条命令。
```bash
$ sudo python get-pip.py
```
> 注意：如果你启动终端会话使用的命令时python3，那么在这里应该使用
> sudo python3 get-pip.py 进行安装。

5. 在Windows系统中安装pip

使用下面命令运行get-pip.py
```bash
C:/> python get-pip.py
```
> 注意：如果你启动终端会话使用的命令时python3，那么在这里应该使用
> sudo python3 get-pip.py 进行安装。

### 2.2 在Linux系统中安装Pygame
如果你使用的时python2.7，请使用包管理器来安装Pygame。打开一个命令行窗口，并执行下面的命令：
```bash
$ sudo apt-get install python-pygame
```
执行如下这些命令，会在终端检查安装状态：
```bash
$ python
Python 3.8.6 (default, XXX XX XXXX, XX:XX:XX) 
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pygame
>>>
```
如果没有任何输出，就说明pygame导入了python中。
如果你是python3，就需要执行两个步骤：安装pygame以来的库；下载并安装pygame。
执行下面的命令来安装pygame以来的库。
```bash
$ sudo apt-get install python3-dev mercurial
$ sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev
$ sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
$ sudo apt-get install libswscale-dev libsmpeg-dev libavcode-dev
$ sudo apt-get install python-numpy
```
接下来，执行下面的命令来安装pygame：
```bash
$ pip install --user hg+http://bitbucket.org/pygame/pygame
```
### 2.3 在OS X系统中安装Pygame
要安装pygame依赖的包，需要Homebrew。Homebrew安装如下：
```bash
$ xcode-select --install
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$
```
安装pygame依赖的库，输入以下命令：
```bash
$ brew install hg sdl sdl_image sdl_ttf
$ brew install sdl_mixer portmidi
```
使用下面命令来安装pygame
```bash
$ pip install --user hg+http://bitbucket.org/pygame/pygame
```
启动一个python终端会话，并导入pygame检擦是否安装成功：
```bash
$ python
Python 3.8.6 (default, XXX XX XXXX, XX:XX:XX) 
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pygame
>>>
```
### 2.4 在Windows系统中安装Pygame
启动cmd命令行窗口，输入一下命令：
```bash
C:/> pip install pygame
```

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
首先，我们导入了模块 **sys** 和 **pygame** 。模块 **pygame** 包含开发游戏所需的功能。玩家退出时，我们将使用 **sys** 来
退出游戏。
游戏《飞机大战》的开头函数 **run_game()** 中 **pygame.init()** 初始化背景设置，让 **Pygame** 能够正常工作，**run_game()** 中调用
**pygame.display.set_mode()** 来创建 一个名为 **screen** 的显示窗口，这个游戏的所有图形元素都将在其中绘制，实参
**(1200, 800)** 是一个元组，制定了游戏窗口的尺寸，通过将这些尺寸传递给 **pygame.display.set_mode()** ，我们创建了一个
宽1200像素、高200像素的游戏窗口（你可以根据自己的显示器尺寸调整这些值）。

对象 **screen**是一个 **surface** 。在 **Pygame** 中，**surface** 是屏幕的一部分，用于显示游戏元素，在这个游戏中，每个元素（如敌军或飞船）
都是一个 **surface** 。 **display.set_mode()** 返回的 **surface** 表示整个游戏窗口。我们激活游戏的动画循环后，每经过一次
循环将自动重新绘制这个 **surface**。

这个游戏由一个 **while** 循环控制，其中包含一个事件循环以及管理屏幕更新的代码。事件是用户玩游戏时执行的操作，如按键或移动鼠标。
为让程序向应事件。我们编写一个事件循环，以侦听事件，并根据发生的事件执行相应的任务，**while** 中的 **for** 循环就是一个事件循环。

为访问 **Pygame** 检测到的事件，我们使用方法 **pygame.event.get()** 。所有键盘和鼠标事件都将促使 **for** 循环运行。在这个循环中，
我们编写一些列的 **if** 语句来检测并向应特定事件。例如：玩家单击游戏窗口的关闭按钮时，将检测到 **pygame.QUIT** 事件，而我们调用
**sys.exit()** 来退出游戏。

**pygame.display.flip()** ，命令 **Pygame** 让最近绘制的屏幕可见，在这里，它在每次执行 **while** 循环时都绘制一个空屏幕，
并擦去旧屏幕，使得只有新屏幕可见。在我们移动游戏结构中，最后一行调用 **run_game()** ，这将初始化游戏并开始主循环。

编写完 **alien_invasion.py** 并且执行之后你将看到一个空的 **Pygame** 窗口。

### 3.2 设置背景色
Pygame 默认创建一个黑色屏幕，这样子看着眼睛太难受了，我们为《飞机大战》游戏设置一个新的背景颜色。
- alien_invasion.py
```python
--snip--
def run_game():
    # 初始化pygame、设置和屏幕对象
    --snip--
    pygame.display.set_caption('飞机大战')

    # 设置背景色
    bg_color = (230, 230, 230)

    # 开始游戏主循环
    while True:

        # 监听键盘和鼠标事件
        --snip--

        # 每次循环时都会重绘屏幕
        screen.fill(bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```
首先，我们创建了以种背景颜色，并将其存储在 **bg_color** 中，该颜色只需指定一次，因此我们在进入主 **while** 循环前定义它。

在 **Pygame** 中，颜色始以 **RGB** 值指定的。这种颜色由红色、绿色和蓝色值组成，其中每个值的取值范围是 **0~255** 。颜色值 **(255,0,0)**
表示红色，**(0,255,0)** 表示绿色，而 **(0,0,255)** 表示蓝色。通过组合不同的 **RGB** 值，可创建1600万种颜色，在颜色值 **(230,230,230)** 中，
红色、蓝色和绿色量相同，它将背景设置为一种浅灰色。

在 **while** 循环中，我们调用 **screen.fill()** ，用背景色填充屏幕：这个方法只接受一个实参，以种颜色。

### 3.3 创建设置类
每次给游戏添加新功能时，通常也将引入一些新设置。下面来编写一个名为 **settings** 的模块，其中包含一个为 **Settings** 的类，
用于将所有设置存储在一个地方，以免在代码中到处添加设置。这样，我们就能传递一个设置对象，而不是众多不同的设置。另外，
这让函数调用更简单，且在项目增大时修改游戏的外观更容易；要修改游戏，只需要修改 **settings.py** 中的一些值，而无需查找散布在文件中的不同位置。
下面是最初的 **Settings** 类：

- settings.py
```python
class Setting() :
    """存储《飞机大战》所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

```
为创建 **Settings** 实列并使用它来访问设置，将 **alien_invasion.py** 修改成下面这样子：
- alien_invasion.py
```python
--snip--
import pygame 

from settings import Settings
def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('飞机大战')

    # 设置背景色
    bg_color = (230, 230, 230)

    # 开始游戏主循环
    while True:

        # 监听键盘和鼠标事件
        --snip--

        # 每次循环时都会重绘屏幕
        screen.fill(ai_settings.bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()

```
在主程序文件中，我们导入 **Settings** 类，调用 **pygame_init()** ，在创建一个 **Settings** 类，并将其存储在变量 **ai_settings** 中。
创建屏幕时，使用了 **ai_screen_width** 和 **ai_screen_height** ;接下来填充屏幕时，也使用了 **ai_settings** 来访问背景色。

## 4.0 添加飞船图像
下面将飞船加入到游戏中。为了在屏幕上绘制玩家的飞船，我们将加载一幅图像，再使用 **Pygame** 方法 **blit()** 绘制它。

为游戏选择素材时，务必要注意许可。最安全、最不费钱的方式是使用 [pixabay](http://pixabay.com/) 等网站提供的图形，这些图形无需许可，你可以对其进行修改。

在游戏中几乎可以使用任何类型的图像文件，但使用位图 **(.bmp)** 文件最为简单，因为 **Pygame** 默认加载位图。
虽然可配置 **Pygame** 以使用其他文件类型，但有些文件类型要求你在计算机上安装相应的图像库。大多数图像都为 **.jpg** 、**.png** 或 **.gif** 格式，
但可使用 **Photoshop**、 **GIMP** 和 **Paint**等工具将其转换为位图。

选择图像时，要特别注意其背景色。请尽可能选择背景透明的图像，这样可使用图像编辑器将其背景设置为任何颜色。图像的背
景色与游戏的背景色相同时，游戏看起来最漂亮；你也可以将游戏的背景色设置成与图像的背景色相同。

就游戏《飞机大战》而言，你可以使用文件 **ship.bmp**（如图4-1所示），这个文件在[ship.bmp](./images) 中找到。
这个文件的背景色与这个项目使用的设置相同。请在主项目文件夹 **alien_invasion**中新建一个文件夹，将其命名为
**images**，并将文件 **ship.bmp** 保存到这个文件夹中。

![4-1 ship.bmp 图片](./images/ship.jpg)


### 4.1 创建Ship类
选择用于表示飞船的图像后，需要将其显示到屏幕上。我们创建一个名为 **ship** 的模块，其中包含 **Ship** 类，它负责管理飞船的大部份行为。
- ship.py
```python
import pygame

class Ship():

    def __init__(self, screen):
        """初始化飞船并设置其初始化位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
```
首先，我们导入 **pygame** 模块。 **Ship** 的方法__init__()接受两个参数：引用 **self** 和 **screen** ，其中后者指定了要将飞船绘制到什么地方。
为加载图像，我们调用了 **pygame.image.load()** 。这个函数返回一个辩是飞船的 **surface** ，而我们将这个 **surface** 存储到了 **self.image** 中。

加载图像后，我们使用 **get_rect()** 获取相应 **surface** 的属性 **rect** 。 **Pygame** 的效率之所以会如此之高，一个原因是让它能够处理矩形
（rect对象）一样处理游戏元素，即使他们的形状并非矩形。像处理矩形一样处理游戏元素之所以高效，是因为矩形是简单的几何形状。这种
做法的效果通常很好，游戏玩家几乎注意不到我们处理的不是游戏元素的实际形状。

处理 **rect** 对象是，可使用矩形四角和中心 *x* 和 *y* 坐标。可通过设置这些值来指定矩形的位置。

要将游戏元素居中，可设置相应 **rect** 对象的属性 **center、centerx、centery** 。 要让游戏元素与屏幕边缘对齐，可使用属性
top、bottom、left或right；要调整游戏元素和水平或垂直位置，可使用属性 *x* 和 *y* ，它们分别是相应矩形左上角的 *x* 和 *y*坐标。
这些属性让你无需要去做游戏开发人员原本需要手工完成的计算，你经常会用到这些属性。

    - 注意：
    - 在Pygame中，原点(0, 0)位于屏幕左上角，向右下方移动时，坐标值将增大。
    - 在1200×800的屏幕上，原点位于左上角，而右下角的坐标为(1200, 800)。

我们将把飞船放在屏幕底部中央。 所以，首先将表示屏幕的矩形存储在 **self.screen_rect** 中，将 **self.rect_centerx** （飞船中心的 *x* 坐标）
设置为表示屏幕的矩形的属性 **centerx** ，并将 **self.rect.bottom** （飞船下边缘的 *y* 坐标）设置为表示屏幕的矩形的属性 **bottom** 。
**Pygame** 将使用 **rect** 属性来放置飞船图像，使其与屏幕下边缘对齐并水平居中。

我们定义了方法 **blitme()** ，它根据 **self.rect** 指定的位置将图像绘制到屏幕上。

### 4.2 在屏幕上绘制飞船
- alien_invasion.py
```python
--snip--
def run_game():
    # 初始化pygame、设置和屏幕对象
    --snip--
    pygame.display.set_caption('飞机大战')

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:

        # 监听键盘和鼠标事件
        --snip--

        # 每次循环时都会重绘屏幕
        screen.fill(bg_color)
        ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```
我们导入 **Ship** 类，并在创建屏幕后创建一个名为 **ship** 的 **Ship** 实列。必须在主 **while** 循环前面创建 **ship** 飞船，以免每次循环时都
会创建一艘飞船。填充背景后，我们调用 **ship.blitme()** 将飞船绘制到屏幕上，确保出现在背景前面。

## 5.0 重构：game_functions模块
在大型项目中，经常需要在添加新代码前重构以有的代码。重构旨在简化以有代码的结构，使其更容易扩展。所以我们将创建一个名为 **game_functions** 的新模块，
它将存储大量让该项目运行的函数。通过创建模块 **game_functions** ，可避免 **alien_invasion.py** 太长太杂乱，并使其逻辑更容易理解。

### 5.1 函数check_events()
我们首先先把管理事件的代码移到一个名为 **check_events()** 函数中，以简化 **run_game()** 并隔离事件管理循环，可将事件管理与游戏的其他方面（如
更新屏幕）进行分离。

将 **check_events()** 放在一个名为 **game_functions** 的模块中：

- game_functions.py
```python
import sys

import pygame

def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
```
这个模块中导入了事件检查循环要使用的 **sys** 和 **pygame** 。当前，函数 **check_events()** 不需要任何形参，其函数体复制了 **alien_invasion.py**的事件循环。
下面来修改 **alien_invasion.py** ，使其导入模块 **game_functions** ，并将事件循环替换为对函数 **check_events()** 的调用：

- alien_invasion.py
```python 
import pygame

from settings import Settings
from ship import Ship
import game_functuons as gf

def run_game()：
    --snip--
    # 开始游戏主循环
    while True:
        gf.check_events()

        # 让最近绘制的屏幕可见
        --snip--
```
在主程序文件中，不再需要直接导入 **sys** ，因为当前只在模块 **game_functions** 中使用了它。出于简化的目的，我们给导入的模块 **game_functions** 指定了别名 **gf** 。

### 5.2 函数update_screen()
为了进一步简化 **run_game()** ，下面将更新屏幕的代码以到一个名为 **update_screen()** 的函数中，并将这个函数放在模块 **game_functions** 中：

- game_functions.py
```python
--snip--

def check_events() :
    --snip--

def update_screen(ai_settings, screen, ship) :
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
```
新函数 **update_screen()** 包含了三个形参： **ai_settings** 、 **screen** 和 **ship** 。 现在需要将 *alien_invasion.py* 的 **while**循环中更新屏幕的代码替换为对函数 **update_screen()** 的调用：

- alien_invasion.py
```python
--snip--
    # 开始游戏主循环
    while True :
        gf.check_events()
        gf.update_screen()

run_game()
```
这两个函数让 **while** 循环更简单，并让后续开发更容易；在模块 **game_functions** 而不是 **run_game()** 中完成大部分工作。

鉴于我们一开始只想使用一个文件，因此没有立刻引入模块 **game_functions** 。这让你能够了解实际的开发过程；一开始将代码编写得尽可能简单，并在项目越来越复杂时进
行重构。

对代码进行重构使其更容易扩展后，可以开始处理游戏的动态方面了。

## 6.0 驾驶飞船
下面来让玩家能够左右移动飞船。因此，我们将写代码，在用户按左或右箭头时做出向应。我们将首先专注于向右移动，在使用同样的原理来空指相左移动，通过这样子做，
我们将会明白如何控制屏幕图像的移动。

### 6.1 响应按键
每当用户按键时，都将在 **Pygame** 中注册一个事件。事件都是通过方法 **pygame.event.get()** 获取的，的因此在函数 **check_events()** 中，我们需要指定要检查哪些类型的事
件。每次按键都会被注册为一个KEYDOWN事件。

检测到 **KEYDOWN** 事件时，我们需要检查按下的是否是特定的键。例如：如果按下的是右箭头。我们就增大飞船的 **rect.centerx** 值，将飞船向右移动。

- game_functions.py

```python
def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()

        elif event.type == pygame.KEYDOWN :
           if event.key == pygame.K_RIGHT :
                # 向右移动飞船
                ship.rect.centerx += 1
```
我们在函数 **check_events()** 中包含形参 **ship** ，因为玩家按右箭头时，需要将飞船向右移动。在函数 **check_events()** 内部，我们在事件循环中添加了一个 **elif** 代码
块，以便在 **Pygame** 检测到 **KEYDOWN** 事件时做出响应。我们读取属性 **event.key** ，以检查按下的是否时右箭头键 **（pygame.K_RIGHT）** 。如果按下的是右
箭头键，就将 **ship.rect.centerx** 的值加1，从而将飞船向右移动。

在 *alien_invasion.py* 中，我们需要更新调用 **check_events** 代码，将 **ship** 作为实参传递给它：

- alien_invasion.py
```python
--snip--
    # 开始游戏主循环
    while True :
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)
```
如果现在运行 *alien_invasion.py* ，则每按右箭头键一次，飞船都将向右移动1像素。这是一个开端，但并非控制飞船的高效方式。下面来改进控制方式，允许持续移动。

### 6.2 允许不断移动
玩家按住右箭头键不放时，我们希望飞船不断地向右移动，直到玩家松开为止。我们将让游戏检测 **pygame.KEYUP** 事件，一边玩家松开右箭头键时我们额能够知道这一点，然
后，我们将结合使用 **KEYDOWN 和KEYUP** 事件，以及一个名为 **moving_right** 的标志来实现持续移动。

飞船不动时，标志 **moving_right** 将为 *False* 。玩家按下右箭头键时，我们将这个标志设置为 *True* ；而玩家松开时，我们将这个标志重新设置为 *Flase* 。

飞船的属性都有 **Ship** 类空指，因此我们将这个类添加一个名为 **moving_rigght** 的属性和一个名为 **update()** 的方法。方法 **update()** 检测标志 **moving_right** 的状态，
如果这个标志为 *True* ，就调制飞船的位置。每当需要调整飞船的位置时，我们都调用这个方法。

以下时对 **Ship**类所做的修改：

- ship.py
```python
class Ship():

    def __init__(self, screen):
        """初始化飞船并设置其初始化位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False


    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right:
            self.rect.centerx += 1


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
```
在方法__init__()中，我们添加了属性 **self.moving_right** ，并将其初始值设置为 *False* 。 接下来，我们添加了方法 **update()** ，它在前述标志为 *True*时向
右移动飞船。

下面来修改 **check_events()** ，使其在玩家按下右箭头键时将 **moving_right** 设置为 *True* ，并在玩家松开时将 **moving_right** 设置为 *False*：

- game_functions.py
```python
def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()

        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                ship.moving_right = True

        elif event.type == pygame.KEYUP :
            if event.key == pygame.K_RIGHT :
                ship.moving_right = False
```

我们用 **ship.moving_right == True** ，修改游戏玩家按下右键箭头键时响应的方式；不直接调整飞船的位置，而是将 **moving_right** 设置为True。
在 **elif event.type == pygame.KEYUP** 用于响应KEYUP事件；玩家松开右箭头键 **（K_RIGHT）** 时，我们将 **moving_right** 设置为 *False* 。

最后，我们需要修改 *alien_invasion.py* 中的 **while** 循环，以便每次执行循环时都调用飞船方法 **update()** :
```python
--snip--
    # 开始游戏主循环
    while True :
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
```
飞船的位置将在检测到键盘事件后（但在更新屏幕前）更新。这样，玩家输入时，飞船的位置将更新，从而确保使用更新后的位置将飞船绘制到屏幕上。

如果你现在运行，*alien_invasion.py* 并按住右箭头键，飞船将不断地向右移动，直到你松开为止。

### 6.3 左右移动
能够不断地向右移动后，添加向做移动的逻辑很容易。我们再次修改Ship类和函数 **check_events()** 。以下显示了对 **Ship** 类的方法__init__()和 **update()** 所做
的相关修改：

- ship.py
```python
--snip--
def __init__(self, screen):
        """初始化飞船并设置其初始化位置"""
        --snip--
        # 移动标志
        self.moving_right = False
        self.moving_lift = False


    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_lift:
            self.rect.centerx -= 1
```
在方法__init__()中，我们添加了标志 **self.moving_left** ；在方法 **update()** 中，我们添加了一个 **if** 代码块而不是**elif**代码块，这样如果玩家同时按下了左右箭头
键，将先增大飞船的 **rect.centerx** 值，在降低这个值，即飞船的位置保持不变。如果使用了一个 **elif**代码块来处理向左移动的情况，右箭头键将始终处于优先地位。从向做移
动切换到向右移动时，玩家可能同时按住左右箭头键，在这种情况下，前面的做法让移动更准确。

我们还需要对 **check_events()** 做两个方面的调整：

- game_functions.py
```python
def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()

        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                ship.moving_right = True
            elif event.key == pygame.K_LEFT :
                ship.moving_lift = True

        elif event.type == pygame.KEYUP :
            if event.key == pygame.K_RIGHT :
                ship.moving_right = False
            elif event.key == pygame.K_LEFT :
                ship.moving_lift = False
```
如果因玩家按下 **K_LEFT** 键而触发了 **KEYDOWN** 事件，我们就将 **moving_left** 设置为 *True*；如果因玩家松开了 **K_LEFT** 而触发了 **KEYUP** 事件，我们就将 **moving_left** 设置
为 *False* 。这里之所以可以使用 **elif** 代码块，是因为每个时间都只与一个键相关联；如果晚间同时按下了左右箭头键，将检测到两个不同的事件。

如果词是运行了 *alien_incasion.py* ，将能够不断地左右移动飞船；如果你同时按左右键头键，飞船将纹丝不动。

下面来进一步优化飞船的移动方式；调整飞船的熟读；限制飞船的移动距离，以免它移动屏幕外面去。

### 6.4 调整飞船的速度
当前，每次执行 **while** 循环时，飞船最多移动1个像素，但是我们可以在Setting类中添加属性 **ship_speed_factor** ，用于控制飞船的速度。我们将根据这个属性决定飞船在
每次循环时最多移动多少距离。下面演示如何在 *settings.py* 中添加这个新属性：

- setting.py
```python
class Settings() :
    """存储《飞机大战》所有设置的类"""

    def __init__(self):
        --snip--

        # 飞船的设置
        self.ship_speed_factor = 1.5

```
我们将 **ship_speed_factor** 的初始值设置为1.5。需要移动飞船时，我们将移动1.5像素而不是1像素。

通过将速度设置指定小数值，可以在后面加快游戏的节奏时更细致地控制飞船。然而，**rect** 和 **centerx** 等属性只能存储整数值，因此我们需要对 **Ship** 类做些修改：

- ship.py
```python
class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始化位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        --snip--

        # 将每艘新飞船放在屏幕底部中央
        --snip--
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_lift = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right :
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_lift :
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        
    def blitme(self):
        --snip--
```
首先，我们在__init__()的形参列表中添加了 **ai_settings** ，让飞船能够获取其熟读设置。接下来，我们将形参 **ai_settings** 的值存储在一个 **self.ai_setting** 属性中，以便能够
在 **update()** 中使用它。鉴于现在调整飞船的位置时，将增加或减去一个单位为像素的小数值，一次需要将位置存储在一个能够存储小数值的变量中。可以使用小数来
设置 **rect** 的属性，单 **rect** 只能存储这个值的整数部分。为准确地存储飞船的位置，我们定义了一个可存储小数值的新属性 **self.conter** 。我们使用函数 **float()**
将 **self.rect.centerx** 的值转换为小数，并将结果保存到 **self.center** 中。

现在在 **update()** 中调整飞船的位置时，将 **self.center** 的值增加或减去 **ai_settings.ship_speed_factor** 。更改 **self.center** 后，我们在根据它来
跟新控制飞船位置的 **self.rect.centerx** 。 **self.rect.centerx** 将只存储 **self.center** 的整数部分，但对显示飞船而言，这问题不大。

在 *alien_invasion.py* 中创建 **Ship** 实列时，需要传入实参 **ai_settings** ：

- alien_invasion.py
```python
--snip--
def run_game():
    --snip--
    # 船舰飞船
    ship = Ship(ai_settings, screen)
    --snip--
```
现在，只要 **ship_speed_factor** 的值大于1，飞船的移动速度就会比以前更快。这有助于让飞船的反应速度足够快，能够将外星人射下来，还让我们够随着游戏的进行加快
游戏的节奏。

### 6.5 限制飞船的活动范围
当前，如果玩家按住箭头键的事件足够长，飞船将移动到屏幕外面，消失得无影无踪。下面来修复这种问题，让飞船达到屏幕边缘后停止移动。为此，我们将修改 **Ship** 类得方
法 **update()** ：

- ship.py
```python
def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:    # <1>
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_lift and self.rect.lift > 0:    # <2>
            self.center -= self.ai_setting.ship_speed_factor
            
        # 根据self.center更新rect对象
        self.rect.centerx = self.center
```

上诉代码在修改 **self.center** 的值之前检查飞船的位置。 **self.rect.right** 返回飞船外界矩形的右边缘 *x* 坐标，如果值小于 **self.screen_rect.right** 的值。
就说明飞船未触及屏幕右边缘（见<1>）。左边边缘的情况与此类似：如果 rect的左边缘的 *x* 坐标大于零，说明飞船未触及屏幕左边缘（见<2>）。这确保仅当飞船在屏幕内时，
菜调整 **self.center** 的值。

如果此时运行 *alien_invasion.py* ，飞船将在初级屏幕左边缘或右边缘停止移动。

### 6.6 重构check_events()
随着游戏开发的进行，函数 **check_events()** 将会越来越长，我们将其部分代码放在两个函数中：一个处理 **KEYDOWN** 事件，另一个处理 **KEYUP** 事件:

- game_functions.ppy
```python
def check_keydown_events(event, ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_lift = True

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_lift = False

def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()

        elif event.type == pygame.KEYDOWN :
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP :
            check_keyup_events(event, ship)
```
我们创建了两个新函数： **check_keydown_events()** 和 **check_keyup_events()** ，它们都包含形参 **event** 和 **ship** 。这两个函数的代码都是从 **check_events()** 中复制
而来的，因此我们将函数 **check_events** 中相应的代码替换成了对这两个函数的调用。现在，函数 **check_events()** 更简单，代码结构更清晰。这样，在其中响应其他玩家
输入时将更容易。

## 7.0 简单回顾
接下来我们将添加射击功能，这需要新增一个名为bullet.py的文件，并对一些已有的文件进行修改。当前，我们有四个文件其中包含了很多类、函数和方法。添加其他功能之前，为让你
轻蹙这个醒目的组织结构，先来回顾一下这些文件。

### 7.1 alien_invasion.py
游戏主文件 *alien_invasion.py* 创建了一系列整个游戏都要用到的对象：存储在 **ai_settings** 中的设置、存储 **screen** 中的主显示 **surface** 以及一个飞船实例。
文件 *alien_invasion.py* 还包含游戏的主循环，这是一个调用 **check_events()** 、 **ship.update()** 和 **update_screen()** 的 **while**循环。
要玩《飞机大战》，只需要运行文件 **alien_invasion.py** 。其他的文件(setting.py、game_functions.py和ship.py）包含的代码被直接或间接地导入到这个文件中。

### 7.1 setting.py
文件 *setting.py* 包含了 **Setting** 类这个类只包含方法__init__()，它初始化控制游戏外观和飞船速度地属性。

### 7.2 game_functions.py
文件 *game_functions.py* 包含一系列函数，游戏地大部分工作都是由它们完成的。函数 **check_events()** 检测相关的事件，如按键和松开并使用辅助函数
 **check_keydown_events()** 和 **check_keyup_events()** 来处理这些事件。就目前而言，这些函数管理飞船的移动。模块 **game_functions** 还包含函数
 **update_screen()** ，它用于在每次执行主循环时都会重绘屏幕。

### 7.3 ship.py
文件 *ship.py* 包含 **Ship** 类，这个类包含方法__init__()、管理飞船位置的方法 **update()** 以及在屏幕上绘制飞船的图像存储在文件夹 **images** 下的
文件 *ship.bmp* 中。

## 8.0 射击
接下来添加设计功能。我们将编写玩家按空格键时发射子弹（小矩形）的代码。子弹将在屏幕中向上穿行。抵达屏幕上边缘后消失。

### 8.1 添加子弹设置
首先，更新 *setting.py* ，在其方法__inti__()末尾存储新类Bullet所需的值：


- setting.py
```python
def __init__():
    --snip--
    # 子弹设置
    self.bullet_speed_factor = 1
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = (60,60,60)
```
这些设置创建宽3像素、高15像素的深色子弹。子弹的速度比飞船稍低。

### 8.2 船舰Bullet类
下面来创建存储 **Bullet**类的文件 *bullet.py* ，其前半部分如下：

- bullet.py
```python
import pygame

from pygame.sprite import Sprite

class Bullet(Sprite) :
    def __init__(self, ai_settings, screen, ship) :
    """一个对飞船发射的位置船舰一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0, 0)处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_setting.bullet_height)    # <1>

        self.rect.centerx = ship.rect.centerx    # <2>
        self.rect.top = ship.rect.top    # <3>

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)    # <4>
        self.color = ai_settings.bullet_color    # <5>
        self.speed_factor = ai_settings.bullet_speed_factor

```
**Bullet** 类继承了我们从模块 **pygame.sprite** 中导入的 **Sprite** 类。通过使用精灵，可将游戏中相关的元素编组，进而同时操作编组中的所有元素。为创建子弹实例，需要
向__init__()传递 **ai_settings** 、 **screen** 和 **ship** 实例，还调用 **super()** 来继承 **Sprite** 。

    - 注意：
    - 代码super(Bullte, self).__init__()使用了Python2.7语法。这种语法也适用于Python3，但那你也可以将这行代码简写成super().__init__()。

在# <1>处，我们创建了子弹的属性 *rect* 。子弹并非基于图像的，因此我们必须使用 **pygame.Rect()** 类从空白开始创建了一个矩形。创建这个类的实例时，必须提供矩形左上角的
*x* 坐标和 *y* 坐标，还有矩形的宽度和高度。我们在(0,0)处创建了这个矩形，但接下来的两行代码将其移到了正确的位置，因为子弹的初始位置取决于飞船当前的位置。子弹的宽度
和高度是从 **ai_setting** 中获取的。

在# <2>处，我们将子弹的 **centerx** 设置为飞船的 **rect.centerx**。子弹应从飞船顶部射出，因此我们将表示子弹的 **rect** 的 **top** 属性设置为飞船的 **rect**的 **top** 属性，让子弹看
起来像是飞船中射出去的，见# <3>。

我们将子弹的 *y* 坐标存储为小数值，以便能够微调子弹的速度（见# <4>）。在# <5>处，我们将子弹的颜色和速度设置分别存储到 **self.color** 和 **self.speed_factor** 中
下面是 *bullet.py* 的第二部分——方法 **update()** 和 **draw_bullet()** 。

- bullet.py
```python
def update(self):
    """向上移动子弹"""
    # 更新表示子弹位置的小数值
    self.y -= self.speed_factor    # <1>

    # 更新表示子弹的rect的位置
    self.rect.y = self.y    # <2>

def draw_bullet(self):
    """在屏幕上绘制子弹"""
    pygame.draw.rect(self.screen, self.color, self.rect)    # <3>
```
方法 **update()** 管理子弹的位置。发射出后，子弹在屏幕中向上移动，这意味着 *y* 坐标将不断减小。，因此更新子弹的位置，我们冲 **self.y** 中减去 **self.speed_factor**
的值（见# <1>）。接下来，我们将 **self.rect.y** 设置为 **self.y** 的值（见# <2>）。属性 **speed_factor** 让我们能够随着游戏的进行或根据需要提高子弹的速度，已调整游戏的行
为。子弹发射后，其 *x* 坐标始终不变，因此子弹将沿直线垂直地往上穿行。

需要绘制子弹时，我们调用 **draw_bullet()** 。函数 **draw_rect()** 使用存储在 **self.color** 中额颜色填充表示 **rect** 占据地屏幕不凡（见# <3>）。

### 8.3 将子弹存储到编组中
定义 **Bullet** 类和必要的设置后，就可以编写代码了，在玩家每次按空格键时都射出依法子弹。首先，我们将在 *alien_invasion.py*中船舰一个编组（group），用于存储所有有效的子
弹，以便能够管理发射出去的所有子弹。这个编组将是 **pygame.sprite.Group** 类的一个实例： **pygame.sprite.Group** 类类似于列表，但提供了有助于开发游戏的额外功
能。在主循环中，我们将使用这个编组在屏幕上绘制子弹，以及更新每颗子弹的位置：

- alien_invasion.py

```python
import pygame

from pygame.sprite import Group
--snip--

def run_game():
    --snip--
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group    # <1>

    # 开始游戏主循环
    while True :
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()    # <2>
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
```
我们导入了 **pygame.sprite** 中的 **Group** 类。在# <1>处，我们创建了一个 **Group** 实例，并将其命名为 **bullets** 。这个编组始在while循环外面创建的 ，这样就无需每次运行该
循环时都创建一个新的子弹编组。
    - 注意：
    - 如果在循环内部船舰这样的编组，游戏运行时将创建数千个子弹编组，导致游戏慢得像乌龟。如果游戏停滞不前，请仔细查看主循环while循环中发生的情况。

我们将 **bullets** 传递给了 **check_events()** 和 **update_screen()** 。在 **check_events()** 中，需要在玩家按空格键时处理 **bullets**；而在 **update_screen()** 中，需要更新要绘制
到屏幕上的 **bullets** 。

当你对编组调用 **update()** 时，编组将自动对其中的每个子弹调用 **update()** ，因此代码 **bullets.update()** 将为编组 **bullets** 中的每颗子弹调用 **bullet.update()** 。

### 8.4 开火
在 *game_functions.py* 中，我们需要修改 **check_keydown_events()** ，以便在玩家按空格键时发射一颗子弹。我们无需修改 **check_keyup_events()** ，因为玩家松开空格键
时什么都不会发生。我们还需修改 **update_screen()** ，确保在调用 **flip()** 前在屏幕上重绘每颗子弹。下面是对 *game_functions.py* 所作的相关修改：

- game_functions.py
```python
--snip--
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):    # <1>
    """响应按键"""
    --snip--
    elif event.key == pygame.K_SPACE:    # <2>
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        --snip--

def check_events(ai_settings, screen, ship, bullets):    # <3>
    """响应按键和鼠标事件"""
    for event in pygame.event.get() :
        --snip--
        elif event.type == pygame.KEYDOWN :
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        --snip--

def update_screen(ai_settings, screen, ship, bullets) :    # <4>
    """更新屏幕上的图像，并切换到新屏幕"""
    --snip--
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():    # <5>
        bullet.draw_bullet()

    ship.blitme()
    --snip--
```
编组 **bullters** 传递给了 **check_keydown_events()**（见 # <1>）。玩家按空格键时，创建一颗新子弹（一个名为 **new_bullet** 的 **Bullet** 的实例），并用方法 **add()** 将其加入
到编组 **bullets** 中（见 # <2>）：代码 **bullets.add(new_bullet)** 将新子弹存储到编组 **bullets** 中。

在 **chenck_events()** 的定义中，我们需要添加形参 **bullets**（见 # <3>）；调用 **check_keydown_events()** 时，我们也需要将 **bullets** 作为实参传递给它。

在# <4>处，我们给在屏幕上绘制子弹的 **update_screen()** 添加了形参 **bullets** 。方法 **bullets.sprites()** 返回一个列表，其中包含编组 **bullets**中的所有子弹。为在屏幕
上绘制发射的所有子弹，我们遍历编组 **bullets** 中的子弹，并对每个子弹都调用 **draw_bullet()**（见 # <5>）。
    
### 8.5 删除已消失的子弹
当前，子弹抵达屏幕后消失，这仅仅是因为 **Pygame** 无法在屏幕外面绘制它们。这些子弹实际上依然存在，它们的 *y* 坐标为负数，且越来越小。这是个问题，因为它们将继续
消耗内存和处理能力。

我们需要将这些已消失的子弹删除，否则游戏所作的无谓工作将越来越多，进而变得越来越慢。为此，我们需要检测这样的条件，即表示子弹的 **rect** 的 **bottom** 属性为零，它
表示子弹已穿过屏幕顶端：

- alien_invasion.py
```python
# 开始游戏主循环
while True:
    gf.check_events(ai_settings, screen, ship, bullets)
    ship.update()
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bulletes))

    gf.update_screen(ai_settings, screen, ship, bullets)
```
在 **for** 循环中，不应从列表或编组中删除条目，因此必须遍历编组的副本。我们使用了方法 **copy()** 来设置 **for** 循环这让我们能够在循环中修改 **bullets** 。我们检
查每颗子弹，看看它是否从屏幕顶端消失。如果是这样，就将其从 **bullets** 中删除。我们使用了一条 **print** 语句，以显示当前还有多少颗子弹，
从而核实已消失的子弹确实删除了。

如果这些代码没有问题，我们发射的子弹后查看终端窗口时，将发现随着以可子弹一颗颗地在屏幕消失，子弹数将逐渐降为零。运行这个游戏并确认子弹已经被删除后，将这
条print语句删除。如果你留下这些语句，游戏的速度大大降低，因为将输出写入到终端而花费的时间比将图形绘制到游戏窗口花费的时间还多。

### 8.6 限制子弹的数量
很多射击游戏都对可同时出现在屏幕上的子弹数量进行限制，以鼓励玩家有目标的射击。下面是限制玩家子弹数量的方法。

首先，在 *settings.py* 中存储所允许的最大子弹数：

- settings.py
```python
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
```
这未消失的子弹数量限制为3颗。在 *game_functions.py* 的 **check_keydown_events()** 中，我们在创建新子弹前检查未消失的子弹数量是否小于该设置：

- game_functions.py
```python
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    --snip--
    elif event.key == pygame.K_SPACE:
        # 创建子弹并将其加入到编组bullets中
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
```
玩家按空格时候，检查 **bullets** 的长度。如果 **len(bullets)** 小于3，我们就创建一个新的子弹；但如果已经有3颗未消失的子弹，则玩家按空格时什么也不会发生。

### 8.7 创建update_bullets()
编写并检查子弹管理代码后，可将其移动到模块 *game_functions.py* 中，以让主程序文件alien_invasion.py尽可能简单。我们创建一个名为 **update_bullets()** 的新函数，并将其添加到 *game_functions.py* 的末尾。

- game_functions.py
```python
def update_bullets(bullets):
    """"更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹
    bullets.update()

    # 删除已经消失的子弹
    for bulelt in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
```
**update_bullets()** 的代码是从 *alien_invasion.py* 剪切并粘贴而来的，它只需要一个参数，即编组 **bullets** 。

*alien_invasion.py* 中的 **while** 循环又变得简单了：

- alien_invasion.py
```python
    # 开始游戏主循环
    while True :
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
```

### 8.8 创建函数fire_bullet()
下面将发射子弹的代码以到一个独立的函数中，这样，在 **check_keydown_events()** 中只需要使用一行代码来发射子弹，让 **elif** 代码变得非常简单：

- game_functions.py
```python
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    --snip--
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
```
函数 **fire_bullet()** 只包含了玩家按空格键时用于发射子弹的代码；在 **check_keydown_events()** 中，我们在玩家按空格键时调用 **fire_bullet()** 。
