#coding=utf-8

import pygame
import sys
from pygame.sprite import Sprite
from bullet import Bullet
from alien import Alien
from time import sleep
from button import Button

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
	#"""��Ӧ����������¼�"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
			

def update_screen(ai_setting, screen, stats, sb, ship, aliens, bullets, play_button):
	#"""������Ļ�ϵ�ͼ�񣬲��л�������Ļ"""
	# ÿ��ѭ��ʱ���ػ���Ļ
	screen.fill(ai_setting.bg_color)
	
	# �ڷɴ��������˺����ػ������ӵ�
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	ship.blitme()
	#�Ա������ draw() ʱ��Pygame�Զ����Ʊ����ÿ��Ԫ�أ�����λ����Ԫ�ص����� rect ����������� aliens.draw(screen) ����Ļ�ϻ��Ʊ����е�ÿ��������
	aliens.draw(screen)
	
	# ��ʾ�÷�
	sb.show_score()
	
	# �����Ϸ���ڷǻ״̬���ͻ���Play��ť
	if not stats.game_active:
		play_button.draw_button()
	
	# ��������Ƶ���Ļ�ɼ�
	pygame.display.flip()
	
	
def check_keydown_events(event, ai_setting, screen, ship, bullets):
	#"""��Ӧ����""
	if event.key == pygame.K_RIGHT:
		#	�����ƶ��ɴ�
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True	
	if event.key == pygame.K_SPACE:
		fire_bullet(ai_setting, screen, ship, bullets)
	if event.key == pygame.K_q:
			sys.exit()
		
		
def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
				
		ship.moving_right = False
	if event.key ==	pygame.K_LEFT:
		ship.moving_left = False
		
		
def update_bullets(ai_settings, screen, stats, sb, ship, aliens ,bullets):
	#"""�����ӵ���λ�ã���ɾ������ʧ���ӵ�"""
	# �����ӵ���λ��
	bullets.update()
		
	# ɾ������ʧ���ӵ�
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
	
		
def fire_bullet(ai_setting, screen, ship, bullets):
	
	#"""�����û�е������ƣ��ͷ���һ���ӵ�"""
	if len(bullets) < ai_setting.bullet_allowed:
			# ����һ���ӵ�����������뵽����bullets��
			new_bullet = Bullet(ai_setting, screen, ship) 
			bullets.add(new_bullet)
			
def create_fleet(ai_settings, screen, ship, aliens):
	#"""����������Ⱥ"""
	# ����һ�������ˣ�������һ�п����ɶ��ٸ�������
	#�����˼��Ϊ�����˿���
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	
	number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
	
	# ����������Ⱥ
	for alien_number in range(number_aliens_x):
		for row_number in range(number_rows):
		
			# ����һ�������˲�������뵱ǰ��
			create_alien(ai_settings, screen, aliens, alien_number, row_number)
		
		
def get_number_aliens_x(ai_settings, alien_width):
	
	#"""����ÿ�п����ɶ��ٸ�������"""
	available_space_x = ai_settings.screen_width - (2 * alien_width)
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x
	
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	
	#"""����һ�������˲�������ڵ�ǰ��"""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width  * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)
	
def get_number_rows(ai_settings, ship_height, alien_height):
	
	#"""������Ļ�����ɶ�����������"""
	available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / ( 2 * alien_height) -3)
	return number_rows
	
def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
	
	#����Ƿ���������λ����Ļ��Ե����������Ⱥ�����˵�λ��
	check_fleet_edges(ai_settings, aliens)
	#"""����������Ⱥ�����������˵�λ��"""
	aliens.update()
	
	# ��������˺ͷɴ�֮�����ײ
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
		
	# ����Ƿ��������˵�����Ļ�׶�
	check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)
	
def check_fleet_edges(ai_settings, aliens):
	
	#"""�������˵����Եʱ��ȡ��Ӧ�Ĵ�ʩ"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	
	#"""����Ⱥ���������ƣ����ı����ǵķ���"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1
		
	
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
	
	# ����Ƿ����ӵ�������������
	# �������������ɾ����Ӧ���ӵ���������
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	
	if collisions:
		for collision in collisions.values():
			
			stats.score += (ai_settings.alien_points * len(collision))
		sb.prep_score()
		check_high_score(stats, sb)
	
	if len(aliens) == 0:
		
		# ɾ�����е��ӵ����ӿ���Ϸ���࣬������һȺ�µ�������
		bullets.empty()
		ai_settings.increase_speed()
		stats.level += 1
		sb.prep_level()
		# ��ߵȼ�
		
		create_fleet(ai_settings, screen, ship, aliens)
		
def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
	
	#"""��Ӧ��������ײ���ķɴ�"""
	# ��ships_left��1
	stats.ships_left -= 1
	
	# ����������б����ӵ��б�
	aliens.empty()
	bullets.empty()
	
	# ����һȺ�µ������ˣ������ɴ��ŵ���Ļ�׶�����
	create_fleet(ai_settings, screen, ship, aliens)
	ship.center_ship()
	if stats.ships_left > 0:
		# ��ships_left��1
		stats.ships_left -= 1
		
		# ���¼Ƿ���
		sb.prep_ships()
		
		# ��ͣ
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)
	
def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
	
	#"""����Ƿ��������˵�������Ļ�׶�"""
	screen_rect = screen.get_rect()
	
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			
			# ��ɴ���ײ��һ�����д���
			ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
			break
			
			
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
	
	#"""����ҵ���Play��ťʱ��ʼ����Ϸ"""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	
	if button_clicked and not stats.game_active:
		
		# ������Ϸ����
		ai_settings.initialize_dynamic_settings()
		
		# ���ع��
		pygame.mouse.set_visible(False)
		
		# ������Ϸͳ����Ϣ
		stats.reset_stats()
		stats.game_active = True
		
		# ���üǷ���ͼ��
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()
		
		# ����������б����ӵ��б� 
		aliens.empty()
		bullets.empty()
		
		# ����һȺ�µ������ˣ����÷ɴ�����
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		

def check_high_score(stats, sb):
	
	#"""����Ƿ������µ���ߵ÷�"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()
		
	
	
	
	
		