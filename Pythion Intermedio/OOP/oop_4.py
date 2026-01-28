class Head:
	def __init__(self, eyes):
		self.eyes = eyes


class Torso:
	def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
		self.head = head
		self.right_arm = right_arm
		self.left_arm = left_arm
		self.right_leg = right_leg
		self.left_leg = left_leg


class Arm:
	def __init__(self, hand):
		self.hand = hand

class Hand:
	def __init__(self, fingers):
		self.fingers = fingers


class Leg:
	def __init__(self, feet):
		self.feet = feet


class Feet:
	def __init__(self, toes):
		self.toes = toes       


class Human:
	def __init__(self):
		self.head = Head(2)
		self.right_hand = Hand(5)
		self.right_arm = Arm(self.right_hand)
		self.left_hand = Hand(5)
		self.left_arm = Arm(self.left_hand)
		self.right_feet = Feet(5)
		self.right_leg = Leg(self.right_feet)
		self.left_feet = Feet(5)
		self.left_leg = Leg(self.left_feet)
		self.torso = Torso(self.head, self.right_arm, self.left_hand, self.right_leg, self.left_leg)