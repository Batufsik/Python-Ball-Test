import pygame
import random
import math #honorable mentions

screen_width, screen_height = 1280, 720

gravity = 0.5
friction = 0.88 #bouncy
wind = 0.3
air_resistance = 0.2
FPS = 60

#I LOVE CLASSES
class buzik:
    def __init__(self, x, y, speed_x, speed_y, color):
        self.id = len(hitboziki)
        self.color = color
        self.radius = 20
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.ballrect = pygame.draw.circle(screen, (255,255,255), (self.x, self.y), self.radius)
        self.dx = self.ballrect.centerx - kubik.centerx
        self.dy = self.ballrect.centery - kubik.centery - kubik[3]
        self.inwall = False
        #self.hitbox_top = pygame.Rect(self.x, self.y, self.radius * 2, 2)
        #self.hitbox_bottom = pygame.Rect(self.x, self.y + self.radius * 2 , self.radius * 2, 2)
        #self.hitbox_left = pygame.Rect(self.x, self.y, 2, self.radius *  2)
        #self.hitbox_right = pygame.Rect(self.x + self.radius * 2, self.y, 2, self.radius * 2)
        #self.collida = 0

        self.hitbox_bottom_vis = pygame.draw.rect(screen, (255, 0, 0), (self.x - self.radius, self.y + self.radius, self.radius * 2, 2), border_radius=2)
        self.hitbox_top_vis = pygame.draw.rect(screen, (255, 0, 0), (self.x - self.radius, self.y - self.radius, self.radius * 2, 2), border_radius=2)
        self.hitbox_left_vis = pygame.draw.rect(screen, (255, 0, 0), (self.x - self.radius, self.y - self.radius, 2, self.radius * 2), border_radius=2)
        self.hitbox_right_vis = pygame.draw.rect(screen, (255, 0, 0), (self.x + self.radius, self.y - self.radius, 2, self.radius * 2), border_radius=2)
        
        #I LOVE MEANINGLESS ABSTRACTIONS
        self.hitboxes = [
            self.hitbox_top_vis,
            self.hitbox_bottom_vis,
            self.hitbox_left_vis,
            self.hitbox_right_vis
        ]        

    def move(self):
        #I LOVE COLLISIONS

        if self.x + self.radius > screen_width or self.x - self.radius < 0:
            self.speed_x = -self.speed_x * friction
        if self.y + self.radius > screen_height:
            self.y = screen_height - self.radius #anti-noclip mechanism
            self.speed_y = -self.speed_y * friction
            self.speed_x = self.speed_x * friction
        if self.y - self.radius < 0:
            self.y = 0 + self.radius
            self.speed_y = -self.speed_y * friction 
        self.x += self.speed_x
        self.y += self.speed_y
        self.hitbox_bottom_vis = pygame.Rect(self.x - self.radius + 4, self.y + self.radius, self.radius * 2 - 3, 4)
        self.hitbox_top_vis = pygame.Rect(self.x - self.radius + 4, self.y - self.radius, self.radius * 2 - 3, 4)
        self.hitbox_left_vis = pygame.Rect(self.x - self.radius, self.y - self.radius + 4, 2, self.radius * 2 - 4)
        self.hitbox_right_vis = pygame.Rect(self.x + self.radius, self.y - self.radius + 4, 2, self.radius * 2 - 4)
        if call:
            pygame.draw.rect(screen, (255, 0, 0), self.hitbox_bottom_vis, border_radius=2)
            pygame.draw.rect(screen, (255, 0, 0), self.hitbox_top_vis, border_radius=2)
            pygame.draw.rect(screen, (255, 0, 0), self.hitbox_left_vis, border_radius=2)
            pygame.draw.rect(screen, (255, 0, 0), self.hitbox_right_vis, border_radius=2)

        self.speed_y += gravity
        self.hitboxes = [
            self.hitbox_top_vis,
            self.hitbox_bottom_vis,
            self.hitbox_left_vis,
            self.hitbox_right_vis
        ]    
    def draw(self, screen):
        self.ballrect = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        
        
    #    self.collida = self.hitbox.collidelist(hitboziki)
    #    if self.collida > 0:
    #        self.speed_y = -self.speed_y * friction
    def collision(self):
        hitboziki.update({"id" + str(self.id) : self.hitboxes})
        '''
        for id, hitball in hitboziki.items():
            if id != "id" + str(self.id):
                for b, i in enumerate(self.hitboxes):
                    if b == 1 and i.colliderect(hitball[0]):
                        self.y = hitball[0][1] - hitball[0][3] - self.radius
                        self.speed_x *= friction
                        self.speed_y = -self.speed_y * friction + random.uniform(0.01, -0.01)
                    if b == 0 and i.colliderect(hitball[1]):
                        self.y = hitball[1][1] + hitball[1][3] + self.radius
                        self.speed_x *= friction
                        self.speed_y = -self.speed_y * friction + random.uniform(0.01, -0.01)
                    if b == 3 and i.colliderect(hitball[2]):
                        self.x = hitball[2][0] - hitball[2][2] - self.radius
                        self.speed_x = -self.speed_x * friction + random.uniform(0.01, -0.01)
                        self.speed_y *= friction
                    if b == 2 and i.colliderect(hitball[3]):
                        self.x = hitball[3][0] + hitball[2][2] + self.radius
                        self.speed_x = -self.speed_x * friction + random.uniform(0.01, -0.01)
                        self.speed_y *= friction
        '''
        
        if self.hitboxes[0].colliderect(kubik):
                self.y = kubik[1] + kubik[3] + self.radius
                self.speed_x *= friction
                self.speed_y = -self.speed_y * friction + random.uniform(0.01, -0.01)
        if self.hitboxes[1].colliderect(kubik):
                self.y = kubik[1] - self.radius
                self.speed_x *= friction
                self.speed_y = -self.speed_y * friction + random.uniform(0.01, -0.01)
        if self.hitboxes[2].colliderect(kubik):
                self.speed_x = -self.speed_x * friction + random.uniform(0.01, -0.01)
                self.speed_y *= friction
        if self.hitboxes[3].colliderect(kubik):
                self.speed_x = -self.speed_x * friction + random.uniform(0.01, -0.01)
                self.speed_y *= friction
        

        


        

    def get_hitbox(self):
        return self.hitboxes


        #insane asylum    
        '''
        for obj in boziki:
            colliding_objects = obj.hitbox.collidelist([other for other in boziki])
            if colliding_objects != -1 and obj != boziki[colliding_objects]:
                # Collision detected
                self.speed_y = -self.speed_y * friction
                
                print(f" {obj} is fucking colliding with {boziki[colliding_objects]}")
        '''

call = False
mode = "click"
wof = 0
gef = False

boziki = []
hitboziki = {}
def add_bozik(mouse_x, mouse_y, speed_x, speed_y, color):
    bozik = buzik(mouse_x, mouse_y, speed_x, speed_y, color)
    boziki.append(bozik)
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
#kubik_rect = pygame.Rect(400, 300, 100, 100)
kubik_width = 100
kubik_height = 100
kubik_color = (125,125,125)
kubik = pygame.draw.rect(screen, kubik_color, (400, 300, 100, 100))
running = True
while running:
    #for hitbozik in boziki:
    #    hitboziki.append(hitbozik.get_hitbox())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEWHEEL:
            FPS = min(FPS + event.y, 240)
            print("FPS set to", FPS)
            

        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                if mode == "click":
                    mode = "hold"
                else:
                    mode = "click" 
            if pygame.key.get_pressed()[pygame.K_r]:
                boziki.clear()
                hitboziki.clear()


        if event.type == pygame.MOUSEBUTTONDOWN and mode == "click" and wof == 0:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            left, middle, right = pygame.mouse.get_pressed()
            if left:
                add_bozik(mouse_x, mouse_y, -5, -5, (255,255,255))
            elif right:
                add_bozik(mouse_x, mouse_y, 5, -5, (255,255,255))
        if event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            if middle:
                #print(hitboziki)
                if not call:
                    call = True
                else:
                    call = False

    if pygame.MOUSEBUTTONDOWN and mode == "hold" and wof == 0:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        left, middle, right = pygame.mouse.get_pressed()
        if left:
            add_bozik(mouse_x, mouse_y, -4, -3, (255,255,255))
        elif right:
            add_bozik(mouse_x, mouse_y, 4, -3, (255,100,100))
        #elif middle:
        #    if not call:
        #        call = True
        #    else:
        #        call = False
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        kubik_width += 5
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        kubik_width -= 5
    if pygame.key.get_pressed()[pygame.K_UP]:
        kubik_height -= 5
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        kubik_height += 5
    if pygame.key.get_pressed()[pygame.K_h]:
        print(hitboziki)
    if pygame.key.get_pressed()[pygame.K_s]:
        friction -= 0.01
        print(friction)

    if kubik.collidepoint(pygame.mouse.get_pos()):
        kubik_color = (200,170,170)
        wof = 1
        
        if pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            if left:
                #add_bozik(kubik.centerx + random.choice([-kubik[1] // 2, kubik[1] // 2]), kubik.centery + random.choice([-kubik[2] // 2, kubik[2] // 2]), random.choice([-3, 3]), random.choice([-3, 3]), (255, 10, 10))
                add_bozik(kubik.centerx, kubik.centery - kubik[2] * 2, random.choice([-3, 3]), random.choice([-3, 3]), (255, 10, 10))

            
    else:
        kubik_color = (125,125,125)
        wof = 0


                
    screen.fill((0,0,0))
    kubik = pygame.draw.rect(screen, kubik_color, (400, 300, kubik_width, kubik_height))

    for bozik in boziki:
        bozik.collision()
        bozik.move()
        bozik.draw(screen)

    screen.blit(pygame.font.Font(None,32).render(f"Current mode: '{mode}', press SPACEBAR to switch", True, (225, 225, 225)), (20, 20))
    screen.blit(pygame.font.Font(None,32).render("LMB / RMB to spawn particles, arrow keys to scale the cube", True, (225, 225, 225)), (20, 45))
    screen.blit(pygame.font.Font(None,32).render("Click on scroll wheel to display hitboxes", True, (225, 225, 225)), (20, 70))
    screen.blit(pygame.font.Font(None,32).render("Press 'R' to clear the screen, scroll to change FPS", True, (225, 225, 225)), (20, 95))
    #screen.blit(pygame.font.Font(None,24).render("Lifesuxia University, Cekaton Y.", True, (225, 225, 225)), (screen_width - 260, 20))
    screen.blit(pygame.font.Font(None,24).render("Python Ball Test by Vladimir Sayapin", True, (225, 225, 225)), (10, screen_height - 30))
    pygame.display.flip()
    clock.tick(FPS)