houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's House"]

def deliver_presents_recursively(houses):
    if len(houses) == 1:
        house = houses[0]
        print("Deliverying presents to", house)
    else:
        mid = len(houses) //2
        first_half = houses[:mid]
        second_half = houses[mid:]

        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)

deliver_presents_recursively(houses)
