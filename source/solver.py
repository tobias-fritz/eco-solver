#!/usr/bin/env python3

class Species:
    ''' A class to represent a species in a food chain.

    Attributes:
        name: A string representing the name of the species.
        calories_needed: An integer representing the number of calories needed by the species.
        calories_provided: An integer representing the number of calories provided by the species.
        eats: A list of strings representing the species that this species eats.
        eaten_by: A list of strings representing the species that eat this species.
    '''

    def __init__(self, 
                 name:str, 
                 calories_needed: int,
                 calories_provided: int, 
                 eats: list, 
                 eaten_by: list,) -> None:
        
        # levels range from apex = 1, predator= 2, prey = 3, producer = 4
        self.name = name
        self.calories_provided = calories_provided
        self.calories_needed = calories_needed
        self.eats = eats
        self.eaten_by = eaten_by

    def __repr__(self) -> str:
        return f'{self.name}'
    
    def __eq__(self, other: object) -> bool:
        return self.name == other.name and self.calories_provided == other.calories_provided and\
               self.calories_needed == other.calories_needed and self.eats == other.eats and\
               self.eaten_by == other.eaten_by


def is_valid_food_chain(species_list: list) -> tuple:
    ''' Check if a given food chain is valid or not. 

    A food chain is valid if all species can eat and are eaten by other 
    species in the food chain, without any species going extinct.

    The rules (based on reports from various websites found online) are as follows:

    1. The species with the highest Calories Provided in the food chain eats first.
    2. It consumes the species with the highest Calories Provided among its prey. 
        If the eating species is a producer, it skips this step and steps 3-5.
    3. The eating species consumes an amount of Calories Provided equal to its Calories Needed from the prey,
        which is subtracted from the prey's Calories Provided.
    4. If there are two top prey species with the same Calories Provided, 
        the eating species will consume an amount equal to half of its Calories Needed from each.
    5. If the eating species' Calories Needed is not fully satisfied after consuming from the first prey,
        it moves on to the next prey with the second-highest Calories Provided and repeats the process.

    Args:
        species_list: A list of Species objects representing the food chain.
    
    Returns:
        Tuple: A tuple where the first element is a boolean indicating if the food chain is valid
               or not, and the second element is the total number of calories provided by all species
    '''

    sorted_species_list = sorted(species_list, key=lambda x: x.calories_provided, reverse=True) # rule 1

    for species in sorted_species_list:

        if species.calories_needed == 0: # rule 2
            continue

        while species.calories_needed > 0: # rule 5
            # get all prey of the species
            prey = [x for x in sorted_species_list if x.name in species.eats]
            sorted_prey = sorted(prey, key=lambda x: x.calories_provided, reverse=True) # rule 2
            # no prey available
            if not len(sorted_prey) > 0: 
                return False, 0
            # only one prey available
            if len(sorted_prey) == 1: 
                # enough calories provided
                if species.calories_needed <= sorted_prey[0].calories_provided: 
                    sorted_species_list[sorted_species_list.index(sorted_prey[0])].calories_provided -= species.calories_needed
                    species.calories_needed -= species.calories_needed
                    continue
                # not enough calories provided -> prey is going extinct, species is going hungry
                else: 
                    return False, 0
            # if two top prey have the same calories provided
            if sorted_prey[0].calories_provided == sorted_prey[1].calories_provided: 
                # enough calories provided
                if species.calories_needed <= sorted_prey[0].calories_provided + sorted_prey[1].calories_provided: 
                    sorted_species_list[sorted_species_list.index(sorted_prey[0])].calories_provided -= species.calories_needed/2
                    sorted_species_list[sorted_species_list.index(sorted_prey[1])].calories_provided -= species.calories_needed/2
                    species.calories_needed -= species.calories_needed # rule 3
                # not enough calories provided -> someone is going extinct
                else: 
                    return False, 0
            # only one top prey
            else: 
                # enough calories provided
                if species.calories_needed <= sorted_prey[0].calories_provided: 
                    sorted_species_list[sorted_species_list.index(sorted_prey[0])].calories_provided -= species.calories_needed # rule 3
                    species.calories_needed -= species.calories_needed # rule 3
                # not enough calories provided -> prey is going extinct, species is going hungry
                else:
                    return False, 0
    # all species have eaten, food chain is valid, calculate total remaining calories provided (for ranking if multiple valid chains)
    return True, sum([species.calories_provided for species in sorted_species_list])
