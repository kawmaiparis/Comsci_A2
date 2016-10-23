import pygame

class Cow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__height = 410
        self.__width = 640
        self.image = pygame.image.load("seacow.png")
        self.image = pygame.transform.scale(self.image,(self.__width,self.__height))
        self.rect = self.image.get_rect()
        self.__hp = 100
        self.__atk = 100
        self.__speed = 5

        self.rect.x = 50
        self.rect.y = 50
        self.__x = self.rect.x
        self.__y = self.rect.y

    def gethp(self):
        return self.__hp
    
    def getatk(self):
        return self.__atk

    def sethp(self,inputdata):
        self.__hp = inputdata

    def setatk(self,inputdata):
        self.__mp = inputdata

    def update(self):
        pass

    def getposi(self):
        return (self.__height, self.__width)

    def move(self, direction):
        if direction == 'r':
            self.__x = self.__x + self.__speed
            self.rect.x = int(self.__x)
        elif direction == 'l':
            self.__x = self.__x - self.__speed
            self.rect.x = int(self.__x)
        elif direction == 'u':
            self.__y = self.__y - self.__speed
            self.rect.y = int(self.__y)
        elif direction == 'd':
            self.__y = self.__y + self.__speed
            self.rect.y = int(self.__y)
        
