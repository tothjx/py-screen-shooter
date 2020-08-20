import os
import sys
import keyboard
# import locale
from datetime import datetime
from PIL import ImageGrab

ENV_PROD = 'prod'
ENV_DEV = 'dev'
ENV = ENV_DEV
DIR_SEP = '\\'
LINE = '################################'
SAVE_PATH = 'C:' + DIR_SEP + 'screenshot'
GAME_DIR_DEFAULT = '_default'
FORMAT_HUMAN = 'human'
FORMAT_TS = 'ts'
POINT_START = 'starting point'
POINT_SAVE = 'saving point'

class ScreenShooter:
	def __init__(self):
		self.log(POINT_START)
		self.log(LINE)
		self.save_path = SAVE_PATH
		self.log('save_path = %s' % self.save_path)
		self.game_dir = self.getGameDir()
		self.log('game_dir = %s' % self.game_dir)
		self.full_path = self.getFullPath()
		self.log('full_path = %s' % self.full_path)
		self.img_path = ''
		self.log('img_path is initialized...')
		print()

	def getGameDir(self):
		print('please enter the name of game!')
		name_of_game = str(input())
		if name_of_game != '':
			return name_of_game
		else:
			self.log('using default directory: ' + GAME_DIR_DEFAULT)
			return GAME_DIR_DEFAULT

	def getFullPath(self):
		full_path = self.save_path + DIR_SEP + self.game_dir
		if os.path.exists(full_path) == False:
			os.mkdir(full_path)
			print('directory created: %s' % full_path)
		else:
			print('directory is exist: %s' % full_path)
		return full_path

	def grabScreen(self):
		screen = ImageGrab.grab()
		# <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=5120x2880 at 0x110BB7748>
		img_name = self.getFormatTime() + '.png'
		self.img_path = self.full_path + DIR_SEP + img_name
		self.log('img_path = ' + self.img_path)
		screen.save(self.img_path)
		print('screenshot saved: %s' % self.img_path)

	# type = human | ts
	def getFormatTime(self, type=FORMAT_TS):
		# locale.setlocale(locale.LC_ALL, '')
		# datetime object and elements
		dto = datetime.now()
		year = str(dto.year)
		month = str(dto.month).zfill(2)
		day = str(dto.day).zfill(2)
		hour = str(dto.hour).zfill(2)
		minute = str(dto.minute).zfill(2)
		second = str(dto.second).zfill(2)
		micros = str(dto.microsecond)
		if type == FORMAT_HUMAN:
			# human format
			return year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second + '.' + micros
		else:
			# like timestamp
			return year + month + day + hour + minute + second + micros

	def run(self):
		while True:
			if keyboard.is_pressed('f12'):
				self.grabScreen()
				print()
			elif keyboard.is_pressed('ctrl+end'):
				self.log('program is stopping...')
				sys.exit(0)

	def log(self, msg):
		if msg != '':
			print(msg)
		else:
			print('message was empty...')

########
