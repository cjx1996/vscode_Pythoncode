import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from gamestats import Gamestats
from scoreboard import Scoreboard
from button import Button

import game_functions as gf
def run_game():

    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创建Play按钮
    play__button = Button(ai_settings, screen, 'Play')


    #创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = Gamestats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #创建一艘飞船,一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen) 
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #开始游戏主循环
    while True:   
        gf.check_events(ai_settings, screen, stats, sb, play__button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()                                                     #对飞船位置进行更新
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)     #对子弹位置及有效性进行更新
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets) 
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play__button)



run_game()






































