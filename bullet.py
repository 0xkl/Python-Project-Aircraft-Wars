import pygame

from pygame.sprite import Sprite

class Bullet(Sprite) :
    def __init__(self, ai_settings, screen, ship) :
        """一个对飞船发射的位置船舰一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0, 0)处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)    # <1>

        self.rect.centerx = ship.rect.centerx    # <2>
        self.rect.top = ship.rect.top    # <3>

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)    # <4>
        self.color = ai_settings.bullet_color    # <5>
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor    # <1>

        # 更新表示子弹的rect的位置
        self.rect.y = self.y    # <2>

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)    # <3>