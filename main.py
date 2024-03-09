
# Judge each of the above based on a set of criteria and recommend a pet for each of them.
# 1. Energy Level
# 2. Diet
# 3. Independence
# 4. Living Space
# 5. Allergen Treshold
#  Use the following membership functions for each of the criteria:

# A given category has an exclusive interval, meaning:
# "category": [inclusive min, exclusive max]
# The membership function may not even be needed
MEMBERSHIP_FX = {
    "ENERGY_LEVEL": {
        "very_inactive": [0,0.3],
        "inactive": [0.3,0.6],
        "active": [0.6,0.8],
        "very_active": [0.8,1]
    },
    "DIET": {
        "carnivore": [0,0.3],
        "omnivore": [0.3,0.6],
        "herbivore": [0.6,1]
    },
    "INDEPENDENCE": {
        "little_attention": [0,0.1],
        "some_attention": [0.1,0.4],
        "moderate_attention": [0.4,0.8],
        "constant_attention": [0.8,1]
    },
    "LIVING_SPACE": {
        "small": [0, 0.3],
        "medium": [0.3,0.7],
        "large": [0.7, 1]
    },
    "ALLERGEN_THRESHOLD": {
        "cant_trigger": [0,0.05],
        "less_likely": [0.05,0.3],
        "may_trigger": [0.3,0.6],
        "more_likely": [0.6,0.8],
        "most_likely": [0.8,1]
    }
}

# Adopters:
# a. Couple looking for a pet - Both working fulltime in small apartment.
# b. Outdoor Person -  Enjoys hiking and camping. They want a furry companion that is energetic, adventurous, and good with outdoor activities.
# c. Allergy-Sensitive Individual - An individual with allergies is interested in adopting a hypoallergenic pet. They are looking for a pet that sheds minimally, requires little grooming, and is known to be less allergenic.

HOURS_PER_DAY  = 24

def ask_away_time() -> float:
    ans = input("In a day, how many hours are you usually away from home? (0 to 24)")
    try:
        HOURS_AWAY = float(ans)
        if HOURS_AWAY < 0 or HOURS_AWAY > HOURS_PER_DAY:
            return ask_away_time()
        return HOURS_AWAY
    except ValueError:
        return ask_away_time()
    
def away_time_to_independence(hours_away:float) -> str:
    PERCENT_AWAY = hours_away/HOURS_PER_DAY
    # as the hours away increases, recommend pets that require less attention
    if PERCENT_AWAY < 0.1:
        return "constant_attention"
    elif PERCENT_AWAY < 0.4:
        return "moderate_attention"
    elif PERCENT_AWAY < 0.8:
        return "some_attention"
    else:
        return "little_attention"
    
def ask_activity_level():
    # make this criteria more specific or stick w/ a booleanish question?
    # Perhaps ask in a week, how often would they go out w/ the pet?
    
    # maybe we should use fuzzy logic and just ask them for a range like
    # time_input = input("On a scale from 1 to 10, with 1 being 'very little time' and 10 being 'a lot of time', how much time are you willing to/can spend on your pet each day? ")
    # then we divide this value by 10 to match the values in the criteria
    # My attempt to code this lmao
    #try:
    #    time_value = int(time_input)
    #    if 1 <= time_value <= 10:
    #        print("Thank you for your input.")
    #        time_value = time_value / 10  # normalize the time value to a range of 0 to 1
    #        if time_value < 0.3:
    #            return "very_inactive"
    #        elif time_value < 0.6:
    #            return "inactive"
    #        elif time_value < 0.8:
    #            return "active"
    #        else:
    #            return "very_active"
    #     else:
    #        print("Please enter a number between 1 and 10.")
    #     except ValueError:
    #        print("Invalid input. Please enter a number.")
    
    ans = input("Do you want to do outdoor activities with the pet (y/n)? ")

def desribe_living_space():
    ans = input("From a scale of 1 to 10, how would you describe your living space? (1 being small, 10 being large)?")
    try:
        LIVING_SPACE = float(ans)
        if LIVING_SPACE < 1 or LIVING_SPACE > 10:
            return desribe_living_space()
        return LIVING_SPACE
    except ValueError:
        return desribe_living_space()
        
def living_space_to_living_space(living_space:float):
    # as the living space increases, recommend pets that require more space
    if living_space < 3:
        return "small"
    elif living_space < 7:
        return "medium"
    else:
        return "large"

# TODO: ask allergies or list allergies below, if allergy is not in the li
# method 1: ask for allergies but how would it be weighed? 
# method 2: list common allergies but still how would it be weighed?
COMMON_ALLERGIES = ["dust", "pollen", "mold", "pet dander", "food", "insect stings", "medications"]

# I dont think the listed elements work since if were talking about rabbits, dogs, and cats its probably just dander they secrete
# however I read online something that says
# "the proteins contained in cat and dog dander differ slightly which is why some people may be allergic to one animal and not the other."
# so maybe we should go for this instead
# ALLERGIES_PROTEINS = [" Can f 1", "Fel d 1", "Ory c 1"]
# then if there's no reaction to any of them then they're ok to recommend??
# https://docs.google.com/document/d/1k0_Oi9CPuABHVaWX1n4abYdqyVi732uiJkEB-RA64FQ/edit?usp=sharing link sa research kong ginawa

def ask_allergen_threshold():
    # as the allergen threshold increases, recommend pets that are less likely to trigger allergies
    # ask common allergies, then recommend pets that are less likely to trigger those allergies
    ans = input("List the allergies your household members have (separate by comma)")
    allergies = ans.strip().split(",")
    
