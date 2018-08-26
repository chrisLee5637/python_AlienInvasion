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
	#"""存储《外星人入侵》的所有设置的类""
	
	def __init__(self):
		
		#"""初始化游戏的静态设置"""
		# 屏幕设置
		
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (7,8,6)
		# 飞船的设置
		self.ship_speed_factor = 1.5
		self.ship_limit = 1
		
		#子弹设置
		self.bullet_speed_factor = 3 
		self.bullet_width = 200
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullet_allowed = 5
		
		# 外星人设置
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction为1表示向右移，为-1表示向左移
		self.fleet_direction = 1
		
		# 以什么样的速度加快游戏节奏
		self.speedup_scale = 1.2
		self.initialize_dynamic_settings()
		
		# 外星人点数的提高速度
		self.score_scale = 2
		
		
	def initialize_dynamic_settings(self):
		
		#"""初始化随游戏进行而变化的设置"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		
		# fleet_direction为1表示向右；为-1表示向左
		self.fleet_direction = 1
		
		# 记分
		self.alien_points = 10
		
		 
		 
	def increase_speed(self):
		
		#"""提高速度设置"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		
		# 记分
		self.alien_points = int(self.alien_points * self.score_scale)
		
	
