# game setup
WIDTH = 1280
HEIGHT = 720
FPS = 60
UI_COLOR = (255, 255, 255)  # White for highlighted text
HOVER_COLOR = (255, 200, 0)  # Gold/yellow for selection
TEXT_COLOR = (255, 255, 255) # White
SPARE = (0,0,0)

# TILESIZE = 64
TILESIZE = 128
COLLISION_GRID_SIZE = 128
HITBOX_OFFSET = {
    'player': 20,
    'object': -40,
    'grass': -10,
    'invisible': 0
}

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../assets/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# #DialogBOx 
DIALOG_BOX_WIDTH = 1060
DIALOG_BOX_HEIGHT = 280
DIALOG_TEXT_WIDTH = 800
DIALOG_TEXT_HEIGHT = 150
DIALOG_FONT_SIZE = 13

# weapons
weapon_data = {
	# 'sword': {'cooldown': 100, 'damage': 15,'graphic':'../graphics/weapons/sword/full.png'},
	# 'lance': {'cooldown': 400, 'damage': 30,'graphic':'../graphics/weapons/lance/full.png'},
	# 'axe': {'cooldown': 300, 'damage': 20, 'graphic':'../graphics/weapons/axe/full.png'},
	# 'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'../graphics/weapons/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 10, 'graphic':'../graphics/weapons/sai/full.png'},
	'katana': {'cooldown': 100, 'damage': 15, 'graphic': '../assets/images/main character/weapons/katana/full.png'},
	'spear': {'cooldown': 400, 'damage': 30, 'graphic': '../assets/images/main character/weapons/spear/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic': '../assets/images/video assets/graphics/weapons/axe/full.png'},
	# 'rapier': {'cooldown': 50, 'damage': 8, 'graphic': '../assets/images/video assets/graphics/weapons/rapier/full.png'},
	# 'sai': {'cooldown': 80, 'damage': 10, 'graphic': '../assets/images/video assets/graphics/weapons/sai/full.png'}
}

# magic
magic_data = {
	# 'flame': {'strength': 5,'cost': 20,'graphic':'../graphics/particles/flame/fire.png'},
	# 'heal' : {'strength': 20,'cost': 10,'graphic':'../graphics/particles/heal/heal.png'}
	'flame': {'strength': 5, 'cost': 20, 'graphic': '../assets/images/video assets/graphics/particles/flame/fire.png'},
	'heal': {'strength': 20, 'cost': 10, 'graphic': '../assets/images/video assets/graphics/particles/heal/heal.png'}}

# enemy
monster_data = {
	# 'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	# 'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'../audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	# 'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	# 'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}
	'tree': {'health': 250, 'exp': 50, 'damage': 20, 'attack_type': 'slash','attack_sound': '../assets/images/video assets/audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
			 'attack_radius': 80, 'notice_radius': 340},
	'cherry tree': {'health': 250, 'exp': 50, 'damage': 20, 'attack_type': 'slash',
					'attack_sound': '../assets/images/video assets/audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
					'attack_radius': 80, 'notice_radius': 340},
	'snowy tree': {'health': 250, 'exp': 50, 'damage': 20, 'attack_type': 'slash',
				   'attack_sound': '../assets/images/video assets/audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
				   'attack_radius': 80, 'notice_radius': 340},
	'raccoon': {'health': 800, 'exp': 125, 'damage': 40, 'attack_type': 'claw',
				'attack_sound': '../assets/images/video assets/audio/attack/claw.wav', 'speed': 2, 'resistance': 3,
				'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 150, 'exp': 55, 'damage': 8, 'attack_type': 'thunder',
			   'attack_sound': '../assets/images/video assets/audio/attack/fireball.wav', 'speed': 6, 'resistance': 3,
			   'attack_radius': 60, 'notice_radius': 330},
	'bamboo': {'health': 150, 'exp': 60, 'damage': 6, 'attack_type': 'leaf_attack',
			   'attack_sound': '../assets/images/video assets/audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
			   'attack_radius': 50, 'notice_radius': 280},
    'oni': {
        'health': 500,'exp': 300,'damage': 40,'attack_type': 'smash','attack_sound': '../assets/images/video assets/audio/attack/claw.wav',
        'speed': 4,'resistance': 5,'attack_radius': 140,'notice_radius': 300},
    'ninja': {
        'health': 250,'exp': 100,'damage': 15,'attack_type': 'slash','attack_sound': '../assets/images/video assets/audio/attack/slash.wav',
        'speed': 5,'resistance': 2,'attack_radius': 60,'notice_radius': 320}
}
