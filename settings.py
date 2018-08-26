#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  settings.py
#  
#  Copyright 2018 Administrator <Administrator@PC-201603201610>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import pygame


class Settings():
	#"""�洢�����������֡����������õ���""
	
	def __init__(self):
		
		#"""��ʼ����Ϸ�ľ�̬����"""
		# ��Ļ����
		
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (7,8,6)
		# �ɴ�������
		self.ship_speed_factor = 1.5
		self.ship_limit = 1
		
		#�ӵ�����
		self.bullet_speed_factor = 3 
		self.bullet_width = 200
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullet_allowed = 5
		
		# ����������
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_directionΪ1��ʾ�����ƣ�Ϊ-1��ʾ������
		self.fleet_direction = 1
		
		# ��ʲô�����ٶȼӿ���Ϸ����
		self.speedup_scale = 1.2
		self.initialize_dynamic_settings()
		
		# �����˵���������ٶ�
		self.score_scale = 2
		
		
	def initialize_dynamic_settings(self):
		
		#"""��ʼ������Ϸ���ж��仯������"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		
		# fleet_directionΪ1��ʾ���ң�Ϊ-1��ʾ����
		self.fleet_direction = 1
		
		# �Ƿ�
		self.alien_points = 10
		
		 
		 
	def increase_speed(self):
		
		#"""����ٶ�����"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		
		# �Ƿ�
		self.alien_points = int(self.alien_points * self.score_scale)
		
	
