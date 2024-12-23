import sys
import os
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))
from random import randint
import pygame
pygame.init()
pygame.mixer.init()
wikno = (pygame.display.Info().current_w , pygame.display.Info().current_h)
window = pygame.display.set_mode(wikno)
COLOR=(23,23,71)
clock = pygame.time.Clock()
program_work = True
pygame.display.set_caption("Шутер")
pygame.display.set_mode(wikno, pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN)
class pic():
    def __init__(self,file,x,y,x_2,y_2,kut=0,zminna = None ):
        self.file = file
        self.x = x
        self.y = y
        self.x_2 = x_2
        self.y_2 = y_2
        self.kut = kut
        self.zminna = zminna
        image_path = os.path.join(application_path, self.file)
        self.image = pygame.image.load(image_path)
    def f(self):
        if hasattr(self, 'kut'):
            rotated_image = pygame.transform.rotate(pygame.transform.scale(self.image, (self.x_2, self.y_2)), self.kut)
            window.blit(rotated_image, rotated_image.get_rect(center=(self.x + self.x_2 / 2, self.y + self.y_2 / 2)).topleft)
        else:
            scaled_image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
            window.blit(scaled_image, (self.rect.x, self.rect.y))
    def g(self,enemy):
        return pygame.Rect(self.x, self.y, self.x_2, self.y_2).colliderect(pygame.Rect(enemy.x, enemy.y, enemy.x_2, enemy.y_2))
class pic2():
    def __init__(self, file='./pic4.png', x=0, y=0, width=1, height=1):
        self.file = file
        self.rect = pygame.Rect(x, y, width, height)
        self.image = image = pygame.image.load(os.path.join(application_path, self.file))
    def f(self):
        if hasattr(self, 'kut'):
            rotated_image = pygame.transform.rotate(pygame.transform.scale(self.image, (self.x_2, self.y_2)), self.kut)
            window.blit(rotated_image, rotated_image.get_rect(center=(self.x + self.x_2 / 2, self.y + self.y_2 / 2)).topleft)
        else:
            scaled_image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
            window.blit(scaled_image, (self.rect.x, self.rect.y))
    def g(self,enemy):
        return self.rect.colliderect(pygame.Rect(enemy.x, enemy.y, enemy.x_2, enemy.y_2))
def to_0(our_n,i=1):
    if our_n > 0:
        return our_n - i
    elif our_n < 0:
        return our_n + i
    else:
        return our_n
stars = []
patrons = []
stones = []
UFOs = []
patrons_ufo = []
fonts = []
white_circles = []
explosions = []
for _ in range(30):
    star_size = randint(15,30)
    stars.append(pic('./pic1.png',randint(-25,wikno[0]+25),randint(-25,wikno[1]+25),star_size,star_size))
victory_color = [255,255,255]
font30 = pygame.font.SysFont('Comic Sans MS', 30)
font40 = pygame.font.SysFont('Comic Sans MS', 40)
font60 = pygame.font.SysFont('Comic Sans MS', 60)
max_hp = 100
victory_size = 150
victory_color_type = 'вниз'
pause2 = True
pause3 = False
win = False
ufo_chance = 1000
circle_size = 8
btn_size = 450
UFO_size = 5
raketa_size = 10
patron_true = 0
patron_size = 45
music_true = randint(-2500,-900)
play = pic('./pic10.png',(wikno[0]/2)-(btn_size/2),(wikno[1]/2)-(btn_size/(2*3)),btn_size,btn_size/3)
exit = pic('./pic9.png',(wikno[0]/2)-(btn_size/2),(wikno[1]/2)-(btn_size/(2*3)) + btn_size/3 + 37,btn_size,btn_size/3)
game_run = False
mouse = pic2()
raketa = pic('./pic3.png',(wikno[0]/2)-(5*raketa_size/2),wikno[1],5*raketa_size,9*raketa_size,0,100)
patron2 = 0
cymbal = pygame.mixer.Sound(os.path.join(application_path, 'cymbal.ogg'))
cymbal.set_volume(1)
music = pygame.mixer.Sound(os.path.join(application_path, 'game-music.mp3'))
music.set_volume(0.6)
raketa_shot = pygame.mixer.Sound(os.path.join(application_path, 'raketa_shot.mp3'))
raketa_shot.set_volume(0.1)
ufo_shot = pygame.mixer.Sound(os.path.join(application_path, 'ufo-shot.mp3'))
ufo_shot.set_volume(0.4)
game_over = pygame.mixer.Sound(os.path.join(application_path, 'game_over.wav'))
game_over.set_volume(0.9)
explosion_noice = pygame.mixer.Sound(os.path.join(application_path, 'assets_sound_explosion.ogg'))
explosion_noice.set_volume(2)
while program_work == True:
    window.fill(COLOR)
    mouse.rect.x, mouse.rect.y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse.g(exit):
            white = 0
            cymbal.play()
            while white < 255:
                window.fill(COLOR)
                for star in stars:
                    star.f()
                play.f()
                exit.f()
                white += 15
                fade_surface = pygame.Surface(wikno)
                fade_surface.fill((255, 255, 255))
                fade_surface.set_alpha(white)
                window.blit(fade_surface, (0, 0))
                pygame.display.update()
                clock.tick(10)
            UFO_size = 228
            break
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse.g(play):
            game_run = True
            patrons = []
            stones = []
            circles = []
            UFOs = []
            patrons_ufo = []
            fonts = []
            white_circles = []
            explosions = []
            for _ in range(8):
                white_circles.append([0,(0,0)])
            for _ in range(4):
                green = randint(200,254)
                circles.append([(randint(green,255),green,0),wikno[0],wikno[1],randint(-20,20)/10,randint(30,40)/10])
            raketa.y = wikno[1] + 30
            raketa.x = (wikno[0]/2)-(5*raketa_size/2)
            raketa.zminna = max_hp
            kills = 100
            ufo_chance = 1000
            win = False
            while game_run:
                window.fill(COLOR)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                for star in stars:
                    star.y += star.y_2 / 10
                    star.f()
                    if star.y > wikno[1]:
                        star.y = -30
                        star.x = randint(-30,wikno[0])
                if btn_size > 1:
                    play.kut += 3
                    play.f()
                    exit.f()
                    btn_size -= 10
                    play = pic('./pic10.png',(wikno[0]/2)-(btn_size/2),(wikno[1]/2)-(btn_size/(2*3)),btn_size,btn_size/3)
                    exit = pic('./pic9.png',(wikno[0]/2)-(btn_size/2),(wikno[1]/2)-(btn_size/(2*3)) + btn_size/3 + 37,btn_size,btn_size/3)
                for circle in white_circles:
                    if not circle[0] <= 0:
                        circle[0] -= 1
                        pygame.draw.circle(window, (255,255,255), circle[1], circle[0], 0)
                for circle in circles:
                    if pic2('./pic4.png',0,0,wikno[0],wikno[1]).g(pic('./pic9.png',circle[1]-circle_size,circle[2]-circle_size,circle[1]+circle_size*2,circle[2]+circle_size*2)):
                        pygame.draw.circle(window, circle[0], (circle[1], circle[2]), circle_size, 0)
                        circle[1] += circle[3]
                        circle[2] += circle[4]
                    else:
                        green = randint(200,254)
                        circles.remove(circle)
                        circles.append([(randint(green,255),green,0),raketa.x+raketa.x_2/2,raketa.y+raketa.y_2,randint(-20,20)/10,randint(30,40)/10])
                for patron in patrons:
                    patron.rect.y -= 10
                    if patron.rect.y < -60:
                        patrons.remove(patron)
                    patron.f()
                raketa.f()
                for circle in explosions:
                    circle[0] -= 1
                    if circle[0] <= 1:
                        explosions.remove(circle)
                    pygame.draw.circle(window, circle[2], circle[1], circle[0], 0)
                if raketa.y > wikno[1]-(raketa.y_2+30):
                    raketa.y -= 3
                keys = pygame.key.get_pressed()
                raketa.kut = to_0(raketa.kut,0.5)
                raketa.x += -raketa.kut
                if keys[pygame.K_RIGHT] and raketa.x+raketa.x_2 < wikno[0]-2:
                    raketa.kut -= 1
                if keys[pygame.K_LEFT] and raketa.x > 2:
                    raketa.kut += 1
                if raketa.x < 0:
                    raketa.kut = -2
                if raketa.x+raketa.x_2 > wikno[0]:
                    raketa.kut =  2
                if raketa.zminna <= 0:
                    game_over.play()
                    game_run = False
                if patron_true > 5 and keys[pygame.K_LCTRL]:
                    raketa_shot.play()
                    patrons.append(pic2('./pic11.png',raketa.x+(raketa.x_2/2)-(patron_size/4),raketa.y,patron_size/2,patron_size))
                    patron2 += 1
                    patron_true = 0
                    if patron2 == 8:
                        patron2 = 0
                        patron_true = -50
                patron_true += 1
                music_true += 1
                if music_true >= 2000:
                    music.play()
                    music_true = randint(-10_000,-2300)
                if randint(0,1000) == 0:
                    stone_size = randint(100,200)
                    stones.append(pic('./pic2.png',randint(0,wikno[0]-stone_size),-stone_size-randint(1,100),stone_size,stone_size,0,0))
                if randint(0,ufo_chance) == 0 or len(UFOs) == 0:
                    UFOs.append(pic('./pic'+str(randint(5,8))+'.png',randint(5,wikno[0]-(24*UFO_size)),-14*UFO_size,23*UFO_size,14*UFO_size,0,[0,-30,randint(50,85)/10,randint(4,8)*10,0]))
                if randint(0,1500) == 0 and raketa.zminna < max_hp:
                    heal = randint(1,50)
                    raketa.zminna += heal
                    if raketa.zminna > max_hp:
                        raketa.zminna = max_hp
                    font_y = 70
                    while any(font_y == font[2] for font in fonts):
                        font_y += 30
                    fonts.append(['+'+str(heal),-50,font_y,2,(max(0,255-heal*10),255,max(0,255-heal*10))])
                for ufo_patron in patrons_ufo:
                    ufo_patron.x -= ufo_patron.zminna[0]
                    ufo_patron.y -= ufo_patron.zminna[1]
                    ufo_patron.f()
                    if pic2('./pic4.png',0,0,wikno[0],wikno[1]).g(ufo_patron) == False:
                        patrons_ufo.remove(ufo_patron)
                    elif raketa.g(ufo_patron):
                        damage = randint(3,6) * 5
                        raketa.zminna -= damage
                        font_y = 70
                        while any(font_y == font[2] for font in fonts):
                            font_y += 30
                        fonts.append(['-'+str(damage),-50,font_y,2,(255,max(255-damage*7,0),max(255-damage*7,0))])
                        patrons_ufo.remove(ufo_patron)
                for ufo in UFOs:
                    ufo.f()
                    ufo.zminna[1] += 1
                    ufo.x += ufo.zminna[0]
                    if ufo.zminna[3] <= 0:
                        if ufo.zminna[4] == 0:
                            if kills > 1:
                                ufo_chance -= 8
                                kills -= 1
                                for _ in range(14):
                                    green = randint(200,254)
                                    explosions.append([randint(20,40),(randint(int(ufo.x),int(ufo.x+ufo.x_2)),randint(int(ufo.y),int(ufo.y+ufo.y_2))),(randint(green,255),green,0)])
                                explosion_noice.play()
                            else:
                                game_run = False
                                win = True
                                max_hp += 10
                                break
                        ufo.zminna[4] = 1
                        ufo.zminna[2] = 6 - ufo.zminna[0] / 4 - ufo.zminna[3]
                    else:
                        if ufo.zminna[1] >= 100:
                            ufo_shot.play()
                            ufo.zminna[1] = randint(-20,20)
                            patron_ufo = pic('./pic12.png',ufo.x+ufo.x_2/2,ufo.y+ufo.y_2/2,UFO_size*10,UFO_size*10)
                            patron_ufo.zminna = [(patron_ufo.x-raketa.x)/100,(patron_ufo.y-raketa.y)/100]
                            patrons_ufo.append(patron_ufo)
                        if ufo.x <= 0 and ufo.zminna[0] < 0:
                            ufo.zminna[0] = -ufo.zminna[0]
                        elif ufo.x + ufo.x_2 >= wikno[0] and ufo.zminna[0] > 0:
                            ufo.zminna[0] = -ufo.zminna[0]
                        else:
                            ufo.zminna[0] = to_0(ufo.zminna[0],0.05)
                        if ufo.zminna[0] // 1 == 0:
                            ufo.zminna[0] = randint(-200,200) / 10
                        for patron in patrons:
                            if patron.g(ufo):
                                patrons.remove(patron)
                                for w_circle in white_circles:
                                    if w_circle[0] <= 0:
                                        w_circle[0] = 30
                                        w_circle[1] = (patron.rect.x + 11, patron.rect.y + 22)
                                        break
                                ufo.zminna[3] -= 10
                        if any(pic2('./pic4.png',stone.x+10,stone.y+30,stone.x_2-20,stone.y_2-40).g(ufo) for stone in stones):
                            ufo.zminna[3] = -4
                    if ufo.zminna[2] // 1 > 0:
                        ufo.y += ufo.zminna[2]
                        ufo.zminna[2] = to_0(ufo.zminna[2],0.1)
                    if ufo.y > wikno[1]:
                        UFOs.remove(ufo)
                for stone in stones:
                    stone.kut += 1
                    stone.y += stone.y_2 / 50
                    stone.x += stone.zminna
                    stone.f()
                    if stone.x_2 < 41 or not pic2('./pic11.png',0,-300,wikno[0],wikno[1]+300).g(stone):
                        stones.remove(stone)
                    if pic2('./pic1.png',stone.x+10,stone.y+30,stone.x_2-20,stone.y_2-40).g(raketa):
                        raketa.zminna -= stone.x_2
                        stones.remove(stone)
                        font_y = 70
                        while any(font_y == font[2] for font in fonts):
                            font_y += 30
                        fonts.append(['-'+str(stone.x_2),-50,font_y,2,(255,max(255-stone.x_2*5,0),max(255-stone.x_2*5,0))])
                    else:
                        for patron in patrons:
                            if patron.g(stone):
                                stones.remove(stone)
                                patrons.remove(patron)
                                stones.append(pic('./pic2.png',stone.x+20,stone.y+20,stone.x_2-40,stone.y_2-40,randint(0,180), 2))
                                stones.append(pic('./pic2.png',stone.x+20,stone.y+20,stone.x_2-40,stone.y_2-40,randint(0,180),-2))
                                for w_circle in white_circles:
                                    if w_circle[0] <= 0:
                                        w_circle[0] = stone.x_2 // 2
                                        w_circle[1] = (stone.x + stone.x_2 / 2, stone.y + stone.x_2 / 2)
                                        break
                                break
                for font in fonts:
                    window.blit(font30.render(font[0], True, font[4]), (font[1], font[2]))
                    font[1] += font[3]
                    font[3] -= 0.02
                for font in fonts:
                    if font[1] < -50:
                        fonts.remove(font)
                if raketa.zminna < 0:
                    raketa.zminna = 0
                window.blit(font60.render(' РЗ: '+str(raketa.zminna), True, (255, 255, 255)), (0, 0))
                window.blit(font40.render('Ще: '+str(kills), True, (255, int(2.55*kills), int(2.55*kills))), (wikno[0]-150, 0))
                if keys[pygame.K_ESCAPE] == False:
                    pause2 = True
                if keys[pygame.K_ESCAPE] and pause2:
                    pause = False
                    while True: 
                        mouse.rect.x, mouse.rect.y = pygame.mouse.get_pos()
                        pause3 = False
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse.g(exit):
                                game_run = False
                                pause3 = True
                                break
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse.g(play):
                                pause3 = True
                                break
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_ESCAPE] == False:
                            pause = True
                        if keys[pygame.K_ESCAPE] and pause == True:
                            break
                        if pause3:
                            break
                        exit = pic('./pic9.png',(wikno[0]/2)-(300/2),(wikno[1]/2)-(300/(2*3)) + 300/3 + 37,300,300/3)
                        exit.f()
                        pygame.display.update()
                        clock.tick(30)
                    pause2 = False
                pygame.display.update()
                clock.tick(60)
    if UFO_size == 228:
        break
    for star in stars:
        star.y += star.y_2 / 10
        star.f()
    for star in stars:
        if star.y > wikno[1]:
            stars.remove(star)
            star_size = randint(15,30)
            stars.append(pic('./pic1.png',randint(-160,wikno[0]+25),-30,star_size,star_size))
    if win == True:
        window.blit(pygame.font.SysFont('Comic Sans MS', victory_size).render("  ПЕРЕМОГА!", True,(victory_color[1],victory_color[0],victory_color[2])), (0,15))
        window.blit(pygame.font.SysFont('Comic Sans MS', 44).render("        максимальний РЗ росте на 10", True,(255,255,255)), (0,200))
        if victory_color_type == 'вниз':
            victory_color[1] -= 1
            victory_color[2] -= 1
        else:
            victory_color[1] += 1
            victory_color[2] += 1
        if victory_color[1] == 255:
            victory_color_type = 'вниз'
        if victory_color[1] == 0:
            victory_color_type = 'вверх'
    if btn_size < 450:
        btn_size += 10
        play = pic('./pic10.png',(wikno[0]/2)-(btn_size/2),(wikno[1]/2)-(btn_size/(2*3)),btn_size,btn_size/3)
        exit = pic('./pic9.png',(wikno[0]/2)-(btn_size/2),(wikno[1]/2)-(btn_size/(2*3)) + btn_size/3 + 37,btn_size,btn_size/3)
    play.f()
    exit.f()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
 # ;) 