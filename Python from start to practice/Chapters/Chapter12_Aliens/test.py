import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
#question 12-3
class Rocket():
    '''
    定义火箭及其行为
    '''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('vscode_Pythoncode/Python from start to practice/Chapter/Chapter12_Aliens/image/ship.bmp')
        self.rect = self.image.get_rect()


        #将每艘新火箭放在屏幕中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery= self.screen_rect.centery

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''根据移动标志调整飞船的位置'''
        #更新火箭的centerx,centery值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx +=1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -=1
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -=1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery +=1
    
    
    def blitme(self):
        '''
        在指定位置绘制火箭
        '''
        self.screen.blit(self.image, self.rect)
        
                
def check_keydown_events(event, rocket):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left =True
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True
    
def check_keyup_events(event, rocket):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False



def check_events(rocket):
    '''
    管理事件
    相应按键和鼠标事件
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


def update_screen( screen, rocket):
    '''
    更新屏幕上的图像，并切换到新屏幕
    '''
    #每次循环时都重绘屏幕
    screen.fill((23,25,253))
    rocket.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()


def run_game():
    
    pygame.init()
   
    screen = pygame.display.set_mode((1200,700))
    pygame.display.set_caption('Rocket')
    #创建一个火箭
    rocket=Rocket(screen)
    

    while True:
        check_events(rocket)
        rocket.update()
        update_screen(screen, rocket)




#question 12-4
def blank_screen():
    screen = pygame.display.set_mode((1200, 700))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.KEYDOWN:
                print(event.key)

##################################################################################################################
########我是分割线####

#question 12-5

class Ship():
    '''
    定义飞船及其行为
    '''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('vscode_Pythoncode/Python from start to practice/Chapter/Chapter12_Aliens/image/ship.bmp')
        self.rect = self.image.get_rect()


        #将每艘新火箭放在屏幕左边缘
        self.rect.left = 0
        self.rect.centery= self.screen_rect.centery

        #移动标志
        '''
        self.moving_right = False
        self.moving_left = False
        '''
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''根据移动标志调整飞船的位置'''
        #更新火箭的centery值
        '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx +=1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -=1
        '''
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -=1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery +=1
    
    
    def blitme(self):
        '''
        在指定位置绘制飞船
        '''
        self.screen.blit(self.image, self.rect)
class Bullet(Sprite):
    '''一个对飞船发射的子弹进行管理的类'''
    def __init__(self,screen, ship):
        '''在飞船所处的位置创建一个子弹对象'''
        super(Bullet, self).__init__()
        self.screen = screen
        #在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, 15,3)
        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.right
        #存储用小数表示的子弹位置
        self.x = float(self.rect.x)
        
        self.color = (60, 60, 60)
        self.speed_factor = 1
    
    def update(self):
        '''向上移动子弹'''
        #更新表示子弹位置的小数值
        self.x +=self.speed_factor
        #更新表示子弹的rect的位置
        self.rect.x = self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color, self.rect)


def ship_check_keydown_events(event, ship, bullets,screen):
    '''响应按键'''
    '''
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left =True
    '''
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(screen, ship, bullets)

def fire_bullet(screen, ship, bullets):
        #创建一颗子弹，并将其加入到编组bullets中
        if len(bullets) < 10:
            new_bullet = Bullet(screen, ship)
            bullets.add(new_bullet)
    
def ship_check_keyup_events(event, ship):
    '''响应松开'''
    '''
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    '''
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False



def ship_check_events(ship,bullets,screen):
    '''
    管理事件
    相应按键和鼠标事件
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            ship_check_keydown_events(event, ship, bullets,screen)
        elif event.type == pygame.KEYUP:
            ship_check_keyup_events(event, ship)
       


def ship_update_screen( screen, ship, bullets):
    '''
    更新屏幕上的图像，并切换到新屏幕
    '''
    #每次循环时都重绘屏幕
    screen.fill((230,230,230))
    #重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
  
    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets,screen):
    '''更新子弹的位置，并删除已消失的子弹'''
    #更新子弹的位置
    bullets.update()
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.right >= screen.get_rect().right:
            bullets.remove(bullet)
    

def ship_run_game():
    
    pygame.init()
   
    screen = pygame.display.set_mode((1200,700))
    pygame.display.set_caption('ship')
    #创建一个火箭
    ship=Ship(screen)
    #创建一个用于存储子弹的编组
    bullets = Group()

    while True:
        ship_check_events(ship, bullets,screen)
        ship.update()  
        update_bullets(bullets, screen)
        ship_update_screen(screen, ship, bullets)

ship_run_game()




































