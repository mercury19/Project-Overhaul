from compiler import *
import random


####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp. is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn.reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below... 
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
  n = 0
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  n |= wp_firearm(x)
  return n

def wp2(x,r):
  n = 0
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(r)
  n |= wp_crossbow(r)
  n |= wp_throwing(r)
  n |= wp_firearm(r)
  return n  
  
def wpe(m,a,c,t,g):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   n |= wp_firearm(g)
   return n
   
def wpm(o,w,p,r):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(r)
   n |= wp_crossbow(r)
   n |= wp_throwing(r)
   n |= wp_firearm(r)
   return n

def wpex(o,w,p,a,c,t,g):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   n |= wp_firearm(g)
   return n
   
def wp_melee(x):
  n = 0
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n
  
def wp_ranged(a,c,t,g):
   n = 0
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   n |= wp_firearm(g)
   return n
   
def wp_bow(m,b):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(b)
   n |= wp_crossbow(m)
   n |= wp_throwing(m)
   n |= wp_firearm(m)
   return n

def wp_xbow(m,x):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(m)
   n |= wp_crossbow(x)
   n |= wp_throwing(m)
   n |= wp_firearm(m)
   return n
   
def wp_throw(m,t):
	n = 0
	n |= wp_one_handed(m)
	n |= wp_two_handed(m)
	n |= wp_polearm(m)
	n |= wp_archery(m)
	n |= wp_crossbow(m)
	n |= wp_throwing(t)
	n |= wp_firearm(m)
	return n

def wp_gun(m,g):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(m)
   n |= wp_crossbow(m)
   n |= wp_throwing(m)
   n |= wp_firearm(g)
   return n
   
def wp_sarranid(m,r,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(r)
   n |= wp_crossbow(r)
   n |= wp_throwing(t)
   n |= wp_firearm(r)
   return n
   
def wp_skirmish(m,r):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(r)
   n |= wp_crossbow(m)
   n |= wp_throwing(r)
   n |= wp_firearm(m)
   return n   
   
def wp_1h(o,m,r):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(r)
   n |= wp_crossbow(r)
   n |= wp_throwing(r)
   n |= wp_firearm(r)
   return n

def wp_2h(w,m,r):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(w)
   n |= wp_polearm(m)
   n |= wp_archery(r)
   n |= wp_crossbow(r)
   n |= wp_throwing(r)
   n |= wp_firearm(r)
   return n
   
def wp_pole(p,m,r):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(p)
   n |= wp_archery(r)
   n |= wp_crossbow(r)
   n |= wp_throwing(r)
   n |= wp_firearm(r)
   return n
   
#Skills
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
knows_common_multiplayer = knows_trade_10|knows_inventory_management_10|knows_prisoner_management_10|knows_leadership_10|knows_spotting_10|knows_pathfinding_10|knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10
def_attrib = str_7 | agi_5 | int_4 | cha_4
def_attrib_multiplayer = int_30 | cha_30



knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

lord_attrib = str_20|agi_20|int_20|cha_20|level(38)

knight_attrib_1 = str_15|agi_14|int_8|cha_16|level(22)
knight_attrib_2 = str_16|agi_16|int_10|cha_18|level(26)
knight_attrib_3 = str_18|agi_17|int_12|cha_20|level(30)
knight_attrib_4 = str_19|agi_19|int_13|cha_22|level(35)
knight_attrib_5 = str_20|agi_20|int_15|cha_25|level(41)
knight_skills_1 = knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3
knight_skills_2 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5
knight_skills_3 = knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6
knight_skills_4 = knows_riding_6|knows_ironflesh_5|knows_power_strike_6|knows_athletics_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7
knight_skills_5 = knows_riding_7|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

swadian_face_younger_1 = 0x0000000000002001355335371861249200000000001c96520000000000000000
swadian_face_young_1   = 0x00000004400023c1355335371861249200000000001c96520000000000000000
swadian_face_middle_1  = 0x00000008000023c1355335371861249200000000001c96520000000000000000
swadian_face_old_1     = 0x0000000e000023c0355335371861249200000000001c96520000000000000000
swadian_face_older_1   = 0x0000000fc00023c0355335371861249200000000001c96520000000000000000

swadian_face_younger_2 = 0x000000003a0045c549fddefdffffffff00000000001e6db60000000000000000
swadian_face_young_2   = 0x000000033a0045c549fddefdffffffff00000000001e6db60000000000000000
swadian_face_middle_2  = 0x00000007ba0045c549fddefdffffffff00000000001e6db60000000000000000
swadian_face_old_2     = 0x0000000e3b0045c549fddefdffffffff00000000001e6db60000000000000000
swadian_face_older_2   = 0x0000000ffa0045c549fddefdffffffff00000000001e6db60000000000000000

vaegir_face_younger_1 = 0x000000001d001141044c21928821245200000000001d22190000000000000000
vaegir_face_young_1   = 0x000000029b001181044c21928821245200000000001d22190000000000000000
vaegir_face_middle_1  = 0x000000075f001181044c21928821245200000000001d22190000000000000000
vaegir_face_old_1     = 0x0000000e1f001181044c21928821245200000000001d22190000000000000000
vaegir_face_older_1   = 0x0000000fdf001180044c21928821245200000000001d22190000000000000000

vaegir_face_younger_2 = 0x0000000037002189497e97cb5fb27fff00000000001ff8370000000000000000
vaegir_face_young_2   = 0x0000000477002249497e97cb5fb27fff00000000001ff8370000000000000000
vaegir_face_middle_2  = 0x0000000877002349497e97cb5fb27fff00000000001ff8370000000000000000
vaegir_face_old_2     = 0x0000000e37002349497e97cb5fb27fff00000000001ff8370000000000000000
vaegir_face_older_2   = 0x0000000ff7002349497e97cb5fb27fff00000000001ff8370000000000000000

khergit_face_younger_1 = 0x00000000190830ca209d69b4100906da00000000001e10e30000000000000000
khergit_face_young_1   = 0x00000003590830ca209d69b4100906da00000000001e10e30000000000000000
khergit_face_middle_1  = 0x00000007d90830ca209d69b4100906da00000000001e10e30000000000000000
khergit_face_old_1     = 0x0000000e190830ca209d69b4100906da00000000001e10e30000000000000000
khergit_face_older_1   = 0x0000000fd90830ca209d69b4100906da00000000001e10e30000000000000000

khergit_face_younger_2 = 0x000000003f08514d49fff7d86cffffff00000000001ff97f0000000000000000
khergit_face_young_2   = 0x000000047f08514d49fff7d86cffffff00000000001ff97f0000000000000000
khergit_face_middle_2  = 0x00000007bf08514d49fff7d86cffffff00000000001ff97f0000000000000000
khergit_face_old_2     = 0x0000000e3f08518d49fff7d86cffffff00000000001ff97f0000000000000000
khergit_face_older_2   = 0x0000000fff0851cd49fff7d86cffffff00000000001ff97f0000000000000000

nord_face_younger_1 = 0x000000000000014104c200928801249200000000001d24100000000000000000
nord_face_young_1   = 0x000000044000014104c200928801249200000000001d24100000000000000000
nord_face_middle_1  = 0x000000084000014104c200928801249200000000001d24100000000000000000
nord_face_old_1     = 0x0000000e0000014104c200928801249200000000001d24100000000000000000
nord_face_older_1   = 0x0000000e0000014004c200928801249200000000001d24100000000000000000

nord_face_younger_2 = 0x000000002b00218a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_young_2   = 0x000000036b00234a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_middle_2  = 0x00000007eb00234a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_old_2     = 0x0000000deb00234a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_older_2   = 0x0000000feb0023465bfcbdbb67b7ff7f00000000001eeb6f0000000000000000

rhodok_face_younger_1 = 0x0000000000003144355355370861008200000000001c96520000000000000000
rhodok_face_young_1   = 0x0000000500003141355355370861008200000000001c96520000000000000000
rhodok_face_middle_1  = 0x0000000840003141355355370861008200000000001c96520000000000000000
rhodok_face_old_1     = 0x0000000dc0003192355355370861008200000000001c96520000000000000000
rhodok_face_older_1   = 0x0000000fc0003192355355370861008200000000001c96520000000000000000

rhodok_face_younger_2 = 0x000000003e0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
rhodok_face_young_2   = 0x000000037e0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
rhodok_face_middle_2  = 0x000000083e0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
rhodok_face_old_2     = 0x0000000dfe0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
rhodok_face_older_2   = 0x0000000ffe0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000

sarranid_face_younger_1 = 0x000000000000710004820c24204c000200000000001d16100000000000000000
sarranid_face_young_1   = 0x000000040000710004820c24204c000200000000001d16100000000000000000
sarranid_face_middle_1  = 0x000000088000710004820c24204c000200000000001d16100000000000000000
sarranid_face_old_1     = 0x0000000e0000718004820c24204c000200000000001d16100000000000000000
sarranid_face_older_1   = 0x0000000fc000718004820c24204c000200000000001d16100000000000000000

sarranid_face_younger_2 = 0x000000003f00714049fefe393fffc7ff00000000001ef96f0000000000000000
sarranid_face_young_2   = 0x000000043f00724049fefe393fffc7ff00000000001ef96f0000000000000000
sarranid_face_middle_2  = 0x00000007bf00728049fefe393fffc7ff00000000001ef96f0000000000000000
sarranid_face_old_2     = 0x0000000e3f00728049fefe393fffc7ff00000000001ef96f0000000000000000
sarranid_face_older_2   = 0x0000000fff00728049fefe393fffc7ff00000000001ef96f0000000000000000

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

vaegir_woman_face_1   = 0x0000000180100006124925124928924900000000001c92890000000000000000
vaegir_woman_face_2   = 0x00000001bf1010061db6d75db6b6dbad00000000001c92890000000000000000

khergit_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
khergit_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

nord_woman_face_1     = 0x0000000180100006124925124928924900000000001c92890000000000000000
nord_woman_face_2     = 0x00000001a01010061db6d75db6b6dbad00000000001c92890000000000000000

rhodok_woman_face_1   = 0x0000000180102006124925124928924900000000001c92890000000000000000
rhodok_woman_face_2   = 0x00000001bf1020061db6d75db6b6dbad00000000001c92890000000000000000

sarranid_woman_face_1 = 0x0000000000004001000000000000000000000000001c00000000000000000000
sarranid_woman_face_2 = 0x00000003bf0040067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_younger_1  = 0x0000000000100006124925124928924900000000001c92890000000000000000
swadian_woman_face_young_1    = 0x0000000400100006124925124928924900000000001c92890000000000000000
swadian_woman_face_middle_1   = 0x0000000800100006124925124928924900000000001c92890000000000000000
swadian_woman_face_old_1      = 0x0000000d00100006124925124928924900000000001c92890000000000000000
swadian_woman_face_older_1    = 0x0000000fc0100006124925124928924900000000001c92890000000000000000

swadian_woman_face_younger_2  = 0x00000000bf1020061db6d75db6b6dbad00000000001c92890000000000000000
swadian_woman_face_young_2    = 0x00000003bf1020061db6d75db6b6dbad00000000001c92890000000000000000
swadian_woman_face_middle_2   = 0x00000007bf1020061db6d75db6b6dbad00000000001c92890000000000000000
swadian_woman_face_old_2      = 0x0000000bff1020061db6d75db6b6dbad00000000001c92890000000000000000
swadian_woman_face_older_2    = 0x0000000fff1020061db6d75db6b6dbad00000000001c92890000000000000000

vaegir_woman_face_younger_1   = 0x0000000000100006124925124928924900000000001c92890000000000000000
vaegir_woman_face_young_1     = 0x0000000400100006124925124928924900000000001c92890000000000000000
vaegir_woman_face_middle_1    = 0x0000000800100006124925124928924900000000001c92890000000000000000
vaegir_woman_face_old_1       = 0x0000000d00100006124925124928924900000000001c92890000000000000000
vaegir_woman_face_older_1     = 0x0000000fc0100006124925124928924900000000001c92890000000000000000

vaegir_woman_face_younger_2   = 0x00000000bf1010061db6d75db6b6dbad00000000001c92890000000000000000
vaegir_woman_face_young_2     = 0x00000003bf1010061db6d75db6b6dbad00000000001c92890000000000000000
vaegir_woman_face_middle_2    = 0x00000007bf1010061db6d75db6b6dbad00000000001c92890000000000000000
vaegir_woman_face_old_2       = 0x0000000bff1010061db6d75db6b6dbad00000000001c92890000000000000000
vaegir_woman_face_older_2     = 0x0000000fff1010061db6d75db6b6dbad00000000001c92890000000000000000

khergit_woman_face_younger_1  = 0x0000000000103006124925124928924900000000001c92890000000000000000
khergit_woman_face_young_1    = 0x0000000400103006124925124928924900000000001c92890000000000000000
khergit_woman_face_middle_1   = 0x0000000800103006124925124928924900000000001c92890000000000000000
khergit_woman_face_old_1      = 0x0000000d00103006124925124928924900000000001c92890000000000000000
khergit_woman_face_older_1    = 0x0000000fc0103006124925124928924900000000001c92890000000000000000

khergit_woman_face_younger_2  = 0x00000000bf1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000
khergit_woman_face_young_2    = 0x00000003bf1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000
khergit_woman_face_middle_2   = 0x00000007bf1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000
khergit_woman_face_old_2      = 0x0000000bff1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000
khergit_woman_face_older_2    = 0x0000000fff1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

nord_woman_face_younger_1     = 0x0000000000100006124925124928924900000000001c92890000000000000000
nord_woman_face_young_1       = 0x0000000400100006124925124928924900000000001c92890000000000000000
nord_woman_face_middle_1      = 0x0000000800100006124925124928924900000000001c92890000000000000000
nord_woman_face_old_1         = 0x0000000d00100006124925124928924900000000001c92890000000000000000
nord_woman_face_older_1       = 0x0000000fc0100006124925124928924900000000001c92890000000000000000

nord_woman_face_younger_2     = 0x00000000b01010061db6d75db6b6dbad00000000001c92890000000000000000
nord_woman_face_young_2       = 0x00000003b01010061db6d75db6b6dbad00000000001c92890000000000000000
nord_woman_face_middle_2      = 0x00000007b01010061db6d75db6b6dbad00000000001c92890000000000000000
nord_woman_face_old_2         = 0x0000000bf01010061db6d75db6b6dbad00000000001c92890000000000000000
nord_woman_face_older_2       = 0x0000000ff01010061db6d75db6b6dbad00000000001c92890000000000000000

rhodok_woman_face_younger_1   = 0x0000000000102006124925124928924900000000001c92890000000000000000
rhodok_woman_face_young_1     = 0x0000000400102006124925124928924900000000001c92890000000000000000
rhodok_woman_face_middle_1    = 0x0000000800102006124925124928924900000000001c92890000000000000000
rhodok_woman_face_old_1       = 0x0000000d00102006124925124928924900000000001c92890000000000000000
rhodok_woman_face_older_1     = 0x0000000fc0102006124925124928924900000000001c92890000000000000000

rhodok_woman_face_younger_2   = 0x00000000bf1020061db6d75db6b6dbad00000000001c92890000000000000000
rhodok_woman_face_young_2     = 0x00000003bf1020061db6d75db6b6dbad00000000001c92890000000000000000
rhodok_woman_face_middle_2    = 0x00000007bf1020061db6d75db6b6dbad00000000001c92890000000000000000
rhodok_woman_face_old_2       = 0x0000000bff1020061db6d75db6b6dbad00000000001c92890000000000000000
rhodok_woman_face_older_2     = 0x0000000fff1020061db6d75db6b6dbad00000000001c92890000000000000000

sarranid_woman_face_younger_1 = 0x0000000000004001000000000000000000000000001c00000000000000000000
sarranid_woman_face_young_1   = 0x0000000400004001000000000000000000000000001c00000000000000000000
sarranid_woman_face_middle_1  = 0x0000000800004001000000000000000000000000001c00000000000000000000
sarranid_woman_face_old_1     = 0x0000000d00004001000000000000000000000000001c00000000000000000000
sarranid_woman_face_older_1   = 0x0000000fc0004001000000000000000000000000001c00000000000000000000

sarranid_woman_face_younger_2 = 0x00000000bf0040067ff7fbffefff6dff00000000001f6dbf0000000000000000
sarranid_woman_face_young_2   = 0x00000003bf0040067ff7fbffefff6dff00000000001f6dbf0000000000000000
sarranid_woman_face_middle_2  = 0x00000007bf0040067ff7fbffefff6dff00000000001f6dbf0000000000000000
sarranid_woman_face_old_2     = 0x0000000bff0040067ff7fbffefff6dff00000000001f6dbf0000000000000000
sarranid_woman_face_older_2   = 0x0000000fff0040067ff7fbffefff6dff00000000001f6dbf0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2

undead_face1  = 0x0000000000000000000000000000000000000000000000000000000000000000
undead_face2  = 0x000000003f000493000000000000000000000000000000000000000000000000
   
#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield


troops = [
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac.player_faction,
   [],
   str_4|agi_4|int_4|cha_4,wp(15),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac.commoners,
   [itm.leather_jerkin, itm.leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac.commoners,
   [itm.tribal_warrior_outfit, itm.leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac.commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
  ["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac.commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],

  ["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["regular_fighter","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_riding_1|knows_shield_2,mercenary_face_1, mercenary_face_2],
  ["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac.commoners,
   [itm.hide_boots],
   str_10|agi_10|level(17),wp(110),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_12|agi_11|level(22),wp(140),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_3|knows_shield_4,mercenary_face_1, mercenary_face_2],

  ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_7|agi_6|level(7),wp(70),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_8|agi_7|level(9),wp(80),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_9|agi_8|level(13),wp(100),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_10|agi_9|level(15),wp(110),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_10|agi_10|level(17),wp(120),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_11|agi_10|level(19),wp(130),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_12|agi_11|level(21),wp(140),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.hide_boots],
   str_12|agi_12|level(23),wp(150),knows_common,mercenary_face_1, mercenary_face_2],

  ["cattle","Cattle","Cattle",0,no_scene,reserved,fac.neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],

# Soldiers:
# This troop is the troop marked as soldiers_begin
  ["farmer","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.cleaver,itm.knife,itm.pitch_fork,itm.sickle,itm.club,itm.stones,itm.leather_cap,itm.felt_hat,itm.felt_hat,itm.linen_tunic,itm.coarse_tunic,itm.nomad_boots,itm.wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.cleaver,itm.knife,itm.club,itm.quarter_staff,itm.dagger,itm.stones,itm.leather_cap,itm.linen_tunic,itm.coarse_tunic,itm.leather_apron,itm.nomad_boots,itm.wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
   
# Mercenaries
#############
  ["watchman","Watchman","Watchmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac.commoners,
   [itm.bolts,itm.spiked_club,itm.fighting_pick,itm.sword_medieval_a,itm.boar_spear,itm.hunting_crossbow,itm.light_crossbow,itm.tab_shield_round_a,itm.tab_shield_round_b,itm.padded_cloth,itm.leather_jerkin,itm.leather_cap,itm.padded_coif,itm.footman_helmet,itm.nomad_boots,itm.wrapping_boots],
   def_attrib|level(9),wp(75),knows_common|knows_shield_1,mercenary_face_1, mercenary_face_2],
  ["caravan_guard","Caravan Guard","Caravan Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,no_scene,0,fac.commoners,
   [itm.spear,itm.fighting_pick,itm.sword_medieval_a,itm.voulge,itm.tab_shield_round_b,itm.tab_shield_round_c,itm.leather_jerkin,itm.leather_vest,itm.hide_boots,itm.padded_coif,itm.nasal_helmet,itm.footman_helmet,itm.saddle_horse],
   def_attrib|level(14),wp(85),knows_common|knows_riding_2|knows_ironflesh_1|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["mercenary_footman","Mercenary Footman","Mercenary Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac.neutral,
   [itm.bolts,itm.spear,itm.fighting_pick,itm.sword_medieval_a,itm.tab_shield_round_b,itm.light_crossbow,
    itm.leather_jerkin,itm.studded_leather_coat,itm.nomad_boots,itm.mail_coif,itm.norman_helmet],
   def_attrib|level(14),wp(95),knows_common|knows_riding_2|knows_ironflesh_2|knows_shield_2|knows_power_strike_2,mercenary_face_1, mercenary_face_2],
  ["mercenary_archer","Mercenary Archer","Mercenary Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac.neutral,
   [itm.arrows,itm.axe,itm.hand_axe,itm.short_bow,itm.leather_jerkin,itm.leather_vest,itm.nomad_boots,itm.skullcap],
   def_attrib|level(14),wp(95),knows_common|knows_riding_2|knows_ironflesh_2|knows_power_draw_2|knows_power_strike_2,mercenary_face_1, mercenary_face_2],
  ["mercenary_swordsman","Mercenary Swordsman","Mercenary Swordsmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac.neutral,
   [itm.bastard_sword_a,itm.sword_medieval_b,itm.sword_medieval_b_small,itm.tab_shield_heater_c,itm.mail_hauberk,itm.haubergeon,itm.leather_boots,itm.mail_chausses,itm.kettle_hat,itm.mail_coif,itm.flat_topped_helmet, itm.helmet_with_neckguard],
   def_attrib|level(20),wp(100),knows_common|knows_riding_3|knows_ironflesh_3|knows_shield_3|knows_power_strike_3,mercenary_face_1, mercenary_face_2],
  ["hired_blade","Hired Blade","Hired Blades",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac.neutral,
   [itm.bastard_sword_b,itm.sword_medieval_c,itm.tab_shield_heater_cav_a,itm.haubergeon,itm.mail_chausses,itm.iron_greaves,itm.plate_boots,itm.guard_helmet,itm.great_helmet,itm.bascinet, itm.leather_gloves],
   def_attrib|level(25),wp(130),knows_common|knows_riding_3|knows_athletics_5|knows_shield_5|knows_power_strike_5|knows_ironflesh_5,mercenary_face_1, mercenary_face_2],
  ["mercenary_crossbowman","Mercenary Crossbowman","Mercenary Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac.neutral,
   [itm.bolts,itm.spiked_club,itm.fighting_pick,itm.sword_medieval_a,itm.boar_spear,itm.crossbow,itm.tab_shield_pavise_a,itm.tab_shield_round_b,itm.padded_cloth,itm.leather_jerkin,itm.leather_cap,itm.padded_coif,itm.footman_helmet,itm.nomad_boots,itm.wrapping_boots],
   def_attrib|level(19),wp_xbow(90,130),knows_common|knows_athletics_5|knows_shield_1,mercenary_face_1, mercenary_face_2],
  ["mercenary_longbowman","Mercenary Longbowman","Mercenary Longbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac.neutral,
   [itm.bodkin_arrows,itm.maul,itm.falchion,itm.long_bow,itm.studded_leather_coat,itm.leather_jerkin,itm.skullcap,itm.nomad_boots,itm.leather_boots],
   def_attrib|level(20),wp_bow(90,120),knows_common|knows_athletics_4|knows_ironflesh_3|knows_power_draw_4|knows_power_strike_3,mercenary_face_1, mercenary_face_2],
  ["mercenary_horse_archer","Mercenary Horse Archer","Mercenary Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged,no_scene,reserved,fac.neutral,
   [itm.sword_khergit_1,itm.fighting_axe,itm.tab_shield_small_round_a,itm.barbed_arrows,itm.nomad_bow,itm.studded_leather_coat,itm.leather_jerkin,itm.leather_boots,itm.spiked_helmet,itm.steppe_horse],
   def_attrib|level(20),wp(100),knows_common|knows_riding_4|knows_ironflesh_3|knows_horse_archery_2|knows_power_draw_3|knows_shield_1|knows_power_strike_2,mercenary_face_1, mercenary_face_2],
  ["mercenary_horseman","Mercenary Horseman","Mercenary Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac.neutral,
   [itm.lance,itm.bastard_sword_a,itm.sword_medieval_b,itm.tab_shield_heater_c,itm.mail_shirt,itm.haubergeon,itm.leather_boots,itm.norman_helmet,itm.mail_coif,itm.helmet_with_neckguard,itm.saddle_horse,itm.courser],
   def_attrib|level(20),wp(100),knows_common|knows_riding_4|knows_ironflesh_3|knows_shield_2|knows_power_strike_3,mercenary_face_1, mercenary_face_2],
  ["mercenary_cavalry","Mercenary Cavalry","Mercenary Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac.neutral,
   [itm.heavy_lance,itm.bastard_sword_a,itm.sword_medieval_b,itm.tab_shield_heater_c,itm.cuir_bouilli,itm.banded_armor,itm.hide_boots,itm.kettle_hat,itm.mail_coif,itm.flat_topped_helmet,itm.helmet_with_neckguard,itm.warhorse,itm.hunter],
   def_attrib|level(25),wp(130),knows_common|knows_riding_5|knows_ironflesh_4|knows_shield_5|knows_power_strike_4,mercenary_face_1, mercenary_face_2],
  # Elite Mercenaries; can't be hired, only upgraded:
  ["mercenary_musketeer","Mercenary Musketeer","Mercenary Musketeers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac.neutral,
   [itm.cartridges,itm.spiked_club,itm.fighting_pick,itm.sword_medieval_a,itm.voulge,itm.arquebus,itm.leather_jerkin,itm.leather_cap,itm.nomad_boots,itm.hide_boots],
   def_attrib|level(20),wp_gun(90,100),knows_common|knows_athletics_5|knows_shield_1,mercenary_face_1, mercenary_face_2],
  ["black_guard","Black Guard","Black Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,no_scene,reserved,fac.neutral,
   [itm.sword_of_war,itm.great_axe,itm.bec_de_corbin_a,itm.black_armor,itm.black_greaves,itm.black_helmet,itm.leather_gloves],
   def_attrib|level(26),wp(130),knows_common|knows_riding_3|knows_athletics_5|knows_shield_5|knows_power_strike_5|knows_ironflesh_5,mercenary_face_1, mercenary_face_2],
  ["black_knight","Black Knight","Black Knights",tf_mounted|tf_guarantee_all_wo_ranged,no_scene,reserved,fac.neutral,
   [itm.heavy_lance,itm.morningstar,itm.morningstar_short,itm.tab_shield_heater_c,itm.black_armor,itm.black_greaves,itm.black_helmet,itm.leather_gloves,[itm.saddle_horse,imod.heavy]],
   def_attrib|level(26),wp(130),knows_common|knows_riding_5|knows_ironflesh_4|knows_shield_5|knows_power_strike_4,mercenary_face_1, mercenary_face_2],

# Kingdom of Swadia
###################
  ["swadian_recruit","Swadian Recruit","Swadian Recruits",tf_guarantee_armor,0,0,fac.kingdom_1,
   [itm.scythe,itm.hatchet,itm.pickaxe,itm.club,itm.stones,itm.tab_shield_heater_a,itm.leather_cap,itm.felt_hat,itm.felt_hat,
    itm.shirt,itm.coarse_tunic,itm.leather_apron,itm.nomad_boots,itm.wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
  ["swadian_militia","Swadian Militia","Swadian Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac.kingdom_1,
   [itm.bolts,itm.spiked_club,itm.fighting_pick,itm.boar_spear,itm.hunting_crossbow,itm.tab_shield_heater_a,
    itm.padded_cloth,itm.red_gambeson,itm.arming_cap,itm.arming_cap,itm.ankle_boots,itm.wrapping_boots],
   def_attrib|level(9),wp(75),knows_common,swadian_face_young_1, swadian_face_old_2],
  ["swadian_footman","Swadian Footman","Swadian Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac.kingdom_1,
   [itm.spear,itm.fighting_pick,itm.sword_medieval_b_small,itm.sword_medieval_a,itm.tab_shield_heater_b,
    itm.mail_with_tunic_red,itm.ankle_boots,itm.mail_coif,itm.norman_helmet],
   def_attrib|level(14),wp_melee(85),knows_common|knows_ironflesh_2|knows_shield_2|knows_athletics_2|knows_power_strike_2,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry","Swadian Infantry","Swadian Infantry",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_1,
   [itm.pike,itm.fighting_pick,itm.bastard_sword_a,itm.sword_medieval_a,itm.sword_medieval_b_small,itm.tab_shield_heater_c,
    itm.mail_with_surcoat,itm.haubergeon,itm.mail_chausses,itm.leather_boots,itm.segmented_helmet,itm.flat_topped_helmet,itm.helmet_with_neckguard],
   def_attrib|level(20),wp_melee(105),knows_common|knows_riding_3|knows_ironflesh_2|knows_power_strike_2|knows_shield_3|knows_athletics_3,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_sergeant","Swadian Sergeant","Swadian Sergeants",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_1,
   [itm.awlpike,itm.bastard_sword_b,itm.morningstar,itm.sword_medieval_c,itm.tab_shield_heater_d,
    itm.coat_of_plates_red,itm.brigandine_red,itm.mail_boots,itm.iron_greaves,itm.flat_topped_helmet,itm.guard_helmet,itm.mail_mittens,itm.gauntlets],
   def_attrib|level(25),wp_melee(135),knows_common|knows_shield_4|knows_ironflesh_4|knows_power_strike_4|knows_athletics_4,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_skirmisher","Swadian Skirmisher","Swadian Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_1,
   [itm.bolts,itm.light_crossbow,itm.hunting_crossbow,itm.club,itm.long_voulge,itm.tab_shield_heater_a,
    itm.red_gambeson,itm.padded_cloth,itm.ankle_boots,itm.arming_cap,itm.arming_cap],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_crossbowman","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_1,
   [itm.bolts,itm.crossbow,itm.light_crossbow,itm.fighting_pick,itm.sword_medieval_a,itm.long_voulge,itm.tab_shield_heater_b,
    itm.leather_jerkin,itm.red_gambeson,itm.leather_boots,itm.ankle_boots,itm.norman_helmet,itm.segmented_helmet],
   def_attrib|level(19),wp_xbow(90,100),knows_common|knows_riding_2|knows_ironflesh_1|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_sharpshooter","Swadian Sharpshooter","Swadian Sharpshooters",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_1,
   [itm.bolts,itm.crossbow,itm.crossbow,itm.heavy_crossbow,itm.sword_medieval_b_small,itm.sword_medieval_a,itm.long_voulge,itm.tab_shield_heater_c,
    itm.haubergeon,itm.arena_armor_red,itm.leather_boots,itm.mail_chausses,itm.kettle_hat,itm.helmet_with_neckguard,itm.leather_gloves],
   str_14 | agi_10 | int_4 | cha_4|level(24),wp_xbow(100,120),knows_common|knows_power_draw_3|knows_ironflesh_1|knows_power_strike_1|knows_athletics_2,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_man_at_arms","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac.kingdom_1,
   [itm.lance,itm.fighting_pick,itm.bastard_sword_b,itm.sword_medieval_b,itm.sword_medieval_c_small,itm.tab_shield_heater_cav_a,
    itm.haubergeon,itm.mail_with_surcoat,itm.mail_chausses,itm.norman_helmet,itm.mail_coif,itm.flat_topped_helmet,itm.helmet_with_neckguard,itm.warhorse,itm.warhorse,itm.hunter],
   def_attrib|level(21),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_knight","Swadian Knight","Swadian Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac.kingdom_1,
   [itm.heavy_lance,itm.sword_two_handed_b,itm.sword_medieval_d_long,itm.morningstar,itm.morningstar,itm.sword_medieval_d_long,itm.tab_shield_heater_cav_b,
    itm.coat_of_plates_red,itm.cuir_bouilli,itm.plate_boots,itm.guard_helmet,itm.great_helmet,itm.bascinet,itm.charger,itm.warhorse,itm.gauntlets,itm.mail_mittens],
   def_attrib|level(28),wp_1h(150,130,75),knows_common|knows_riding_5|knows_shield_5|knows_ironflesh_5|knows_power_strike_5,swadian_face_middle_1, swadian_face_older_2],

  ["swadian_musketeer","Swadian Musketeer","Swadian Musketeers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_1,
   [itm.cartridges,itm.arquebus,itm.club,itm.spiked_club,itm.red_gambeson,itm.leather_cap,itm.leather_cap,itm.ankle_boots],
   def_attrib|level(15),wp_gun(80,60),knows_common|knows_ironflesh_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_elite_guard","Swadian Royal Guard","Swadian Royal Guards",tf_mounted|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_1,
   [itm.awlpike,itm.shortened_voulge,itm.sword_two_handed_b,itm.morningstar,itm.great_sword,
    itm.plate_armor,itm.plate_boots,itm.gauntlets,itm.great_helmet,itm.guard_helmet],
   def_attrib|level(25),wp_melee(135),knows_common|knows_shield_4|knows_ironflesh_4|knows_power_strike_4|knows_athletics_4,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_heavy_crossbowman","Swadian Heavy Crossbowman","Swadian Heavy Crossbowmen",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac.kingdom_1,
   [itm.bolts,itm.heavy_crossbow,itm.sword_medieval_c_small,itm.sword_medieval_c,itm.tab_shield_heater_d,
    itm.coat_of_plates_red,itm.mail_boots,itm.kettle_hat,itm.guard_helmet,itm.leather_gloves],
   str_15 | agi_10 | int_4 | cha_4|level(25),wp_xbow(110,130),knows_common|knows_power_draw_3|knows_shield_2|knows_ironflesh_1|knows_power_strike_1|knows_athletics_3,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_reiter","Swadian Reiter","Swadian Reiter",tf_mounted|tf_guarantee_all,0,0,fac.kingdom_1,
   [itm.cartridges,itm.flintlock_pistol,itm.fighting_pick,itm.bastard_sword_b,itm.sword_medieval_b,itm.fighting_axe,itm.steel_shield,
    itm.brigandine_red,itm.splinted_greaves,itm.bascinet,itm.guard_helmet,itm.leather_gloves,itm.hunter],
   def_attrib|level(24),wp_gun(100,80),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_horse_archery_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_cuirassier","Swadian Cuirassier","Swadian Cuirassiers",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac.kingdom_1,
   [itm.great_lance,itm.great_lance,itm.sword_medieval_d_long,itm.morningstar,itm.tab_shield_heater_cav_b,
    itm.plate_armor,itm.plate_boots,itm.guard_helmet,itm.great_helmet,itm.gauntlets,itm.charger],
   def_attrib|level(28),wp_melee(130),knows_common|knows_riding_5|knows_shield_5|knows_ironflesh_5|knows_power_strike_5,swadian_face_middle_1, swadian_face_older_2],
  
  ["swadian_messenger","Swadian Messenger","Swadian Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac.kingdom_1,
   [itm.sword_medieval_a,itm.leather_jerkin,itm.leather_boots,itm.courser,itm.leather_gloves,itm.light_crossbow,itm.bolts],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_young_1, swadian_face_old_2],
  ["swadian_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_1,
   [itm.awlpike,itm.pike,itm.great_sword,itm.morningstar,itm.sword_medieval_b,itm.tab_shield_heater_c,itm.coat_of_plates_red,itm.plate_armor,itm.plate_boots,itm.guard_helmet,itm.helmet_with_neckguard,itm.bascinet,itm.guard_helmet,itm.leather_gloves],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_1,
   [itm.awlpike,itm.pike,itm.great_sword,itm.morningstar,itm.sword_medieval_b,itm.tab_shield_heater_c,itm.tab_shield_heater_d,itm.coat_of_plates_red,itm.plate_armor,itm.plate_boots,itm.guard_helmet,itm.helmet_with_neckguard,itm.bascinet,itm.guard_helmet,itm.leather_gloves],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

# Kingdom of Vaegirs
####################
  ["vaegir_recruit","Vaegir Recruit","Vaegir Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_2,
   [itm.scythe,itm.hatchet,itm.cudgel,itm.axe,itm.stones,itm.tab_shield_kite_a, itm.tab_shield_kite_a,
    itm.linen_tunic, itm.rawhide_coat,itm.nomad_boots],
   def_attrib|level(4),wp(60),knows_common, vaegir_face_younger_1, vaegir_face_middle_2],
  ["vaegir_footman","Vaegir Footman","Vaegir Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac.kingdom_2,
   [itm.spiked_club,itm.hand_axe,itm.sword_viking_1,itm.two_handed_axe,itm.tab_shield_kite_a,itm.tab_shield_kite_b,itm.spear,itm.nomad_cap,itm.vaegir_fur_cap,itm.rawhide_coat,itm.nomad_armor,itm.nomad_boots],
   def_attrib|level(9),wp(75),knows_common, vaegir_face_young_1, vaegir_face_middle_2],
  ["vaegir_skirmisher","Vaegir Skirmisher","Vaegir Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_2,
   [itm.arrows,itm.spiked_mace,itm.axe,itm.sword_khergit_1,itm.short_bow,itm.short_bow,itm.hunting_bow,itm.javelin,itm.javelin,itm.steppe_cap,itm.nomad_cap,itm.leather_vest,itm.leather_vest,itm.nomad_armor,itm.nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(60),knows_ironflesh_1|knows_power_draw_1|knows_power_throw_1,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_archer","Vaegir Archer","Vaegir Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_2,
   [itm.arrows_cav,itm.arrows,itm.axe,itm.sword_khergit_1,itm.nomad_bow,itm.nomad_bow,itm.short_bow,
    itm.leather_jerkin,itm.leather_vest,itm.nomad_boots,itm.vaegir_spiked_helmet,itm.vaegir_fur_helmet,itm.vaegir_fur_cap,itm.nomad_cap],
   str_12 | agi_5 | int_4 | cha_4|level(19),wp_bow(70,110),knows_ironflesh_1|knows_power_draw_3|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_marksman","Vaegir Marksman","Vaegir Marksmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_2,
   [itm.barbed_arrows,itm.axe,itm.voulge,itm.sword_khergit_2,itm.strong_bow,itm.war_bow,itm.strong_bow,
    itm.leather_vest,itm.studded_leather_coat,itm.leather_boots,itm.vaegir_lamellar_helmet,itm.vaegir_spiked_helmet,itm.vaegir_fur_helmet],
   str_14 | agi_5 | int_4 | cha_4|level(24),wp_bow(80,140),knows_ironflesh_2|knows_power_draw_5|knows_athletics_3|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_veteran","Vaegir Veteran","Vaegir Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac.kingdom_2,
   [itm.spiked_mace,itm.two_handed_axe,itm.sword_viking_1,itm.tab_shield_kite_b,itm.tab_shield_kite_c,itm.spear,
    itm.steppe_cap,itm.vaegir_spiked_helmet,itm.vaegir_fur_helmet,itm.vaegir_fur_cap,itm.leather_jerkin,itm.studded_leather_coat,itm.nomad_boots],
   def_attrib|level(14),wp_melee(85),knows_athletics_2|knows_ironflesh_1|knows_power_strike_2|knows_shield_2,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_infantry","Vaegir Infantry","Vaegir Infantry",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_2,
   [itm.pike,itm.battle_axe,itm.sword_viking_2,itm.sword_khergit_2,itm.tab_shield_kite_c,itm.spear,
    itm.lamellar_vest,itm.leather_boots,itm.vaegir_lamellar_helmet,itm.vaegir_spiked_helmet,itm.vaegir_fur_helmet],
   def_attrib|level(19),wp_melee(100),knows_athletics_3|knows_ironflesh_2|knows_power_strike_3|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_guard","Vaegir Guard","Vaegir Guards",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_2,
   [itm.ashwood_pike,itm.fighting_axe,itm.bardiche,itm.battle_axe,itm.fighting_axe,itm.tab_shield_kite_d,
    itm.lamellar_vest,itm.lamellar_armor,itm.splinted_leather_greaves,itm.iron_greaves,itm.vaegir_war_helmet,itm.vaegir_war_helmet,itm.vaegir_guard_helmet,itm.leather_gloves],
   def_attrib|level(24),wp_melee(130),knows_riding_2|knows_athletics_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_4,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_horseman","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac.kingdom_2,
   [itm.battle_axe,itm.sword_khergit_2,itm.lance,itm.tab_shield_kite_cav_a,itm.spear,
    itm.studded_leather_coat,itm.lamellar_vest,itm.leather_boots,itm.vaegir_lamellar_helmet,itm.vaegir_spiked_helmet,itm.vaegir_fur_helmet,itm.steppe_horse,itm.hunter],
   def_attrib|level(21),wp(100),knows_riding_3|knows_ironflesh_3|knows_power_strike_3,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_knight","Vaegir Knight","Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac.kingdom_2,
   [itm.bardiche,itm.great_bardiche,itm.war_axe,itm.fighting_axe,itm.lance,itm.lance,itm.tab_shield_kite_cav_b,
    itm.lamellar_vest,itm.lamellar_armor,itm.mail_boots,itm.plate_boots,itm.vaegir_war_helmet,itm.vaegir_war_helmet,itm.vaegir_guard_helmet,itm.hunter, itm.warhorse_steppe,itm.leather_gloves],
   def_attrib|level(26),wp_2h(140,120,120),knows_riding_4|knows_shield_2|knows_ironflesh_4|knows_power_strike_4,vaegir_face_middle_1, vaegir_face_older_2],

  ["vaegir_raider","Vaegir Raider","Vaegir Raiders",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac.kingdom_2,
   [itm.spiked_mace,itm.two_handed_axe,itm.sword_viking_1,itm.tab_shield_kite_b,itm.tab_shield_kite_c,itm.spear,
    itm.steppe_cap,itm.vaegir_spiked_helmet,itm.vaegir_fur_helmet,itm.vaegir_fur_cap,itm.leather_jerkin,itm.studded_leather_coat,itm.nomad_boots,itm.saddle_horse],
   def_attrib|level(15),wp_melee(85),knows_riding_3|knows_athletics_2|knows_ironflesh_1|knows_power_strike_2|knows_shield_2,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_cossack","Vaegir Cossack","Vaegir Cossacks",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac.kingdom_2,
   [itm.arrows_cav,itm.axe,itm.sword_khergit_1,itm.nomad_bow,itm.nomad_bow,
    itm.leather_jerkin,itm.leather_vest,itm.nomad_boots,itm.vaegir_spiked_helmet,itm.vaegir_fur_helmet,itm.vaegir_fur_cap,itm.nomad_cap,itm.saddle_horse],
   str_12 | agi_5 | int_4 | cha_4|level(20),wp_bow(70,110),knows_riding_4|knows_horse_archery_2|knows_ironflesh_1|knows_power_draw_3|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_strelets","Vaegir Strelets","Vaegir Strelcy",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_2,
   [itm.cartridges,itm.arquebus,itm.bardiche,itm.bardiche,itm.sword_khergit_1,itm.fur_hat,itm.fur_hat,itm.fur_coat,itm.nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(15),wp_gun(60,50),knows_ironflesh_1|knows_power_draw_1|knows_power_throw_1,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_elite_guard","Vaegir Principal Guard","Vaegir Principal Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac.kingdom_2,
   [itm.ashwood_pike,itm.great_bardiche,itm.bardiche,itm.battle_axe,itm.great_axe,
    itm.vaegir_elite_armor,itm.iron_greaves,itm.vaegir_war_helmet,itm.vaegir_war_helmet,itm.vaegir_guard_helmet,itm.scale_gauntlets,itm.lamellar_gauntlets],
   def_attrib|level(25),wp_2h(150,130,130),knows_riding_2|knows_athletics_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_4,vaegir_face_middle_1, vaegir_face_older_2],
  ["strange_marksman","Strange Marksman","Strange Marksmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac.kingdom_2,
   [itm.bodkin_arrows,itm.strange_short_sword,itm.strange_sword,itm.war_bow,
    itm.strange_armor,itm.strange_boots,itm.nomad_boots,itm.strange_helmet,itm.leather_gloves],
   str_14 | agi_5 | int_4 | cha_4|level(25),wp_bow(90,140),knows_ironflesh_2|knows_power_draw_5|knows_athletics_3|knows_power_strike_1,vaegir_face_young_1, vaegir_face_older_2],
  ["strange_swordsman","Strange Swordsman","Strange Swordsmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac.kingdom_2,
   [itm.ashwood_pike,itm.strange_great_sword,itm.strange_sword,itm.strange_short_sword,
    itm.strange_armor,itm.strange_boots,itm.strange_helmet,itm.leather_gloves,itm.scale_gauntlets],
   def_attrib|level(20),wp_melee(100),knows_athletics_3|knows_ironflesh_2|knows_power_strike_3|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["strange_knight","Strange Knight","Strange Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac.kingdom_2,
   [itm.strange_great_sword,itm.strange_great_sword,itm.strange_sword,itm.strange_short_sword,itm.war_spear,
    itm.strange_armor,itm.strange_boots,itm.strange_helmet,itm.leather_gloves,itm.scale_gauntlets,itm.hunter,itm.warhorse_steppe],
   def_attrib|level(26),wp_2h(140,120,120),knows_riding_4|knows_shield_2|knows_ironflesh_4|knows_power_strike_4,vaegir_face_young_1, vaegir_face_older_2],
   
  ["vaegir_messenger","Vaegir Messenger","Vaegir Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac.kingdom_2,
   [itm.sword_medieval_b,itm.leather_jerkin,itm.leather_boots,itm.courser,itm.leather_gloves,itm.short_bow,itm.arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_2,
   [itm.ashwood_pike,itm.battle_fork,itm.bardiche,itm.battle_axe,itm.fighting_axe,itm.tab_shield_kite_b,itm.studded_leather_coat,itm.lamellar_armor,itm.mail_chausses,itm.iron_greaves,itm.nordic_helmet,itm.nordic_helmet,itm.nordic_helmet,itm.spiked_helmet,itm.leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_2,
   [itm.ashwood_pike,itm.battle_fork,itm.bardiche,itm.battle_axe,itm.fighting_axe,itm.tab_shield_kite_d,itm.studded_leather_coat,itm.lamellar_armor,itm.mail_chausses,itm.iron_greaves,itm.nordic_helmet,itm.nordic_helmet,itm.nordic_helmet,itm.spiked_helmet,itm.leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],

# Khergit Khanate
#################
  ["khergit_tribesman","Khergit Tribesman","Khergit Tribesmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_3,
   [itm.arrows,itm.arrows_cav,itm.club,itm.spear,itm.hunting_bow,
    itm.steppe_cap,itm.nomad_cap_b,itm.leather_vest,itm.steppe_armor,itm.nomad_boots,itm.khergit_leather_boots],
   def_attrib|level(5),wp(50),knows_common|knows_riding_3|knows_power_draw_2|knows_horse_archery_2,khergit_face_younger_1, khergit_face_old_2],
  ["khergit_skirmisher","Khergit Skirmisher","Khergit Skirmishers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac.kingdom_3,
   [itm.arrows_cav,itm.sword_khergit_1,itm.mace_4,itm.spear,itm.nomad_bow,itm.javelin,itm.tab_shield_small_round_a,
    itm.steppe_cap,itm.nomad_cap_b,itm.leather_steppe_cap_a,itm.khergit_armor,itm.steppe_armor,itm.leather_vest,itm.nomad_boots,itm.khergit_leather_boots,itm.steppe_horse,itm.saddle_horse],
   def_attrib|level(10),wp_skirmish(60,80),knows_common|knows_riding_4|knows_power_draw_3|knows_power_throw_1|knows_horse_archery_3,khergit_face_younger_1, khergit_face_old_2],
  ["khergit_horseman","Khergit Horseman","Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac.kingdom_3,
  [itm.arrows_cav,itm.light_lance,itm.nomad_bow,itm.sword_khergit_2,itm.tab_shield_small_round_a,itm.tab_shield_small_round_b,itm.spear,itm.javelin,itm.javelin,
   itm.leather_steppe_cap_a, itm.leather_steppe_cap_b,itm.nomad_robe,itm.nomad_vest,itm.khergit_leather_boots,itm.hide_boots,itm.spiked_helmet,itm.nomad_cap,itm.steppe_horse,itm.hunter],
   def_attrib|level(14),wp(80),knows_common|knows_riding_5|knows_power_draw_4|knows_ironflesh_2|knows_power_throw_2|knows_horse_archery_3|knows_shield_1,khergit_face_young_1, khergit_face_older_2],
  ["khergit_horse_archer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac.kingdom_3,
   [itm.arrows_cav,itm.sword_khergit_2,itm.mace_4,itm.spear,itm.khergit_bow,itm.tab_shield_small_round_a,itm.tab_shield_small_round_a,itm.tab_shield_small_round_b,itm.bodkin_arrows,itm.arrows,
    itm.leather_steppe_cap_b,itm.nomad_cap_b,itm.tribal_warrior_outfit,itm.nomad_robe,itm.khergit_leather_boots,itm.tab_shield_small_round_a,itm.tab_shield_small_round_b,itm.steppe_horse],
   def_attrib|level(14),wp_skirmish(80,110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_3,khergit_face_young_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer","Khergit Veteran Horse Archer","Khergit Veteran Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac.kingdom_3,
   [itm.sword_khergit_3,itm.winged_mace,itm.spear,itm.khergit_bow,itm.khergit_bow,itm.khergit_bow
   ,itm.nomad_bow,itm.arrows_cav,itm.khergit_arrows,itm.khergit_arrows,itm.khergit_arrows,itm.tab_shield_small_round_b,itm.tab_shield_small_round_c,
    itm.khergit_cavalry_helmet,itm.khergit_cavalry_helmet,itm.leather_warrior_cap,itm.lamellar_vest_khergit,itm.tribal_warrior_outfit,itm.khergit_leather_boots,itm.leather_gloves,itm.steppe_horse,itm.courser],
   def_attrib|level(21),wp_skirmish(90,130),knows_riding_7|knows_power_draw_5|knows_ironflesh_3|knows_horse_archery_7|knows_power_throw_4|knows_shield_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac.kingdom_3,
   [itm.sword_khergit_4,itm.spiked_mace,itm.one_handed_war_axe_b,itm.hafted_blade_a,itm.hafted_blade_b,itm.heavy_lance,itm.lance,
    itm.khergit_guard_helmet,itm.khergit_cavalry_helmet,itm.khergit_war_helmet,itm.lamellar_vest_khergit,itm.lamellar_armor,itm.khergit_leather_boots,itm.splinted_leather_greaves,itm.leather_gloves,itm.scale_gauntlets,itm.tab_shield_small_round_b,itm.tab_shield_small_round_c,itm.courser,itm.warhorse_steppe,itm.warhorse_steppe,itm.warhorse_steppe],
   def_attrib|level(23),wp_pole(150,110,110),knows_riding_7|knows_power_strike_4|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_4|knows_horse_archery_1|knows_shield_2,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_guard","Khergit Guard","Khergit Guards",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac.kingdom_3,
   [itm.sword_khergit_4,itm.spiked_mace,itm.one_handed_war_axe_b,itm.hafted_blade_a,itm.hafted_blade_b,itm.hafted_blade_a,itm.hafted_blade_b,itm.heavy_lance,itm.lance,itm.throwing_spears,itm.throwing_spears,
    itm.khergit_guard_helmet,itm.khergit_cavalry_helmet,itm.khergit_war_helmet,itm.khergit_guard_armor,itm.khergit_leather_boots,itm.khergit_guard_boots,itm.leather_gloves,itm.lamellar_gauntlets,itm.tab_shield_small_round_b,itm.tab_shield_small_round_c,itm.warhorse_steppe],
   def_attrib|level(26),wp(135),knows_riding_8|knows_power_strike_4|knows_power_draw_4|knows_power_throw_4|knows_ironflesh_4|knows_horse_archery_4|knows_shield_2,khergit_face_middle_1, khergit_face_older_2],

  ["khergit_elite_guard","Khergit Keshig","Khergit Keshig",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac.kingdom_3,
   [itm.sword_khergit_4,itm.khergit_sword_two_handed_a,itm.khergit_sword_two_handed_b,itm.hafted_blade_a,itm.hafted_blade_b,itm.hafted_blade_a,itm.hafted_blade_b,itm.heavy_lance,itm.lance,itm.throwing_spears,itm.throwing_spears,
    itm.khergit_guard_helmet,itm.khergit_cavalry_helmet,itm.khergit_elite_armor,itm.khergit_guard_boots,itm.lamellar_gauntlets,itm.tab_shield_small_round_b,itm.tab_shield_small_round_c,itm.warhorse_steppe],
   def_attrib|level(26),wp(135),knows_riding_8|knows_power_strike_4|knows_power_draw_4|knows_power_throw_4|knows_ironflesh_4|knows_horse_archery_4|knows_shield_2,khergit_face_middle_1, khergit_face_older_2],
  ["strange_horse_archer","Strange Horse Archer","Strange Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac.kingdom_3,
   [itm.strange_sword,itm.strange_short_sword,itm.khergit_bow,itm.khergit_arrows,
    itm.strange_helmet,itm.strange_armor,itm.strange_boots,itm.leather_gloves,itm.courser],
   def_attrib|level(22),wp_skirmish(100,130),knows_riding_7|knows_power_draw_5|knows_ironflesh_3|knows_horse_archery_7|knows_power_throw_4|knows_shield_1,khergit_face_middle_1, khergit_face_older_2],
  ["strange_lancer","Strange Lancer","Strange Lancers",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac.kingdom_3,
   [itm.strange_sword,itm.strange_short_sword,itm.hafted_blade_a,itm.hafted_blade_b,itm.heavy_lance,itm.lance,itm.lance,itm.war_darts,
    itm.strange_helmet,itm.strange_armor,itm.strange_boots,itm.leather_gloves,itm.scale_gauntlets,itm.courser],
   def_attrib|level(23),wp_pole(150,110,110),knows_riding_7|knows_power_strike_4|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_4|knows_horse_archery_1|knows_shield_2,khergit_face_middle_1, khergit_face_older_2],
   
  ["khergit_messenger","Khergit Messenger","Khergit Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac.kingdom_3,
   [itm.sword_khergit_2,itm.leather_jerkin,itm.leather_boots,itm.courser,itm.leather_gloves,itm.short_bow,itm.arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(125),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,khergit_face_young_1, khergit_face_older_2],
  ["khergit_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_3,
   [itm.sword_khergit_3,itm.tab_shield_small_round_b,itm.tab_shield_small_round_a,itm.lamellar_vest_khergit,itm.lamellar_armor,itm.khergit_leather_boots,itm.iron_greaves,itm.khergit_guard_helmet,itm.khergit_cavalry_helmet,itm.leather_warrior_cap],
   def_attrib|level(24),wp(130),knows_athletics_5|knows_shield_2|knows_ironflesh_5,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_3,
   [itm.sword_khergit_4,itm.tab_shield_small_round_b,itm.tab_shield_small_round_a,itm.lamellar_vest_khergit,itm.lamellar_armor,itm.khergit_leather_boots,itm.iron_greaves,itm.khergit_guard_helmet,itm.khergit_cavalry_helmet,itm.leather_warrior_cap],
   def_attrib|level(24),wp(130),knows_athletics_5|knows_shield_2|knows_ironflesh_5,khergit_face_middle_1, khergit_face_older_2],

# Kingdom of Nords
##################
  ["nord_recruit","Nord Recruit","Nord Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_4,
   [itm.axe,itm.hatchet,itm.spear,itm.tab_shield_round_a,itm.tab_shield_round_a,
    itm.blue_tunic,itm.coarse_tunic,itm.hide_boots,itm.nomad_boots],
   def_attrib|level(6),wp(50),knows_power_strike_1|knows_power_throw_1|knows_riding_1|knows_athletics_1,nord_face_younger_1, nord_face_old_2],
  ["nord_footman","Nord Footman","Nord Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac.kingdom_4,
   [itm.fighting_axe,itm.one_handed_war_axe_a,itm.spear,itm.tab_shield_round_a,itm.tab_shield_round_b,itm.javelin,itm.throwing_axes,
    itm.leather_cap,itm.skullcap,itm.nomad_vest,itm.leather_boots,itm.nomad_boots],
   def_attrib|level(10),wp(70),knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_riding_2|knows_athletics_2|knows_shield_1,nord_face_young_1, nord_face_old_2],
  ["nord_trained_footman","Nord Trained Footman","Nord Trained Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac.kingdom_4,
   [itm.one_handed_war_axe_a,itm.one_handed_war_axe_b,itm.one_handed_battle_axe_a,itm.tab_shield_round_b,
    itm.skullcap,itm.nasal_helmet,itm.nordic_footman_helmet,itm.byrnie,itm.studded_leather_coat,itm.leather_boots],
   def_attrib|level(14),wp(100),knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_riding_2|knows_athletics_3|knows_shield_2,nord_face_young_1, nord_face_old_2],
  ["nord_warrior","Nord Warrior","Nord Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac.kingdom_4,
   [itm.sword_viking_1,itm.one_handed_war_axe_b,itm.one_handed_battle_axe_a,itm.tab_shield_round_c,itm.javelin,
    itm.nordic_footman_helmet,itm.nordic_fighter_helmet,itm.mail_shirt,itm.studded_leather_coat,itm.hunter_boots,itm.leather_boots],
   def_attrib|level(19),wp(115),knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_riding_2|knows_athletics_4|knows_shield_3,nord_face_young_1, nord_face_older_2],
  ["nord_veteran","Nord Veteran","Nord Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac.kingdom_4,
   [itm.sword_viking_2,itm.sword_viking_2_small,itm.one_handed_battle_axe_b,itm.mace_3,itm.tab_shield_round_d,itm.javelin,itm.throwing_axes,
    itm.nordic_helmet,itm.nordic_fighter_helmet,itm.mail_hauberk,itm.mail_shirt,itm.splinted_leather_greaves,itm.leather_boots,itm.leather_gloves],
   def_attrib|level(24),wp(145),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_riding_3|knows_athletics_5|knows_shield_4,nord_face_young_1, nord_face_older_2],
  ["nord_champion","Nord Huscarl","Nord Huscarls",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac.kingdom_4,
   [itm.sword_viking_3,itm.sword_viking_3_small,itm.great_axe_2,itm.one_handed_battle_axe_c,itm.tab_shield_round_e,itm.throwing_spears,itm.heavy_throwing_axes,itm.heavy_throwing_axes,
    itm.nordic_huscarl_helmet,itm.nordic_warlord_helmet,itm.banded_armor,itm.mail_boots,itm.mail_chausses,itm.mail_mittens],
   def_attrib|level(28),wp(170),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_riding_2|knows_athletics_7|knows_shield_6,nord_face_middle_1, nord_face_older_2],
  ["nord_huntsman","Nord Huntsman","Nord Huntsmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_4,
   [itm.arrows,itm.rawhide_coat,itm.hatchet,itm.hunting_bow,itm.hide_boots],
   str_10 | agi_5 | int_4 | cha_4|level(11),wp_bow(60,70),knows_ironflesh_1|knows_power_draw_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],
  ["nord_archer","Nord Archer","Nord Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_4,
   [itm.arrows,itm.axe,itm.short_bow,itm.padded_leather,itm.leather_jerkin,itm.padded_leather,itm.leather_boots,itm.nasal_helmet,itm.nordic_archer_helmet,itm.leather_cap],
   str_11 | agi_5 | int_4 | cha_4|level(15),wp_bow(80,95),knows_ironflesh_2|knows_power_draw_3|knows_athletics_5,nord_face_young_1, nord_face_old_2],
  ["nord_veteran_archer","Nord Longbowman","Nord Longbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_4,
   [itm.bodkin_arrows,itm.sword_viking_2,itm.fighting_axe,itm.two_handed_axe,itm.long_bow,itm.mail_shirt,itm.mail_shirt,itm.byrnie,itm.leather_boots,itm.nordic_archer_helmet,itm.nordic_veteran_archer_helmet],
   str_12 | agi_5 | int_4 | cha_4|level(19),wp_bow(95,120),knows_power_strike_3|knows_ironflesh_4|knows_power_draw_5|knows_athletics_7,nord_face_middle_1, nord_face_older_2],

  ["nord_handgunner","Nord Handgunner","Nord Handgunners",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_4,
   [itm.cartridges,itm.nomad_vest,itm.padded_leather,itm.sword_viking_2_small,itm.wooden_round_shield,itm.arquebus,itm.hide_boots,itm.nordic_footman_helmet],
   str_11 | agi_5 | int_4 | cha_4|level(15),wp_gun(95,80),knows_power_strike_1|knows_ironflesh_2|knows_power_draw_1|knows_athletics_5,nord_face_young_1, nord_face_old_2],
  ["nord_shocktrooper","Nord Shocktrooper","Nord Shocktroopers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac.kingdom_4,
   [itm.cartridges,itm.arquebus,itm.fighting_axe,itm.one_handed_war_axe_b,itm.one_handed_battle_axe_a,itm.plate_covered_round_shield,
    itm.nordic_helmet,itm.nordic_fighter_helmet,itm.mail_shirt,itm.studded_leather_coat,itm.splinted_leather_greaves,itm.leather_boots,itm.leather_gloves],
   str_12 | agi_5 | int_4 | cha_4|level(20),wp_gun(115,100),knows_ironflesh_4|knows_power_strike_5|knows_athletics_7|knows_shield_3,nord_face_young_1, nord_face_older_2],
  ["nord_mounted_archer","Nord Mounted Archer","Nord Mounted Archers",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac.kingdom_4,
   [itm.bodkin_arrows,itm.sword_viking_2,itm.fighting_axe,itm.two_handed_axe,itm.long_bow,itm.mail_shirt,itm.mail_shirt,itm.studded_leather_coat,itm.leather_boots,itm.nordic_archer_helmet,itm.nordic_veteran_archer_helmet,itm.nord_pony],
   str_12 | agi_5 | int_4 | cha_4|level(20),wp_bow(95,120),knows_riding_2|knows_power_strike_3|knows_ironflesh_4|knows_power_draw_5|knows_athletics_7,nord_face_middle_1, nord_face_older_2],
  ["nord_cavalry","Nord Cavalry","Nord Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac.kingdom_4,
   [itm.sword_viking_2,itm.sword_viking_2_long,itm.two_handed_battle_axe_2,itm.war_spear,itm.tab_shield_round_d,itm.javelin,itm.throwing_axes,
    itm.nordic_helmet,itm.nordic_fighter_helmet,itm.mail_hauberk,itm.banded_armor,itm.splinted_leather_greaves,itm.mail_chausses,itm.leather_gloves,itm.mail_mittens,itm.warhorse],
   def_attrib|level(25),wp(145),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_riding_4|knows_athletics_4|knows_shield_4,nord_face_young_1, nord_face_older_2],
  ["nord_elite","Nord Berserker","Nord Berserkers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac.kingdom_4,
   [itm.long_axe_b,itm.long_axe_c,itm.nordic_huscarl_helmet,itm.nordic_warlord_helmet,itm.cuir_bouilli,itm.mail_boots,itm.mail_mittens],
   def_attrib|level(28),wp(170),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_riding_2|knows_athletics_7|knows_shield_6,nord_face_middle_1, nord_face_older_2],

  ["nord_messenger","Nord Messenger","Nord Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac.kingdom_4,
   [itm.sword_viking_2,itm.leather_jerkin,itm.leather_boots,itm.courser,itm.leather_gloves,itm.short_bow,itm.arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,nord_face_young_1, nord_face_older_2],
  ["nord_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_4,
   [itm.ashwood_pike,itm.battle_fork,itm.battle_axe,itm.fighting_axe,itm.tab_shield_round_d,itm.mail_hauberk,itm.mail_chausses,itm.iron_greaves,itm.nordic_helmet,itm.nordic_helmet,itm.nordic_helmet,itm.spiked_helmet,itm.leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2],
  ["nord_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_4,
   [itm.ashwood_pike,itm.battle_fork,itm.battle_axe,itm.fighting_axe,itm.tab_shield_round_d,itm.tab_shield_round_e,itm.mail_hauberk,itm.heraldic_mail_with_tabard,itm.mail_chausses,itm.iron_greaves,itm.nordic_helmet,itm.nordic_helmet,itm.nordic_helmet,itm.spiked_helmet,itm.leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2],

# Kingdom of Rhodoks
####################
  ["rhodok_recruit","Rhodok Recruit","Rhodok Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_5,
   [itm.pitch_fork,itm.tab_shield_pavise_a,
    itm.shirt,itm.coarse_tunic,itm.wrapping_boots,itm.nomad_boots,itm.head_wrappings,itm.straw_hat],
   def_attrib|level(4),wp(55),knows_common|knows_power_draw_2|knows_ironflesh_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_spearman","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_5,
   [itm.spear,itm.pike,itm.spear,itm.tab_shield_pavise_a,itm.falchion,
    itm.felt_hat_b,itm.common_hood,itm.leather_armor,itm.arena_tunic_green,itm.wrapping_boots,itm.nomad_boots],
   def_attrib|level(9),wp(80),knows_common|knows_ironflesh_2|knows_shield_1|knows_power_strike_2|knows_athletics_1,rhodok_face_young_1, rhodok_face_old_2],
  ["rhodok_trained_spearman","Rhodok Trained Spearman","Rhodok Trained Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac.kingdom_5,
   [itm.pike,itm.war_spear,itm.tab_shield_pavise_b,
    itm.footman_helmet,itm.padded_coif,itm.aketon_green,itm.aketon_green,itm.ragged_outfit,itm.nomad_boots,itm.leather_boots],
   def_attrib|level(14),wp_pole(115,105,105),knows_common|knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_athletics_2,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman","Rhodok Veteran Spearman","Rhodok Veteran Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac.kingdom_5,
   [itm.ashwood_pike,itm.glaive,itm.tab_shield_pavise_c,
    itm.kettle_hat,itm.mail_coif,itm.mail_with_tunic_green,itm.leather_boots,itm.splinted_leather_greaves,itm.leather_gloves],
   def_attrib|level(19),wp_pole(130,115,115),knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_sergeant","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac.kingdom_5,
   [itm.glaive,itm.military_hammer,itm.military_cleaver_c,itm.tab_shield_pavise_d,
    itm.full_helm, itm.bascinet_3,itm.bascinet_2,itm.surcoat_over_mail,itm.surcoat_over_mail,itm.heraldic_mail_with_surcoat,itm.mail_chausses,itm.leather_gloves,itm.mail_mittens],
   def_attrib|level(25),wpm(130,115,155,115),knows_common|knows_ironflesh_6|knows_shield_5|knows_power_strike_5|knows_athletics_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_crossbowman","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac.kingdom_5,
   [itm.sword_medieval_a,itm.falchion,itm.club_with_spike_head,itm.tab_shield_pavise_a,itm.crossbow,itm.bolts,
    itm.arena_tunic_green,itm.felt_hat_b,itm.common_hood,itm.nomad_boots,itm.wrapping_boots],
   def_attrib|level(10),wp(85),knows_common|knows_ironflesh_2|knows_shield_1|knows_power_strike_1|knows_athletics_2,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_trained_crossbowman","Rhodok Trained Crossbowman","Rhodok Trained Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac.kingdom_5,
   [itm.sword_medieval_a,itm.sword_medieval_b_small,itm.club_with_spike_head,itm.tab_shield_pavise_a,itm.crossbow,itm.bolts,
    itm.common_hood,itm.leather_armor,itm.arena_tunic_green,itm.nomad_boots],
   def_attrib|level(15),wp_xbow(90,105),knows_common|knows_ironflesh_1|knows_shield_2|knows_power_strike_2|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_crossbowman","Rhodok Veteran Crossbowman","Rhodok Veteran Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac.kingdom_5,
   [itm.sword_medieval_a,itm.sword_medieval_b_small,itm.fighting_pick,itm.club_with_spike_head,itm.tab_shield_pavise_b,itm.tab_shield_pavise_c,itm.heavy_crossbow,itm.bolts,
    itm.leather_cap,itm.felt_hat_b,itm.aketon_green,itm.leather_boots],
   def_attrib|level(20),wp_xbow(100,120),knows_common|knows_ironflesh_2|knows_shield_3|knows_power_strike_3|knows_athletics_4,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sharpshooter","Rhodok Sharpshooter","Rhodok Sharpshooters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac.kingdom_5,
   [itm.sword_medieval_b,itm.military_pick,itm.military_hammer,itm.tab_shield_pavise_c,itm.sniper_crossbow,itm.steel_bolts,
    itm.kettle_hat,itm.mail_coif,itm.mail_with_tunic_green,itm.leather_boots,itm.splinted_leather_greaves],
   str_14 | agi_5 | int_4 | cha_4|level(25),wp_xbow(110,140),knows_common|knows_ironflesh_3|knows_shield_4|knows_power_strike_4|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],

  ["rhodok_chasseur","Rhodok Chasseur","Rhodok Chasseurs",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_gloves,0,0,fac.kingdom_5,
   [itm.falchion,itm.arquebus,itm.cartridges,itm.common_hood,itm.leather_armor,itm.nomad_boots],
   def_attrib|level(15),wp_gun(90,100),knows_common|knows_ironflesh_1|knows_shield_1|knows_power_strike_2|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_lancer","Rhodok Lancer","Rhodok Lancers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse,0,0,fac.kingdom_5,
   [itm.lance,itm.lance,itm.lance,itm.fighting_axe,itm.fighting_pick,itm.military_hammer,itm.wooden_shield,
    itm.kettle_hat,itm.mail_coif,itm.mail_with_tunic_green,itm.leather_boots,itm.splinted_leather_greaves,itm.leather_gloves,itm.courser],
   def_attrib|level(20),wp_pole(130,115,115),knows_common|knows_riding_3|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_2,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_mounted_crossbowman","Rhodok Mounted Crossbowman","Rhodok Mounted Crossbowmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_horse,0,0,fac.kingdom_5,
   [itm.sword_medieval_a,itm.sword_medieval_b,itm.fighting_pick,itm.club_with_spike_head,itm.tab_shield_pavise_b,itm.tab_shield_pavise_c,itm.heavy_crossbow,itm.bolts,
    itm.leather_cap,itm.felt_hat_b,itm.leather_jerkin,itm.leather_boots,itm.courser],
   def_attrib|level(20),wp_xbow(100,120),knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_3|knows_athletics_4,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_elite_guard","Rhodok Honor Guard","Rhodok Honor Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac.kingdom_5,
   [itm.glaive,itm.bec_de_corbin_a,itm.two_handed_cleaver,itm.full_helm,itm.plate_armor,itm.plate_boots,itm.gauntlets],
   def_attrib|level(25),wpm(130,115,155,115),knows_common|knows_ironflesh_6|knows_shield_5|knows_power_strike_5|knows_athletics_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_heavy_crossbowman","Rhodok Heavy Crossbowman","Rhodok Heavy Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac.kingdom_5,
   [itm.military_cleaver_c,itm.military_pick,itm.military_hammer,itm.tab_shield_pavise_d,itm.sniper_crossbow,itm.steel_bolts,
    itm.kettle_hat,itm.bascinet_2,itm.coat_of_plates,itm.mail_chausses,itm.splinted_leather_greaves,itm.leather_gloves],
   str_15 | agi_5 | int_4 | cha_4|level(25),wp_xbow(110,140),knows_common|knows_ironflesh_3|knows_shield_5|knows_power_strike_4|knows_athletics_7,rhodok_face_middle_1, rhodok_face_older_2],

  ["rhodok_messenger","Rhodok Messenger","Rhodok Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac.kingdom_5,
   [itm.sword_medieval_b,itm.leather_jerkin,itm.leather_boots,itm.courser,itm.leather_gloves,itm.light_crossbow,itm.bolts],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_5,
   [itm.ashwood_pike,itm.battle_fork,itm.battle_axe,itm.fighting_axe,itm.tab_shield_pavise_b,itm.bascinet_2,itm.surcoat_over_mail,itm.mail_chausses,itm.iron_greaves,itm.leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_5,
   [itm.ashwood_pike,itm.battle_fork,itm.battle_axe,itm.fighting_axe,itm.tab_shield_pavise_c,itm.bascinet_2,itm.surcoat_over_mail,itm.mail_chausses,itm.iron_greaves,itm.leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,rhodok_face_middle_1, rhodok_face_older_2],

# Sarranid Sultanate
####################
 ["sarranid_recruit","Sarranid Recruit","Sarranid Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_6,
   [itm.scythe,itm.hatchet,itm.pickaxe,itm.club,itm.stones,itm.tab_shield_kite_a,itm.sarranid_felt_hat,itm.turban,itm.sarranid_boots_a,
    itm.sarranid_cloth_robe, itm.sarranid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common|knows_athletics_1,sarranid_face_younger_1, sarranid_face_middle_2],
 ["sarranid_footman","Sarranid Footman","Sarranid Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac.kingdom_6,
   [itm.bamboo_spear,itm.arabian_sword_a,itm.tab_shield_kite_a,itm.desert_turban,
    itm.skirmisher_armor,itm.turban,itm.sarranid_boots_a,itm.sarranid_boots_b],
   def_attrib|level(9),wp(75),knows_common|knows_athletics_2,sarranid_face_young_1, sarranid_face_old_2],
 ["sarranid_veteran_footman","Sarranid Veteran Footman","Sarranid Veteran Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac.kingdom_6,
   [itm.bamboo_spear,itm.arabian_sword_a,itm.arabian_sword_b,itm.tab_shield_kite_b,
    itm.sarranid_boots_b,itm.sarranid_warrior_cap,itm.sarranid_leather_armor,itm.jarid,itm.arabian_sword_a,itm.mace_3],
   def_attrib|level(14),wp_sarranid(85,75,100),knows_common|knows_athletics_2|knows_power_throw_2|knows_ironflesh_1|knows_power_strike_2|knows_shield_2,sarranid_face_young_1, sarranid_face_old_2],
 ["sarranid_infantry","Sarranid Infantry","Sarranid Infantry",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_6,
   [itm.sarranid_mail_shirt,itm.sarranid_mail_coif,itm.jarid,itm.sarranid_boots_c,itm.sarranid_boots_b,itm.sarranid_axe_a,itm.arabian_sword_b,itm.mace_3,itm.spear,itm.tab_shield_kite_c],
   def_attrib|level(20),wp_sarranid(105,75,110),knows_common|knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_shield_3 | knows_power_throw_3|knows_athletics_3,sarranid_face_middle_1, sarranid_face_old_2],
 ["sarranid_guard","Sarranid Guard","Sarranid Guards",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_6,
   [itm.military_pick,itm.sarranid_two_handed_axe_a,itm.jarid,itm.scimitar_b,itm.war_spear,itm.mace_4,itm.sarranid_boots_d, itm.sarranid_boots_c,itm.arabian_armor_b,itm.sarranid_mail_coif,itm.sarranid_veiled_helmet,itm.mail_mittens,itm.leather_gloves,itm.tab_shield_kite_d],
   def_attrib|level(25),wp_sarranid(135,75,140),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_4|knows_athletics_5,sarranid_face_middle_1, sarranid_face_older_2],
 ["sarranid_skirmisher","Sarranid Skirmisher","Sarranid Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_6,
   [itm.turban,itm.desert_turban,itm.skirmisher_armor,itm.jarid,itm.jarid,itm.arabian_sword_a,itm.spiked_club,itm.tab_shield_small_round_a,itm.sarranid_warrior_cap,itm.sarranid_boots_a],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_power_throw_2|knows_ironflesh_1|knows_athletics_3,sarranid_face_young_1, sarranid_face_middle_2],
 ["sarranid_archer","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_6,
   [itm.arrows_cav,itm.arrows_cav,itm.nomad_bow,itm.arabian_sword_a,itm.archers_vest,itm.sarranid_boots_b,itm.sarranid_helmet1,itm.sarranid_warrior_cap,itm.turban,itm.desert_turban],
   def_attrib|level(19),wp_skirmish(90,100),knows_common|knows_power_draw_3|knows_ironflesh_2|knows_power_throw_3|knows_athletics_4,sarranid_face_young_1, sarranid_face_old_2],
 ["sarranid_master_archer","Sarranid Master Archer","Sarranid Master Archers",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_6,
   [itm.barbed_arrows,itm.barbed_arrows,itm.arabian_sword_b,itm.mace_3,itm.strong_bow,itm.nomad_bow,
    itm.arabian_armor_b,itm.sarranid_boots_c,itm.sarranid_boots_b,itm.sarranid_mail_coif],
   str_14 | agi_5 | int_4 | cha_4|level(24),wp_skirmish(100,130),knows_common|knows_power_draw_4|knows_power_throw_4|knows_ironflesh_3|knows_athletics_5,sarranid_face_middle_1, sarranid_face_older_2],
 ["sarranid_raider","Sarranid Raider","Sarranid Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac.kingdom_6,
   [itm.arrows_cav,itm.turban,itm.desert_turban,itm.skirmisher_armor,itm.jarid,itm.jarid,itm.nomad_bow,itm.short_bow,itm.arabian_sword_a,itm.spear,itm.light_lance,itm.tab_shield_small_round_a,itm.sarranid_warrior_cap,itm.sarranid_boots_a,itm.arabian_horse_a],
   def_attrib|level(15),wp(80),knows_common|knows_riding_3|knows_horse_archery_2|knows_power_draw_2|knows_power_throw_2,sarranid_face_young_1, sarranid_face_middle_2],
 ["sarranid_horseman","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac.kingdom_6,
   [itm.lance,itm.arabian_sword_b,itm.scimitar_b,itm.mace_4,itm.tab_shield_small_round_b,
    itm.sarranid_mail_shirt,itm.sarranid_boots_c,itm.sarranid_boots_b, itm.sarranid_horseman_helmet,itm.leather_gloves,itm.arabian_horse_a,itm.courser,itm.hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,sarranid_face_young_1, sarranid_face_old_2],
 ["sarranid_mamluke","Sarranid Mamluke","Sarranid Mamlukes",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac.kingdom_6,
   [itm.heavy_lance,itm.scimitar_b,itm.sarranid_two_handed_mace_1,itm.sarranid_cavalry_sword,itm.tab_shield_small_round_c,
    itm.mamluke_mail,itm.sarranid_boots_d,itm.sarranid_boots_c,itm.sarranid_veiled_helmet,itm.arabian_horse_b,itm.warhorse_sarranid,itm.scale_gauntlets,itm.mail_mittens],
   def_attrib|level(27),wpex(150,130,130,75,75,110,75),knows_common|knows_riding_6|knows_shield_5|knows_ironflesh_5|knows_power_strike_5,sarranid_face_middle_1, sarranid_face_older_2],
   
 ["sarranid_handgunner","Sarranid Handgunner","Sarranid Handgunners",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_6,
   [itm.cartridges,itm.arquebus,itm.arabian_sword_a,itm.tab_shield_small_round_a,itm.archers_vest,itm.sarranid_boots_b,itm.sarranid_warrior_cap,itm.turban,itm.desert_turban],
   def_attrib|level(19),wp_gun(90,80),knows_common|knows_power_draw_3|knows_ironflesh_2|knows_power_throw_3|knows_athletics_4,sarranid_face_young_1, sarranid_face_old_2],
 ["sarranid_janissary","Sarranid Janissary","Sarranid Janissary",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_6,
   [itm.cartridges,itm.scimitar,itm.scimitar_b,itm.arquebus,itm.tab_shield_small_round_b,itm.arabian_armor_b,itm.sarranid_boots_b,itm.sarranid_boots_d,itm.sarranid_helmet1],
   str_14 | agi_5 | int_4 | cha_4|level(24),wp_gun(100,100),knows_common|knows_power_strike_2|knows_power_draw_3|knows_power_throw_3|knows_ironflesh_4|knows_athletics_5,sarranid_face_middle_1, sarranid_face_older_2],
 ["sarranid_elite_guard","Sarranid Immortal","Sarranid Immortals",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac.kingdom_6,
   [itm.military_pick,itm.sarranid_two_handed_axe_a,itm.jarid,itm.jarid,itm.light_throwing_axes,itm.scimitar_b,itm.arabian_sword_d,itm.mace_bronze,itm.sarranid_axe_a,itm.sarranid_axe_b,itm.sarranid_boots_d, itm.sarranid_boots_c,itm.sarranid_elite_armor,itm.sarranid_mail_coif,itm.sarranid_veiled_helmet,itm.lamellar_gauntlets,itm.steel_shield],
   def_attrib|level(26),wp_sarranid(135,75,140),knows_common|knows_shield_4|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_4|knows_athletics_7,sarranid_face_middle_1, sarranid_face_older_2],
 ["strange_infantry","Strange Infantry","Strange Infantry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac.kingdom_6,
   [itm.military_sickle_a,itm.military_sickle_a,itm.strange_great_sword,itm.strange_sword,itm.strange_sword,itm.strange_short_sword,itm.war_spear,itm.shortened_military_scythe,itm.military_scythe,itm.double_sided_lance,
    itm.ashwood_pike,itm.long_hafted_spiked_mace,itm.hafted_blade_a,itm.hafted_blade_b,itm.military_fork,itm.battle_fork,itm.war_darts,itm.war_darts,itm.throwing_daggers,itm.light_throwing_axes,itm.jarid,itm.jarid,
	itm.strange_armor,itm.strange_boots,itm.strange_helmet,itm.scale_gauntlets,itm.leather_gloves],
   def_attrib|level(20),wp_sarranid(105,75,110),knows_common|knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_shield_3|knows_power_throw_3|knows_athletics_3,sarranid_face_middle_1, sarranid_face_old_2],
 ["strange_horseman","Strange Horseman","Strange Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac.kingdom_6,
   [itm.lance,itm.lance,itm.lance,itm.strange_sword,itm.strange_short_sword,itm.darts,itm.darts,
    itm.strange_armor,itm.strange_boots,itm.strange_helmet,itm.leather_gloves,itm.arabian_horse_a,itm.courser],
   def_attrib|level(21),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,sarranid_face_young_1, sarranid_face_old_2],
 ["strange_cavalry","Strange Cavalry","Strange Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac.kingdom_6,
   [itm.heavy_lance,itm.strange_great_sword,itm.strange_sword,itm.strange_short_sword,itm.war_darts,itm.war_darts,
    itm.strange_armor,itm.strange_boots,itm.strange_helmet,itm.hunter,itm.arabian_horse_b,itm.scale_gauntlets,itm.lamellar_gauntlets],
   def_attrib|level(26),wpex(150,130,130,75,75,110,75),knows_common|knows_riding_6|knows_shield_2|knows_ironflesh_5|knows_power_strike_5|knows_horse_archery_2|knows_power_throw_2,sarranid_face_middle_1, sarranid_face_older_2],
   
  ["sarranid_messenger","Sarranid Messenger","Sarranid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac.kingdom_1,
   [itm.lance,itm.arabian_sword_b,itm.scimitar_b,itm.mace_4,itm.tab_shield_small_round_b,
    itm.sarranid_mail_shirt,itm.mail_chausses,itm.sarranid_helmet1,itm.courser,itm.hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,sarranid_face_young_1, sarranid_face_old_2],
  ["sarranid_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_1,
   [itm.arabian_sword_b,itm.scimitar_b,itm.war_spear,itm.mace_4,itm.sarranid_boots_c,itm.arabian_armor_b,itm.sarranid_mail_coif,itm.sarranid_helmet1,itm.sarranid_horseman_helmet,itm.mail_boots,itm.iron_greaves,itm.mail_mittens,itm.leather_gloves,itm.tab_shield_kite_d],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,sarranid_face_middle_1, sarranid_face_older_2],
  ["sarranid_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_1,
   [itm.arabian_sword_b,itm.scimitar_b,itm.war_spear,itm.mace_4,itm.sarranid_boots_c, itm.sarranid_boots_d,itm.arabian_armor_b,itm.sarranid_mail_coif,itm.sarranid_helmet1,itm.sarranid_horseman_helmet,itm.mail_boots,itm.iron_greaves,itm.mail_mittens,itm.leather_gloves,itm.tab_shield_kite_d],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,sarranid_face_middle_1, sarranid_face_older_2],

# Bandits and Outlaws
#####################
  ["looter","Looter","Looters",0,0,0,fac.outlaws,
   [itm.hatchet,itm.club,itm.butchering_knife,itm.falchion,itm.rawhide_coat,itm.stones,itm.nomad_armor,itm.nomad_armor,itm.woolen_cap,itm.woolen_cap,itm.nomad_boots,itm.wrapping_boots],
   def_attrib|level(4),wp(20),knows_common,bandit_face1, bandit_face2],
  ["bandit","Bandit","Bandits",tf_guarantee_armor,0,0,fac.outlaws,
   [itm.arrows,itm.mace_3,itm.sword_viking_1,itm.short_bow,itm.falchion,itm.nordic_shield,itm.rawhide_coat,itm.leather_cap,itm.leather_jerkin,itm.nomad_armor,itm.nomad_boots,itm.wrapping_boots,itm.saddle_horse],
   def_attrib|level(10),wp(60),knows_common|knows_power_draw_1,bandit_face1, bandit_face2],
  ["brigand","Brigand","Brigands",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac.outlaws,
   [itm.arrows,itm.mace_3,itm.sword_viking_1,itm.falchion,itm.wooden_shield,itm.hide_covered_round_shield,itm.long_bow,itm.leather_cap,itm.leather_jerkin,itm.nomad_boots,itm.saddle_horse],
   def_attrib|level(16),wp(90),knows_common|knows_power_draw_3,bandit_face1, bandit_face2],
  ["mountain_bandit","Mountain Bandit","Mountain Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac.outlaws,
   [itm.arrows,itm.sword_viking_1,itm.spear,itm.mace_4,itm.maul,itm.falchion,itm.short_bow,itm.javelin,itm.fur_covered_shield,itm.hide_covered_round_shield,
    itm.felt_hat,itm.head_wrappings,itm.skullcap,itm.ragged_outfit,itm.rawhide_coat,itm.leather_armor,itm.hide_boots,itm.nomad_boots,itm.wooden_shield,itm.nordic_shield],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_2,rhodok_face_young_1, rhodok_face_old_2],
  ["forest_bandit","Forest Bandit","Forest Bandits",tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots,0,0,fac.outlaws,
   [itm.arrows,itm.axe,itm.hatchet,itm.quarter_staff,itm.short_bow,itm.hunting_bow,
    itm.common_hood,itm.black_hood,itm.shirt,itm.padded_leather,itm.leather_jerkin,itm.ragged_outfit,itm.hide_boots,itm.leather_boots],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_3,swadian_face_young_1, swadian_face_old_2],
  ["sea_raider","Sea Raider","Sea Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac.outlaws,
   [itm.arrows,itm.sword_viking_1,itm.sword_viking_2,itm.fighting_axe,itm.battle_axe,itm.spear,itm.nordic_shield,itm.nordic_shield,itm.nordic_shield,itm.wooden_shield,itm.long_bow,itm.javelin,itm.throwing_axes,
    itm.nordic_helmet,itm.nordic_helmet,itm.nasal_helmet,itm.nomad_vest,itm.byrnie,itm.mail_shirt,itm.leather_boots, itm.nomad_boots],
   def_attrib|level(16),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],
  ["steppe_bandit","Steppe Bandit","Steppe Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_mounted,0,0,fac.outlaws,
   [itm.arrows_cav,itm.sword_khergit_1,itm.mace_4,itm.spear, itm.light_lance,itm.nomad_bow,itm.nomad_bow,itm.short_bow,itm.jarid,itm.leather_steppe_cap_a,itm.leather_steppe_cap_b,itm.nomad_cap,itm.nomad_cap_b,itm.khergit_armor,itm.steppe_armor,itm.leather_vest,itm.hide_boots,itm.nomad_boots,itm.leather_covered_round_shield,itm.leather_covered_round_shield,itm.saddle_horse,itm.steppe_horse,itm.steppe_horse],
   def_attrib|level(12),wp(100),knows_riding_4|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],
  ["taiga_bandit","Taiga Bandit","Taiga Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac.outlaws,
   [itm.arrows_cav,itm.sword_khergit_1,itm.mace_4,itm.spear, itm.light_lance,itm.nomad_bow,itm.nomad_bow,itm.short_bow,itm.jarid,itm.javelin,itm.vaegir_fur_cap,itm.leather_steppe_cap_c,itm.nomad_armor,itm.leather_jerkin,itm.hide_boots,itm.nomad_boots,itm.leather_covered_round_shield,itm.leather_covered_round_shield],
   def_attrib|level(15),wp(110),knows_common|knows_power_draw_4|knows_power_throw_3,vaegir_face_young_1, vaegir_face_old_2],
  ["desert_bandit","Desert Bandit","Desert Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac.outlaws,
   [itm.arrows_cav,itm.arabian_sword_a,itm.mace_4,itm.spear, itm.light_lance,itm.jarid,itm.nomad_bow,itm.short_bow,itm.jarid,itm.sarranid_cloth_robe, itm.sarranid_cloth_robe, itm.skirmisher_armor, itm.desert_turban, itm.turban,itm.leather_steppe_cap_b,itm.leather_covered_round_shield,itm.leather_covered_round_shield,itm.saddle_horse,itm.arabian_horse_a],
   def_attrib|level(12),wp(100),knows_riding_4|knows_horse_archery_3|knows_power_draw_3,sarranid_face_young_1, sarranid_face_old_2],
  
  ["black_khergit_horseman","Black Khergit Horseman","Black Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac.outlaws,
   [itm.barbed_arrows,itm.sword_khergit_2b,itm.sword_khergit_2b,itm.sword_khergit_3b,itm.mace_4,itm.spear,itm.lance,itm.khergit_bow,itm.khergit_bow,itm.nomad_bow,itm.nomad_bow,itm.leather_warrior_cap,itm.leather_warrior_cap,itm.khergit_war_helmet,itm.khergit_war_helmet,itm.lamellar_armor,itm.khergit_leather_boots,itm.saddle_horse,itm.steppe_horse],
   def_attrib|level(21),wp(100),knows_riding_3|knows_ironflesh_3|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],
  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac.outlaws,
   [itm.khergit_arrows,itm.sword_khergit_3b,itm.sword_khergit_4b,itm.winged_mace,itm.lance,itm.khergit_bow,itm.khergit_guard_helmet,itm.khergit_guard_boots,itm.khergit_guard_armor,itm.lamellar_gauntlets,itm.warhorse_steppe],
   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,khergit_face_middle_1, khergit_face_old_2],

  ["zombie","Zombie","Zombies",tf_undead|tf_always_fall_dead,0,0,fac.undeads,
   [itm.cleaver,itm.sickle,itm.hatchet,itm.knife,itm.butchering_knife,itm.wooden_stick,itm.mace_1], 
   def_attrib|level(3),wp(60),knows_ironflesh_10,undead_face1,undead_face2],
  ["zombie_spear","Zombie with Spear","Zombies with Spears",tf_undead|tf_always_fall_dead|tf_guarantee_shield,0,0,fac.undeads,
   [itm.spear,itm.shortened_spear,itm.fur_covered_shield], 
   def_attrib|level(8),wp(80),knows_ironflesh_10|knows_power_strike_1|knows_shield_2,undead_face1,undead_face2],
  ["zombie_axe","Zombie with Axe","Zombies with Axes",tf_undead|tf_always_fall_dead,0,0,fac.undeads,
   [itm.axe,itm.hand_axe,itm.hide_covered_round_shield,itm.hide_covered_round_shield], 
   def_attrib|level(8),wp(80),knows_ironflesh_10|knows_power_strike_2|knows_shield_1,undead_face1,undead_face2],

# Manhunters
############
  ["manhunter","Manhunter","Manhunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac.manhunters,
   [itm.mace_3,itm.mace_4,itm.nasal_helmet,itm.padded_cloth,itm.aketon_green,itm.aketon_green,itm.wooden_shield,itm.nomad_boots,itm.wrapping_boots,itm.sumpter_horse],
   def_attrib|level(10),wp(50),knows_common,bandit_face1, bandit_face2],
  ["bounty_hunter","Bounty Hunter","Bounty Hunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac.manhunters,
   [itm.spiked_mace,itm.winged_mace,itm.kettle_hat,itm.mail_shirt,itm.nordic_shield,itm.leather_boots,itm.leather_gloves,itm.hunter],
   def_attrib|level(16),wp(90),knows_common,bandit_face1, bandit_face2],
  ["knight_errant","Knight Errant","Knights Errant",tf_mounted|tf_guarantee_all_wo_ranged ,0,0,fac.manhunters,
   [itm.military_hammer,itm.warhammer,itm.jousting_lance,itm.mail_with_surcoat,itm.great_helmet,itm.guard_helmet,itm.mail_mittens,itm.tab_shield_heater_cav_a,itm.mail_chausses,itm.splinted_leather_greaves,itm.warhorse],
   def_attrib|level(22),wp(120),knows_common|knows_riding_4|knows_power_strike_4,bandit_face1, bandit_face2],
   
# Slavers
#########
  ["slave_keeper","Slave Keeper","Slave Keepers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor ,0,0,fac.slavers,
   [itm.cudgel,itm.club,itm.woolen_cap,itm.rawhide_coat,itm.coarse_tunic,itm.nomad_armor,itm.wooden_round_shield,itm.nomad_boots,itm.wrapping_boots,itm.sumpter_horse],
   def_attrib|level(10),wp(60),knows_common,bandit_face1, bandit_face2],
  ["slave_driver","Slave Driver","Slave Drivers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse ,0,0,fac.slavers,
   [itm.club_with_spike_head,itm.segmented_helmet,itm.tribal_warrior_outfit,itm.leather_covered_round_shield,itm.leather_boots,itm.leather_gloves,itm.khergit_leather_boots,itm.steppe_horse],
   def_attrib|level(14),wp(80),knows_common,bandit_face1, bandit_face2],
  ["slave_hunter","Slave Hunter","Slave Hunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac.slavers,
   [itm.mace_4,itm.maul,itm.spiked_helmet,itm.studded_leather_coat,itm.tab_shield_small_round_a,itm.leather_boots,itm.leather_gloves,itm.courser],
   def_attrib|level(18),wp(90),knows_common,bandit_face1, bandit_face2],
  ["slave_crusher","Slave Crusher","Slave Crushers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac.slavers,
   [itm.sledgehammer,itm.mace_3,itm.mail_hauberk,itm.bascinet_2,itm.bascinet_3,itm.mail_mittens,itm.tab_shield_small_round_b,itm.mail_chausses,itm.splinted_leather_greaves,itm.hunter],
   def_attrib|level(22),wp(110),knows_common|knows_riding_4|knows_power_strike_3,bandit_face1, bandit_face2],
  ["slaver_chief","Slaver Chief","Slaver Chiefs",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac.slavers,
   [itm.military_hammer,itm.warhammer,itm.brigandine_red,itm.steel_shield,itm.scale_gauntlets,itm.mail_mittens,itm.guard_helmet,itm.plate_boots,itm.mail_boots,itm.warhorse],
   def_attrib|level(26),wp(130),knows_common|knows_riding_4|knows_power_strike_5,bandit_face1, bandit_face2],

# Fighting Women
################
  ["follower_woman","Camp Follower","Camp Follower",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.bolts,itm.arrows,itm.hunting_bow,itm.short_bow,itm.hunting_crossbow,itm.light_crossbow,itm.nordic_shield,itm.hide_covered_round_shield,itm.hatchet,itm.hand_axe,itm.voulge,itm.fighting_pick,itm.club,itm.dress,itm.woolen_dress, itm.skullcap, itm.wrapping_boots],
   def_attrib|level(5),wp(70),knows_common,refugee_face1,refugee_face2],
  ["hunter_woman","Huntress","Huntresses",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac.commoners,
   [itm.bolts,itm.arrows,itm.short_bow,itm.short_bow,itm.light_crossbow,itm.crossbow,itm.nordic_shield,itm.hide_covered_round_shield,itm.hatchet,itm.hand_axe,itm.voulge,itm.fighting_pick,itm.club,itm.leather_jerkin,itm.leather_vest,itm.skullcap, itm.wrapping_boots],
   def_attrib|level(10),wp(85),knows_common|knows_power_strike_1,refugee_face1,refugee_face2],
  ["ranger_woman","Ranger","Rangers",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac.commoners,
   [itm.arrows,itm.short_bow,itm.nordic_shield,itm.hide_covered_round_shield,itm.hatchet,itm.voulge,itm.byrnie,itm.skullcap,itm.wrapping_boots],
   def_attrib|level(16),wp(100),knows_common|knows_riding_3|knows_power_draw_2|knows_power_strike_1|knows_athletics_2|knows_ironflesh_1,refugee_face1,refugee_face2],
  ["shield_maiden","Shield Maiden","Shield Maidens",tf_female|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac.commoners,
   [itm.bodkin_arrows_cav,itm.sword_viking_2,itm.sword_khergit_2,itm.tab_shield_round_e,itm.strong_bow,itm.banded_armor,itm.splinted_leather_greaves,itm.nordic_warlord_helmet,itm.nordic_huscarl_helmet,itm.courser,itm.leather_gloves],
   def_attrib|level(22),wp(140),knows_common|knows_power_draw_3|knows_horse_archery_2|knows_riding_5|knows_athletics_3|knows_ironflesh_1|knows_power_strike_1,refugee_face1,refugee_face2],
  ["fighter_woman","Defender","Defenders",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac.commoners,
   [itm.bolts,itm.light_crossbow,itm.crossbow,itm.nordic_shield,itm.wooden_shield,itm.sword_medieval_a,itm.shortened_spear,itm.mail_shirt,itm.skullcap,itm.hide_boots],
   def_attrib|level(16),wp(100),knows_common|knows_riding_3|knows_power_strike_2|knows_athletics_2|knows_ironflesh_1,refugee_face1,refugee_face2],
  ["chukonu_woman","Sentinel","Sentinels",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac.commoners,
   [itm.bolts,itm.rpt_crossbow,itm.nordic_shield,itm.wooden_shield,itm.sword_medieval_a,itm.shortened_spear,itm.mail_shirt,itm.skullcap,itm.hide_boots],
   def_attrib|level(16),wp(100),knows_common|knows_riding_3|knows_power_strike_2|knows_athletics_2|knows_ironflesh_1,refugee_face1,refugee_face2],
  ["sword_sister","Sword Sister","Sword Sisters",tf_female|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac.commoners,
   [itm.bolts,itm.sword_medieval_b,itm.sword_khergit_3,itm.sarranid_cavalry_sword,itm.plate_covered_round_shield,itm.tab_shield_small_round_c, itm.crossbow,itm.plate_armor,itm.coat_of_plates,itm.plate_boots,itm.guard_helmet,itm.helmet_with_neckguard,itm.courser,itm.leather_gloves],
   def_attrib|level(22),wp(140),knows_common|knows_power_strike_3|knows_riding_5|knows_athletics_3|knows_ironflesh_2|knows_shield_2,refugee_face1,refugee_face2],

 # Civilians
 ###########
  ["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor,0,0,fac.commoners,
   [itm.knife,itm.dagger,itm.sickle,itm.hatchet,itm.club,itm.dress,itm.robe,itm.woolen_dress, itm.headcloth, itm.woolen_hood, itm.wrapping_boots],
   def_attrib|level(1),wp(45),knows_common,refugee_face1,refugee_face2],
  ["peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor,0,0,fac.commoners,
   [itm.knife,itm.pitch_fork,itm.sickle,itm.hatchet,itm.club,itm.dress,itm.woolen_dress, itm.headcloth, itm.woolen_hood, itm.wrapping_boots],
   def_attrib|level(1),wp(40),knows_common,refugee_face1,refugee_face2],

  ["caravan_master","Caravan Master","Caravan Masters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac.commoners,
   [itm.sword_medieval_c,itm.fur_coat,itm.hide_boots,itm.saddle_horse,itm.leather_jacket,itm.leather_cap],
   def_attrib|level(9),wp(100),knows_common|knows_riding_4|knows_ironflesh_3,mercenary_face_1, mercenary_face_2],

#This troop is the troop marked as soldiers_end
  ["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.commoners,
   [itm.dress,itm.leather_boots],
   def_attrib|level(2),wp(50),knows_common|knows_riding_2,woman_face_1, woman_face_2],

#This troop is the troop marked as town_walkers_begin
 ["town_walker_m","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.short_tunic, itm.linen_tunic,itm.fur_coat, itm.coarse_tunic, itm.tabard, itm.leather_vest, itm.arena_tunic_white, itm.leather_apron, itm.shirt, itm.arena_tunic_green, itm.arena_tunic_blue, itm.woolen_hose, itm.nomad_boots, itm.blue_hose, itm.hide_boots, itm.ankle_boots, itm.leather_boots, itm.fur_hat, itm.leather_cap, itm.straw_hat, itm.felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2],
 ["town_walker_f","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.blue_dress, itm.dress, itm.woolen_dress, itm.peasant_dress, itm.woolen_hose, itm.blue_hose, itm.wimple_a, itm.wimple_with_veil, itm.female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["town_walker_1_m","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.short_tunic,itm.red_tunic,itm.green_tunic,itm.blue_tunic,itm.arena_tunic_yellow,itm.arena_tunic_white,itm.tabard,itm.leather_apron,itm.gambeson,itm.blue_gambeson,itm.red_gambeson,itm.woolen_hose,itm.blue_hose,itm.hide_boots,itm.ankle_boots,itm.leather_boots,itm.leather_cap,itm.straw_hat,itm.felt_hat,itm.felt_hat_b],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_old_2],
 ["town_walker_1_f","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.blue_dress,itm.dress,itm.woolen_dress,itm.woolen_hose,itm.blue_hose,itm.wimple_a,itm.wimple_with_veil,itm.female_hood],
   def_attrib|level(2),wp(40),knows_common,swadian_woman_face_younger_1,swadian_woman_face_old_2],
 ["town_walker_2_m","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.linen_tunic,itm.fur_coat,itm.coarse_tunic,itm.nomad_vest,itm.leather_vest,itm.shirt,itm.leather_jacket,itm.nomad_boots,itm.hide_boots,itm.leather_boots,itm.fur_hat,itm.fur_hat,itm.fur_hat,itm.leather_cap],
   def_attrib|level(4),wp(60),knows_common,vaegir_face_younger_1, vaegir_face_old_2],
 ["town_walker_2_f","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.linen_tunic,itm.woolen_dress,itm.peasant_dress,itm.hide_boots,itm.blue_hose],
   def_attrib|level(2),wp(40),knows_common,vaegir_woman_face_younger_1,vaegir_woman_face_old_2],
 ["town_walker_3_m","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.headcloth,itm.wrapping_boots,itm.khergit_leather_boots,itm.linen_tunic,itm.leather_vest,itm.nomad_vest,itm.robe,itm.leather_jacket],
   def_attrib|level(4),wp(60),knows_common,khergit_face_younger_1, khergit_face_old_2],
 ["town_walker_3_f","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.leather_vest,itm.woolen_dress,itm.wrapping_boots,itm.khergit_leather_boots,itm.headcloth,itm.headcloth,itm.headcloth],
   def_attrib|level(2),wp(40),knows_common,khergit_woman_face_younger_1,khergit_woman_face_old_2],
 ["town_walker_4_m","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.coarse_tunic,itm.leather_jacket,itm.nomad_vest,itm.leather_apron,itm.linen_tunic,itm.arena_tunic_white,itm.arena_tunic_green,itm.arena_tunic_blue,itm.arena_tunic_red,itm.arena_tunic_yellow,itm.gambeson,itm.blue_gambeson,itm.red_gambeson,itm.woolen_hose,itm.nomad_boots,itm.blue_hose,itm.hide_boots,itm.leather_boots],
   def_attrib|level(4),wp(60),knows_common,nord_face_younger_1, nord_face_old_2],
 ["town_walker_4_f","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.blue_dress,itm.woolen_dress,itm.peasant_dress,itm.nomad_vest,itm.linen_tunic,itm.hide_boots,itm.leather_boots,itm.blue_hose],
   def_attrib|level(2),wp(40),knows_common,nord_woman_face_younger_1,nord_woman_face_old_2],
 ["town_walker_5_m","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.short_tunic,itm.linen_tunic,itm.leather_jacket,itm.coarse_tunic,itm.tabard,itm.leather_apron,itm.arena_tunic_white,itm.arena_tunic_green,itm.arena_tunic_blue,itm.arena_tunic_red,itm.arena_tunic_yellow,itm.gambeson,itm.blue_gambeson,itm.red_gambeson,itm.woolen_hose,itm.nomad_boots,itm.blue_hose,itm.hide_boots,itm.ankle_boots,itm.leather_boots,itm.straw_hat,itm.leather_cap,itm.straw_hat,itm.felt_hat_b,itm.felt_hat_b],
   def_attrib|level(4),wp(60),knows_common,rhodok_face_younger_1, rhodok_face_old_2],
 ["town_walker_5_f","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.blue_dress,itm.dress,itm.woolen_dress,itm.peasant_dress,itm.woolen_hose,itm.blue_hose,itm.wimple_a,itm.wimple_with_veil,itm.woolen_hood,itm.female_hood,itm.straw_hat,itm.straw_hat],
   def_attrib|level(2),wp(40),knows_common,rhodok_woman_face_younger_1,rhodok_woman_face_old_2],
 ["town_walker_6_m","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.sarranid_felt_hat,itm.turban,itm.wrapping_boots,itm.sarranid_boots_a,itm.sarranid_boots_b,itm.sarranid_cloth_robe,itm.sarranid_cloth_robe_b,itm.robe,itm.sarranid_cloth_robe,itm.sarranid_cloth_robe_b,itm.sarranid_cloth_robe,itm.tunic_with_green_cape],
   def_attrib|level(4),wp(60),knows_common,sarranid_face_younger_1, sarranid_face_old_2],
 ["town_walker_6_f","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.sarranid_common_dress,itm.sarranid_common_dress_b,itm.sarranid_boots_a,itm.sarranid_felt_head_cloth,itm.sarranid_felt_head_cloth_b],
   def_attrib|level(2),wp(40),knows_common,sarranid_woman_face_younger_1,sarranid_woman_face_old_2],
  
#This troop is the troop marked as town_walkers_end and village_walkers_begin
 ["village_walker_m","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.short_tunic, itm.linen_tunic, itm.coarse_tunic, itm.leather_vest, itm.leather_apron, itm.shirt, itm.woolen_hose, itm.nomad_boots, itm.blue_hose, itm.hide_boots, itm.ankle_boots, itm.leather_boots, itm.fur_hat, itm.leather_cap, itm.straw_hat, itm.felt_hat, itm.woolen_cap],
   def_attrib|level(4),wp(60),knows_common,man_face_younger_1, man_face_older_2],
 ["village_walker_f","Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.dress, itm.woolen_dress, itm.peasant_dress, itm.woolen_hose, itm.blue_hose, itm.wimple_a, itm.wimple_with_veil, itm.female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["village_walker_3_m","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.leather_steppe_cap_a,itm.nomad_cap_b,itm.woolen_cap,itm.wrapping_boots,itm.nomad_boots,itm.hunter_boots,itm.khergit_leather_boots,itm.pelt_coat,itm.leather_vest,itm.nomad_armor,itm.khergit_armor,itm.rawhide_coat,itm.shirt],
   def_attrib|level(4),wp(60),knows_common,khergit_face_younger_1, khergit_face_middle_2],
 ["village_walker_3_f","Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.leather_vest,itm.shirt,itm.sarranid_common_dress_b,itm.wrapping_boots,itm.khergit_leather_boots,itm.headcloth,itm.headcloth,itm.headcloth],
   def_attrib|level(2),wp(40),knows_common,khergit_woman_face_younger_1,khergit_woman_face_middle_2],
 ["village_walker_6_m","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.sarranid_felt_hat,itm.turban,itm.desert_turban,itm.wrapping_boots,itm.sarranid_boots_a,itm.sarranid_cloth_robe,itm.sarranid_cloth_robe_b,itm.tunic_with_green_cape],
   def_attrib|level(4),wp(60),knows_common,sarranid_face_younger_1, sarranid_face_middle_2],
 ["village_walker_6_f","Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.sarranid_common_dress,itm.sarranid_common_dress_b,itm.sarranid_boots_a,itm.sarranid_felt_head_cloth,itm.sarranid_felt_head_cloth_b],
   def_attrib|level(2),wp(40),knows_common,sarranid_woman_face_younger_1,sarranid_woman_face_middle_2],
  
#This troop is the troop marked as village_walkers_end and spy_walkers_begin
 ["spy_walker_m","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.commoners,
   [itm.short_tunic,itm.linen_tunic,itm.coarse_tunic,itm.leather_apron,itm.arena_tunic_white,itm.arena_tunic_green,itm.arena_tunic_blue,itm.arena_tunic_red,itm.arena_tunic_yellow,itm.gambeson,itm.blue_gambeson,itm.red_gambeson,itm.woolen_hose,itm.nomad_boots,itm.blue_hose,itm.hide_boots,itm.ankle_boots,itm.leather_boots,itm.fur_hat,itm.leather_cap,itm.straw_hat,itm.felt_hat,itm.felt_hat_b,itm.common_hood,itm.woolen_cap],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1,mercenary_face_2],
 ["spy_walker_f","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.commoners,
   [itm.blue_dress,itm.dress,itm.woolen_dress,itm.peasant_dress,itm.woolen_hose,itm.blue_hose,itm.wimple_a,itm.wimple_with_veil,itm.woolen_hood,itm.female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["spy_walker_3_m","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.commoners,
   [itm.headcloth,itm.wrapping_boots,itm.khergit_leather_boots,itm.leather_vest,itm.robe],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1,mercenary_face_2],
 ["spy_walker_3_f","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.commoners,
   [itm.leather_vest,itm.woolen_dress,itm.wrapping_boots,itm.khergit_leather_boots,itm.headcloth],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["spy_walker_6_m","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.commoners,
   [itm.sarranid_felt_hat,itm.turban,itm.desert_turban,itm.wrapping_boots,itm.sarranid_boots_a,itm.sarranid_boots_b,itm.sarranid_cloth_robe,itm.sarranid_cloth_robe_b,itm.robe,itm.sarranid_cloth_robe,itm.sarranid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1,mercenary_face_2],
 ["spy_walker_6_f","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.commoners,
   [itm.sarranid_common_dress,itm.sarranid_common_dress_b,itm.sarranid_boots_a,itm.sarranid_felt_head_cloth,itm.sarranid_felt_head_cloth_b],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
# Ryan END

#This troop is the troop marked as spy_walkers_end
# Zendar
  ["tournament_master","Tournament Master","{!}Tournament Master",tf_hero, scn.zendar_center|entry(8),reserved,  fac.commoners,[itm.nomad_armor,itm.falchion,itm.nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000088b0005113b5646c91b8e329c00000000001cb6d20000000000000000],
  ["constable_hareck","Constable Hareck","{!}Constable Hareck",tf_hero, scn.zendar_center|entry(11),reserved,  fac.neutral,[itm.mail_with_surcoat,itm.mace_2,itm.leather_boots],def_attrib|level(5),wp(20),knows_common,0x0000000d7d00521348ad655b225ab51c00000000001dba9d0000000000000000],
  ["mercenary_master","Mercenary Master","{!}Mercenary Master",tf_hero, scn.zendar_center|entry(13),reserved,  fac.commoners,[itm.leather_jerkin,itm.sword_viking_1,itm.hide_boots],def_attrib|level(2),wp(20),knows_common,0x000000018200410627953194b256446500000000000d3ceb0000000000000000],

  ["zendar_armorer","Armorer",  "{!}Zendar Armorer",  tf_hero|tf_female|tf_is_merchant, scn.zendar_center|entry(9), 0, fac.commoners,[itm.aketon_green,itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000079f0010067adc95ca5c663d1900000000001e28660000000000000000],
  ["zendar_weaponsmith","Weaponsmith","{!}Zendar Weaponsmith",tf_hero|tf_is_merchant, scn.zendar_center|entry(10), 0, fac.commoners,[itm.leather_apron,itm.wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000043d00501433a449a8eb9a5759000000000012a8740000000000000000],
  ["zendar_horse_merchant","Horse Merchant","{!}Zendar Horse Merchant",tf_hero|tf_is_merchant, scn.zendar_center|entry(12), 0, fac.commoners,[itm.coarse_tunic, itm.straw_hat, itm.hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x0000000fdd00761232e22a559db64c1900000000001d28f40000000000000000],
  ["zendar_merchant","Pawnbroker","{!}Zendar Merchant",tf_hero|tf_is_merchant, scn.zendar_merchant|entry(9), 0, fac.commoners,[itm.rich_outfit,itm.ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x0000000d7f0001521cca5b326d48a74e00000000001e3aee0000000000000000],
  ["zendar_bodger","Bodger","{!}Zendar Bodger",tf_hero|tf_is_merchant, scn.zendar_bodger|entry(9), 0, fac.commoners,[itm.leather_apron,itm.ankle_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000009bf005393575b67448b68b55400000000001dea9c0000000000000000],
 
  ["zendar_tavernkeeper","Tavern Keeper","{!}Tavern Keeper",tf_hero|tf_randomize_face|tf_female, scn.the_happy_boar|entry(9),0,  fac.commoners,[itm.peasant_dress, itm.hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["xerina","Xerina","Xerina",tf_hero|tf_female, scn.the_happy_boar|entry(14),reserved,  fac.commoners,[itm.leather_jerkin,itm.sword_medieval_c_small,itm.hide_boots],def_attrib|str_15|agi_15|level(39),wp(312),knows_power_strike_5|knows_ironflesh_5|knows_riding_6|knows_power_draw_4|knows_athletics_8|knows_shield_3,0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],
  ["dranton","Dranton","Dranton",tf_hero, scn.the_happy_boar|entry(12),reserved,  fac.commoners,[itm.leather_vest,itm.sword_khergit_3,itm.hide_boots],def_attrib|str_15|agi_14|level(42),wp(324),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],
  ["kradus","Kradus","Kradus",tf_hero, scn.the_happy_boar|entry(13),reserved,  fac.commoners,[itm.padded_leather,itm.bastard_sword_a,itm.hide_boots],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000],
  ["fight_promoter","Rough-Looking Guy","Rough-Looking Guy",tf_hero|tf_randomize_face,scn.the_happy_boar|entry(10),0,fac.commoners,
   [itm.nomad_vest,itm.nomad_boots,itm.woolen_cap,itm.spiked_club], def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3, bandit_face1, bandit_face2],

#Salt mine
  ["galeas","Galeas","Galeas",tf_hero, scn.salt_mine|entry(2), reserved, fac.slavers,[itm.leather_jacket,itm.mace_3,itm.khergit_leather_boots],def_attrib|level(5),wp(20),knows_common,0x0000000ff100610524d671a71c674b0b00000000001db5090000000000000000],
  ["barezan","Barezan","Barezan", tf_hero|tf_is_merchant, scn.salt_mine|entry(1),reserved, fac.commoners, [itm.leather_apron,itm.hammer,itm.leather_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x0000000bff0061533ac3ddb722965edd00000000001d24f20000000000000000],

#Dhorak keep
  ["sister_tajel","Sister Tajel","{!}Sister Tajel",tf_hero|tf_female, scn.dhorak_keep|entry(11), 0, fac.manhunters,[itm.blue_dress,itm.arabian_sword_b,itm.wimple_a,itm.blue_hose], def_attrib|level(5),wp(20),knows_common, 0x0000000019000004177d30d6a350123500000000001e476a0000000000000000],
  ["sister_yuna","Sister Yuna","{!}Sister Yuna",tf_hero|tf_female, scn.dhorak_keep|entry(8), 0, fac.manhunters,[itm.mail_shirt,itm.morningstar_short,itm.mail_boots], def_attrib|level(5),wp(20),knows_common, 0x000000003f00300660129e26016204d000000000001e08210000000000000000],

  ["dhorak_armorer","Armorer",  "{!}Dhorak Keep Armorer",  tf_hero|tf_female|tf_is_merchant, scn.dhorak_keep|entry(9), 0, fac.commoners,[itm.leather_apron,itm.leather_gloves,itm.leather_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000002f0020024e6428c4dab23aa400000000001f67590000000000000000],
  ["dhorak_weaponsmith","Weaponsmith","{!}Dhorak Keep Weaponsmith",tf_hero|tf_female|tf_is_merchant, scn.dhorak_keep|entry(10), 0, fac.commoners,[itm.leather_jerkin,itm.hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x0000000a4600200435338cb5328d448a00000000001e48e30000000000000000],
  ["dhorak_horse_merchant","Horse Merchant","{!}Dhorak Keep Horse Merchant",tf_hero|tf_is_merchant|tf_female, scn.dhorak_keep|entry(12), 0, fac.commoners,[itm.peasant_dress,itm.wimple_a,itm.nomad_boots],   def_attrib|level(5),wp(20),knows_inventory_management_10, 0x0000000a7b0010034499a9b69d4ab32300000000001d470c0000000000000000],
 
#Four Ways Inn
 ["four_ways_guide","Quick Jimmy","{!}Quick Jimmy",tf_hero, scn.four_ways_inn|entry(11) ,0,  fac.outlaws,[itm.coarse_tunic,itm.butchering_knife,itm.leather_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x0000000d400025d176c26a371db1e87400000000001c57550000000000000000],
 
 ["four_ways_armorer","Armorer",  "{!}Four Ways Inn Armorer",  tf_hero|tf_is_merchant, scn.four_ways_inn|entry(9), 0, fac.commoners,[itm.tribal_warrior_outfit,itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x0000000b7500730b1a9e5224eb92daec000000000012c4ab0000000000000000],
 ["four_ways_weaponsmith","Weaponsmith","{!}Four Ways Inn Weaponsmith",tf_hero|tf_is_merchant, scn.four_ways_inn|entry(10), 0, fac.commoners,[itm.leather_jerkin,itm.nomad_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x0000000b620003073b22862d1499d89b00000000001db7630000000000000000],
 ["four_ways_horse_merchant","Horse Merchant","{!}Four Ways Inn Horse Merchant",tf_hero|tf_is_merchant, scn.four_ways_inn|entry(12), 0, fac.commoners,[itm.pelt_coat,itm.knife,itm.wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x0000000b7c00054316ac6e25a56dcc6900000000001e19110000000000000000],

 ["four_ways_bandit_chief","Ronnie the Sly","{!}Bandit Chief",tf_hero, scn.the_smiling_fox|entry(8),0,  fac.outlaws,[itm.nomad_vest,itm.sword_viking_1,itm.nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x0000000aff0000cb64ac5247655a570c00000000001f69250000000000000000],
 ["four_ways_tavernkeeper","Tavern Keeper","{!}Tavern Keeper",tf_hero|tf_randomize_face|tf_female, scn.the_smiling_fox|entry(9),0,  fac.commoners,[itm.peasant_dress, itm.blue_hose],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
 ["four_ways_bouncer","Bouncer","{!}Bouncer",tf_hero|tf_randomize_face, scn.the_smiling_fox|entry(10),0,  fac.outlaws,[itm.nomad_armor,itm.mace_1,itm.nomad_boots],def_attrib|level(2),wp(20),knows_common, bandit_face1, bandit_face2],
 ["four_ways_owner","Smiling Louie","{!}Smiling Louie",tf_hero, scn.the_smiling_fox|entry(11),0,  fac.slavers,[itm.leather_jacket,itm.dagger,itm.khergit_leather_boots],def_attrib|level(2),wp(20),knows_common, 0x0000000acf001094489e73cb15b7a2a400000000001daa6b0000000000000000],
 ["four_ways_barmaid_1","Barmaid","{!}Barmaid",tf_hero|tf_female|tf_randomize_face, scn.the_smiling_fox|entry(12),0,  fac.commoners,[itm.red_dress,itm.woolen_hose],def_attrib|level(2),wp(20),knows_common, swadian_woman_face_younger_1, swadian_woman_face_young_2],
 ["four_ways_barmaid_2","Barmaid","{!}Barmaid",tf_hero|tf_female|tf_randomize_face, scn.the_smiling_fox|entry(13),0,  fac.commoners,[itm.brown_dress,itm.woolen_hose],def_attrib|level(2),wp(20),knows_common, vaegir_woman_face_younger_1, vaegir_woman_face_young_2],
 ["four_ways_barmaid_3","Barmaid","{!}Barmaid",tf_hero|tf_female|tf_randomize_face, scn.the_smiling_fox|entry(14),0,  fac.commoners,[itm.green_dress,itm.blue_hose],def_attrib|level(2),wp(20),knows_common, khergit_woman_face_younger_1, khergit_woman_face_young_2],
 ["four_ways_barmaid_4","Barmaid","{!}Barmaid",tf_hero|tf_female|tf_randomize_face, scn.the_smiling_fox|entry(15),0,  fac.commoners,[itm.blue_dress,itm.blue_hose],def_attrib|level(2),wp(20),knows_common, nord_woman_face_younger_1, nord_woman_face_young_2],

 ["four_ways_smuggler_1","Alhazar","{!}Smuggler",tf_hero|tf_is_merchant, 0, reserved, fac.commoners,[itm.robe,itm.headcloth,itm.khergit_leather_boots],def_attrib|level(5),wp(20),knows_common,0x00000007360061c0375c8d395c99320c00000000001d56ec0000000000000000],
 ["four_ways_smuggler_2","Cheng Zhen","{!}Smuggler",tf_hero|tf_is_merchant, 0, reserved, fac.commoners,[itm.fur_coat,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,0x0000000d3f00438b221e70b44360a8c400000000001dc6ff0000000000000000],
 ["four_ways_smuggler_3","Hanzo","{!}Smuggler",tf_hero|tf_is_merchant, 0, reserved, fac.commoners,[itm.steppe_armor,itm.woolen_cap,itm.nomad_boots],def_attrib|level(5),wp(20),knows_common,0x0000000fec00600a3ccd55c6919ab69b00000000001ca88b0000000000000000],
 ["four_ways_smuggler_4","Fortunato","{!}Smuggler",tf_hero|tf_is_merchant, 0, reserved, fac.commoners,[itm.pilgrim_disguise,itm.pilgrim_hood,itm.wrapping_boots],def_attrib|level(5),wp(20),knows_common,0x000000047f0020cf3d1eaa2b5cd1bb1b00000000001e48920000000000000000],

# Stays in Thir for now...
 ["ramun","Ramun","Ramun",tf_hero, no_scene,reserved, fac.slavers,[itm.leather_jacket,itm.club,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],

#Tutorial
  ["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero, 0, 0, fac.commoners,[itm.robe,itm.nomad_boots],def_attrib|level(2),wp(20),knows_common,0x0000000d600023d168eb8e485cca230c00000000000e594a0000000000000000],
  ["tutorial_student_1","{!}tutorial_student_1","{!}tutorial_student_1",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.neutral,
   [itm.practice_sword, itm.practice_shield, itm.leather_jerkin,itm.padded_leather,itm.leather_armor,itm.ankle_boots,itm.padded_coif,itm.footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_2","{!}tutorial_student_2","{!}tutorial_student_2",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.neutral,
   [itm.practice_sword, itm.practice_shield, itm.leather_jerkin,itm.padded_leather,itm.leather_armor,itm.ankle_boots,itm.padded_coif,itm.footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_3","{!}tutorial_student_3","{!}tutorial_student_3",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.neutral,
   [itm.practice_staff, itm.leather_jerkin,itm.padded_leather,itm.leather_armor,itm.ankle_boots,itm.padded_coif,itm.footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_4","{!}tutorial_student_4","{!}tutorial_student_4",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac.neutral,
   [itm.practice_staff, itm.leather_jerkin,itm.padded_leather,itm.leather_armor,itm.ankle_boots,itm.padded_coif,itm.footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],

  ["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac.commoners,
   [itm.linen_tunic,itm.coarse_tunic,itm.shirt,itm.nomad_boots,itm.wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],

  ["trainer_1","Trainer","Trainer",tf_hero, scn.training_ground_ranged_melee_1|entry(6),reserved,  fac.commoners,[itm.leather_jerkin,itm.hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
  ["trainer_2","Trainer","Trainer",tf_hero, scn.training_ground_ranged_melee_2|entry(6),reserved,  fac.commoners,[itm.nomad_vest,itm.hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
  ["trainer_3","Trainer","Trainer",tf_hero, scn.training_ground_ranged_melee_3|entry(6),reserved,  fac.commoners,[itm.padded_leather,itm.hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
  ["trainer_4","Trainer","Trainer",tf_hero, scn.training_ground_ranged_melee_4|entry(6),reserved,  fac.commoners,[itm.leather_jerkin,itm.hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
  ["trainer_5","Trainer","Trainer",tf_hero, scn.training_ground_ranged_melee_5|entry(6),reserved,  fac.commoners,[itm.leather_vest,itm.hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

# Ransom brokers.
  ["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.leather_vest,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.tabard,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.leather_vest,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.short_tunic,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.gambeson,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.blue_gambeson,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.red_gambeson,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.fur_coat,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.leather_vest,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.leather_jacket,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.fur_coat,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.tabard,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.leather_vest,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.blue_gambeson,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.short_tunic,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.fur_coat,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.leather_jacket,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.tabard,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.fur_coat,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac.commoners,[itm.leather_jacket,itm.hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_bookseller_1","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac.commoners,[itm.fur_coat,itm.hide_boots,
               itm.book_tactics, itm.book_persuasion, itm.book_wound_treatment_reference, itm.book_leadership, 
               itm.book_intelligence, itm.book_training_reference, itm.book_surgery_reference],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_bookseller_2","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac.commoners,[itm.fur_coat,itm.hide_boots,
               itm.book_wound_treatment_reference, itm.book_leadership, itm.book_intelligence, itm.book_trade, 
               itm.book_engineering, itm.book_weapon_mastery],def_attrib|level(5),wp(20),knows_common,merchant_face_1, merchant_face_2],

# Tavern minstrel.
  ["tavern_minstrel_1","Wandering Minstrel","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac.commoners,[itm.leather_jacket, itm.hide_boots, itm.lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute
  ["tavern_minstrel_2","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac.commoners,[itm.tunic_with_green_cape, itm.hide_boots, itm.lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],  #early harp/lyre
  ["tavern_minstrel_3","Wandering Ashik","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac.commoners,[itm.nomad_robe, itm.hide_boots, itm.lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute/oud or rebab
  ["tavern_minstrel_4","Wandering Skald","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac.commoners,[itm.fur_coat, itm.hide_boots, itm.lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #No instrument or lyre
  ["tavern_minstrel_5","Wandering Troubadour","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac.commoners,[itm.short_tunic, itm.hide_boots, itm.lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #Lute or Byzantine/Occitan lyra
  
#NPC system changes begin
#Companions
  ["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac.kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],

  ["npc1","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[itm.khergit_armor,itm.nomad_boots,itm.knife],
   str_8|agi_7|int_12|cha_7|level(3),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac.commoners,[itm.linen_tunic,itm.hide_boots,itm.club],
   str_7|agi_7|int_11|cha_6|level(1),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac.commoners,[itm.dress,itm.woolen_hose,itm.knife],
   str_6|agi_9|int_11|cha_6|level(1),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac.commoners,[itm.leather_jerkin,itm.nomad_boots, itm.sword_medieval_a],
   str_10|agi_9|int_13|cha_10|level(10),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac.commoners,[itm.nomad_vest,itm.nomad_boots, itm.sword_khergit_1],
   str_9|agi_9|int_12|cha_7|level(5),wp(90),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac.commoners,[itm.tabard,itm.nomad_boots, itm.sword_medieval_a],
   str_10|agi_12|int_10|cha_5|level(6),wp(105),knows_warrior_npc|
   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac.commoners,[itm.ragged_outfit,itm.wrapping_boots, itm.hunting_bow, itm.arrows, itm.quarter_staff],
   str_8|agi_9|int_10|cha_6|level(2),wp(80),knows_tracker_npc|
   knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac.commoners,[itm.tribal_warrior_outfit,itm.nomad_boots, itm.sword_viking_1],
   str_9|agi_10|int_9|cha_10|level(7),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac.commoners,[itm.tabard,itm.nomad_boots, itm.sword_medieval_b_small],
   str_11|agi_8|int_7|cha_8|level(2),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac.commoners,[itm.padded_leather,itm.nomad_boots, itm.crossbow, itm.bolts, itm.pickaxe],
   str_12|agi_8|int_9|cha_11|level(9),wp(105),knows_warrior_npc|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac.commoners,[itm.leather_apron, itm.falchion, itm.wrapping_boots],
   str_8|agi_11|int_10|cha_10|level(8),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac.commoners,[itm.pilgrim_disguise,itm.nomad_boots, itm.staff],
   str_8|agi_7|int_13|cha_7|level(4),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac.commoners,[itm.nomad_robe,itm.nomad_boots, itm.scimitar, itm.courser],
   str_7|agi_7|int_12|cha_8|level(3),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac.commoners,[itm.nobleman_outfit,itm.nomad_boots, itm.sword_medieval_b_small],
   str_9|agi_8|int_11|cha_8|level(5),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac.commoners,[itm.rich_outfit,itm.nomad_boots, itm.sword_medieval_b_small],
   str_9|agi_9|int_12|cha_8|level(7),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac.commoners,[itm.peasant_dress,itm.nomad_boots, itm.dagger, itm.throwing_knives],
   str_7|agi_11|int_8|cha_7|level(2),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],
#NPC system changes end


#governers olgrel rasevas                                                                        Horse          Bodywear                Footwear_in                     Footwear_out                    Armor                       Weapon                  Shield                  Headwaer
  ["kingdom_1_lord",  "King Harlaus",  "Harlaus",  tf_hero, 0,reserved,  fac.kingdom_1,[itm.charger,   itm.rich_outfit,        itm.blue_hose,                  itm.plate_boots,               itm.plate_armor, itm.gauntlets,    itm.bastard_sword_b,      itm.tab_shield_heater_cav_b,       itm.great_helmet],          knight_attrib_5,wp(220),knight_skills_5|knows_trainer_5, 0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000,swadian_face_older_2],
  ["kingdom_2_lord",  "King Yaroglek",  "Yaroglek",  tf_hero, 0,reserved,  fac.kingdom_2,[itm.hunter,    itm.courtly_outfit,      itm.leather_boots,              itm.plate_boots,              itm.heraldic_mail_with_surcoat, itm.gauntlets,      itm.military_pick,      itm.tab_shield_kite_cav_b,      itm.vaegir_war_mask],    knight_attrib_5,wp(220),knight_skills_5|knows_trainer_4, 0x0000000ec50001400a2269f919dee11700000000001cc57d0000000000000000, vaegir_face_old_2],
  ["kingdom_3_lord",  "Sanjar Khan",  "Sanjar",  tf_hero, 0,reserved,  fac.kingdom_3,[itm.courser,   itm.nomad_robe,             itm.leather_boots,              itm.splinted_greaves,           itm.khergit_guard_armor,  itm.lamellar_gauntlets,       itm.sword_khergit_3,              itm.tab_shield_small_round_c,       itm.guard_helmet],      knight_attrib_5,wp(220),knight_skills_5|knows_trainer_6, 0x0000000cee0051cc44be2d14d370c65c00000000001ed6df0000000000000000,khergit_face_old_2],
  ["kingdom_4_lord",  "King Ragnar",  "Ragnar",  tf_hero, 0,reserved,  fac.kingdom_4,[itm.hunter,    itm.nobleman_outfit,    itm.leather_boots,              itm.mail_boots,                 itm.cuir_bouilli,  itm.gauntlets,    itm.great_axe,           itm.tab_shield_round_e,    itm.nordic_helmet],            knight_attrib_5,wp(220),knight_skills_5|knows_trainer_4, 0x0000000e2c0c028a068e8c18557b12a500000000001c0fe80000000000000000, nord_face_older_2],
  ["kingdom_5_lord",  "King Graveth",  "Graveth",  tf_hero, 0,reserved,  fac.kingdom_5,[itm.warhorse,  itm.tabard,             itm.leather_boots,              itm.splinted_leather_greaves,   itm.heraldic_mail_with_tabard,  itm.gauntlets,         itm.bastard_sword_b,         itm.tab_shield_heater_cav_b,        itm.spiked_helmet],         knight_attrib_4,wp(220),knight_skills_4|knows_trainer_5, 0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000, rhodok_face_old_2],
  ["kingdom_6_lord",  "Sultan Hakim",  "Hakim",  tf_hero, 0,reserved,  fac.kingdom_6,[itm.warhorse_sarranid,     itm.mamluke_mail,          itm.sarranid_boots_c,       itm.sarranid_mail_coif,  itm.mail_mittens,      itm.sarranid_cavalry_sword,    itm.tab_shield_small_round_c],         knight_attrib_4,wp(220),knight_skills_5|knows_trainer_5, 0x0000000a4b107354189c71d6d386e8ac00000000001e24eb0000000000000000, sarranid_face_old_2],


#    Imbrea   Belinda Ruby Qaelmas Rose    Willow 
#  Alin  Ganzo            Zelka Rabugti
#  Qlurzach Ruhbus Givea_alsev  Belanz        Bendina  
# Dunga        Agatha     Dibus Crahask
  
#                                                                               Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
  #Swadian civilian clothes: itm.courtly_outfit itm.gambeson itm.blue_gambeson itm.red_gambeson itm.nobleman_outfit itm.rich_outfit itm.short_tunic itm.tabard
  #Older knights with higher skills moved to top
  ["knight_1_1", "Count Klargus", "Klargus", tf_hero, 0, reserved,  fac.kingdom_1, [itm.saddle_horse,      itm.courtly_outfit,      itm.heraldic_mail_with_surcoat,   itm.nomad_boots, itm.splinted_greaves,       itm.great_helmet,           itm.sword_medieval_c,  itm.scale_gauntlets,         itm.tab_shield_heater_cav_a],   knight_attrib_5,wp(230),knight_skills_5|knows_trainer_1|knows_trainer_3, 0x0000000c3e08601414ab4dc6e39296b200000000001e231b0000000000000000, swadian_face_older_2],
  ["knight_1_2", "Count Delinard", "Delinard", tf_hero, 0, reserved,  fac.kingdom_1, [itm.courser,           itm.red_gambeson,      itm.heraldic_mail_with_surcoat,               itm.nomad_boots,            itm.iron_greaves,                    itm.guard_helmet,  itm.gauntlets,        itm.bastard_sword_a,    itm.tab_shield_heater_cav_b],       knight_attrib_5,wp(240),knight_skills_5, 0x0000000c0f0c320627627238dcd6599400000000001c573d0000000000000000, swadian_face_young_2],
  ["knight_1_3", "Count Haringoth", "Haringoth", tf_hero, 0, reserved,  fac.kingdom_1, [itm.warhorse,          itm.nobleman_outfit,     itm.coat_of_plates,                 itm.leather_boots,          itm.splinted_leather_greaves,        itm.flat_topped_helmet, itm.gauntlets, itm.bastard_sword_b,   itm.tab_shield_heater_d],  knight_attrib_5,wp(260),knight_skills_5|knows_trainer_3, 0x0000000cb700210214ce89db276aa2f400000000001d36730000000000000000, swadian_face_young_2],
  ["knight_1_4", "Count Clais", "Clais", tf_hero, 0, reserved,  fac.kingdom_1, [itm.saddle_horse,      itm.short_tunic,       itm.heraldic_mail_with_surcoat,           itm.leather_boots,          itm.mail_chausses,                   itm.winged_great_helmet, itm.gauntlets,       itm.bastard_sword_a,  itm.sword_two_handed_a,  itm.tab_shield_heater_d],    knight_attrib_5,wp(180),knight_skills_5|knows_trainer_4, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000, swadian_face_older_2],
  ["knight_1_5", "Count Deglan", "Deglan", tf_hero, 0, reserved,  fac.kingdom_1, [itm.hunter,            itm.rich_outfit,        itm.mail_hauberk,itm.woolen_hose, itm.mail_chausses, itm.guard_helmet, itm.gauntlets,         itm.sword_medieval_c,    itm.tab_shield_heater_d],      knight_attrib_4,wp(200),knight_skills_4|knows_trainer_6, 0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000, swadian_face_older_2],
  ["knight_1_6", "Count Tredian", "Tredian", tf_hero, 0, reserved,  fac.kingdom_1, [itm.hunter,            itm.tabard,      itm.heraldic_mail_with_surcoat,               itm.leather_boots,          itm.mail_boots,                      itm.winged_great_helmet, itm.gauntlets, itm.bastard_sword_b, itm.sword_two_handed_b,  itm.tab_shield_heater_cav_b], knight_attrib_5,wp(240),knight_skills_4|knows_trainer_4, 0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000, swadian_face_older_2],
  ["knight_1_7", "Count Grainwad", "Grainwad", tf_hero, 0, reserved,  fac.kingdom_1, [itm.hunter,            itm.tabard,      itm.heraldic_mail_with_surcoat,               itm.leather_boots,          itm.mail_boots,                      itm.flat_topped_helmet, itm.gauntlets, itm.bastard_sword_b,   itm.sword_two_handed_b, itm.tab_shield_heater_cav_b], knight_attrib_5,wp(290),knight_skills_4|knows_trainer_4, 0x0000000c1e001500589dae4094aa291c00000000001e37a80000000000000000, swadian_face_young_2],
  ["knight_1_8", "Count Ryis", "Ryis", tf_hero, 0, reserved,  fac.kingdom_1, [itm.warhorse,          itm.nobleman_outfit,     itm.coat_of_plates,                 itm.leather_boots,          itm.splinted_leather_greaves,        itm.winged_great_helmet,  itm.gauntlets,itm.bastard_sword_b,  itm.sword_two_handed_a, itm.tab_shield_heater_d],  knight_attrib_4,wp(250),knight_skills_4, 0x0000000c330855054aa9aa431a48d74600000000001ed5240000000000000000, swadian_face_older_2],
  ["knight_1_9", "Count Plais", "Plais", tf_hero, 0, reserved,  fac.kingdom_1, [itm.steppe_horse,      itm.gambeson,     itm.heraldic_mail_with_surcoat,                 itm.blue_hose,              itm.mail_boots,                      itm.nasal_helmet,  itm.scale_gauntlets,     itm.fighting_pick,   itm.tab_shield_heater_c],    knight_attrib_3,wp(160),knight_skills_3, 0x0000000c0f08000458739a9a1476199800000000001fb6f10000000000000000, swadian_face_old_2],
  ["knight_1_10", "Count Mirchaud", "Mirchaud", tf_hero, 0, reserved,  fac.kingdom_1, [itm.courser,           itm.blue_gambeson,        itm.mail_hauberk,                   itm.woolen_hose,            itm.mail_chausses,                   itm.guard_helmet,    itm.gauntlets,    itm.sword_two_handed_b,        itm.tab_shield_heater_cav_b],   knight_attrib_3,wp(190),knight_skills_3, 0x0000000c0610351048e325361d7236cd00000000001d532a0000000000000000, swadian_face_older_2],
  ["knight_1_11", "Count Stamar", "Stamar", tf_hero, 0, reserved,  fac.kingdom_1, [itm.courser,           itm.red_gambeson,      itm.heraldic_mail_with_surcoat,               itm.nomad_boots,            itm.iron_greaves,                    itm.guard_helmet,   itm.gauntlets,       itm.bastard_sword_a,    itm.tab_shield_heater_cav_b],       knight_attrib_3,wp(220),knight_skills_3, 0x0000000c03104490280a8cb2a24196ab00000000001eb4dc0000000000000000, swadian_face_older_2],
  ["knight_1_12", "Count Meltor", "Meltor", tf_hero, 0, reserved,  fac.kingdom_1, [itm.saddle_horse,      itm.rich_outfit,        itm.heraldic_mail_with_surcoat,                    itm.nomad_boots,            itm.mail_boots,                      itm.guard_helmet,   itm.gauntlets,         itm.fighting_pick,   itm.tab_shield_heater_c],    knight_attrib_3,wp(130),knight_skills_3, 0x0000000c2a0805442b2c6cc98c8dbaac00000000001d389b0000000000000000, swadian_face_older_2],
  ["knight_1_13", "Count Beranz", "Beranz", tf_hero, 0, reserved,  fac.kingdom_1, [itm.saddle_horse,      itm.ragged_outfit,      itm.heraldic_mail_with_surcoat,           itm.nomad_boots,            itm.splinted_greaves,                itm.guard_helmet,   itm.gauntlets,         itm.sword_medieval_c,  itm.sword_two_handed_a,     itm.tab_shield_heater_c],   knight_attrib_2,wp(160),knight_skills_2, 0x0000000c380c30c2392a8e5322a5392c00000000001e5c620000000000000000, swadian_face_older_2],
  ["knight_1_14", "Count Rafard", "Rafard", tf_hero, 0, reserved,  fac.kingdom_1, [itm.saddle_horse,      itm.short_tunic,       itm.heraldic_mail_with_tabard,           itm.leather_boots,          itm.mail_chausses,                   itm.nasal_helmet,  itm.scale_gauntlets,     itm.bastard_sword_a,    itm.tab_shield_heater_cav_a],    knight_attrib_2,wp(190),knight_skills_3|knows_trainer_6, 0x0000000c3f10000532d45203954e192200000000001e47630000000000000000, swadian_face_older_2],
  ["knight_1_15", "Count Regas", "Regas", tf_hero, 0, reserved,  fac.kingdom_1, [itm.hunter,            itm.rich_outfit,        itm.mail_hauberk,                   itm.woolen_hose,            itm.mail_chausses,                   itm.great_helmet,   itm.gauntlets,       itm.sword_viking_3, itm.sword_two_handed_a,  itm.tab_shield_heater_d],      knight_attrib_4,wp(140),knight_skills_2, 0x0000000c5c0840034895654c9b660c5d00000000001e34530000000000000000, swadian_face_young_2],
  ["knight_1_16", "Count Devlian", "Devlian", tf_hero, 0, reserved,  fac.kingdom_1, [itm.saddle_horse,      itm.courtly_outfit,      itm.heraldic_mail_with_surcoat,                     itm.nomad_boots,            itm.splinted_greaves,                itm.great_helmet,   itm.gauntlets,         itm.sword_medieval_c,           itm.tab_shield_heater_c],   knight_attrib_1,wp(130),knight_skills_2, 0x000000095108144657a1ba3ad456e8cb00000000001e325a0000000000000000, swadian_face_young_2],
  ["knight_1_17", "Count Rafarch", "Rafarch", tf_hero, 0, reserved,  fac.kingdom_1, [itm.steppe_horse,      itm.gambeson,     itm.heraldic_mail_with_surcoat,                 itm.blue_hose,              itm.mail_boots,                      itm.nasal_helmet,   itm.scale_gauntlets,    itm.fighting_pick,   itm.tab_shield_heater_cav_b],    knight_attrib_2,wp(190),knight_skills_1|knows_trainer_4, 0x0000000c010c42c14d9d6918bdb336e200000000001dd6a30000000000000000, swadian_face_young_2],
  ["knight_1_18", "Count Rochabarth", "Rochabarth", tf_hero, 0, reserved,  fac.kingdom_1, [itm.courser,           itm.blue_gambeson,        itm.mail_hauberk,                   itm.woolen_hose,            itm.mail_chausses,                   itm.winged_great_helmet,   itm.gauntlets,     itm.sword_two_handed_a,        itm.tab_shield_heater_cav_a],   knight_attrib_3,wp(210),knight_skills_1, 0x0000000c150045c6365d8565932a8d6400000000001ec6940000000000000000, swadian_face_young_2],
  ["knight_1_19", "Count Despin", "Despin", tf_hero, 0, reserved,  fac.kingdom_1, [itm.saddle_horse,      itm.rich_outfit,        itm.heraldic_mail_with_surcoat,                    itm.nomad_boots,            itm.mail_boots,                      itm.great_helmet, itm.gauntlets,           itm.fighting_pick,  itm.sword_two_handed_a, itm.tab_shield_heater_cav_a],    knight_attrib_1,wp(120),knight_skills_1, 0x00000008200012033d9b6d4a92ada53500000000001cc1180000000000000000, swadian_face_young_2],
  ["knight_1_20", "Count Montewar", "Montewar", tf_hero, 0, reserved,  fac.kingdom_1, [itm.saddle_horse,      itm.ragged_outfit,      itm.heraldic_mail_with_surcoat,           itm.nomad_boots,            itm.splinted_greaves,                itm.great_helmet, itm.gauntlets,           itm.sword_medieval_c,   itm.sword_two_handed_a,   itm.tab_shield_heater_cav_a],   knight_attrib_2,wp(150),knight_skills_1, 0x0000000c4d0840d24a9b2ab4ac2a332400000000001d34db0000000000000000, swadian_face_young_2],

  ["knight_2_1", "Boyar Vuldrat", "Vuldrat", tf_hero, 0, reserved,  fac.kingdom_2, [itm.saddle_horse,      itm.fur_coat,     itm.vaegir_elite_armor,                   itm.nomad_boots,            itm.splinted_leather_greaves,        itm.vaegir_noble_helmet,    itm.mail_mittens,       itm.sword_viking_3,           itm.tab_shield_kite_c],    knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],
  ["knight_2_2", "Boyar Naldera", "Naldera", tf_hero, 0, reserved,  fac.kingdom_2, [itm.saddle_horse,      itm.rich_outfit,        itm.lamellar_armor,               itm.woolen_hose,            itm.mail_chausses,                   itm.vaegir_noble_helmet,  itm.mail_mittens,      itm.shortened_military_scythe,    itm.tab_shield_kite_cav_a],    knight_attrib_2,wp(160),knight_skills_2, 0x0000000c2a0015d249b68b46a98e176400000000001d95a40000000000000000, vaegir_face_old_2],
  ["knight_2_3", "Boyar Meriga", "Meriga", tf_hero, 0, reserved,  fac.kingdom_2, [itm.warhorse_steppe,            itm.short_tunic,        itm.mail_hauberk,                   itm.woolen_hose,            itm.mail_chausses,                   itm.vaegir_lamellar_helmet, itm.lamellar_gauntlets,           itm.great_bardiche,           itm.tab_shield_kite_cav_b],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000c131031c546a38a2765b4c86000000000001e58d30000000000000000, vaegir_face_older_2],
  ["knight_2_4", "Boyar Khavel", "Khavel", tf_hero, 0, reserved,  fac.kingdom_2, [itm.saddle_horse,      itm.courtly_outfit,     itm.lamellar_armor,               itm.leather_boots,          itm.mail_boots,                      itm.vaegir_noble_helmet, itm.lamellar_gauntlets,         itm.bastard_sword_b,   itm.tab_shield_kite_cav_b],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c2f0832c748f272540d8ab65900000000001d34e60000000000000000, vaegir_face_older_2],
  ["knight_2_5", "Boyar Doru", "Doru", tf_hero, 0, reserved,  fac.kingdom_2, [itm.warhorse_steppe,            itm.rich_outfit,        itm.haubergeon,                     itm.leather_boots,          itm.mail_chausses,                   itm.vaegir_noble_helmet, itm.scale_gauntlets,   itm.bastard_sword_b,   itm.tab_shield_kite_d],       knight_attrib_5,wp(250),knight_skills_5, 0x0000000e310061435d76bb5f55bad9ad00000000001ed8ec0000000000000000, vaegir_face_older_2],
  ["knight_2_6", "Boyar Belgaru", "Belgaru", tf_hero, 0, reserved,  fac.kingdom_2, [itm.saddle_horse,      itm.nomad_vest,      itm.vaegir_elite_armor,                   itm.woolen_hose,            itm.mail_chausses,                   itm.vaegir_lamellar_helmet,  itm.mail_mittens,          itm.sword_viking_3,           itm.tab_shield_kite_c],   knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a0100421038da7157aa4e430a00000000001da8bc0000000000000000, vaegir_face_middle_2],
  ["knight_2_7", "Boyar Ralcha", "Ralcha", tf_hero, 0, reserved,  fac.kingdom_2, [itm.steppe_horse,      itm.leather_jacket,     itm.mail_hauberk,                   itm.leather_boots,          itm.mail_boots,                      itm.vaegir_noble_helmet,  itm.lamellar_gauntlets,          itm.great_bardiche,    itm.tab_shield_kite_cav_a],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c04100153335ba9390b2d277500000000001d89120000000000000000, vaegir_face_old_2],
  ["knight_2_8", "Boyar Vlan", "Vlan", tf_hero, 0, reserved,  fac.kingdom_2, [itm.hunter,            itm.nomad_robe,             itm.nomad_vest,                     itm.woolen_hose,            itm.mail_chausses,                   itm.vaegir_noble_helmet, itm.lamellar_gauntlets,       itm.shortened_military_scythe,    itm.tab_shield_kite_d],    knight_attrib_3,wp(200),knight_skills_3|knows_trainer_5, 0x0000000c00046581234e8da2cdd248db00000000001f569c0000000000000000, vaegir_face_older_2],
  ["knight_2_9", "Boyar Mleza", "Mleza", tf_hero, 0, reserved,  fac.kingdom_2, [itm.saddle_horse,      itm.rich_outfit,        itm.vaegir_elite_armor,                     itm.leather_boots,          itm.mail_chausses,                   itm.vaegir_lamellar_helmet,  itm.lamellar_gauntlets,        itm.great_bardiche,   itm.tab_shield_kite_d],    knight_attrib_4,wp(230),knight_skills_4, 0x0000000c160451d2136469c4d9b159ad00000000001e28f10000000000000000, vaegir_face_older_2],
  ["knight_2_10", "Boyar Nelag", "Nelag", tf_hero, 0, reserved,  fac.kingdom_2, [itm.warhorse_steppe,          itm.fur_coat,        itm.lamellar_armor,               itm.woolen_hose,            itm.mail_boots,                      itm.vaegir_noble_helmet,  itm.scale_gauntlets,      itm.military_pick,   itm.tab_shield_kite_cav_b],      knight_attrib_5,wp(260),knight_skills_5|knows_trainer_6, 0x0000000f7c00520e66b76edd5cd5eb6e00000000001f691e0000000000000000, vaegir_face_older_2],
  ["knight_2_11", "Boyar Crahask", "Crahask", tf_hero, 0, reserved,  fac.kingdom_2, [itm.saddle_horse,      itm.leather_jacket,     itm.vaegir_elite_armor,                   itm.nomad_boots,            itm.splinted_leather_greaves,        itm.vaegir_noble_helmet, itm.scale_gauntlets,           itm.sword_viking_3,           itm.tab_shield_kite_cav_a],    knight_attrib_1,wp(130),knight_skills_1, 0x0000000c1d0821d236acd6991b74d69d00000000001e476c0000000000000000, vaegir_face_middle_2],
  ["knight_2_12", "Boyar Bracha", "Bracha", tf_hero, 0, reserved,  fac.kingdom_2, [itm.saddle_horse,      itm.rich_outfit,        itm.lamellar_armor,               itm.woolen_hose,            itm.mail_chausses,                   itm.vaegir_noble_helmet,  itm.mail_mittens,      itm.great_bardiche,    itm.tab_shield_kite_cav_a],    knight_attrib_2,wp(170),knight_skills_2, 0x0000000c0f04024b2509d5d53944c6a300000000001d5b320000000000000000, vaegir_face_old_2],
  ["knight_2_13", "Boyar Druli", "Druli", tf_hero, 0, reserved,  fac.kingdom_2, [itm.hunter,            itm.short_tunic,        itm.mail_hauberk,                   itm.woolen_hose,            itm.mail_chausses,                   itm.vaegir_lamellar_helmet,  itm.lamellar_gauntlets,          itm.great_bardiche,           itm.tab_shield_kite_cav_b],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000c680432d3392230cb926d56ca00000000001da69b0000000000000000, vaegir_face_older_2],
  ["knight_2_14", "Boyar Marmun", "Marmun", tf_hero, 0, reserved,  fac.kingdom_2, [itm.saddle_horse,      itm.courtly_outfit,     itm.lamellar_armor,               itm.leather_boots,          itm.mail_boots,                      itm.vaegir_noble_helmet,  itm.lamellar_gauntlets,        itm.shortened_military_scythe,   itm.tab_shield_kite_cav_b],    knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x0000000c27046000471bd2e93375b52c00000000001dd5220000000000000000, vaegir_face_older_2],
  ["knight_2_15", "Boyar Gastya", "Gastya", tf_hero, 0, reserved,  fac.kingdom_2, [itm.hunter,            itm.rich_outfit,        itm.haubergeon,                     itm.leather_boots,          itm.mail_chausses,                   itm.vaegir_lamellar_helmet, itm.lamellar_gauntlets,   itm.bastard_sword_b,  itm.shortened_military_scythe, itm.tab_shield_kite_cav_b],       knight_attrib_5,wp(250),knight_skills_5, 0x0000000de50052123b6bb36de5d6eb7400000000001dd72c0000000000000000, vaegir_face_older_2],
  ["knight_2_16", "Boyar Harish", "Harish", tf_hero, 0, reserved,  fac.kingdom_2, [itm.saddle_horse,      itm.nomad_vest,      itm.vaegir_elite_armor,                   itm.woolen_hose,            itm.mail_chausses,                   itm.vaegir_noble_helmet,  itm.mail_mittens,          itm.great_bardiche,           itm.tab_shield_kite_c],   knight_attrib_1,wp(120),knight_skills_1, 0x000000085f00000539233512e287391d00000000001db7200000000000000000, vaegir_face_middle_2],
  ["knight_2_17", "Boyar Taisa", "Taisa", tf_hero, 0, reserved,  fac.kingdom_2, [itm.steppe_horse,      itm.leather_jacket,     itm.mail_hauberk,                   itm.leather_boots,          itm.mail_boots,                      itm.vaegir_noble_helmet,   itm.scale_gauntlets,         itm.great_bardiche,    itm.tab_shield_kite_cav_a],     knight_attrib_2,wp(150),knight_skills_2, 0x0000000a070c4387374bd19addd2a4ab00000000001e32cc0000000000000000, vaegir_face_old_2],
  ["knight_2_18", "Boyar Valishin", "Valishin", tf_hero, 0, reserved,  fac.kingdom_2, [itm.hunter,            itm.nomad_robe,             itm.nomad_vest,                     itm.woolen_hose,            itm.mail_chausses,                   itm.vaegir_lamellar_helmet,  itm.lamellar_gauntlets,      itm.great_bardiche,    itm.tab_shield_kite_cav_a],    knight_attrib_3,wp(180),knight_skills_3, 0x0000000b670012c23d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_older_2],
  ["knight_2_19", "Boyar Rudin", "Rudin", tf_hero, 0, reserved,  fac.kingdom_2, [itm.saddle_horse,      itm.rich_outfit,        itm.vaegir_elite_armor,                     itm.leather_boots,          itm.mail_chausses,                   itm.vaegir_noble_helmet, itm.scale_gauntlets,         itm.fighting_pick,  itm.shortened_military_scythe, itm.tab_shield_kite_d],    knight_attrib_4,wp(210),knight_skills_4|knows_trainer_4, 0x0000000e070050853b0a6e4994ae272a00000000001db4e10000000000000000, vaegir_face_older_2],
  ["knight_2_20", "Boyar Kumipa", "Kumipa", tf_hero, 0, reserved,  fac.kingdom_2, [itm.warhorse_steppe,          itm.fur_coat,        itm.lamellar_armor,               itm.woolen_hose,            itm.mail_boots,                      itm.vaegir_lamellar_helmet,  itm.lamellar_gauntlets,      itm.great_bardiche,   itm.tab_shield_kite_cav_b],      knight_attrib_5,wp(240),knight_skills_5|knows_trainer_5, 0x0000000f800021c63b0a6e4994ae272a00000000001db4e10000000000000000, vaegir_face_older_2],

  ["knight_3_1", "Alagur Noyan", "Alagur", tf_hero, 0, reserved,  fac.kingdom_3, [itm.courser, itm.leather_vest,  itm.studded_leather_coat,itm.nomad_boots,  itm.mail_boots, itm.khergit_guard_helmet, itm.lamellar_gauntlets, itm.leather_gloves,  itm.sword_khergit_3, itm.tab_shield_small_round_c, itm.khergit_bow, itm.arrows],  knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3|knows_power_draw_4, 0x000000043000318b54b246b7094dc39c00000000001d31270000000000000000, khergit_face_middle_2],
  ["knight_3_2", "Tonju Noyan",  "Tonju", tf_hero, 0, reserved,  fac.kingdom_3, [itm.courser, itm.nomad_vest,   itm.lamellar_armor, itm.hide_boots,  itm.mail_boots, itm.khergit_cavalry_helmet, itm.lamellar_gauntlets, itm.leather_gloves, itm.khergit_sword_two_handed_b,  itm.tab_shield_small_round_b, itm.khergit_bow, itm.arrows], knight_attrib_2,wp(160),knight_skills_2|knows_power_draw_4, 0x0000000c280461004929b334ad632aa200000000001e05120000000000000000, khergit_face_old_2],
  ["knight_3_3", "Belir Noyan",  "Belir", tf_hero, 0, reserved,  fac.kingdom_3, [itm.courser, itm.nomad_robe, itm.lamellar_armor,itm.nomad_boots,  itm.splinted_leather_greaves,  itm.khergit_guard_helmet, itm.lamellar_gauntlets, itm.fighting_pick,  itm.tab_shield_small_round_c, itm.khergit_bow, itm.arrows],  knight_attrib_3,wp(190),knight_skills_3|knows_trainer_5|knows_power_draw_4, 0x0000000e880062c53b0a6e4994ae272a00000000001db4e10000000000000000, khergit_face_older_2],
  ["knight_3_4", "Asugan Noyan", "Asugan", tf_hero, 0, reserved,  fac.kingdom_3, [itm.courser, itm.lamellar_vest_khergit,  itm.khergit_elite_armor, itm.hide_boots,  itm.splinted_greaves,   itm.khergit_cavalry_helmet, itm.lamellar_gauntlets, itm.khergit_sword_two_handed_b, itm.lance,  itm.tab_shield_small_round_c],  knight_attrib_4,wp(220),knight_skills_4|knows_power_draw_4, 0x0000000c23085386391b5ac72a96d95c00000000001e37230000000000000000, khergit_face_older_2],
  ["knight_3_5", "Brula Noyan",  "Brula", tf_hero, 0, reserved,  fac.kingdom_3, [itm.warhorse_steppe, itm.ragged_outfit,  itm.lamellar_vest_khergit, itm.hide_boots,  itm.mail_boots, itm.khergit_guard_helmet, itm.lamellar_gauntlets, itm.sword_khergit_3, itm.lance, itm.tab_shield_small_round_c],  knight_attrib_5,wp(250),knight_skills_5|knows_power_draw_4, 0x0000000efe0051ca4b377b4964b6eb6500000000001f696c0000000000000000, khergit_face_older_2],
  ["knight_3_6", "Imirza Noyan", "Imirza", tf_hero, 0, reserved,  fac.kingdom_3, [itm.courser, itm.tribal_warrior_outfit,itm.hide_boots, itm.splinted_leather_greaves,  itm.khergit_cavalry_helmet,  itm.lamellar_gauntlets, itm.sword_khergit_4,itm.lance,  itm.tab_shield_small_round_b], knight_attrib_1,wp(130),knight_skills_1|knows_power_draw_4, 0x00000006f600418b54b246b7094dc31a00000000001d37270000000000000000, khergit_face_middle_2],
  ["knight_3_7", "Urumuda Noyan","Urumuda", tf_hero, 0, reserved,  fac.kingdom_3, [itm.courser,  itm.leather_vest,itm.leather_boots, itm.hide_boots, itm.skullcap, itm.khergit_guard_helmet, itm.lamellar_gauntlets,  itm.sword_khergit_3, itm.tab_shield_small_round_b], knight_attrib_2,wp(160),knight_skills_2|knows_power_draw_4, 0x0000000bdd00510a44be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_old_2],
  ["knight_3_8", "Kramuk Noyan", "Kramuk", tf_hero, 0, reserved,  fac.kingdom_3, [itm.courser,  itm.nomad_vest, itm.lamellar_armor, itm.woolen_hose, itm.splinted_greaves, itm.khergit_cavalry_helmet, itm.lamellar_gauntlets,   itm.great_bardiche,  itm.tab_shield_small_round_c],  knight_attrib_3,wp(190),knight_skills_3|knows_power_draw_4, 0x0000000abc00518b5af4ab4b9c8e596400000000001dc76d0000000000000000, khergit_face_older_2],
  ["knight_3_9", "Chaurka Noyan","Chaurka", tf_hero, 0, reserved,  fac.kingdom_3, [itm.hunter,  itm.nomad_robe, itm.lamellar_vest_khergit,  itm.leather_boots, itm.splinted_leather_greaves,  itm.khergit_guard_helmet, itm.lamellar_gauntlets,  itm.khergit_sword_two_handed_b,  itm.tab_shield_small_round_c],  knight_attrib_4,wp(220),knight_skills_4|knows_power_draw_4, 0x0000000a180441c921a30ea68b54971500000000001e54db0000000000000000, khergit_face_older_2],
  ["knight_3_10", "Sebula Noyan","Sebula", tf_hero, 0, reserved,  fac.kingdom_3, [itm.warhorse_steppe,  itm.lamellar_vest_khergit, itm.lamellar_armor, itm.hide_boots, itm.mail_chausses,  itm.khergit_guard_helmet, itm.lamellar_gauntlets,  itm.sword_khergit_4, itm.khergit_sword_two_handed_b,  itm.tab_shield_small_round_c], knight_attrib_5,wp(250),knight_skills_5|knows_trainer_6|knows_power_draw_4, 0x0000000a3b00418c5b36c686d920a76100000000001c436f0000000000000000, khergit_face_older_2],
  ["knight_3_11", "Tulug Noyan", "Tulug", tf_hero, 0, reserved,  fac.kingdom_3, [itm.courser, itm.leather_vest, itm.studded_leather_coat, itm.nomad_boots, itm.mail_boots,  itm.khergit_cavalry_helmet,  itm.leather_gloves, itm.sword_khergit_4,  itm.tab_shield_small_round_b, itm.khergit_bow, itm.arrows],  knight_attrib_1,wp(150),knight_skills_1|knows_power_draw_4, 0x00000007d100534b44962d14d370c65c00000000001ed6df0000000000000000, khergit_face_middle_2],
  ["knight_3_12", "Nasugei Noyan", "Nasugei", tf_hero, 0, reserved,  fac.kingdom_3, [itm.courser, itm.nomad_vest, itm.lamellar_armor, itm.hide_boots, itm.mail_boots,  itm.khergit_guard_helmet,  itm.leather_gloves, itm.sword_khergit_3,  itm.tab_shield_small_round_b], knight_attrib_2,wp(190),knight_skills_2|knows_power_draw_4, 0x0000000bf400610c5b33d3c9258edb6c00000000001eb96d0000000000000000, khergit_face_old_2],
  ["knight_3_13", "Urubay Noyan","Urubay", tf_hero, 0, reserved,  fac.kingdom_3, [itm.courser, itm.nomad_robe,  itm.lamellar_vest_khergit, itm.nomad_boots, itm.splinted_leather_greaves,  itm.khergit_cavalry_helmet, itm.lamellar_gauntlets, itm.fighting_pick,  itm.tab_shield_small_round_c, itm.khergit_bow, itm.arrows],  knight_attrib_3,wp(200),knight_skills_3|knows_trainer_3|knows_power_draw_4, 0x0000000bfd0061c65b6eb33b25d2591d00000000001f58eb0000000000000000, khergit_face_older_2],
  ["knight_3_14", "Hugu Noyan",  "Hugu", tf_hero, 0, reserved,  fac.kingdom_3, [itm.courser,  itm.lamellar_vest_khergit, itm.hide_boots, itm.splinted_greaves, itm.khergit_guard_helmet, itm.lamellar_gauntlets, itm.shortened_military_scythe,  itm.tab_shield_small_round_c, itm.khergit_bow, itm.arrows],  knight_attrib_4,wp(300),knight_skills_4|knows_trainer_6|knows_power_draw_4, 0x0000000b6900514144be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_older_2],
  ["knight_3_15", "Tansugai Noyan", "Tansugai", tf_hero, 0, reserved,  fac.kingdom_3, [itm.warhorse_steppe,   itm.ragged_outfit, itm.lamellar_vest_khergit, itm.hide_boots, itm.mail_boots,  itm.khergit_cavalry_helmet, itm.sword_khergit_4, itm.khergit_sword_two_handed_b, itm.tab_shield_small_round_c],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_4|knows_power_draw_4, 0x0000000c360c524b6454465b59b9d93500000000001ea4860000000000000000, khergit_face_older_2],
  ["knight_3_16", "Tirida Noyan","Tirida", tf_hero, 0, reserved,  fac.kingdom_3, [itm.courser, itm.tribal_warrior_outfit,  itm.khergit_elite_armor,  itm.hide_boots,  itm.splinted_leather_greaves,  itm.khergit_guard_helmet, itm.leather_gloves,   itm.khergit_sword_two_handed_a,  itm.lance, itm.tab_shield_small_round_b, itm.khergit_bow, itm.arrows],  knight_attrib_1,wp(120),knight_skills_1|knows_power_draw_4, 0x0000000c350c418438ab85b75c61b8d300000000001d21530000000000000000, khergit_face_middle_2],
  ["knight_3_17", "Ulusamai Noyan", "Ulusamai", tf_hero, 0, reserved,  fac.kingdom_3, [itm.courser,  itm.leather_vest, itm.lamellar_vest_khergit, itm.leather_boots, itm.mail_boots, itm.khergit_guard_helmet, itm.leather_gloves,   itm.great_bardiche, itm.tab_shield_small_round_c, itm.khergit_bow, itm.arrows],  knight_attrib_2,wp(150),knight_skills_2|knows_power_draw_4, 0x0000000c3c0821c647264ab6e68dc4d500000000001e42590000000000000000, khergit_face_old_2],
  ["knight_3_18", "Karaban Noyan", "Karaban", tf_hero, 0, reserved,  fac.kingdom_3, [itm.courser,   itm.nomad_vest, itm.khergit_elite_armor, itm.hide_boots, itm.splinted_greaves,  itm.khergit_guard_helmet, itm.scale_gauntlets,   itm.war_axe, itm.tab_shield_small_round_c, itm.lance,  itm.khergit_bow, itm.arrows],   knight_attrib_3,wp(180),knight_skills_3|knows_trainer_4|knows_power_draw_4, 0x0000000c0810500347ae7acd0d3ad74a00000000001e289a0000000000000000, khergit_face_older_2],
  ["knight_3_19", "Akadan Noyan","Akadan", tf_hero, 0, reserved,  fac.kingdom_3, [itm.hunter,   itm.nomad_robe, itm.lamellar_vest_khergit, itm.leather_boots, itm.splinted_leather_greaves,  itm.khergit_cavalry_helmet, itm.lamellar_gauntlets, itm.sword_khergit_4, itm.shortened_military_scythe, itm.tab_shield_small_round_c],  knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5|knows_power_draw_4, 0x0000000c1500510528f50d52d20b152300000000001d66db0000000000000000, khergit_face_older_2],
  ["knight_3_20", "Dundush Noyan","Dundush", tf_hero, 0, reserved,  fac.kingdom_3, [itm.warhorse_steppe, itm.lamellar_vest, itm.khergit_elite_armor, itm.hide_boots, itm.mail_chausses, itm.khergit_guard_helmet, itm.scale_gauntlets, itm.khergit_sword_two_handed_a, itm.tab_shield_small_round_c, itm.lance, itm.khergit_bow, itm.arrows],  knight_attrib_5,wp(240),knight_skills_5|knows_power_draw_4, 0x0000000f7800620d66b76edd5cd5eb6e00000000001f691e0000000000000000, khergit_face_older_2],

  ["knight_4_1", "Jarl Aedin", "Aedin", tf_hero, 0, reserved,  fac.kingdom_4, [itm.rich_outfit,  itm.banded_armor,   itm.woolen_hose,  itm.mail_boots,  itm.nordic_huscarl_helmet, itm.mail_mittens, itm.great_axe, itm.tab_shield_round_d, itm.throwing_axes], knight_attrib_1,wp(130),knight_skills_1, 0x0000000c13002254340eb1d91159392d00000000001eb75a0000000000000000, nord_face_middle_2],
  ["knight_4_2", "Jarl Irya", "Irya", tf_hero, 0, reserved,  fac.kingdom_4, [ itm.short_tunic,  itm.banded_armor, itm.blue_hose,  itm.splinted_greaves,  itm.nordic_warlord_helmet, itm.scale_gauntlets, itm.one_handed_battle_axe_c,  itm.tab_shield_round_d, itm.throwing_axes],  knight_attrib_2,wp(160),knight_skills_2|knows_trainer_3, 0x0000000c1610218368e29744e9a5985b00000000001db2a10000000000000000, nord_face_old_2],
  ["knight_4_3", "Jarl Olaf", "Olaf", tf_hero, 0, reserved,  fac.kingdom_4, [itm.warhorse, itm.rich_outfit,  itm.heraldic_mail_with_tabard,   itm.nomad_boots,  itm.mail_chausses, itm.scale_gauntlets,   itm.nordic_warlord_helmet,   itm.great_axe, itm.tab_shield_round_e, itm.throwing_axes],  knight_attrib_3,wp(190),knight_skills_3, 0x0000000c03040289245a314b744b30a400000000001eb2a90000000000000000, nord_face_older_2],
  ["knight_4_4", "Jarl Reamald", "Reamald", tf_hero, 0, reserved,  fac.kingdom_4, [itm.hunter,   itm.leather_vest,   itm.banded_armor,   itm.woolen_hose,  itm.mail_boots, itm.scale_gauntlets,  itm.nordic_huscarl_helmet, itm.fighting_pick, itm.tab_shield_round_e, itm.throwing_axes],  knight_attrib_4,wp(210),knight_skills_4, 0x0000000c3f1001ca3d6955b26a8939a300000000001e39b60000000000000000, nord_face_older_2],
  ["knight_4_5", "Jarl Turya", "Turya", tf_hero, 0, reserved,  fac.kingdom_4, [  itm.fur_coat,   itm.heraldic_mail_with_surcoat,   itm.leather_boots,  itm.splinted_leather_greaves,  itm.scale_gauntlets, itm.nordic_huscarl_helmet, itm.bastard_sword_b, itm.tab_shield_round_e, itm.throwing_axes, itm.throwing_axes], knight_attrib_5,wp(250),knight_skills_5, 0x0000000ff508330546dc4a59422d450c00000000001e51340000000000000000, nord_face_older_2],
  ["knight_4_6", "Jarl Gundur", "Gundur", tf_hero, 0, reserved,  fac.kingdom_4, [   itm.nomad_robe,   itm.banded_armor,  itm.nomad_boots,  itm.mail_chausses,   itm.nordic_warlord_helmet, itm.mail_mittens,   itm.war_axe, itm.tab_shield_round_d],   knight_attrib_1,wp(130),knight_skills_1, 0x00000005b00011813d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_middle_2],
  ["knight_4_7", "Jarl Harald", "Harald", tf_hero, 0, reserved,  fac.kingdom_4, [  itm.fur_coat,   itm.studded_leather_coat,   itm.nomad_boots,  itm.mail_boots,  itm.nordic_warlord_helmet, itm.mail_mittens,   itm.sword_viking_3, itm.shortened_military_scythe,  itm.tab_shield_round_d],   knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x00000006690002873d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_old_2],
  ["knight_4_8", "Jarl Knudarr", "Knudarr", tf_hero, 0, reserved,  fac.kingdom_4, [ itm.rich_outfit,  itm.mail_and_plate,   itm.woolen_hose,  itm.mail_chausses,   itm.segmented_helmet, itm.scale_gauntlets, itm.war_axe,  itm.tab_shield_round_e, itm.throwing_axes],   knight_attrib_3,wp(190),knight_skills_3, 0x0000000f830051c53b026e4994ae272a00000000001db4e10000000000000000, nord_face_older_2],
  ["knight_4_9", "Jarl Haeda", "Haeda", tf_hero, 0, reserved,  fac.kingdom_4, [itm.warhorse, itm.nomad_robe,   itm.haubergeon, itm.blue_hose,  itm.mail_boots,  itm.guard_helmet, itm.scale_gauntlets, itm.arrows, itm.long_bow,   itm.one_handed_battle_axe_c,  itm.tab_shield_round_e],  knight_attrib_4,wp(220),knight_skills_4|knows_trainer_5|knows_power_draw_4, 0x00000000080c54c1345bd21349b1b67300000000001c90c80000000000000000, nord_face_older_2],
  ["knight_4_10", "Jarl Turegor", "Turegor", tf_hero, 0, reserved,  fac.kingdom_4, [itm.hunter,   itm.courtly_outfit,   itm.coat_of_plates,   itm.nomad_boots,  itm.splinted_greaves, itm.scale_gauntlets,  itm.winged_great_helmet,itm.great_axe, itm.tab_shield_round_e],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_6, 0x000000084b0002063d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_older_2],
  ["knight_4_11", "Jarl Logarson", "Logarson", tf_hero, 0, reserved,  fac.kingdom_4, [ itm.rich_outfit,  itm.banded_armor,   itm.woolen_hose,  itm.mail_boots,  itm.nordic_helmet,  itm.mail_mittens,  itm.great_bardiche, itm.tab_shield_round_d], knight_attrib_1,wp(140),knight_skills_1, 0x000000002d100005471d4ae69ccacb1d00000000001dca550000000000000000, nord_face_middle_2],
  ["knight_4_12", "Jarl Aeric", "Aeric", tf_hero, 0, reserved,  fac.kingdom_4, [ itm.short_tunic,  itm.banded_armor, itm.blue_hose,  itm.splinted_greaves,  itm.nordic_huscarl_helmet,  itm.mail_mittens,  itm.one_handed_battle_axe_c,  itm.tab_shield_round_d],  knight_attrib_2,wp(200),knight_skills_2, 0x0000000b9500020824936cc51cb5bb2500000000001dd4d80000000000000000, nord_face_old_2],
  ["knight_4_13", "Jarl Faarn", "Faarn", tf_hero, 0, reserved,  fac.kingdom_4, [itm.warhorse, itm.rich_outfit,  itm.heraldic_mail_with_tabard,   itm.nomad_boots,  itm.mail_chausses, itm.scale_gauntlets,   itm.nordic_warlord_helmet,   itm.war_axe, itm.tab_shield_round_e],  knight_attrib_3,wp(250),knight_skills_3|knows_trainer_3, 0x0000000a300012c439233512e287391d00000000001db7200000000000000000, nord_face_older_2],
  ["knight_4_14", "Jarl Bulba", "Bulba", tf_hero, 0, reserved,  fac.kingdom_4, [  itm.leather_vest,   itm.banded_armor,   itm.woolen_hose,  itm.mail_boots,  itm.nordic_helmet, itm.scale_gauntlets, itm.fighting_pick, itm.tab_shield_round_e, itm.throwing_axes],  knight_attrib_4,wp(200),knight_skills_4, 0x0000000c0700414f2cb6aa36ea50a69d00000000001dc55c0000000000000000, nord_face_older_2],
  ["knight_4_15", "Jarl Rayeck", "Rayeck", tf_hero, 0, reserved,  fac.kingdom_4, [itm.hunter,   itm.leather_jacket,   itm.heraldic_mail_with_tabard,   itm.leather_boots, itm.scale_gauntlets,  itm.splinted_leather_greaves,  itm.nordic_huscarl_helmet, itm.shortened_military_scythe, itm.tab_shield_round_e], knight_attrib_5,wp(290),knight_skills_5|knows_trainer_6, 0x0000000d920801831715d1aa9221372300000000001ec6630000000000000000, nord_face_older_2],
  ["knight_4_16", "Jarl Dirigun", "Dirigun", tf_hero, 0, reserved,  fac.kingdom_4, [   itm.nomad_robe,   itm.banded_armor,  itm.nomad_boots,  itm.mail_chausses,   itm.nordic_huscarl_helmet, itm.mail_mittens,   itm.war_axe, itm.tab_shield_round_d, itm.throwing_axes],   knight_attrib_1,wp(120),knight_skills_1, 0x000000099700124239233512e287391d00000000001db7200000000000000000, nord_face_middle_2],
  ["knight_4_17", "Jarl Marayirr", "Marayirr", tf_hero, 0, reserved,  fac.kingdom_4, [  itm.fur_coat,   itm.banded_armor,   itm.nomad_boots,  itm.mail_boots,  itm.nordic_warlord_helmet, itm.mail_mittens,   itm.sword_viking_3,  itm.tab_shield_round_d, itm.throwing_axes],   knight_attrib_2,wp(150),knight_skills_2|knows_trainer_4, 0x0000000c2f0442036d232a2324b5b81400000000001e55630000000000000000, nord_face_old_2],
  ["knight_4_18", "Jarl Gearth", "Gearth", tf_hero, 0, reserved,  fac.kingdom_4, [ itm.rich_outfit,  itm.mail_and_plate,   itm.woolen_hose,  itm.mail_chausses,   itm.segmented_helmet, itm.scale_gauntlets, itm.sword_viking_3, itm.shortened_military_scythe,  itm.tab_shield_round_d],   knight_attrib_3,wp(180),knight_skills_3, 0x0000000c0d00118866e22e3d9735a72600000000001eacad0000000000000000, nord_face_older_2],
  ["knight_4_19", "Jarl Surdun", "Surdun", tf_hero, 0, reserved,  fac.kingdom_4, [itm.warhorse, itm.nomad_robe,   itm.haubergeon, itm.blue_hose,  itm.mail_boots,  itm.guard_helmet, itm.scale_gauntlets,   itm.one_handed_battle_axe_c,  itm.tab_shield_round_e, itm.throwing_axes],  knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x0000000c0308225124e26d4a6295965a00000000001d23e40000000000000000, nord_face_older_2],
  ["knight_4_20", "Jarl Gerlad", "Gerlad", tf_hero, 0, reserved,  fac.kingdom_4, [itm.hunter,   itm.courtly_outfit,   itm.coat_of_plates,   itm.nomad_boots,  itm.splinted_greaves, itm.scale_gauntlets,  itm.winged_great_helmet,itm.great_axe, itm.tab_shield_round_e, itm.throwing_axes],  knight_attrib_5,wp(240),knight_skills_5, 0x0000000f630052813b6bb36de5d6eb7400000000001dd72c0000000000000000, nord_face_older_2],

  ["knight_5_1", "Count Matheas", "Matheas", tf_hero, 0, reserved,  fac.kingdom_5, [itm.saddle_horse,   itm.tabard,   itm.heraldic_mail_with_surcoat,       itm.leather_boots,    itm.mail_boots,    itm.guard_helmet, itm.leather_gloves,     itm.fighting_pick,   itm.tab_shield_heater_c],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_5_2", "Count Gutlans", "Gutlans", tf_hero, 0, reserved,  fac.kingdom_5, [itm.courser,    itm.red_gambeson,       itm.heraldic_mail_with_tabard,    itm.leather_boots,    itm.mail_boots,    itm.nasal_helmet, itm.leather_gloves,      itm.military_pick,  itm.sword_two_handed_a,   itm.tab_shield_heater_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_5_3", "Count Laruqen", "Laruqen", tf_hero, 0, reserved,  fac.kingdom_5, [itm.hunter,     itm.short_tunic,  itm.mail_and_plate,     itm.nomad_boots,      itm.splinted_leather_greaves,  itm.kettle_hat, itm.gauntlets, itm.shortened_military_scythe,  itm.tab_shield_heater_d],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_5_4", "Count Raichs", "Raichs", tf_hero, 0, reserved,  fac.kingdom_5, [itm.hunter,     itm.leather_jacket,     itm.brigandine_red,       itm.woolen_hose,      itm.splinted_greaves,    itm.flat_topped_helmet, itm.gauntlets, itm.bastard_sword_a,    itm.tab_shield_heater_d],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_5_5", "Count Reland", "Reland", tf_hero, 0, reserved,  fac.kingdom_5, [itm.hunter,     itm.rich_outfit,  itm.heraldic_mail_with_tabard,     itm.leather_boots,    itm.mail_boots,    itm.great_helmet, itm.gauntlets, itm.shortened_military_scythe,  itm.tab_shield_heater_d], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_5_6", "Count Tarchias", "Tarchias", tf_hero, 0, reserved,  fac.kingdom_5, [itm.sumpter_horse,    itm.ragged_outfit,      itm.heraldic_mail_with_tabard,       itm.woolen_hose,      itm.splinted_greaves, itm.gauntlets,   itm.skullcap,     itm.sword_two_handed_b,   itm.tab_shield_heater_c],    knight_attrib_1,wp(130),knight_skills_1, 0x000000001100000648d24d36cd964b1d00000000001e2dac0000000000000000, rhodok_face_middle_2],
  ["knight_5_7", "Count Gharmall", "Gharmall", tf_hero, 0, reserved,  fac.kingdom_5, [itm.saddle_horse,     itm.coarse_tunic,       itm.heraldic_mail_with_surcoat,   itm.leather_boots,    itm.mail_chausses,  itm.gauntlets,      itm.nasal_helmet,       itm.bastard_sword_a,    itm.tab_shield_heater_c],     knight_attrib_2,wp(160),knight_skills_2, 0x0000000c3a0455c443d46e4c8b91291a00000000001ca51b0000000000000000, rhodok_face_old_2],
  ["knight_5_8", "Count Talbar", "Talbar", tf_hero, 0, reserved,  fac.kingdom_5, [itm.saddle_horse, itm.courtly_outfit,     itm.heraldic_mail_with_tabard,    itm.woolen_hose,      itm.mail_boots,    itm.nasal_helmet,  itm.gauntlets,      itm.military_pick, itm.sword_two_handed_b,  itm.tab_shield_heater_c],    knight_attrib_3,wp(190),knight_skills_3|knows_trainer_3, 0x0000000c2c0844d42914d19b2369b4ea00000000001e331b0000000000000000, rhodok_face_older_2],
  ["knight_5_9", "Count Rimusk", "Rimusk", tf_hero, 0, reserved,  fac.kingdom_5, [itm.warhorse,     itm.leather_jacket,     itm.heraldic_mail_with_tabard,   itm.leather_boots,    itm.splinted_leather_greaves,       itm.kettle_hat, itm.gauntlets,   itm.great_bardiche,   itm.tab_shield_heater_d],   knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x00000000420430c32331b5551c4724a100000000001e39a40000000000000000, rhodok_face_older_2],
  ["knight_5_10", "Count Falsevor", "Falsevor", tf_hero, 0, reserved,  fac.kingdom_5, [itm.warhorse,     itm.rich_outfit,  itm.heraldic_mail_with_tabard,     itm.blue_hose,  itm.mail_chausses,       itm.great_helmet, itm.gauntlets,       itm.bastard_sword_a,   itm.tab_shield_heater_d],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_4, 0x00000008e20011063d9b6d4a92ada53500000000001cc1180000000000000000, rhodok_face_older_2],
  ["knight_5_11", "Count Etrosq", "Etrosq", tf_hero, 0, reserved,  fac.kingdom_5, [itm.saddle_horse,     itm.tabard,       itm.heraldic_mail_with_surcoat,       itm.leather_boots,    itm.mail_boots,    itm.skullcap,  itm.leather_gloves,    itm.fighting_pick,   itm.tab_shield_heater_c],     knight_attrib_1,wp(130),knight_skills_1, 0x0000000c170c14874752adb6eb3228d500000000001c955c0000000000000000, rhodok_face_middle_2],
  ["knight_5_12", "Count Kurnias", "Kurnias", tf_hero, 0, reserved,  fac.kingdom_5, [itm.courser,    itm.red_gambeson,       itm.heraldic_mail_with_tabard,    itm.leather_boots,    itm.mail_boots,    itm.nasal_helmet,  itm.leather_gloves,      itm.military_pick,   itm.tab_shield_heater_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_5, 0x0000000c080c13d056ec8da85e3126ed00000000001d4ce60000000000000000, rhodok_face_old_2],
  ["knight_5_13", "Count Tellrog", "Tellrog", tf_hero, 0, reserved,  fac.kingdom_5, [itm.hunter,     itm.short_tunic,  itm.mail_and_plate,     itm.nomad_boots,      itm.splinted_leather_greaves,  itm.winged_great_helmet, itm.gauntlets,       itm.sword_two_handed_a,  itm.tab_shield_heater_d],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000cbf10100562a4954ae731588a00000000001d6b530000000000000000, rhodok_face_older_2],
  ["knight_5_14", "Count Tribidan", "Tribidan", tf_hero, 0, reserved,  fac.kingdom_5, [itm.hunter,     itm.leather_jacket,     itm.brigandine_red,       itm.woolen_hose,      itm.splinted_greaves,    itm.flat_topped_helmet, itm.gauntlets, itm.bastard_sword_a,    itm.tab_shield_heater_d],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c330805823baa77556c4e331a00000000001cb9110000000000000000, rhodok_face_older_2],
  ["knight_5_15", "Count Gerluchs", "Gerluchs", tf_hero, 0, reserved,  fac.kingdom_5, [itm.hunter,     itm.rich_outfit,  itm.heraldic_mail_with_tabard,     itm.leather_boots,    itm.mail_boots,    itm.great_helmet, itm.gauntlets,       itm.sword_two_handed_a,  itm.tab_shield_heater_d], knight_attrib_5,wp(250),knight_skills_5, 0x0000000d51000106370c4d4732b536de00000000001db9280000000000000000, rhodok_face_older_2],
  ["knight_5_16", "Count Fudreim", "Fudreim", tf_hero, 0, reserved,  fac.kingdom_5, [itm.sumpter_horse,    itm.ragged_outfit,      itm.heraldic_mail_with_tabard,       itm.woolen_hose,      itm.splinted_greaves,    itm.guard_helmet, itm.leather_gloves,     itm.fighting_pick,   itm.tab_shield_heater_c],    knight_attrib_1,wp(120),knight_skills_1, 0x0000000c06046151435b5122a37756a400000000001c46e50000000000000000, rhodok_face_middle_2],
  ["knight_5_17", "Count Nealcha", "Nealcha", tf_hero, 0, reserved,  fac.kingdom_5, [itm.saddle_horse,     itm.coarse_tunic,       itm.heraldic_mail_with_surcoat,   itm.leather_boots,    itm.mail_chausses,       itm.nasal_helmet,  itm.leather_gloves,      itm.bastard_sword_a,    itm.tab_shield_heater_c],     knight_attrib_2,wp(150),knight_skills_2, 0x0000000c081001d3465c89a6a452356300000000001cda550000000000000000, rhodok_face_old_2],
  ["knight_5_18", "Count Fraichin", "Fraichin", tf_hero, 0, reserved,  fac.kingdom_5, [itm.saddle_horse, itm.courtly_outfit,     itm.heraldic_mail_with_tabard,    itm.woolen_hose,      itm.mail_boots,    itm.nasal_helmet, itm.gauntlets,       itm.military_pick,   itm.tab_shield_heater_d],    knight_attrib_3,wp(180),knight_skills_3, 0x0000000a3d0c13c3452aa967276dc95c00000000001dad350000000000000000, rhodok_face_older_2],
  ["knight_5_19", "Count Trimbau", "Trimbau", tf_hero, 0, reserved,  fac.kingdom_5, [itm.warhorse,     itm.leather_jacket,     itm.heraldic_mail_with_tabard,   itm.leather_boots,    itm.splinted_leather_greaves,       itm.kettle_hat, itm.gauntlets,   itm.fighting_pick,  itm.sword_two_handed_a, itm.tab_shield_heater_d],   knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x0000000038043194092ab4b2d9adb44c00000000001e072c0000000000000000, rhodok_face_older_2],
  ["knight_5_20", "Count Reichsin", "Reichsin", tf_hero, 0, reserved,  fac.kingdom_5, [itm.warhorse,     itm.rich_outfit,  itm.heraldic_mail_with_tabard,     itm.blue_hose,  itm.mail_chausses,       itm.great_helmet, itm.gauntlets,       itm.bastard_sword_b,   itm.tab_shield_heater_d],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_6, 0x000000003600420515a865b45c64d64c00000000001d544b0000000000000000, rhodok_face_older_2],

  ["knight_6_1", "Emir Uqais", "Uqais", tf_hero, 0, reserved,  fac.kingdom_6, [itm.arabian_horse_a,   itm.mamluke_mail,          itm.sarranid_boots_c,    itm.mail_boots,    itm.sarranid_warrior_cap, itm.leather_gloves,    itm.heavy_lance, itm.sarranid_cavalry_sword,   itm.tab_shield_small_round_c],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x00000000600c7084486195383349eae500000000001d16a30000000000000000, sarranid_face_middle_2],
  ["knight_6_2", "Emir Hamezan", "Hamezan", tf_hero, 0, reserved,  fac.kingdom_6, [itm.arabian_horse_b,    itm.sarranid_elite_armor,       itm.sarranid_boots_c,    itm.mail_boots,    itm.sarranid_warrior_cap, itm.leather_gloves,   itm.lance,   itm.military_pick,  itm.sword_two_handed_a,   itm.tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x00000001380875d444cb68b92b8d3b1d00000000001dd71e0000000000000000, sarranid_face_old_2],
  ["knight_6_3", "Emir Atis", "Atis", tf_hero, 0, reserved,  fac.kingdom_6, [itm.arabian_horse_a,     itm.mamluke_mail,       itm.nomad_boots,      itm.sarranid_warrior_cap,  itm.shortened_military_scythe, itm.lamellar_gauntlets,  itm.tab_shield_small_round_c],    knight_attrib_3,wp(190),knight_skills_3, 0x000000002208728579723147247ad4e500000000001f14d40000000000000000, sarranid_face_older_2],
  ["knight_6_4", "Emir Nuwas", "Nuwas", tf_hero, 0, reserved,  fac.kingdom_6, [itm.hunter,     itm.sarranid_mail_shirt,            itm.sarranid_boots_c,          itm.sarranid_mail_coif,  itm.sarranid_cavalry_sword, itm.lamellar_gauntlets, itm.lance,   itm.tab_shield_small_round_c],    knight_attrib_4,wp(220),knight_skills_4, 0x00000009bf087285050caa7d285be51a00000000001d11010000000000000000, sarranid_face_older_2],
  ["knight_6_5", "Emir Mundhalir", "Mundhalir", tf_hero, 0, reserved,  fac.kingdom_6, [itm.arabian_horse_b,     itm.sarranid_cavalry_robe,       itm.sarranid_boots_c,    itm.sarranid_veiled_helmet,  itm.shortened_military_scythe,  itm.tab_shield_small_round_c], knight_attrib_5,wp(250),knight_skills_5, 0x000000002a087003330175aae175da9c00000000001e02150000000000000000, sarranid_face_older_2],
  ["knight_6_6", "Emir Ghanawa", "Ghanawa", tf_hero, 0, reserved,  fac.kingdom_6, [itm.arabian_horse_a,    itm.sarranid_elite_armor,            itm.sarranid_boots_c,      itm.splinted_greaves,    itm.sarranid_helmet1, itm.lance,      itm.sarranid_cavalry_sword,   itm.tab_shield_small_round_c],    knight_attrib_1,wp(130),knight_skills_1, 0x00000001830073834733294c89b128e200000000001259510000000000000000, sarranid_face_middle_2],
  ["knight_6_7", "Emir Nuam", "Nuam", tf_hero, 0, reserved,  fac.kingdom_6, [itm.arabian_horse_b,     itm.sarranid_mail_shirt,          itm.sarranid_boots_c,          itm.sarranid_mail_coif,       itm.sarranid_cavalry_sword,  itm.lamellar_gauntlets,  itm.tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2, 0x0000000cbf10734020504bbbda9135d500000000001f62380000000000000000, sarranid_face_old_2],
  ["knight_6_8", "Emir Dhiyul", "Dhiyul", tf_hero, 0, reserved,  fac.kingdom_6, [itm.arabian_horse_a, itm.mamluke_mail,         itm.sarranid_boots_c,      itm.mail_boots,    itm.sarranid_helmet1,        itm.military_pick, itm.lance,  itm.sarranid_cavalry_sword,  itm.tab_shield_small_round_c],    knight_attrib_3,wp(190),knight_skills_3|knows_trainer_3, 0x0000000190047003336dcd3ca2cacae300000000001f47640000000000000000, sarranid_face_older_2],
  ["knight_6_9", "Emir Lakhem", "Lakhem", tf_hero, 0, reserved,  fac.kingdom_6, [itm.warhorse_sarranid,     itm.sarranid_mail_shirt,        itm.sarranid_boots_c,    itm.sarranid_helmet1, itm.lamellar_gauntlets,   itm.lance, itm.tab_shield_small_round_c],   knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x0000000dde0070c4549dd5ca6f4dd56500000000001e291b0000000000000000, sarranid_face_older_2],
  ["knight_6_10", "Emir Ghulassen", "Ghulassen", tf_hero, 0, reserved,  fac.kingdom_6, [itm.warhorse_sarranid,     itm.sarranid_cavalry_robe,       itm.sarranid_boots_c,  itm.sarranid_boots_c,       itm.sarranid_helmet1, itm.lamellar_gauntlets,   itm.lance,     itm.sarranid_cavalry_sword,   itm.tab_shield_small_round_c],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_4, 0x00000001a60471c66ce99256b4ad4b3300000000001d392c0000000000000000, sarranid_face_older_2],
  ["knight_6_11", "Emir Azadun", "Azadun", tf_hero, 0, reserved,  fac.kingdom_6, [itm.arabian_horse_a,     itm.sarranid_mail_shirt,              itm.sarranid_boots_c,    itm.sarranid_boots_c,    itm.sarranid_mail_coif,  itm.leather_gloves,    itm.fighting_pick,   itm.tab_shield_small_round_c],     knight_attrib_1,wp(130),knight_skills_1, 0x0000000fff08734726c28af8dc96e4da00000000001e541d0000000000000000, sarranid_face_middle_2],
  ["knight_6_12", "Emir Quryas", "Quryas", tf_hero, 0, reserved,  fac.kingdom_6, [itm.courser,    itm.mamluke_mail,           itm.sarranid_boots_c,    itm.mail_boots,    itm.sarranid_helmet1, itm.lance,    itm.military_pick,   itm.tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_5, 0x0000000035107084635b74ba5491a7a400000000001e46d60000000000000000, sarranid_face_old_2],
  ["knight_6_13", "Emir Amdar", "Amdar", tf_hero, 0, reserved,  fac.kingdom_6, [itm.arabian_horse_b,     itm.sarranid_mail_shirt,       itm.sarranid_boots_c,      itm.sarranid_boots_c,  itm.sarranid_helmet1,   itm.lamellar_gauntlets,     itm.sword_two_handed_a,  itm.tab_shield_small_round_c],    knight_attrib_3,wp(190),knight_skills_3, 0x00000000001071435b734d4ad94eba9400000000001eb8eb0000000000000000, sarranid_face_older_2],
  ["knight_6_14", "Emir Hiwan", "Hiwan", tf_hero, 0, reserved,  fac.kingdom_6, [itm.arabian_horse_b,     itm.sarranid_elite_armor,       itm.sarranid_boots_c,      itm.sarranid_boots_c,    itm.sarranid_mail_coif, itm.lance,  itm.sarranid_cavalry_sword,    itm.tab_shield_small_round_c],    knight_attrib_4,wp(220),knight_skills_4, 0x000000000c0c75c63a5b921ac22db8e200000000001cca530000000000000000, sarranid_face_older_2],
  ["knight_6_15", "Emir Muhnir", "Muhnir", tf_hero, 0, reserved,  fac.kingdom_6, [itm.hunter,     itm.sarranid_mail_shirt,       itm.sarranid_boots_c,    itm.mail_boots,    itm.sarranid_helmet1,  itm.sword_two_handed_a,  itm.tab_shield_small_round_c], knight_attrib_5,wp(250),knight_skills_5, 0x000000001b0c7185369a6938cecde95600000000001f25210000000000000000, sarranid_face_older_2],
  ["knight_6_16", "Emir Ayyam", "Ayyam", tf_hero, 0, reserved,  fac.kingdom_6, [itm.arabian_horse_a,    itm.mamluke_mail,             itm.sarranid_boots_c,      itm.sarranid_boots_c,    itm.sarranid_mail_coif, itm.leather_gloves,  itm.lance,    itm.fighting_pick,   itm.tab_shield_small_round_c],    knight_attrib_1,wp(120),knight_skills_1, 0x00000007770871c80a01e1c5eb51ffff00000000001f12d80000000000000000, sarranid_face_middle_2],
  ["knight_6_17", "Emir Raddoun", "Raddoun", tf_hero, 0, reserved,  fac.kingdom_6, [itm.arabian_horse_b,     itm.sarranid_mail_shirt,          itm.sarranid_boots_c,    itm.sarranid_boots_c,       itm.sarranid_mail_coif,  itm.leather_gloves,      itm.sarranid_cavalry_sword,    itm.tab_shield_small_round_c],     knight_attrib_2,wp(150),knight_skills_2, 0x000000007f0472c32419f47a1aba8bcf00000000001e7e090000000000000000, sarranid_face_old_2],
  ["knight_6_18", "Emir Tilimsan", "Tilimsan", tf_hero, 0, reserved,  fac.kingdom_6, [itm.arabian_horse_a,  itm.sarranid_elite_armor,     itm.sarranid_boots_c,      itm.mail_boots,    itm.sarranid_helmet1,  itm.lance,       itm.military_pick,   itm.tab_shield_small_round_c],    knight_attrib_3,wp(180),knight_skills_3, 0x000000003410710070d975caac91aca500000000001c27530000000000000000, sarranid_face_older_2],
  ["knight_6_19", "Emir Dhashwal", "Dhashwal", tf_hero, 0, reserved,  fac.kingdom_6, [itm.warhorse_sarranid,     itm.sarranid_mail_shirt,        itm.sarranid_boots_c,    itm.sarranid_boots_c,       itm.sarranid_mail_coif, itm.lamellar_gauntlets,   itm.fighting_pick,  itm.sword_two_handed_a, itm.tab_shield_small_round_c],   knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x000000018a08718016ac36bc8b6e4a9900000000001dd45d0000000000000000, sarranid_face_older_2],
  ["knight_6_20", "Emir Biliya", "Biliya", tf_hero, 0, reserved,  fac.kingdom_6, [itm.warhorse_sarranid,     itm.sarranid_cavalry_robe,       itm.sarranid_boots_c,  itm.sarranid_boots_c,       itm.sarranid_veiled_helmet,   itm.lance,      itm.sarranid_cavalry_sword,   itm.tab_shield_small_round_c],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_6, 0x00000001bd0070c0281a899ac956b94b00000000001ec8910000000000000000, sarranid_face_older_2],
  
  
  ["kingdom_1_pretender",  "Lady Isolla of Suno",       "Isolla",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac.kingdom_1,[itm.charger,   itm.rich_outfit,  itm.blue_hose,      itm.iron_greaves,         itm.mail_shirt,      itm.sword_medieval_c_small,      itm.tab_shield_small_round_c,       itm.bascinet],          lord_attrib,wp(220),knight_skills_5, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],
  ["kingdom_2_pretender",  "Prince Valdym the Bastard", "Valdym",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac.kingdom_2,[itm.hunter,    itm.courtly_outfit,      itm.leather_boots,              itm.mail_chausses,              itm.lamellar_armor,       itm.military_pick,      itm.tab_shield_heater_b,      itm.flat_topped_helmet],    lord_attrib,wp(220),knight_skills_5, 0x00000000200412142452ed631b30365c00000000001c94e80000000000000000, vaegir_face_middle_2],
  ["kingdom_3_pretender",  "Dustum Khan",               "Dustum",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac.kingdom_3,[itm.courser,   itm.nomad_robe,             itm.leather_boots,              itm.splinted_greaves,           itm.khergit_guard_armor,         itm.sword_khergit_2,              itm.tab_shield_small_round_c,       itm.segmented_helmet],      lord_attrib,wp(220),knight_skills_5, 0x000000065504310b30d556b51238f66100000000001c256d0000000000000000, khergit_face_middle_2],
  ["kingdom_4_pretender",  "Lethwin Far-Seeker",   "Lethwin",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac.kingdom_4,[itm.hunter,    itm.tabard,    itm.leather_boots,              itm.mail_boots,                 itm.brigandine_red,           itm.sword_medieval_c,           itm.tab_shield_heater_cav_a,    itm.kettle_hat],            lord_attrib,wp(220),knight_skills_5, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],
  ["kingdom_5_pretender",  "Lord Kastor of Veluca",  "Kastor",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac.kingdom_5,[itm.warhorse,  itm.nobleman_outfit,             itm.leather_boots,              itm.splinted_leather_greaves,   itm.mail_hauberk,           itm.sword_medieval_c,         itm.tab_shield_heater_d,        itm.spiked_helmet],         lord_attrib,wp(220),knight_skills_5, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, rhodok_face_old_2],
  ["kingdom_6_pretender",  "Arwa the Pearled One",       "Arwa",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac.kingdom_6,[itm.arabian_horse_b, itm.sarranid_mail_shirt, itm.sarranid_boots_c, itm.sarranid_cavalry_sword,      itm.tab_shield_small_round_c],          lord_attrib,wp(220),knight_skills_5, 0x000000050b004004072d51c293a9a70b00000000001dd6a90000000000000000],

#Royal family members

  #Swadian ladies - eight mothers, eight daughters, four sisters
  ["kingdom_1_lady_1","Lady Anna","Anna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [          itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_1_lady_2","Lady Nelda","Nelda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_1_lady_3","Lady Bela","Bela",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1,  [       itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_1_lady_4","Lady Elina","Elina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1,  [       itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_l_lady_5","Lady Constanis","Constanis",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_6","Lady Vera","Vera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_1_lady_7","Lady Auberina","Auberina",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_8","Lady Tibal","Tibal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [        itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_1_lady_9","Lady Magar","Magar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_10","Lady Thedosa","Thedosa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_1_lady_11","Lady Melisar","Melisar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_12","Lady Irena","Irena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_l_lady_13","Lady Philenna","Philenna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [     itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_14","Lady Sonadel","Sonadel",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_1_lady_15","Lady Boadila","Boadila",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_16","Lady Elys","Elys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_1_lady_17","Lady Johana","Johana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_1_lady_18","Lady Bernatys","Bernatys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_1_lady_19","Lady Enricata","Enricata",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_1_lady_20","Lady Gaeta","Gaeta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_1, [itm.lady_dress_green,      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
  
  ["kingdom_2_lady_1","Lady Junitha","Junitha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2, [      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_2","Lady Katia","Katia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2, [    itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_3","Lady Seomis","Seomis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2,  [   itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_4","Lady Drina","Drina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2,  [    itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_5","Lady Nesha","Nesha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2, [      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_6","Lady Tabath","Tabath",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2, [     itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_7","Lady Pelaeka","Pelaeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2,  [     itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_8","Lady Haris","Haris",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2,  [    itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_9","Lady Vayen","Vayen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2, [    itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_10","Lady Joaka","Joaka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2, [      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_11","Lady Tejina","Tejina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2,  [    itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_12","Lady Olekseia","Olekseia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2,  [      itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_13","Lady Myntha","Myntha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2, [      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_14","Lady Akilina","Akilina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2, [     itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_15","Lady Sepana","Sepana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2,  [     itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_16","Lady Iarina","Iarina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2,  [       itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_17","Lady Sihavan","Sihavan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2, [      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_18","Lady Erenchina","Erenchina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2, [  itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_19","Lady Tamar","Tamar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2,  [  itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_20","Lady Valka","Valka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_2,  [itm.green_dress,   itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],

  ["kingdom_3_lady_1","Lady Borge","Borge",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3, [      itm.brown_dress,       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_2","Lady Tuan","Tuan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3, [      itm.green_dress,       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_3","Lady Mahraz","Mahraz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3, [itm.red_dress ,     itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_4","Lady Ayasu","Ayasu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3,  [    itm.red_dress ,     itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_5","Lady Ravin","Ravin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3, [      itm.green_dress,       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_6","Lady Ruha","Ruha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3, [      itm.green_dress,       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_7","Lady Chedina","Chedina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3,  [    itm.brown_dress,     itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_8","Lady Kefra","Kefra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3,  [    itm.brown_dress ,     itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_9","Lady Nirvaz","Nirvaz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3, [      itm.brown_dress,       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
  ["kingdom_3_lady_10","Lady Dulua","Dulua",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3, [      itm.brown_dress,       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_11","Lady Selik","Selik",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3,  [    itm.brown_dress ,     itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
  ["kingdom_3_lady_12","Lady Thalatha","Thalatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3,  [    itm.brown_dress ,     itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_3_lady_13","Lady Yasreen","Yasreen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3, [      itm.brown_dress,       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_14","Lady Nadha","Nadha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3, [      itm.brown_dress,       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_15","Lady Zenur","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3,  [    itm.brown_dress ,     itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_16","Lady Arjis","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3,  [    itm.brown_dress ,     itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],
  ["kingdom_3_lady_17","Lady Atjahan", "Atjahan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3, [      itm.brown_dress,       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
  ["kingdom_3_lady_18","Lady Qutala","Qutala",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3, [      itm.brown_dress,       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_19","Lady Hindal","Hindal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3,  [    itm.brown_dress ,     itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_20","Lady Mechet","Mechet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_3,  [    itm.brown_dress ,     itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  
  ["kingdom_4_lady_1","Lady Jadeth","Jadeth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4, [      itm.court_dress ,   itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_2","Lady Miar","Miar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4, [      itm.court_dress ,   itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_3","Lady Dria","Dria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4,  [    itm.peasant_dress, itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_4","Lady Glunde","Glunde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4,  [    itm.peasant_dress,  itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_5","Lady Loeka","Loeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4, [      itm.court_dress ,   itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_6","Lady Bryn","Bryn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4, [      itm.court_dress ,   itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_7","Lady Eir","Eir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4,  [    itm.peasant_dress,  itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_8","Lady Thera","Thera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4,  [    itm.peasant_dress,  itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_9","Lady Hild","Hild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4, [      itm.court_dress ,  itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_10","Lady Endegrid","Endegrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4, [      itm.court_dress ,   itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_11","Lady Herjasa","Herjasa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4,  [    itm.peasant_dress,  itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_12","Lady Svipul","Svipul",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4,  [    itm.peasant_dress,  itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_13","Lady Ingunn","Ingunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4, [      itm.court_dress ,   itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_14","Lady Kaeteli","Kaeteli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4, [      itm.court_dress ,   itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_15","Lady Eilif","Eilif",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4,  [    itm.peasant_dress,  itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_16","Lady Gudrun","Gudrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4,  [    itm.peasant_dress,  itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_17","Lady Bergit","Bergit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4, [      itm.court_dress ,    itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_18","Lady Aesa","Aesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4, [      itm.court_dress ,   itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_19","Lady Alfrun","Alfrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4,  [    itm.peasant_dress,  itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_20","Lady Afrid","Afrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_4,  [    itm.peasant_dress,  itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],

  ["kingdom_5_lady_1","Lady Brina","Brina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5, [      itm.lady_dress_green,     itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_lady_2","Lady Aliena","Aliena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5, [      itm.lady_dress_green,      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_lady_3","Lady Aneth","Aneth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5,  [ itm.lady_dress_ruby ,     itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_4","Lady Reada","Reada",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5,  [ itm.lady_dress_ruby ,     itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_lady_5","Lady Saraten","Saraten",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5, [      itm.lady_dress_green,    itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_5_lady_6","Lady Baotheia","Baotheia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5, [itm.lady_dress_green,     itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000bf0400035913aa236b4d975a00000000001eb69c0000000000000000],
  ["kingdom_5_lady_7","Lady Eleandra","Eleandra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5,  [ itm.lady_dress_ruby ,     itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_8","Lady Meraced","Meraced",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5,  [ itm.lady_dress_ruby ,     itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_lady_9","Lady Adelisa","Adelisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5, [      itm.lady_dress_green,   itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_lady_10","Lady Calantina","Calantina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5, [      itm.lady_dress_green,   itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_lady_11","Lady Forbesa","Forbesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5,  [ itm.lady_dress_ruby ,  itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_12","Lady Claudora","Claudora",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5,  [ itm.lady_dress_ruby ,  itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_lady_13","Lady Anais","Anais",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5, [      itm.lady_dress_green,   itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_lady_14","Lady Miraeia","Miraeia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5, [      itm.lady_dress_green,   itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_lady_15","Lady Agasia","Agasia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5,  [ itm.lady_dress_ruby ,  itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_16","Lady Geneiava","Geneiava",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5,  [ itm.lady_dress_ruby ,  itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_lady_17","Lady Gwenael","Gwenael",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5, [      itm.lady_dress_green,   itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_lady_18","Lady Ysueth","Ysueth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5, [      itm.lady_dress_green,   itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_lady_19","Lady Ellian","Ellian",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5,  [ itm.lady_dress_ruby ,  itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_20","Lady Timethi","Timethi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_5,  [ itm.lady_dress_ruby ,  itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  
  ["kingdom_6_lady_1","Lady Rayma","Rayma",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress,  itm.sarranid_head_cloth,        itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910400107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_6_lady_2","Lady Thanaikha","Thanaikha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress_b,      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08400232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_6_lady_3","Lady Sulaha","Sulaha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6,  [itm.sarranid_lady_dress,       itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0440064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_6_lady_4","Lady Shatha","Shatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6,  [itm.sarranid_lady_dress,       itm.leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204400629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_6_lady_5","Lady Bawthan","Bawthan",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress,      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, sarranid_woman_face_1, sarranid_woman_face_2],
  ["kingdom_6_lady_6","Lady Mahayl","Mahayl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress_b,      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0840011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_6_lady_7","Lady Isna","Isna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress,      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, sarranid_woman_face_1, sarranid_woman_face_2],
  ["kingdom_6_lady_8","Lady Siyafan","Siyafan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress_b,        itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900400542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_6_lady_9","Lady Ifar","Ifar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress_b,      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, sarranid_woman_face_1, sarranid_woman_face_2],
  ["kingdom_6_lady_10","Lady Yasmin","Yasmin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress,       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00400646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_6_lady_11","Lady Dula","Dula",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress,      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, sarranid_woman_face_1, sarranid_woman_face_2],
  ["kingdom_6_lady_12","Lady Ruwa","Ruwa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress_b,       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04400148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_6_lady_13","Lady Luqa","Luqa",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress_b,     itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, sarranid_woman_face_1, sarranid_woman_face_2],
  ["kingdom_6_lady_14","Lady Zandina","Zandina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress,      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c4003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_6_lady_15","Lady Lulya","Lulya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress_b,       itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, sarranid_woman_face_1, sarranid_woman_face_2],
  ["kingdom_6_lady_16","Lady Zahara","Zahara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress,      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b084003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_6_lady_17","Lady Safiya","Safiya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress_b,      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c400446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_6_lady_18","Lady Khalisa","Khalisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress,      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000084006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_6_lady_19","Lady Janab","Janab",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress_b,      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, sarranid_woman_face_1],
  ["kingdom_6_lady_20","Lady Sur","Sur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac.kingdom_6, [itm.sarranid_lady_dress,      itm.leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, sarranid_woman_face_2],

  ["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac.neutral,[itm.saddle_horse,itm.leather_jacket,itm.nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],

#Chests (used to be seneschals, but that job is now done by ministers and ladies)
  ["town_1_chest", "{!}Town 1 Chest", "{!}Town 1 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_chest", "{!}Town 2 Chest", "{!}Town 2 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_chest", "{!}Town 3 Chest", "{!}Town 3 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_chest", "{!}Town 4 Chest", "{!}Town 4 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_chest", "{!}Town 5 Chest", "{!}Town 5 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_chest", "{!}Town 6 Chest", "{!}Town 6 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_chest", "{!}Town 7 Chest", "{!}Town 7 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_chest", "{!}Town 8 Chest", "{!}Town 8 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_chest", "{!}Town 9 Chest", "{!}Town 9 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_chest", "{!}Town 10 Chest", "{!}Town 10 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_chest", "{!}Town 11 Chest", "{!}Town 11 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_chest", "{!}Town 12 Chest", "{!}Town 12 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_chest", "{!}Town 13 Chest", "{!}Town 13 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_chest", "{!}Town 14 Chest", "{!}Town 14 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_chest", "{!}Town 15 Chest", "{!}Town 15 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_chest", "{!}Town 16 Chest", "{!}Town 16 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_17_chest", "{!}Town 17 Chest", "{!}Town 17 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_18_chest", "{!}Town 18 Chest", "{!}Town 18 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_19_chest", "{!}Town 19 Chest", "{!}Town 19 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_20_chest", "{!}Town 20 Chest", "{!}Town 20 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_21_chest", "{!}Town 21 Chest", "{!}Town 21 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_22_chest", "{!}Town 22 Chest", "{!}Town 22 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],

  ["castle_1_chest", "{!}Castle 1 Chest", "{!}Castle 1 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_chest", "{!}Castle 2 Chest", "{!}Castle 2 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_chest", "{!}Castle 3 Chest", "{!}Castle 3 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_chest", "{!}Castle 4 Chest", "{!}Castle 4 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_chest", "{!}Castle 5 Chest", "{!}Castle 5 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_chest", "{!}Castle 6 Chest", "{!}Castle 6 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_chest", "{!}Castle 7 Chest", "{!}Castle 7 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_chest", "{!}Castle 8 Chest", "{!}Castle 8 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_chest", "{!}Castle 9 Chest", "{!}Castle 9 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_chest", "{!}Castle 10 Chest", "{!}Castle 10 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_chest", "{!}Castle 11 Chest", "{!}Castle 11 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_chest", "{!}Castle 12 Chest", "{!}Castle 12 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_chest", "{!}Castle 13 Chest", "{!}Castle 13 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_chest", "{!}Castle 14 Chest", "{!}Castle 14 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_chest", "{!}Castle 15 Chest", "{!}Castle 15 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_chest", "{!}Castle 16 Chest", "{!}Castle 16 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_chest", "{!}Castle 17 Chest", "{!}Castle 17 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_chest", "{!}Castle 18 Chest", "{!}Castle 18 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_chest", "{!}Castle 19 Chest", "{!}Castle 19 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_chest", "{!}Castle 20 Chest", "{!}Castle 20 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_chest", "{!}Castle 21 Chest", "{!}Castle 21 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_chest", "{!}Castle 22 Chest", "{!}Castle 22 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_chest", "{!}Castle 23 Chest", "{!}Castle 23 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_chest", "{!}Castle 24 Chest", "{!}Castle 24 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_chest", "{!}Castle 25 Chest", "{!}Castle 25 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_chest", "{!}Castle 26 Chest", "{!}Castle 26 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_chest", "{!}Castle 27 Chest", "{!}Castle 27 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_chest", "{!}Castle 28 Chest", "{!}Castle 28 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_chest", "{!}Castle 29 Chest", "{!}Castle 29 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_chest", "{!}Castle 30 Chest", "{!}Castle 30 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_chest", "{!}Castle 31 Chest", "{!}Castle 31 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_chest", "{!}Castle 32 Chest", "{!}Castle 32 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_chest", "{!}Castle 33 Chest", "{!}Castle 33 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_chest", "{!}Castle 34 Chest", "{!}Castle 34 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_chest", "{!}Castle 35 Chest", "{!}Castle 35 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_chest", "{!}Castle 36 Chest", "{!}Castle 36 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_chest", "{!}Castle 37 Chest", "{!}Castle 37 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_chest", "{!}Castle 38 Chest", "{!}Castle 38 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_chest", "{!}Castle 39 Chest", "{!}Castle 39 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_chest", "{!}Castle 40 Chest", "{!}Castle 40 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_41_chest", "{!}Castle 41 Chest", "{!}Castle 41 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_42_chest", "{!}Castle 42 Chest", "{!}Castle 42 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_43_chest", "{!}Castle 43 Chest", "{!}Castle 43 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_44_chest", "{!}Castle 44 Chest", "{!}Castle 44 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_45_chest", "{!}Castle 45 Chest", "{!}Castle 45 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_46_chest", "{!}Castle 46 Chest", "{!}Castle 46 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_47_chest", "{!}Castle 47 Chest", "{!}Castle 47 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_48_chest", "{!}Castle 48 Chest", "{!}Castle 48 Chest", tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],

#Arena Masters
  ["town_1_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_1_arena|entry(52),reserved,   fac.commoners,[itm.coarse_tunic,      itm.hide_boots],    def_attrib|level(2),wp(20),knows_common,nord_face_middle_1, nord_face_older_2],
  ["town_2_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_2_arena|entry(52),reserved,   fac.commoners,[itm.linen_tunic,       itm.nomad_boots],   def_attrib|level(2),wp(20),knows_common,nord_face_middle_1, nord_face_older_2],
  ["town_3_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_3_arena|entry(52),reserved,   fac.commoners,[itm.nomad_armor,       itm.hide_boots],    def_attrib|level(2),wp(20),knows_common,rhodok_face_middle_1, rhodok_face_older_2],
  ["town_4_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_4_arena|entry(52),reserved,   fac.commoners,[itm.coarse_tunic,      itm.hide_boots],    def_attrib|level(2),wp(20),knows_common,swadian_face_middle_1, swadian_face_older_2],
  ["town_5_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_5_arena|entry(52),reserved,   fac.commoners,[itm.linen_tunic,       itm.nomad_boots],   def_attrib|level(2),wp(20),knows_common,rhodok_face_middle_1, rhodok_face_older_2],
  ["town_6_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_6_arena|entry(52),reserved,   fac.commoners,[itm.leather_jerkin,    itm.leather_boots], def_attrib|level(2),wp(20),knows_common,swadian_face_middle_1, swadian_face_older_2],
  ["town_7_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_7_arena|entry(52),reserved,   fac.commoners,[itm.padded_leather,    itm.nomad_boots],   def_attrib|level(2),wp(20),knows_common,swadian_face_middle_1, swadian_face_older_2],
  ["town_8_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_8_arena|entry(52),reserved,   fac.commoners,[itm.linen_tunic,       itm.hide_boots],    def_attrib|level(2),wp(20),knows_common,vaegir_face_middle_1, vaegir_face_older_2],
  ["town_9_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_9_arena|entry(52),reserved,   fac.commoners,[itm.leather_jerkin,    itm.leather_boots], def_attrib|level(2),wp(20),knows_common,vaegir_face_middle_1, vaegir_face_older_2],
  ["town_10_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_10_arena|entry(52),reserved,  fac.commoners,[itm.nomad_armor,       itm.nomad_boots],   def_attrib|level(2),wp(20),knows_common,khergit_face_middle_1, khergit_face_older_2],
  ["town_11_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_11_arena|entry(52),reserved,  fac.commoners,[itm.coarse_tunic,      itm.hide_boots],    def_attrib|level(2),wp(20),knows_common,vaegir_face_middle_1, vaegir_face_older_2],
  ["town_12_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_12_arena|entry(52),reserved,  fac.commoners,[itm.padded_leather,    itm.hide_boots],    def_attrib|level(2),wp(20),knows_common,nord_face_middle_1, nord_face_older_2],
  ["town_13_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_13_arena|entry(52),reserved,  fac.commoners,[itm.coarse_tunic,      itm.nomad_boots],   def_attrib|level(2),wp(20),knows_common,vaegir_face_middle_1, vaegir_face_older_2],
  ["town_14_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_14_arena|entry(52),reserved,  fac.commoners,[itm.tribal_warrior_outfit, itm.hide_boots],def_attrib|level(2),wp(20),knows_common,khergit_face_middle_1, khergit_face_older_2],
  ["town_15_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_15_arena|entry(52),reserved,  fac.commoners,[itm.padded_leather,    itm.hide_boots],    def_attrib|level(2),wp(20),knows_common,rhodok_face_middle_1, rhodok_face_older_2],
  ["town_16_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_16_arena|entry(52),reserved,  fac.commoners,[itm.fur_coat,          itm.hide_boots],    def_attrib|level(2),wp(20),knows_common,swadian_face_middle_1, swadian_face_older_2],
  ["town_17_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_17_arena|entry(52),reserved,  fac.commoners,[itm.nomad_robe,        itm.hide_boots],    def_attrib|level(2),wp(20),knows_common,khergit_face_middle_1, khergit_face_older_2],
  ["town_18_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_18_arena|entry(52),reserved,  fac.commoners,[itm.tribal_warrior_outfit, itm.hide_boots],def_attrib|level(2),wp(20),knows_common,khergit_face_middle_1, khergit_face_older_2],
  ["town_19_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_19_arena|entry(52),reserved,  fac.commoners,[itm.sarranid_leather_armor, itm.sarranid_boots_b], def_attrib|level(2),wp(20),knows_common,sarranid_face_middle_1, sarranid_face_older_2],
  ["town_20_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_20_arena|entry(52),reserved,  fac.commoners,[itm.archers_vest,    itm.sarranid_boots_b],        def_attrib|level(2),wp(20),knows_common,sarranid_face_middle_1, sarranid_face_older_2],
  ["town_21_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_21_arena|entry(52),reserved,  fac.commoners,[itm.sarranid_leather_armor, itm.sarranid_boots_b], def_attrib|level(2),wp(20),knows_common,sarranid_face_middle_1, sarranid_face_older_2],
  ["town_22_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn.town_22_arena|entry(52),reserved,  fac.commoners,[itm.sarranid_leather_armor, itm.sarranid_boots_b], def_attrib|level(2),wp(20),knows_common,sarranid_face_middle_1, sarranid_face_older_2],

# Armor Merchants
  ["town_1_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.linen_tunic,           itm.leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, nord_face_young_1, nord_face_old_2],
  ["town_2_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac.commoners,[itm.peasant_dress,itm.hide_boots,itm.straw_hat  ],def_attrib|level(2),wp(20),knows_inventory_management_10, nord_woman_face_middle_1, nord_woman_face_old_2],
  ["town_3_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.arena_tunic_red,        itm.hide_boots      ],def_attrib|level(2),wp(20),knows_inventory_management_10, rhodok_face_young_1, rhodok_face_old_2],
  ["town_4_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.red_gambeson,         itm.leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, swadian_face_young_1, swadian_face_old_2],
  ["town_5_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.linen_tunic,          itm.nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, rhodok_face_young_1, rhodok_face_old_2],
  ["town_6_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.leather_apron,       itm.ankle_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, swadian_face_young_1, swadian_face_old_2],
  ["town_7_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.leather_jerkin,       itm.hide_boots    ],def_attrib|level(5),wp(20),knows_inventory_management_10, swadian_face_young_1, swadian_face_old_2],
  ["town_8_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.fur_coat,       itm.leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, vaegir_face_young_1, vaegir_face_old_2],
  ["town_9_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.blue_gambeson,        itm.nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, vaegir_face_young_1, vaegir_face_old_2],
  ["town_10_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.leather_jerkin,       itm.hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, khergit_face_young_1, khergit_face_old_2],
  ["town_11_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.fur_coat,        itm.leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, vaegir_face_young_1, vaegir_face_old_2],
  ["town_12_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.red_gambeson,         itm.nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, nord_face_young_1, nord_face_old_2],
  ["town_13_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.leather_jacket,       itm.hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, vaegir_face_young_1, vaegir_face_old_2],
  ["town_14_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac.commoners,[itm.woolen_dress,itm.wrapping_boots, itm.headcloth  ],def_attrib|level(5),wp(20),knows_inventory_management_10, khergit_woman_face_middle_1, khergit_woman_face_old_2],
  ["town_15_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.blue_gambeson,        itm.leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, rhodok_face_young_1, rhodok_face_old_2],
  ["town_16_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.padded_leather,       itm.leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, swadian_face_young_1, swadian_face_old_2],
  ["town_17_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.tribal_warrior_outfit,    itm.hide_boots  ],def_attrib|level(5),wp(20),knows_inventory_management_10, khergit_face_young_1, khergit_face_old_2],
  ["town_18_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac.commoners,[itm.leather_vest,itm.khergit_leather_boots,itm.headcloth],def_attrib|level(5),wp(20),knows_inventory_management_10, khergit_woman_face_middle_1, khergit_woman_face_old_2],
  ["town_19_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.sarranid_cloth_robe_b,  itm.sarranid_boots_b   ],def_attrib|level(5),wp(20),knows_inventory_management_10, sarranid_face_young_1, sarranid_face_older_2],
  ["town_20_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.tunic_with_green_cape,  itm.nomad_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, sarranid_face_young_1, sarranid_face_older_2],
  ["town_21_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.sarranid_cloth_robe,       itm.sarranid_boots_b  ],def_attrib|level(5),wp(20),knows_inventory_management_10, sarranid_face_young_1, sarranid_face_older_2],
  ["town_22_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac.commoners,[itm.sarranid_common_dress, itm.sarranid_head_cloth, itm.sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, sarranid_woman_face_young_1, sarranid_woman_face_older_2],

# Weapon merchants
  ["town_1_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac.commoners,[itm.linen_tunic,      itm.hide_boots,itm.straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, nord_woman_face_middle_1, nord_woman_face_old_2],
  ["town_2_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.shirt,     itm.nomad_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, nord_face_young_1, nord_face_old_2],
  ["town_3_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.fur_coat,   itm.hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, rhodok_face_young_1, rhodok_face_old_2],
  ["town_4_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.shirt,            itm.hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, swadian_face_young_1, swadian_face_old_2],
  ["town_5_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.leather_jerkin,   itm.wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, rhodok_face_young_1, rhodok_face_old_2],
  ["town_6_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.linen_tunic,      itm.hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, swadian_face_young_1, swadian_face_old_2],
  ["town_7_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.shirt,            itm.hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, swadian_face_young_1, swadian_face_old_2],
  ["town_8_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac.commoners,[itm.woolen_dress,     itm.wrapping_boots,itm.straw_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, vaegir_woman_face_young_1, vaegir_woman_face_old_2],
  ["town_9_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.leather_jerkin,   itm.leather_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, vaegir_face_young_1, vaegir_face_old_2],
  ["town_10_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.nomad_armor,     itm.hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, khergit_face_young_1, khergit_face_old_2],
  ["town_11_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.leather_jacket,  itm.woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, vaegir_face_young_1, vaegir_face_old_2],
  ["town_12_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.shirt,           itm.hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, nord_face_young_1, nord_face_old_2],
  ["town_13_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.arena_tunic_red,     itm.wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, vaegir_face_young_1, vaegir_face_old_2],
  ["town_14_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.khergit_armor,     itm.wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, khergit_face_young_1, khergit_face_old_2],
  ["town_15_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.leather_jacket,  itm.woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, rhodok_face_young_1, rhodok_face_old_2],
  ["town_16_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.shirt,           itm.hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, swadian_face_young_1, swadian_face_old_2],
  ["town_17_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.khergit_armor,     itm.wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, khergit_face_young_1, khergit_face_old_2],
  ["town_18_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.nomad_armor,     itm.wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, khergit_face_young_1, khergit_face_old_2],
  ["town_19_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.leather_jacket,  itm.sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, sarranid_face_young_1, sarranid_face_old_2],
  ["town_20_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.leather_apron,      itm.sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, sarranid_face_young_1, sarranid_face_old_2],
  ["town_21_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.tunic_with_green_cape, itm.sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, sarranid_face_young_1, sarranid_face_old_2],
  ["town_22_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac.commoners,[itm.sarranid_cloth_robe,  itm.sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, sarranid_face_young_1, sarranid_face_old_2],
    
#Tavern keepers
  ["town_1_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn.town_1_tavern|entry(9),0,   fac.commoners,[itm.leather_apron,       itm.wrapping_boots],def_attrib|level(2),wp(20),knows_common, nord_face_young_1, nord_face_old_2],
  ["town_2_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn.town_2_tavern|entry(9),0,   fac.commoners,[itm.leather_apron,       itm.leather_boots],def_attrib|level(2),wp(20),knows_common, nord_face_young_1, nord_face_old_2],
  ["town_3_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn.town_3_tavern|entry(9),0,   fac.commoners,[itm.woolen_dress,        itm.hide_boots],def_attrib|level(2),wp(20),knows_common, rhodok_woman_face_young_1, rhodok_woman_face_old_2],
  ["town_4_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn.town_4_tavern|entry(9),0,   fac.commoners,[itm.leather_apron,       itm.leather_boots],def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["town_5_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn.town_5_tavern|entry(9),0,   fac.commoners,[itm.leather_apron,       itm.hide_boots],def_attrib|level(2),wp(20),knows_common, rhodok_face_young_1, rhodok_face_old_2],
  ["town_6_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn.town_6_tavern|entry(9),0,   fac.commoners,[itm.woolen_dress,        itm.hide_boots],def_attrib|level(2),wp(20),knows_common, swadian_woman_face_young_1, swadian_woman_face_old_2],
  ["town_7_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn.town_7_tavern|entry(9),0,   fac.commoners,[itm.woolen_dress,        itm.leather_boots,      itm.headcloth],def_attrib|level(2),wp(20),knows_common, swadian_woman_face_young_1, swadian_woman_face_old_2],
  ["town_8_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn.town_8_tavern|entry(9),0,   fac.commoners,[itm.leather_apron,      itm.leather_boots],def_attrib|level(2),wp(20),knows_common, vaegir_face_young_1, vaegir_face_old_2],
  ["town_9_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn.town_9_tavern|entry(9),0,   fac.commoners,[itm.woolen_dress,        itm.nomad_boots],def_attrib|level(2),wp(20),knows_common, vaegir_woman_face_young_1, vaegir_woman_face_old_2],
  ["town_10_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn.town_10_tavern|entry(9),0,  fac.commoners,[itm.woolen_dress,        itm.hide_boots],def_attrib|level(2),wp(20),knows_common, khergit_woman_face_young_1, khergit_woman_face_old_2],
  ["town_11_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn.town_11_tavern|entry(9),0,  fac.commoners,[itm.woolen_dress,        itm.nomad_boots],def_attrib|level(2),wp(20),knows_common, vaegir_woman_face_young_1, vaegir_woman_face_old_2],
  ["town_12_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn.town_12_tavern|entry(9),0,  fac.commoners,[itm.leather_apron,       itm.hide_boots],def_attrib|level(2),wp(20),knows_common, nord_face_young_1, nord_face_old_2],
  ["town_13_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn.town_13_tavern|entry(9),0,  fac.commoners,[itm.woolen_dress,        itm.hide_boots,     itm.headcloth],def_attrib|level(2),wp(20),knows_common, vaegir_woman_face_young_1, vaegir_woman_face_old_2],
  ["town_14_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn.town_14_tavern|entry(9),0,  fac.commoners,[itm.shirt,               itm.leather_boots],def_attrib|level(2),wp(20),knows_common, khergit_face_young_1, khergit_face_old_2],
  ["town_15_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn.town_15_tavern|entry(9),0,  fac.commoners,[itm.woolen_dress,        itm.nomad_boots],def_attrib|level(2),wp(20),knows_common, rhodok_woman_face_young_1, rhodok_woman_face_old_2],
  ["town_16_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn.town_16_tavern|entry(9),0,  fac.commoners,[itm.leather_apron,       itm.hide_boots],def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["town_17_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn.town_17_tavern|entry(9),0,  fac.commoners,[itm.woolen_dress,        itm.hide_boots,     itm.headcloth],def_attrib|level(2),wp(20),knows_common, khergit_woman_face_young_1, khergit_woman_face_old_2],
  ["town_18_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn.town_18_tavern|entry(9),0,  fac.commoners,[itm.shirt,               itm.leather_boots],def_attrib|level(2),wp(20),knows_common, khergit_face_young_1, khergit_face_old_2],
  ["town_19_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn.town_19_tavern|entry(9),0,  fac.commoners,[itm.sarranid_common_dress_b,        itm.sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, sarranid_woman_face_young_1, sarranid_woman_face_old_2],
  ["town_20_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn.town_20_tavern|entry(9),0,  fac.commoners,[itm.sarranid_cloth_robe,       itm.sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, sarranid_face_young_1, sarranid_face_old_2],
  ["town_21_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn.town_21_tavern|entry(9),0,  fac.commoners,[itm.sarranid_common_dress,        itm.sarranid_boots_a,     itm.headcloth],def_attrib|level(2),wp(20),knows_common, sarranid_woman_face_young_1, sarranid_woman_face_old_2],
  ["town_22_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn.town_22_tavern|entry(9),0,  fac.commoners,[itm.sarranid_cloth_robe_b,               itm.sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, sarranid_face_young_1, sarranid_face_old_2],

#Goods Merchants
  ["town_1_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn.town_1_store|entry(9),0, fac.commoners,     [itm.coarse_tunic,  itm.leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, nord_face_young_1, nord_face_older_2],
  ["town_2_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn.town_2_store|entry(9),0, fac.commoners,     [itm.leather_apron, itm.leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, nord_face_young_1, nord_face_older_2],
  ["town_3_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn.town_3_store|entry(9),0, fac.commoners,     [itm.dress,         itm.leather_boots,  itm.straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, rhodok_woman_face_young_1, rhodok_woman_face_older_2],
  ["town_4_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn.town_4_store|entry(9),0, fac.commoners,     [itm.leather_apron, itm.leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, swadian_face_young_1, swadian_face_older_2],
  ["town_5_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn.town_5_store|entry(9),0, fac.commoners,     [itm.leather_apron, itm.leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, rhodok_face_young_1, rhodok_face_older_2],
  ["town_6_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn.town_6_store|entry(9),0, fac.commoners,     [itm.woolen_dress,  itm.leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, swadian_face_young_1, swadian_face_older_2],
  ["town_7_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn.town_7_store|entry(9),0, fac.commoners,     [itm.leather_jerkin,itm.leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, swadian_face_young_1, swadian_face_older_2],
  ["town_8_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn.town_8_store|entry(9),0, fac.commoners,     [itm.nomad_armor,   itm.leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, vaegir_face_young_1, vaegir_face_older_2],
  ["town_9_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn.town_9_store|entry(9),0, fac.commoners,     [itm.leather_apron, itm.leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, vaegir_face_young_1, vaegir_face_older_2],
  ["town_10_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn.town_10_store|entry(9),0, fac.commoners,    [itm.leather_jerkin,itm.leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, khergit_face_young_1, khergit_face_older_2],
  ["town_11_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn.town_11_store|entry(9),0, fac.commoners,    [itm.leather_apron, itm.leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, vaegir_face_young_1, vaegir_face_older_2],
  ["town_12_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn.town_12_store|entry(9),0, fac.commoners,    [itm.woolen_dress,  itm.leather_boots,  itm.female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, nord_woman_face_middle_1, nord_woman_face_older_2],
  ["town_13_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn.town_13_store|entry(9),0, fac.commoners,    [itm.dress,         itm.leather_boots,  itm.straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, vaegir_woman_face_middle_1, vaegir_woman_face_older_2],
  ["town_14_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn.town_14_store|entry(9),0, fac.commoners,    [itm.leather_apron, itm.leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, khergit_face_young_1, khergit_face_older_2],
  ["town_15_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn.town_15_store|entry(9),0, fac.commoners,    [itm.leather_apron, itm.leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, rhodok_face_young_1, rhodok_face_older_2],
  ["town_16_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn.town_16_store|entry(9),0, fac.commoners,    [itm.blue_dress,    itm.leather_boots,  itm.female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, swadian_woman_face_young_1, swadian_woman_face_older_2],
  ["town_17_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn.town_17_store|entry(9),0, fac.commoners,    [itm.woolen_dress,  itm.leather_boots,  itm.headcloth   ],def_attrib|level(2),wp(20),knows_inventory_management_10, khergit_woman_face_young_1, khergit_woman_face_older_2],
  ["town_18_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn.town_18_store|entry(9),0, fac.commoners,    [itm.leather_apron, itm.leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, khergit_face_young_1, khergit_face_older_2],
  ["town_19_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn.town_19_store|entry(9),0, fac.commoners,    [itm.leather_apron, itm.leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, sarranid_face_young_1, sarranid_face_older_2],
  ["town_20_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn.town_20_store|entry(9),0, fac.commoners,    [itm.sarranid_common_dress_b,  itm.sarranid_boots_a, itm.sarranid_felt_head_cloth_b  ],def_attrib|level(2),wp(20),knows_inventory_management_10, sarranid_woman_face_young_1, sarranid_woman_face_older_2],
  ["town_21_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn.town_21_store|entry(9),0, fac.commoners,    [itm.sarranid_common_dress,     itm.sarranid_boots_a,  itm.sarranid_felt_head_cloth  ],def_attrib|level(2),wp(20),knows_inventory_management_10, sarranid_woman_face_young_1, sarranid_woman_face_older_2],
  ["town_22_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn.town_22_store|entry(9),0, fac.commoners,    [itm.leather_apron, itm.leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, sarranid_face_young_1, sarranid_face_older_2],

# Horse Merchants
  ["town_1_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac.commoners,[itm.blue_dress,           itm.blue_hose,      itm.female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, nord_woman_face_young_1, nord_woman_face_older_2],
  ["town_2_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac.commoners,[itm.nomad_armor,          itm.nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, nord_face_young_1, nord_face_older_2],
  ["town_3_horse_merchant","Horse Merchant","{!}Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac.commoners,[itm.linen_tunic,          itm.hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, rhodok_face_young_1, rhodok_face_older_2],
  ["town_4_horse_merchant","Horse Merchant","{!}Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac.commoners,[itm.leather_jerkin,       itm.nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, swadian_face_young_1, swadian_face_older_2],
  ["town_5_horse_merchant","Horse Merchant","{!}Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac.commoners,[itm.dress,                itm.woolen_hose,    itm.straw_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, rhodok_woman_face_young_1, rhodok_woman_face_older_2],
  ["town_6_horse_merchant","Horse Merchant","{!}Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac.commoners,[itm.coarse_tunic,         itm.hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, swadian_face_young_1, swadian_face_older_2],
  ["town_7_horse_merchant","Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac.commoners,[itm.coarse_tunic,         itm.leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, swadian_face_young_1, swadian_face_older_2],
  ["town_8_horse_merchant","Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac.commoners,[itm.coarse_tunic,         itm.hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, vaegir_face_young_1, vaegir_face_older_2],
  ["town_9_horse_merchant","Horse Merchant","{!}Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac.commoners,[itm.leather_jerkin,       itm.hunter_boots],                      def_attrib|level(5),wp(20),knows_inventory_management_10, vaegir_face_young_1, vaegir_face_older_2],
  ["town_10_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac.commoners,[itm.woolen_dress,          itm.blue_hose,      itm.headcloth],   def_attrib|level(5),wp(20),knows_inventory_management_10, khergit_woman_face_young_1, khergit_woman_face_older_2],
  ["town_11_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac.commoners,[itm.nomad_armor,         itm.leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, vaegir_face_young_1, vaegir_face_older_2],
  ["town_12_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac.commoners,[itm.leather_jacket,      itm.hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, nord_face_young_1, nord_face_older_2],
  ["town_13_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac.commoners,[itm.nomad_armor,        itm.nomad_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, vaegir_face_young_1, vaegir_face_older_2],
  ["town_14_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac.commoners,[itm.peasant_dress,       itm.blue_hose,      itm.headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, khergit_woman_face_young_1, khergit_woman_face_older_2],
  ["town_15_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac.commoners,[itm.coarse_tunic,         itm.leather_boots],                    def_attrib|level(5),wp(20),knows_inventory_management_10, rhodok_face_young_1, rhodok_face_older_2],
  ["town_16_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac.commoners,[itm.leather_jacket,      itm.hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, swadian_face_young_1, swadian_face_older_2],
  ["town_17_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac.commoners,[itm.khergit_armor,        itm.nomad_boots],                      def_attrib|level(5),wp(20),knows_inventory_management_10, khergit_face_young_1, khergit_face_older_2],
  ["town_18_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac.commoners,[itm.peasant_dress,       itm.blue_hose,      itm.headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, khergit_woman_face_young_1, khergit_woman_face_older_2],
  ["town_19_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac.commoners,[itm.skirmisher_armor,         itm.sarranid_boots_a, itm.turban],                     def_attrib|level(5),wp(20),knows_inventory_management_10, sarranid_face_young_1, sarranid_face_older_2],
  ["town_20_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac.commoners,[itm.sarranid_cloth_robe,      itm.sarranid_boots_a, itm.sarranid_felt_hat],          def_attrib|level(5),wp(20),knows_inventory_management_10, sarranid_face_young_1, sarranid_face_older_2],
  ["town_21_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac.commoners,[itm.sarranid_cloth_robe_b,    itm.sarranid_boots_a, itm.sarranid_felt_hat],          def_attrib|level(5),wp(20),knows_inventory_management_10, sarranid_face_young_1, sarranid_face_older_2],
  ["town_22_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac.commoners,[itm.sarranid_common_dress_b,  itm.sarranid_boots_a, itm.sarranid_felt_head_cloth_b], def_attrib|level(5),wp(20),knows_inventory_management_10, sarranid_woman_face_young_1, sarranid_woman_face_older_2],

#Town Mayors
  ["town_1_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[     itm.courtly_outfit, itm.leather_boots], def_attrib|level(2),wp(20),knows_common, nord_face_middle_1, nord_face_older_2],
  ["town_2_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[     itm.gambeson,     itm.woolen_hose],   def_attrib|level(2),wp(20),knows_common,  nord_face_middle_1, nord_face_older_2],
  ["town_3_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[     itm.blue_gambeson,       itm.leather_boots], def_attrib|level(2),wp(20),knows_common,  rhodok_face_middle_1, rhodok_face_older_2],
  ["town_4_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[     itm.courtly_outfit,      itm.blue_hose],     def_attrib|level(2),wp(20),knows_common,  swadian_face_middle_1, swadian_face_older_2],
  ["town_5_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[     itm.nobleman_outfit,     itm.woolen_hose],   def_attrib|level(2),wp(20),knows_common,  rhodok_face_middle_1, rhodok_face_older_2],
  ["town_6_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[     itm.red_gambeson,       itm.hide_boots],   def_attrib|level(2),wp(20),knows_common,  swadian_face_middle_1, swadian_face_older_2],
  ["town_7_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[     itm.rich_outfit,     itm.woolen_hose],   def_attrib|level(2),wp(20),knows_common,  swadian_face_middle_1, swadian_face_older_2],
  ["town_8_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[     itm.red_gambeson,       itm.nomad_boots],   def_attrib|level(2),wp(20),knows_common,  vaegir_face_middle_1, vaegir_face_older_2],
  ["town_9_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[     itm.fur_coat,       itm.leather_boots], def_attrib|level(2),wp(20),knows_common,  vaegir_face_middle_1, vaegir_face_older_2],
  ["town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[ itm.leather_jerkin,     itm.nomad_boots],     def_attrib|level(2),wp(20),knows_common,  khergit_face_middle_1, khergit_face_older_2],
  ["town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[ itm.leather_jacket,     itm.nomad_boots],   def_attrib|level(2),wp(20),knows_common,  vaegir_face_middle_1, vaegir_face_older_2],
  ["town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[ itm.red_gambeson,       itm.leather_boots], def_attrib|level(2),wp(20),knows_common,  nord_face_middle_1, nord_face_older_2],
  ["town_13_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[ itm.nobleman_outfit,    itm.woolen_hose],   def_attrib|level(2),wp(20),knows_common,  vaegir_face_middle_1, vaegir_face_older_2],
  ["town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[ itm.nomad_robe,      itm.khergit_leather_boots],     def_attrib|level(2),wp(20),knows_common,  khergit_face_middle_1, khergit_face_older_2],
  ["town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[ itm.leather_jacket,     itm.nomad_boots],   def_attrib|level(2),wp(20),knows_common,  rhodok_face_middle_1, rhodok_face_older_2],
  ["town_16_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[ itm.blue_gambeson,      itm.blue_hose], def_attrib|level(2),wp(20),knows_common,  swadian_face_middle_1, swadian_face_older_2],
  ["town_17_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[ itm.nobleman_outfit,    itm.woolen_hose],   def_attrib|level(2),wp(20),knows_common,  khergit_face_middle_1, khergit_face_older_2],
  ["town_18_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[ itm.fur_coat,       itm.leather_boots],     def_attrib|level(2),wp(20),knows_common,  khergit_face_middle_1, khergit_face_older_2],
  ["town_19_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[ itm.sarranid_cloth_robe, itm.sarranid_boots_a],             def_attrib|level(2),wp(20),knows_common,  sarranid_face_middle_1, sarranid_face_older_2],
  ["town_20_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[ itm.sarranid_cloth_robe, itm.sarranid_boots_b, itm.turban], def_attrib|level(2),wp(20),knows_common,  sarranid_face_middle_1, sarranid_face_older_2],
  ["town_21_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[ itm.sarranid_cloth_robe_b, itm.sarranid_boots_b],           def_attrib|level(2),wp(20),knows_common,  sarranid_face_middle_1, sarranid_face_older_2],
  ["town_22_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac.neutral,[ itm.sarranid_cloth_robe, itm.sarranid_boots_a, itm.sarranid_felt_hat], def_attrib|level(2),wp(20),knows_common,  sarranid_face_middle_1, sarranid_face_older_2],

#Village elders (and stores)
  ["village_1_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots, itm.felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_2_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_3_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_4_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_5_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_6_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_7_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.fur_coat, itm.nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_8_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.wrapping_boots, itm.felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_9_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
  ["village_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots, itm.felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots, itm.leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.fur_coat, itm.nomad_boots,itm.fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots, itm.leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots, itm.fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots, itm.leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.fur_coat, itm.nomad_boots,itm.fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots, itm.felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.fur_coat, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_26_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_27_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.wrapping_boots, itm.felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_28_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_29_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_30_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_31_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_32_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_33_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_34_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots,itm.fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_35_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_36_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_37_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_38_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_39_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_40_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_41_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_42_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_43_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_44_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots,itm.fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_45_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_46_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_47_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_48_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_49_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.fur_coat, itm.nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_50_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_51_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_52_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots,itm.fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_53_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots, itm.felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_54_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_55_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_56_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_57_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.wrapping_boots, itm.felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_58_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.fur_coat, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_59_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_60_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_61_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_62_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots,itm.fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_63_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots, itm.felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_64_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_65_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.fur_coat, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_66_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_67_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.wrapping_boots, itm.felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_68_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_69_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_70_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_71_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_72_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots,itm.fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_73_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots, itm.felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_74_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_75_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_76_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.fur_coat, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_77_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.wrapping_boots, itm.felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_78_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_79_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_80_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_81_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_82_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_83_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.fur_coat, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_84_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots,itm.fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_85_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_86_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_87_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_88_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.fur_coat, itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_89_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_90_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.sarranid_cloth_robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_91_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.sarranid_cloth_robe, itm.nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         sarranid_face_old_1, sarranid_face_older_2],
  ["village_92_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              sarranid_face_old_1, sarranid_face_older_2],
  ["village_93_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.sarranid_cloth_robe, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,     sarranid_face_old_1, sarranid_face_older_2],
  ["village_94_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.sarranid_cloth_robe, itm.nomad_boots,itm.fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             sarranid_face_old_1, sarranid_face_older_2],
  ["village_95_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.sarranid_cloth_robe_b, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                    sarranid_face_old_1, sarranid_face_older_2],
  ["village_96_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          sarranid_face_old_1, sarranid_face_older_2],
  ["village_97_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.sarranid_cloth_robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                     sarranid_face_old_1, sarranid_face_older_2],
  ["village_98_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.sarranid_cloth_robe, itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          sarranid_face_old_1, sarranid_face_older_2],
  ["village_99_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         sarranid_face_old_1, sarranid_face_older_2],
  ["village_100_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.sarranid_cloth_robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                     sarranid_face_old_1, sarranid_face_older_2],
  ["village_101_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.sarranid_cloth_robe_b, itm.nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      sarranid_face_old_1, sarranid_face_older_2],
  ["village_102_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              sarranid_face_old_1, sarranid_face_older_2],
  ["village_103_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.sarranid_cloth_robe, itm.wrapping_boots, itm.leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,    sarranid_face_old_1, sarranid_face_older_2],
  ["village_104_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.nomad_boots,itm.fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             sarranid_face_old_1, sarranid_face_older_2],
  ["village_105_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.sarranid_cloth_robe_b, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                   sarranid_face_old_1, sarranid_face_older_2],
  ["village_106_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.coarse_tunic, itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          sarranid_face_old_1, sarranid_face_older_2],
  ["village_107_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              sarranid_face_old_1, sarranid_face_older_2],
  ["village_108_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.sarranid_cloth_robe_b, itm.hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                       sarranid_face_old_1, sarranid_face_older_2],
  ["village_109_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.sarranid_cloth_robe_b, itm.nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      sarranid_face_old_1, sarranid_face_older_2],
  ["village_110_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac.commoners,[itm.robe, itm.wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              sarranid_face_old_1, sarranid_face_older_2],
# Place extra merchants before this point
  ["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac.commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

#Used for player enterprises
  ["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[     itm.leather_apron,       itm.leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[     itm.padded_leather,     itm.hide_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[     itm.coarse_tunic,       itm.leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[     itm.leather_apron,      itm.hide_boots],     def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[     itm.leather_jerkin,     itm.hide_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
  ["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[     itm.leather_apron,       itm.nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
  ["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[     itm.leather_jerkin,     itm.hide_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[     itm.leather_apron,       itm.nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[     itm.coarse_tunic,       itm.leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[ itm.leather_jerkin,     itm.hide_boots],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[ itm.leather_apron,     itm.nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_12_master_craftsman", "{!}Town 12 Craftsman", "{!}Town 12 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[ itm.coarse_tunic,       itm.leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_13_master_craftsman", "{!}Town 13 Craftsman", "{!}Town 13 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[ itm.leather_jerkin,     itm.hide_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_14_master_craftsman", "{!}Town 14 Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[ itm.leather_apron,      itm.hide_boots],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_15_master_craftsman", "{!}Town 15 Craftsman", "{!}Town 15 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[ itm.leather_apron,      itm.hide_boots],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_16_master_craftsman", "{!}Town 16 Craftsman", "{!}Town 16 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[ itm.leather_apron,      itm.hide_boots],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
  ["town_17_master_craftsman", "{!}Town 17 Craftsman", "{!}Town 17 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[ itm.leather_apron,      itm.nomad_boots],     def_attrib|level(2),wp(20),knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
  ["town_18_master_craftsman", "{!}Town 18 Craftsman", "{!}Town 18 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[ itm.leather_apron,      itm.nomad_boots],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0051003a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_19_master_craftsman", "{!}Town 19 Craftsman", "{!}Town 19 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[ itm.sarranid_cloth_robe,   itm.sarranid_boots_a],     def_attrib|level(2),wp(20),knows_common, 0x000000002408714852a432e88aaa42e100000000001e284e0000000000000000],
  ["town_20_master_craftsman", "{!}Town 20 Craftsman", "{!}Town 20 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[ itm.sarranid_cloth_robe_b, itm.sarranid_boots_a],     def_attrib|level(2),wp(20),knows_common, 0x000000001104749136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_21_master_craftsman", "{!}Town 21 Craftsman", "{!}Town 21 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[ itm.sarranid_cloth_robe,   itm.sarranid_boots_b],     def_attrib|level(2),wp(20),knows_common, 0x00000000131072d3351c6e43226ec96c000000000005b5240000000000000000],
  ["town_22_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 22 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac.neutral,[ itm.sarranid_cloth_robe_b, itm.sarranid_boots_b],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c758a5723b1a3148dc455000000000015ab920000000000000000],
  
# Chests
  ["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac.neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],  
  ["bonus_chest_0","{!}Zendar Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac.neutral, [itm.light_mail_and_plate,itm.mail_and_plate,itm.shield_kite_g,itm.shield_kite_h,itm.shield_kite_i,itm.shield_kite_k],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_1","{!}Four Ways Inn Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac.neutral,[itm.hood_b,itm.hood_c,itm.hood_d,itm.double_axe,itm.norman_shield_1,itm.norman_shield_2,itm.norman_shield_3,itm.norman_shield_4,itm.norman_shield_5,itm.norman_shield_6,itm.norman_shield_7,itm.norman_shield_8],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_2","{!}Salt Mine Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac.neutral,[itm.burlap_tunic,itm.stone_hammer,itm.polehammer],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_3","{!}Dhorak Keep Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac.neutral,[itm.pilgrim_disguise,itm.pilgrim_hood,itm.broadsword],def_attrib|level(18),wp(60),knows_common, 0],

# These are used as arrays in the scripts.
  ["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac.neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac.neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac.neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

  ["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac.neutral,[],def_attrib,0,knows_common,0],
  ["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac.neutral,[],def_attrib,0,knows_common,0],

  ["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac.neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac.neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac.neutral,[],def_attrib,0,knows_common,0],

  ["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac.neutral,[],def_attrib,0,knows_common,0],

  ["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac.neutral,[],def_attrib,0,knows_common,0],

# Add Extra Quest NPCs below this point  

  ["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac.commoners,[itm.leather_apron,itm.leather_boots,itm.butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac.commoners,
   [itm.cleaver,itm.knife,itm.pitch_fork,itm.sickle,itm.club,itm.stones,itm.leather_cap,itm.felt_hat,itm.felt_hat,itm.linen_tunic,itm.coarse_tunic,itm.nomad_boots,itm.wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["trainee_peasant","Peasant","Peasants",tf_guarantee_armor,0,reserved,fac.commoners,
   [itm.cleaver,itm.knife,itm.pitch_fork,itm.sickle,itm.club,itm.stones,itm.leather_cap,itm.felt_hat,itm.felt_hat,itm.linen_tunic,itm.coarse_tunic,itm.nomad_boots,itm.wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.short_tunic,itm.linen_tunic,itm.coarse_tunic, itm.tabard, itm.leather_vest, itm.woolen_hose, itm.nomad_boots, itm.blue_hose, itm.wrapping_boots, itm.fur_hat, itm.leather_cap, itm.sword_medieval_b, itm.throwing_daggers],
   def_attrib|str_24|agi_25|level(26),wp(180),knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,man_face_middle_1, man_face_old_2],
   
  ["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners,
   [itm.short_tunic,itm.linen_tunic,itm.coarse_tunic, itm.tabard, itm.leather_vest, itm.woolen_hose, itm.nomad_boots, itm.blue_hose, itm.wrapping_boots, itm.fur_hat, itm.leather_cap, itm.sword_viking_1],
   def_attrib|str_20|agi_8|level(15),wp(120),knows_common|knows_power_strike_2|knows_ironflesh_9,    bandit_face1, bandit_face2],
  ["hired_assassin","Hired Assassin","Hired Assassin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac.commoners, #they look like belligerent drunks
   [itm.short_tunic,itm.linen_tunic,itm.coarse_tunic, itm.tabard, itm.leather_vest, itm.woolen_hose, itm.nomad_boots, itm.blue_hose, itm.wrapping_boots, itm.fur_hat, itm.leather_cap, itm.sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

  ["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac.neutral,
   [itm.sword_viking_1,itm.leather_jerkin,itm.leather_boots,itm.courser,itm.leather_gloves],
   def_attrib|agi_11|level(20),wp(130),knows_common,man_face_middle_1, man_face_older_2],
  ["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac.neutral,
   [itm.sword_medieval_b,itm.leather_jerkin,itm.leather_boots,itm.courser,itm.leather_gloves],
   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],

  ["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac.commoners,
   [itm.robe, itm.black_hood, itm.wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,woman_face_1, woman_face_2],   
  ["temporary_minister","Minister","Minister",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac.commoners,
   [itm.rich_outfit, itm.wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],   

  ["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac.player_faction, [itm.padded_cloth,itm.nomad_boots, itm.splinted_leather_greaves, itm.skullcap, itm.sword_medieval_b,  itm.crossbow, itm.bolts, itm.plate_covered_round_shield],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

#Multiplayer ai troops
  ["swadian_crossbowman_multiplayer_ai","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac.kingdom_1,
   [itm.bolts,itm.crossbow,itm.sword_medieval_a,itm.tab_shield_heater_b,
    itm.leather_jerkin,itm.leather_armor,itm.ankle_boots,itm.footman_helmet],
   def_attrib|level(19),wp_melee(90)|wp_crossbow(100),knows_common|knows_ironflesh_4|knows_athletics_6|knows_shield_5|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer_ai","Swadian Infantry","Swadian Infantry",tf_guarantee_all_wo_ranged,0,0,fac.kingdom_1,
   [itm.pike,itm.bastard_sword_a,itm.tab_shield_heater_c,
    itm.studded_leather_coat,itm.ankle_boots,itm.flat_topped_helmet],
   def_attrib|level(19),wp_melee(105),knows_common|knows_ironflesh_5|knows_shield_4|knows_power_strike_5|knows_athletics_4,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac.kingdom_1,
   [itm.lance,itm.bastard_sword_a,itm.tab_shield_heater_cav_a,
    itm.mail_with_surcoat,itm.hide_boots,itm.norman_helmet,itm.hunter],
   def_attrib|level(19),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_4|knows_shield_4|knows_power_strike_4|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer_ai","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac.kingdom_2,
   [itm.arrows,itm.scimitar,itm.nomad_bow,
    itm.leather_vest,itm.nomad_boots,itm.spiked_helmet,itm.nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_4|knows_power_draw_5|knows_athletics_6|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer_ai","Vaegir Spearman","Vaegir Spearmen",tf_guarantee_all_wo_ranged,0,0,fac.kingdom_2,
   [itm.padded_leather,itm.nomad_boots,itm.spiked_helmet,itm.nomad_cap, itm.spear, itm.tab_shield_kite_b, itm.mace_1, itm.javelin],
   def_attrib|str_12|level(19),wp_melee(90),knows_ironflesh_4|knows_athletics_6|knows_power_throw_3|knows_power_strike_3|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer_ai","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac.kingdom_2,
   [itm.battle_axe,itm.scimitar,itm.lance,itm.tab_shield_kite_cav_a,
     itm.studded_leather_coat,itm.lamellar_vest,itm.nomad_boots,itm.spiked_helmet,itm.saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_4|knows_ironflesh_4|knows_power_strike_4|knows_shield_3,vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_dismounted_lancer_multiplayer_ai","Khergit Dismounted Lancer","Khergit Dismounted Lancer",tf_guarantee_all_wo_ranged,0,0,fac.kingdom_3,
   [itm.sword_khergit_4,itm.spiked_mace,itm.one_handed_war_axe_b,itm.one_handed_war_axe_a,itm.hafted_blade_a,itm.hafted_blade_b,itm.heavy_lance,itm.lance,
    itm.khergit_cavalry_helmet,itm.khergit_war_helmet,itm.lamellar_vest_khergit,itm.tribal_warrior_outfit,itm.khergit_leather_boots,itm.splinted_leather_greaves,itm.leather_gloves,itm.mail_mittens,itm.tab_shield_small_round_b,itm.tab_shield_small_round_c],
   def_attrib|level(19),wp(100),knows_riding_4|knows_power_strike_1|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_1|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer_ai","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac.kingdom_3,
   [itm.sword_khergit_3,itm.khergit_bow,itm.khergit_arrows,itm.tab_shield_small_round_b,
    itm.khergit_cavalry_helmet,itm.tribal_warrior_outfit,itm.khergit_leather_boots,itm.steppe_horse],
   def_attrib|level(19),wp(90)|wp_archery(100),knows_riding_6|knows_power_draw_5|knows_shield_2|knows_horse_archery_5,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer_ai","Khergit Lancer","Khergit Lancers",tf_guarantee_all_wo_ranged,0,0,fac.kingdom_3,
   [itm.sword_khergit_4,itm.spiked_mace,itm.one_handed_war_axe_b,itm.one_handed_war_axe_a,itm.hafted_blade_a,itm.hafted_blade_b,itm.heavy_lance,itm.lance,
    itm.khergit_guard_helmet,itm.khergit_cavalry_helmet,itm.khergit_war_helmet,itm.lamellar_vest_khergit,itm.lamellar_armor,itm.khergit_leather_boots,itm.splinted_leather_greaves,itm.leather_gloves,itm.mail_mittens,itm.scale_gauntlets,itm.tab_shield_small_round_b,itm.tab_shield_small_round_c,itm.courser],
   def_attrib|level(19),wp(100),knows_riding_7|knows_power_strike_2|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_1|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["nord_veteran_multiplayer_ai","Nord Footman","Nord Footmen",tf_guarantee_all_wo_ranged,0,0,fac.kingdom_4,
   [itm.sword_viking_2,itm.one_handed_battle_axe_b,itm.two_handed_axe,itm.tab_shield_round_d,itm.throwing_axes,
    itm.nordic_helmet,itm.nordic_fighter_helmet,itm.mail_hauberk,itm.splinted_leather_greaves,itm.leather_boots,itm.leather_gloves],
   def_attrib|level(19),wp(130),knows_ironflesh_3|knows_power_strike_5|knows_power_throw_3|knows_athletics_5|knows_shield_3,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer_ai","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac.kingdom_4,
   [itm.javelin,itm.sword_viking_1,itm.two_handed_axe,itm.spear,itm.tab_shield_round_a,
    itm.skullcap,itm.nordic_archer_helmet,itm.leather_jerkin,itm.leather_boots,itm.saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,nord_face_young_1, nord_face_older_2],
  ["nord_archer_multiplayer_ai","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac.kingdom_4,
   [itm.arrows,itm.two_handed_axe,itm.sword_viking_2,itm.short_bow,
    itm.leather_jerkin,itm.blue_tunic,itm.leather_boots,itm.nasal_helmet,itm.leather_cap],
   def_attrib|str_11|level(19),wp_melee(80)|wp_archery(110),knows_ironflesh_4|knows_power_strike_2|knows_shield_1|knows_power_draw_5|knows_athletics_6,nord_face_young_1, nord_face_old_2],
  ["rhodok_veteran_crossbowman_multiplayer_ai","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac.kingdom_5,
   [itm.fighting_pick,itm.club_with_spike_head,itm.maul,itm.tab_shield_pavise_c,itm.heavy_crossbow,itm.bolts,
    itm.leather_cap,itm.padded_leather,itm.nomad_boots],
   def_attrib|level(19),wp_melee(100)|wp_crossbow(120),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_3|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman_multiplayer_ai","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_all_wo_ranged,0,0,fac.kingdom_5,
   [itm.ashwood_pike,itm.war_spear,itm.pike,itm.club_with_spike_head,itm.sledgehammer,itm.tab_shield_pavise_c,itm.sword_medieval_a,
    itm.leather_cap,itm.byrnie,itm.ragged_outfit,itm.nomad_boots],
   def_attrib|level(19),wp(115),knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai","Rhodok Scout","Rhodok Scouts",tf_mounted|tf_guarantee_all,0,0,fac.kingdom_5,
   [itm.sword_medieval_a,itm.tab_shield_heater_cav_a,itm.light_lance,itm.skullcap,itm.aketon_green,
    itm.ragged_outfit,itm.nomad_boots,itm.ankle_boots,itm.saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,rhodok_face_young_1, rhodok_face_older_2],
  ["sarranid_infantry_multiplayer_ai","Sarranid Infantry","Sarranid Infantry",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac.kingdom_6,
   [itm.sarranid_mail_shirt,itm.sarranid_horseman_helmet,itm.sarranid_boots_b,itm.sarranid_boots_c,itm.splinted_leather_greaves,itm.arabian_sword_b,itm.mace_3,itm.spear,itm.tab_shield_kite_c],
   def_attrib|level(20),wp_melee(105),knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3,sarranid_face_middle_1, sarranid_face_old_2],
  ["sarranid_archer_multiplayer_ai","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_6,
   [itm.arrows,itm.nomad_bow,itm.arabian_sword_a,itm.archers_vest,itm.sarranid_boots_b,itm.sarranid_helmet1,itm.turban,itm.desert_turban],
   def_attrib|level(19),wp_melee(90)|wp_archery(100),knows_common|knows_riding_2|knows_ironflesh_1,sarranid_face_young_1, sarranid_face_old_2],
  ["sarranid_horseman_multiplayer_ai","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac.kingdom_6,
   [itm.lance,itm.arabian_sword_b,itm.scimitar_b,itm.mace_4,itm.tab_shield_small_round_b,
    itm.sarranid_mail_shirt,itm.sarranid_boots_b,itm.sarranid_boots_c,itm.sarranid_horseman_helmet,itm.courser,itm.hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,sarranid_face_young_1, sarranid_face_old_2],

#Multiplayer troops (they must have the base items only, nothing else)
  ["swadian_crossbowman_multiplayer","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac.kingdom_1,
   [itm.bolts,itm.crossbow,itm.sword_medieval_b_small,itm.tab_shield_heater_a,itm.red_shirt,itm.ankle_boots],
   str_14 | agi_15 |def_attrib_multiplayer|level(19),wpe(90,60,180,90,60),knows_common_multiplayer|knows_ironflesh_2|knows_athletics_4|knows_shield_5|knows_power_strike_2|knows_riding_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac.kingdom_1,
   [itm.sword_medieval_a,itm.tab_shield_heater_a,itm.red_tunic,itm.ankle_boots],
   str_15 | agi_15 |def_attrib_multiplayer|level(20),wpex(105,130,110,40,60,110,40),knows_common_multiplayer|knows_ironflesh_5|knows_shield_4|knows_power_strike_4|knows_power_throw_2|knows_athletics_6|knows_riding_1,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac.kingdom_1,
   [itm.lance,itm.sword_medieval_a,itm.tab_shield_heater_a,itm.red_tunic,itm.ankle_boots,itm.saddle_horse],
   str_14 | agi_16 |def_attrib_multiplayer|level(20),wp_melee(110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_3|knows_shield_2|knows_power_throw_2|knows_power_strike_3|knows_athletics_3,swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac.kingdom_2,
   [itm.arrows,itm.mace_1,itm.nomad_bow,itm.linen_tunic,itm.hide_boots],
   str_14 | agi_14 |def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80,60),knows_common_multiplayer|knows_ironflesh_2|knows_power_draw_7|knows_athletics_3|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac.kingdom_2,
   [itm.spear, itm.tab_shield_kite_a, itm.mace_1,itm.linen_tunic,itm.hide_boots],
   str_15 | agi_15 |def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120,50),knows_common_multiplayer|knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_4|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac.kingdom_2,
   [itm.scimitar,itm.lance,itm.tab_shield_kite_cav_a,itm.linen_tunic,itm.hide_boots,itm.saddle_horse],
   str_16 | agi_15 |def_attrib_multiplayer|level(19),wpe(110,90,60,110,60),knows_common_multiplayer|knows_riding_5|knows_ironflesh_4|knows_power_strike_3|knows_shield_3|knows_power_throw_4|knows_horse_archery_1,vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac.kingdom_3,
   [itm.sword_khergit_1,itm.nomad_bow,itm.arrows,itm.khergit_armor,itm.leather_steppe_cap_a,itm.hide_boots,itm.steppe_horse],
   str_15 | agi_18 |def_attrib_multiplayer|level(21),wpe(70,142,60,100,60),knows_common_multiplayer|knows_riding_2|knows_power_draw_5|knows_horse_archery_3|knows_athletics_3|knows_shield_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_infantry_multiplayer","Khergit Infantry","Khergit Infantry",tf_guarantee_all,0,0,fac.kingdom_3,
   [itm.sword_khergit_1,itm.spear,itm.tab_shield_small_round_a,itm.steppe_armor,itm.hide_boots,itm.leather_gloves],
   str_14 | agi_15 |def_attrib_multiplayer|level(19),wp(110),knows_common_multiplayer|knows_ironflesh_3|knows_power_throw_3|knows_shield_4|knows_power_strike_3|knows_athletics_6|knows_riding_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac.kingdom_3,
   [itm.sword_khergit_1,itm.lance,itm.tab_shield_small_round_a,itm.khergit_armor,itm.leather_steppe_cap_a,itm.hide_boots,itm.steppe_horse],
   str_15 | agi_14 |def_attrib_multiplayer|level(21),wp(115),knows_common_multiplayer|knows_riding_6|knows_ironflesh_3|knows_power_throw_3|knows_shield_4|knows_power_strike_3|knows_athletics_4,khergit_face_middle_1, khergit_face_older_2],
  ["nord_archer_multiplayer","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac.kingdom_4,
   [itm.arrows,itm.sword_viking_2_small,itm.short_bow,itm.blue_tunic,itm.leather_boots],
   str_15 | agi_14 |def_attrib_multiplayer|str_11|level(15),wpe(90,150,60,80,60),knows_common_multiplayer|knows_ironflesh_2|knows_power_strike_2|knows_shield_3|knows_power_draw_5|knows_athletics_3|knows_riding_1,nord_face_young_1, nord_face_old_2],
  ["nord_veteran_multiplayer","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac.kingdom_4,
   [itm.sword_viking_1,itm.one_handed_war_axe_a,itm.tab_shield_round_a,itm.blue_tunic,itm.leather_boots],
   str_17 | agi_15 |def_attrib_multiplayer|level(24),wpex(110,135,100,40,60,140,60),knows_common_multiplayer|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6|knows_shield_3|knows_riding_1,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac.kingdom_4,
   [itm.javelin,itm.sword_viking_1,itm.spear,itm.tab_shield_small_round_a,itm.blue_tunic,itm.leather_boots,itm.saddle_horse],
   str_16 | agi_15 |def_attrib_multiplayer|level(19),wp(105),knows_common_multiplayer|knows_riding_6|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_3|knows_power_throw_3|knows_athletics_3,vaegir_face_young_1, vaegir_face_older_2],
  ["rhodok_veteran_crossbowman_multiplayer","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac.kingdom_5,
   [itm.crossbow,itm.bolts,itm.fighting_pick,itm.tab_shield_pavise_a,itm.tunic_with_green_cape,itm.ankle_boots],
   str_16 | agi_15 |def_attrib_multiplayer|level(20),wpe(100,60,180,90,60),knows_common_multiplayer|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_4|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sergeant_multiplayer","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac.kingdom_5,
   [itm.fighting_pick,itm.tab_shield_pavise_a,itm.spear,itm.green_tunic,itm.ankle_boots],
   str_16 | agi_14 |def_attrib_multiplayer|level(20),wpex(110,100,140,30,50,110,50),knows_common_multiplayer|knows_ironflesh_4|knows_shield_5|knows_power_strike_4|knows_power_throw_1|knows_athletics_6|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac.kingdom_5,
   [itm.sword_medieval_a,itm.tab_shield_heater_cav_a, itm.light_lance,itm.green_tunic,itm.ankle_boots,itm.saddle_horse],
   str_15 | agi_15 |def_attrib_multiplayer|level(20),wp(100),knows_common_multiplayer|knows_riding_4|knows_ironflesh_3|knows_shield_3|knows_power_strike_3|knows_power_throw_1|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["sarranid_archer_multiplayer","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac.kingdom_6,
   [itm.arrows,itm.arabian_sword_a,itm.nomad_bow,itm.sarranid_cloth_robe, itm.sarranid_boots_b],
   str_15 | agi_16 |def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80,60),knows_common_multiplayer|knows_ironflesh_4|knows_power_draw_5|knows_athletics_3|knows_shield_2|knows_riding_1|knows_weapon_master_1,sarranid_face_young_1, sarranid_face_older_2],
  ["sarranid_footman_multiplayer","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac.kingdom_6,
   [itm.bamboo_spear, itm.tab_shield_kite_a, itm.arabian_sword_a,itm.sarranid_cloth_robe, itm.sarranid_boots_b],
   str_14 | agi_15 |def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120,50),knows_common_multiplayer|knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_4|knows_athletics_6|knows_riding_1,sarranid_face_young_1, sarranid_face_older_2],
  ["sarranid_mamluke_multiplayer","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac.kingdom_6,
   [itm.arabian_sword_a,itm.lance,itm.tab_shield_small_round_a,itm.sarranid_cloth_robe, itm.sarranid_boots_b,itm.saddle_horse],
   str_15 | agi_14 |def_attrib_multiplayer|level(19),wpe(110,90,60,110,60),knows_common_multiplayer|knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_power_throw_2|knows_weapon_master_1,sarranid_face_young_1, sarranid_face_older_2],

  ["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac.kingdom_5, [], 0, 0, 0, 0, 0],
 
#Player history array
  ["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac.commoners,[itm.leather_apron,itm.leather_boots,itm.butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac.commoners,[itm.leather_apron,itm.leather_boots,itm.butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac.commoners,[itm.leather_apron,itm.leather_boots,itm.butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac.commoners,[itm.leather_apron,itm.leather_boots,itm.butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac.commoners,[itm.leather_apron,itm.leather_boots,itm.butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac.commoners,[itm.leather_apron,itm.leather_boots,itm.butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac.commoners,[itm.leather_apron,itm.leather_boots,itm.butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac.commoners,[itm.leather_apron,itm.leather_boots,itm.butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac.commoners,[itm.leather_apron,itm.leather_boots,itm.butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],

  ["quick_battle_troop_1","Rodrigo de Braganca","Rodrigo de Braganca", tf_hero,0,0,fac.kingdom_1,
   [itm.long_hafted_knobbed_mace, itm.wooden_shield, itm.iron_staff, itm.throwing_daggers,
    itm.felt_hat, itm.fur_coat, itm.light_leather_boots, itm.leather_gloves],
   str_9|agi_15|int_12|cha_12|level(15),wpex(109,33,132,15,32,100,15),knows_riding_3|knows_athletics_5|knows_shield_3|knows_weapon_master_3|knows_power_throw_3|knows_power_strike_2|knows_ironflesh_3,0x0000000e240070cd598bb02b9556428c00000000001eabce0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_2","Usiatra","Usiatra", tf_hero|tf_female,0,0,fac.kingdom_1,
   [itm.nomad_bow, itm.barbed_arrows, itm.scimitar, itm.tab_shield_small_round_c, itm.sumpter_horse,
    itm.leather_armor, itm.splinted_greaves],
   str_12|agi_14|int_11|cha_18|level(22),wpex(182,113,112,159,82,115,55),knows_horse_archery_2|knows_riding_3|knows_athletics_4|knows_shield_2|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_1|knows_power_strike_3|knows_ironflesh_4,0x000000007f004000719b69422165b71300000000001d5d1d0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_3","Hegen","Hegen", tf_hero,0,0,fac.kingdom_1,
   [itm.heavy_lance, itm.sword_two_handed_b, itm.sword_medieval_c, itm.tab_shield_heater_c, itm.warhorse,
    itm.guard_helmet, itm.coat_of_plates, itm.mail_mittens, itm.mail_boots],
   str_18|agi_16|int_12|cha_11|level(24),wpex(90,152,102,31,33,34,30),knows_riding_5|knows_athletics_5|knows_shield_3|knows_weapon_master_5|knows_power_strike_6|knows_ironflesh_6,0x000000018000324428db8a431491472400000000001e44a90000000000000000, swadian_face_old_2],
  ["quick_battle_troop_4","Konrad","Konrad", tf_hero,0,0,fac.kingdom_1,
   [itm.sword_two_handed_a, itm.mace_4, itm.tab_shield_kite_d,
    itm.bascinet_3, itm.scale_armor, itm.mail_mittens, itm.mail_boots],
   str_18|agi_15|int_12|cha_12|level(24),wpex(130,150,130,30,50,90,30),knows_riding_2|knows_athletics_5|knows_shield_4|knows_weapon_master_5|knows_power_throw_3|knows_power_strike_6|knows_ironflesh_6,0x000000081700205434db6df4636db8e400000000001db6e30000000000000000, swadian_face_old_2],
  ["quick_battle_troop_5","Sverre","Sverre", tf_hero,0,0,fac.kingdom_1,
   [itm.long_axe, itm.sword_viking_1, itm.light_throwing_axes, itm.tab_shield_round_d,
    itm.nordic_fighter_helmet, itm.byrnie, itm.leather_gloves, itm.leather_boots],
   str_15|agi_15|int_12|cha_12|level(21),wpex(110,130,110,80,15,110,15),knows_riding_1|knows_athletics_5|knows_shield_4|knows_weapon_master_5|knows_power_draw_2|knows_power_throw_4|knows_power_strike_5|knows_ironflesh_5,0x000000048a00024723134e24cb51c91b00000000001dc6aa0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_6","Borislav","Borislav", tf_hero,0,0,fac.kingdom_1,
   [itm.strong_bow, itm.barbed_arrows, itm.barbed_arrows, itm.shortened_spear,
    itm.leather_warrior_cap, itm.leather_jerkin, itm.leather_gloves, itm.ankle_boots],
   str_12|agi_15|int_15|cha_9|level(18),wpex(70,70,100,140,15,100,15),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_weapon_master_3|knows_power_draw_4|knows_power_throw_3|knows_power_strike_2|knows_ironflesh_2,0x000000089e00444415136e36e34dc8e400000000001d46d90000000000000000, swadian_face_old_2],
  ["quick_battle_troop_7","Stavros","Stavros", tf_hero,0,0,fac.kingdom_1,
   [itm.heavy_crossbow, itm.bolts, itm.sword_medieval_b_small, itm.tab_shield_pavise_c,
    itm.nasal_helmet, itm.padded_leather, itm.leather_gloves, itm.leather_boots],
   str_12|agi_15|int_15|cha_12|level(21),wpex(100,70,70,30,140,80,30),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_shield_3|knows_weapon_master_5|knows_power_throw_2|knows_power_strike_4|knows_ironflesh_4,0x0000000e1400659226e34dcaa46e36db00000000001e391b0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_8","Gamara","Gamara", tf_hero|tf_female,0,0,fac.kingdom_1,
   [itm.throwing_spears, itm.throwing_spears, itm.scimitar, itm.leather_covered_round_shield,
    itm.desert_turban, itm.skirmisher_armor, itm.leather_gloves, itm.sarranid_boots_b],
   str_12|agi_15|int_12|cha_12|level(18),wpex(100,40,100,85,15,130,15),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_shield_2|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_4|knows_power_strike_2|knows_ironflesh_2,0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_9","Aethrod","Aethrod", tf_hero,0,0,fac.kingdom_1,
   [itm.nomad_bow, itm.barbed_arrows, itm.barbed_arrows, itm.scimitar_b,
    itm.splinted_greaves, itm.lamellar_vest],
   str_16|agi_21|int_12|cha_14|level(26),wpex(182,113,112,159,82,115,65),knows_horse_archery_2|knows_riding_2|knows_athletics_7|knows_shield_2|knows_weapon_master_4|knows_power_draw_7|knows_power_throw_3|knows_power_strike_3|knows_ironflesh_4,0x000000000000210536db6db6db6db6db00000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_10","Zaira","Zaira", tf_hero|tf_female,0,0,fac.kingdom_1,
   [itm.sarranid_cavalry_sword, itm.strong_bow, itm.bodkin_arrows, itm.bodkin_arrows, itm.arabian_horse_b,
    itm.sarranid_felt_head_cloth_b, itm.sarranid_common_dress, itm.sarranid_boots_b],
   str_13|agi_18|int_15|cha_9|level(18),wpex(126,19,23,149,41,26,30),knows_horse_archery_6|knows_riding_6|knows_weapon_master_2|knows_power_draw_4|knows_power_throw_1|knows_power_strike_4|knows_ironflesh_1,0x0000000502003001471a6a24dc6594cb00000000001da4840000000000000000, swadian_face_old_2],
  ["quick_battle_troop_11","Argo Sendnar","Argo Sendnar", tf_hero,0,0,fac.kingdom_1,
   [itm.morningstar, itm.tab_shield_round_d, itm.war_spear, itm.courser,
    itm.leather_gloves, itm.fur_hat, itm.leather_boots, itm.leather_jacket],
   str_15|agi_12|int_14|cha_20|level(28),wpex(101,35,136,15,17,19,15),knows_riding_4|knows_athletics_2|knows_shield_4|knows_weapon_master_4|knows_power_strike_5|knows_ironflesh_5,0x0000000e800015125adb702de3459a9c00000000001ea6d00000000000000000, swadian_face_old_2],
  ["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac.kingdom_5, [], 0, 0, 0, 0, 0],

  ["tutorial_fighter_1","Novice Fighter","Fighters",tf_hero,0,0,fac.kingdom_2,
   [itm.linen_tunic,itm.nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_2","Novice Fighter","Fighters",tf_hero,0,0,fac.kingdom_2,
   [itm.green_tunic,itm.nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_3","Regular Fighter","Fighters",tf_hero,0,0,fac.kingdom_2,
   [itm.green_tunic,itm.nomad_boots],
   def_attrib|level(9),wp_melee(50),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_4","Veteran Fighter","Fighters",tf_hero,0,0,fac.kingdom_2,
   [itm.linen_tunic,itm.nomad_boots],
   def_attrib|level(16),wp_melee(110),knows_athletics_1|knows_ironflesh_3|knows_power_strike_2|knows_shield_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000, vaegir_face_older_2],
  ["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac.kingdom_2,
   [itm.leather_jerkin,itm.leather_vest,itm.nomad_boots,itm.vaegir_spiked_helmet,itm.vaegir_fur_helmet,itm.vaegir_fur_cap,itm.nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac.kingdom_2,
   [itm.linen_tunic,itm.nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000, vaegir_face_older_2],
  ["tutorial_rider_1","Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac.kingdom_2,
   [itm.green_tunic,itm.hunter, itm.saddle_horse,itm.leather_gloves],
   def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["tutorial_rider_2","Horse archer","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac.kingdom_3,
   [itm.tribal_warrior_outfit,itm.nomad_robe,itm.hide_boots,itm.tab_shield_small_round_a,itm.steppe_horse],
   def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,khergit_face_young_1, khergit_face_older_2],
  ["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac.kingdom_2,
   [itm.leather_vest,itm.nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000, vaegir_face_older_2],
   
  ["swadian_merchant", "Merchant of Praven", "{!}Prominent", tf_hero, 0, reserved, fac.kingdom_1, [itm.light_leather_boots, itm.rich_outfit, itm.sword_medieval_c_small], def_attrib|level(2),wp(20),knows_common, 0x0000000a2910305135ac7169644c5d6400000000001e5b2b0000000000000000, 0x0000000a2910305135ac7169644c5d6400000000001e5b2b0000000000000000],
  ["vaegir_merchant", "Merchant of Reyvadin", "{!}Prominent", tf_hero, 0, reserved, fac.kingdom_2, [itm.fur_hat, itm.leather_jacket, itm.leather_gloves, itm.hide_boots, itm.sword_viking_2_small], def_attrib|level(2),wp(20),knows_common, 0x0000000b3f0402cf48e49bc55b91f7a400000000001dc6b50000000000000000, 0x0000000b3f0402cf48e49bc55b91f7a400000000001dc6b50000000000000000],
  ["khergit_merchant", "Merchant of Tulga", "{!}Prominent", tf_hero, 0, reserved, fac.kingdom_3, [itm.khergit_leather_boots, itm.leather_gloves, itm.nomad_vest, itm.nomad_cap, itm.sword_khergit_3], def_attrib|level(2),wp(20),knows_common, 0x00000008e610338d151dab4b1b516a7800000000001e52eb0000000000000000, 0x00000008e610338d151dab4b1b516a7800000000001e52eb0000000000000000],
  ["nord_merchant", "Merchant of Sargoth", "{!}Prominent", tf_hero, 0, reserved, fac.kingdom_4, [itm.sword_viking_2_small, itm.leather_gloves, itm.light_leather_boots, itm.light_leather], def_attrib|level(2),wp(20),knows_common, 0x000000091900130f232355ab5d5338dd00000000001eb95c0000000000000000, 0x000000091900130f232355ab5d5338dd00000000001eb95c0000000000000000],
  ["rhodok_merchant", "Merchant of Jelkala", "{!}Prominent", tf_hero, 0, reserved, fac.kingdom_5, [itm.khergit_leather_boots, itm.courtly_outfit, itm.sword_medieval_c_small], def_attrib|level(2),wp(20),knows_common, 0x00000008b30c20c565344cd95d52272b00000000001dcb290000000000000000, 0x00000008b30c20c565344cd95d52272b00000000001dcb290000000000000000],
  ["sarranid_merchant", "Merchant of Shariz", "{!}Prominent", tf_hero, 0, reserved, fac.kingdom_6, [itm.scimitar, itm.sarranid_boots_b, itm.sarranid_cavalry_robe, itm.headcloth], def_attrib|level(2),wp(20),knows_common, 0x000000093f0071c0376cb222eaba472600000000001e30190000000000000000, 0x000000093f0071c0376cb222eaba472600000000001e30190000000000000000],   
  ["default_merchant", "Rich Merchant", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac.commoners, [itm.sword_two_handed_a, itm.rich_outfit, itm.hide_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],

  ["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac.kingdom_2,
   [itm.linen_tunic,itm.nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2, 0x00000000320410022d2595495491afa400000000001d9ae30000000000000000, mercenary_face_2],   
  ["looter_leader","Robber","Looters",tf_hero,0,0,fac.outlaws,
   [itm.hatchet,itm.club,itm.butchering_knife,itm.falchion,itm.rawhide_coat,itm.stones,itm.nomad_armor,itm.nomad_armor,itm.woolen_cap,itm.woolen_cap,itm.nomad_boots,itm.wrapping_boots],
   def_attrib|level(4),wp(20),knows_common,0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2],

]


#Troop upgrade declarations

upgrade(troops,"farmer", "watchman")
upgrade(troops,"townsman","watchman")
upgrade2(troops,"watchman","mercenary_footman","caravan_guard")
upgrade2(troops,"mercenary_footman","mercenary_swordsman","mercenary_crossbowman")
upgrade2(troops,"mercenary_archer","mercenary_horse_archer","mercenary_longbowman")
upgrade(troops,"mercenary_swordsman","hired_blade")
upgrade2(troops,"caravan_guard","mercenary_horseman","mercenary_horse_archer")
upgrade(troops,"mercenary_horseman","mercenary_cavalry")

upgrade(troops,"swadian_recruit","swadian_militia")
upgrade2(troops,"swadian_militia","swadian_footman","swadian_skirmisher")
upgrade2(troops,"swadian_footman","swadian_man_at_arms","swadian_infantry")
upgrade(troops,"swadian_infantry","swadian_sergeant")
upgrade(troops,"swadian_skirmisher","swadian_crossbowman")
upgrade(troops,"swadian_crossbowman","swadian_sharpshooter")
upgrade(troops,"swadian_man_at_arms","swadian_knight")

upgrade(troops,"vaegir_recruit","vaegir_footman")
upgrade2(troops,"vaegir_footman","vaegir_veteran","vaegir_skirmisher")
upgrade(troops,"vaegir_skirmisher","vaegir_archer")
upgrade(troops,"vaegir_archer","vaegir_marksman")
upgrade2(troops,"vaegir_veteran","vaegir_horseman","vaegir_infantry")
upgrade(troops,"vaegir_infantry","vaegir_guard")
upgrade(troops,"vaegir_raider","vaegir_horseman")
upgrade(troops,"vaegir_horseman","vaegir_knight")

upgrade(troops,"khergit_tribesman","khergit_skirmisher")
upgrade2(troops,"khergit_skirmisher","khergit_horseman","khergit_horse_archer")
upgrade(troops,"khergit_horseman","khergit_lancer")
upgrade(troops,"khergit_lancer","khergit_guard")
upgrade(troops,"khergit_horse_archer","khergit_veteran_horse_archer")
upgrade(troops,"khergit_veteran_horse_archer","khergit_guard")

upgrade2(troops,"nord_recruit","nord_footman","nord_huntsman")
upgrade(troops,"nord_footman","nord_trained_footman")
upgrade(troops,"nord_trained_footman","nord_warrior")
upgrade(troops,"nord_warrior","nord_veteran")
upgrade(troops,"nord_veteran","nord_champion")
upgrade(troops,"nord_huntsman","nord_archer")
upgrade(troops,"nord_archer","nord_veteran_archer")
upgrade(troops,"nord_handgunner","nord_shocktrooper")

upgrade2(troops,"rhodok_recruit","rhodok_spearman","rhodok_crossbowman")
upgrade(troops,"rhodok_spearman","rhodok_trained_spearman")
upgrade(troops,"rhodok_trained_spearman","rhodok_veteran_spearman")
upgrade(troops,"rhodok_veteran_spearman","rhodok_sergeant")
upgrade(troops,"rhodok_crossbowman","rhodok_trained_crossbowman")
upgrade(troops,"rhodok_trained_crossbowman","rhodok_veteran_crossbowman")
upgrade(troops,"rhodok_veteran_crossbowman","rhodok_sharpshooter")

upgrade(troops,"sarranid_recruit","sarranid_footman")
upgrade2(troops,"sarranid_footman","sarranid_veteran_footman","sarranid_skirmisher")
upgrade2(troops,"sarranid_veteran_footman","sarranid_horseman","sarranid_infantry")
upgrade(troops,"sarranid_infantry","sarranid_guard")
upgrade(troops,"sarranid_skirmisher","sarranid_archer")
upgrade(troops,"sarranid_archer","sarranid_master_archer")
upgrade(troops,"sarranid_raider","sarranid_horseman")
upgrade(troops,"sarranid_horseman","sarranid_mamluke")
upgrade(troops,"sarranid_handgunner","sarranid_janissary")

#new tree connections
upgrade(troops,"mountain_bandit","mercenary_footman")
upgrade(troops,"forest_bandit","mercenary_archer")
upgrade(troops,"steppe_bandit","mercenary_horse_archer")
upgrade(troops,"taiga_bandit","mercenary_longbowman")
upgrade(troops,"sea_raider","mercenary_swordsman")
upgrade(troops,"desert_bandit","mercenary_horseman")
#new tree connections ended

upgrade(troops,"looter","bandit")
upgrade2(troops,"bandit","brigand","mercenary_footman")
upgrade(troops,"brigand","mercenary_horseman")

upgrade(troops,"black_khergit_horseman","black_khergit_guard")

upgrade2(troops,"zombie","zombie_spear","zombie_axe")

upgrade(troops,"manhunter","bounty_hunter")
upgrade(troops,"bounty_hunter","knight_errant")

upgrade(troops,"slave_keeper","slave_driver")
upgrade(troops,"slave_driver","slave_hunter")
upgrade(troops,"slave_hunter","slave_crusher")
upgrade(troops,"slave_crusher","slaver_chief")

upgrade(troops,"refugee","follower_woman")
upgrade(troops,"peasant_woman","follower_woman")
upgrade(troops,"follower_woman","hunter_woman")
upgrade2(troops,"hunter_woman","ranger_woman","fighter_woman")
upgrade(troops,"ranger_woman","shield_maiden")
upgrade(troops,"fighter_woman","sword_sister")
