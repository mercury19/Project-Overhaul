from header_common import bignum

###################################################
# header_troops.py
# This file contains declarations for troops
# DO NOT EDIT THIS FILE!
###################################################

#Troop flags
tf_male           = 0
tf_female         = 1
tf_undead         = 2
troop_type_mask   = 0x0000000f
tf_hero              = 0x00000010
tf_inactive          = 0x00000020
tf_unkillable        = 0x00000040
tf_always_fall_dead  = 0x00000080
tf_no_capture_alive  = 0x00000100
tf_mounted           = 0x00000400 #Troop's movement speed on map is determined by riding skill.
tf_is_merchant       = 0x00001000 #When set, troop does not equip stuff he owns
tf_randomize_face    = 0x00008000 #randomize face at the beginning of the game.
tf_allways_fall_dead = tf_always_fall_dead # For compatibility reasons...

tf_guarantee_boots            = 0x00100000
tf_guarantee_armor            = 0x00200000
tf_guarantee_helmet           = 0x00400000
tf_guarantee_gloves           = 0x00800000
tf_guarantee_horse            = 0x01000000
tf_guarantee_shield           = 0x02000000
tf_guarantee_ranged           = 0x04000000
tf_unmoveable_in_party_window = 0x10000000

# Character attributes...
ca_strength     = 0
ca_agility      = 1
ca_intelligence = 2
ca_charisma     = 3

wpt_one_handed_weapon = 0
wpt_two_handed_weapon = 1
wpt_polearm           = 2
wpt_archery           = 3
wpt_crossbow          = 4
wpt_throwing          = 5
wpt_firearm           = 6


#personality modifiers:
# courage 8 means neutral
courage_4  = 0x0004
courage_5  = 0x0005
courage_6  = 0x0006
courage_7  = 0x0007
courage_8  = 0x0008
courage_9  = 0x0009
courage_10 = 0x000A
courage_11 = 0x000B
courage_12 = 0x000C
courage_13 = 0x000D
courage_14 = 0x000E
courage_15 = 0x000F

aggresiveness_1  = 0x0010
aggresiveness_2  = 0x0020
aggresiveness_3  = 0x0030
aggresiveness_4  = 0x0040
aggresiveness_5  = 0x0050
aggresiveness_6  = 0x0060
aggresiveness_7  = 0x0070
aggresiveness_8  = 0x0080
aggresiveness_9  = 0x0090
aggresiveness_10 = 0x00A0
aggresiveness_11 = 0x00B0
aggresiveness_12 = 0x00C0
aggresiveness_13 = 0x00D0
aggresiveness_14 = 0x00E0
aggresiveness_15 = 0x00F0

is_bandit        = 0x0100
#-----------------------------------
#these also in sentences.py
tsf_site_id_mask = 0x0000ffff
tsf_entry_mask   = 0x00ff0000
tsf_entry_bits   = 16

def entry(n):
  return (((n) << tsf_entry_bits) & tsf_entry_mask)
#-------------------------------------

# LAV TWEAKS BEGIN

# Generate constants for attribute levels in [3..64) range.
for index in range(3, 64):
	globals()['str_%d' % index] = bignum | index
	globals()['agi_%d' % index] = bignum | (index << 8)
	globals()['int_%d' % index] = bignum | (index << 16)
	globals()['cha_%d' % index] = bignum | (index << 24)

# LAV TWEAKS END

level_mask       = 0x000000FF
level_bits       = 32

def level(v):
  if (v > level_mask):
    v = level_mask
  return (bignum|v) << level_bits
  
def_attrib = str_5 | agi_5 | int_4 | cha_4

# Weapon proficiencies:
one_handed_bits = 0
two_handed_bits = 10
polearm_bits    = 20
archery_bits    = 30
crossbow_bits   = 40
throwing_bits   = 50
firearm_bits    = 60

num_weapon_proficiencies = 7
def wp_one_handed(x):
  return (((bignum | x) & 0x3FF) << one_handed_bits)
def wp_two_handed(x):
  return (((bignum | x) & 0x3FF) << two_handed_bits)
def wp_polearm(x):
  return (((bignum | x) & 0x3FF) << polearm_bits)
def wp_archery(x):
  return (((bignum | x) & 0x3FF) << archery_bits)
def wp_crossbow(x):
  return (((bignum | x) & 0x3FF) << crossbow_bits)
def wp_throwing(x):
  return (((bignum | x) & 0x3FF) << throwing_bits)
def wp_firearm(x):
  return (((bignum | x) & 0x3FF) << firearm_bits)

def find_troop(troops,troop_id):
  result = -1
  num_troops = len(troops)
  i_troop = 0
  while (i_troop < num_troops) and (result == -1):
    troop = troops[i_troop]
    if (troop[0] == troop_id):
      result = i_troop
    else:
      i_troop += 1
  return result



def upgrade(troops,troop1_id,troop2_id):
  troop1_no = find_troop(troops,troop1_id)
  troop2_no = find_troop(troops,troop2_id)
  if (troop1_no == -1):
    print "Error with upgrade def: Unable to find troop1-id: " + troop1_id
  elif (troop2_no == -1):
    print "Error with upgrade def: Unable to find troop2-id: " + troop2_id
  else:
    cur_troop = troops[troop1_no]
    cur_troop_length = len(cur_troop)
    if cur_troop_length == 11:
      cur_troop[11:11] = [0, 0, 0, troop2_no, 0]
    elif cur_troop_length == 12:
      cur_troop[12:12] = [0, 0, troop2_no, 0]
    elif cur_troop_length == 13:
      cur_troop[13:13] = [0, troop2_no, 0]
    else:
      cur_troop[14:14] = [troop2_no, 0]
      

def upgrade2(troops,troop1_id,troop2_id,troop3_id):
  troop1_no = find_troop(troops,troop1_id)
  troop2_no = find_troop(troops,troop2_id)
  troop3_no = find_troop(troops,troop3_id)
  if (troop1_no == -1):
    print "Error with upgrade2 def: Unable to find troop1-id: " + troop1_id
  elif (troop2_no == -1):
    print "Error with upgrade2 def: Unable to find troop2-id: " + troop2_id
  elif (troop3_no == -1):
    print "Error with upgrade2 def: Unable to find troop3-id: " + troop3_id
  else:
    cur_troop = troops[troop1_no]
    cur_troop_length = len(cur_troop)
    if cur_troop_length == 11:
      cur_troop[11:11] = [0, 0, 0, troop2_no, troop3_no]
    elif cur_troop_length == 12:
      cur_troop[12:12] = [0, 0, troop2_no, troop3_no]
    elif cur_troop_length == 13:
      cur_troop[13:13] = [0, troop2_no, troop3_no]
    else:
      cur_troop[14:14] = [troop2_no, troop3_no]

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
