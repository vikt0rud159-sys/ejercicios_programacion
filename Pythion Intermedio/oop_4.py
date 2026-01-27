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


head = Head(2)
right_hand = Hand(5)
right_arm = Arm(right_hand)
left_hand = Hand(5)
left_arm = Arm(left_hand)
right_feet = Feet(5)
right_leg = Leg(right_feet)
left_feet = Feet(5)
left_leg = Leg(left_feet)
torso = Torso(head, right_arm, left_hand, right_leg, left_leg)