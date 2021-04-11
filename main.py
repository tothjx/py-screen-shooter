import os
import sys
import keyboard
import time
from datetime import datetime
import pyautogui as pyag

'''
pyinstaller 
	--onefile main.py --name=screenshooter --hiddenimport=os --hiddenimport=sys --hiddenimport=time 
	--hiddenimport=keyboard._winkeyboard --hiddenimport=datetime.datetime --hiddenimport=pyautogui
'''

APP_NAME = 'ScreenShooter'
APP_VER = '1.3.0'
KEY_SCREEN = 'f12'
KEY_EXIT = 'ctrl+end'
HELP_1 = 'make a screenshot: ' + KEY_SCREEN.upper()
HELP_2 = 'exit: ' + KEY_EXIT.upper()
DIR_SEP = '/'
SAVE_PATH = 'C:' + DIR_SEP + 'screenshot'
GAME_DIR_DEFAULT = '_default'
# .jpg or .png
FILE_EXT = '.jpg'
SLEEP = 0.2


class ScreenShooter:
	def __init__(self):
		self.show_about()
		self.save_path = SAVE_PATH
		print('save_path: %s' % self.save_path)
		self.game_dir = self.get_game_dir()
		print('game_dir: %s' % self.game_dir)
		self.full_path = self.get_full_path()
		print('full_path: %s' % self.full_path)
		self.img_path = ''
		print('img_path is initialized...')
		print()

	@staticmethod
	def get_game_dir():
		print('please enter the name of game!')
		name_of_game = str(input())
		if name_of_game != '':
			return name_of_game
		else:
			print('using default directory: ' + GAME_DIR_DEFAULT)
			return GAME_DIR_DEFAULT

	def get_full_path(self):
		full_path = self.save_path + DIR_SEP + self.game_dir
		if os.path.exists(full_path):
			print('directory is exist: %s' % full_path)
		else:
			os.mkdir(full_path)
			print('directory created: %s' % full_path)
		return full_path

	def grab_screen(self):
		screen = pyag.screenshot()
		filename = self.get_format_time()
		img_name = filename + FILE_EXT
		self.img_path = self.full_path + DIR_SEP + img_name
		screen.save(self.img_path)
		del screen
		print('screenshot saved: %s' % self.img_path)

	@staticmethod
	def show_about():
		print(APP_NAME)
		print('version: ' + APP_VER)
		print(HELP_1)
		print(HELP_2)
		print()

	def run(self):
		while True:
			if keyboard.is_pressed(KEY_SCREEN):
				self.grab_screen()
				time.sleep(SLEEP)
			elif keyboard.is_pressed(KEY_EXIT):
				print('exit...')
				sys.exit(0)

	# type = human | ts
	@staticmethod
	def get_format_time():
		# datetime object and elements
		dto = datetime.now()
		year = str(dto.year)
		month = str(dto.month).zfill(2)
		day = str(dto.day).zfill(2)
		hour = str(dto.hour).zfill(2)
		minute = str(dto.minute).zfill(2)
		second = str(dto.second).zfill(2)
		micros = str(dto.microsecond)
		# human format
		# return year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second + '.' + micros
		# timestamp-like format
		return year + month + day + '_' + hour + minute + second + '_' + micros


ScreenShooter().run()
