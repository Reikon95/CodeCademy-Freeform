class Menu: #created class
  def __init__(self, name, items, start_time, end_time): #constructor
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self): #REPER GIVES YOU THE REPRESENTATION
    return self.name + ' this menu is available between ' + str(self.start_time) + ' and ' + str(self.end_time) + '.'
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
} #dictionary of menu

brunch_menu = Menu('Brunch', brunch_items, 1100, 1600) #constructs a new Menu option

print(brunch_menu.start_time)


early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird_menu = Menu('Early Bird', early_bird_items, 1500, 1800) #constructs another menu option

print(early_bird_menu.name)

dinner_items = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,

}

dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)

print(dinner_menu.end_time)

kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00

}

kids_menu = Menu('Kids', kids_items, 1100, 2100)

print(kids_menu)
