 
 #coding=utf-8
 
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	
	def __init__(self,ai_settings, screen):
		# ��ʼ���ɴ��ͷɴ���ʼλ��
		super(Ship,self).__init__()
		self.screen = screen
		
		# ���طɴ�ͼ�񲢻�ȡ����Ӿ���
		self.image = pygame.image.load('image/ship4.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		
		# ��ÿ���·ɴ�������Ļ�ײ�����
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# �ڷɴ�������center�д洢С��ֵ
		self.center = float(self.rect.centerx)
		
		# �ƶ���־
		self.moving_right = False
		self.moving_left = False
		
		
	def blitme(self):
		#"""��ָ��λ�û��Ʒɴ�"""
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		#"""�����ƶ���־�����ɴ���λ��"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
			
		# ����self.center����rect����
		self.rect.centerx = self.center
		
		
	def center_ship(self):
		
		#"""�÷ɴ�����Ļ�Ͼ���"""
		self.center = self.screen_rect.centerx
		
		
		
		
