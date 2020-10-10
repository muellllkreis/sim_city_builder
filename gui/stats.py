import collections

Box = collections.namedtuple('Box', 'left top width height')

time_money = Box(138, 139, 337, 14)

##################
#TAX WINDOW
tx_property = Box(294, 185, 30, 11)
tx_raise_property = Box(327, 182, 10, 8)
tx_lower_property = Box(327, 191, 10, 8)
tx_property_to_date = Box(341, 185, 41, 11)
tx_property_eoy = Box(388, 185, 41, 11)
#######################CITY ORDINANCE
tx_ordinance_to_date = Box(341, 204, 41, 11)
tx_ordinance_eoy = Box(388, 204, 41, 11)
#######################BOND PAYMENTS
tx_bond_to_date = Box(341, 223, 41, 11)
tx_bond_eoy = Box(388, 223, 41, 11)
#######################POLICE DEPARTMENT
tx_police = Box(294, 242, 30, 11)
tx_raise_police = Box(327, 293, 10, 8)
tx_lower_police = Box(327, 248, 10, 8)
tx_police_to_date = Box(341, 242, 41, 11)
tx_police_eoy = Box(388, 242, 41, 11)
#######################FIRE DEPARTMENT
tx_fire = Box(294, 261, 30, 11)
tx_raise_fire = Box(327, 258, 10, 8)
tx_lower_fire = Box(327, 267, 10, 8)
tx_fire_to_date = Box(341, 261, 41, 11)
tx_fire_eoy = Box(388, 261, 41, 11)
#######################HEALTH AND WELFARE
tx_health = Box(294, 280, 30, 11)
tx_raise_health = Box(327, 277, 10, 8)
tx_lower_health = Box(327, 286, 10, 8)
tx_health_to_date = Box(341, 280, 41, 11)
tx_health_eoy = Box(388, 280, 41, 11)
#######################EDUCATION
tx_edu = Box(294, 299, 30, 11)
tx_raise_edu = Box(327, 296, 10, 8)
tx_lower_edu = Box(327, 305, 10, 8)
tx_edu_to_date = Box(341, 299, 41, 11)
tx_edu_eoy = Box(388, 299, 41, 11)
#######################TRANSIT
tx_transit = Box(294, 318, 30, 11)
tx_raise_transit = Box(327, 315, 10, 8)
tx_lower_transit = Box(327, 324, 10, 8)
tx_transit_to_date = Box(341, 318, 41, 11)
tx_transit_eoy = Box(388, 318, 41, 11)
#######################TOTALS
tx_to_date_total = Box(294, 338, 135, 11)
tx_eoy_total = Box(294, 315, 135, 11)
tx_eoy_treasury = Box(294, 376, 135, 11)
