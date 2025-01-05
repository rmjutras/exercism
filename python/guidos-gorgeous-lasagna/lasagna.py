'''Coding exercise from exercism.com
Simple functions to calculate the time involved in baking a (imaginary) lasagna
'''
EXPECTED_BAKE_TIME: int = 40
LAYER_PREP_TIME: int = 2 #for each layer there is additional 2 min overhead of prep time

def bake_time_remaining(elapsed_bake_time: int) -> int:
    '''Calculate the bake time remaining based on the actual minutes the lasagna has been
    in the oven and returns how many minutes the lasagna still needs to bake based on
    the `EXPECTED_BAKE_TIME` constant.
    '''
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
def preparation_time_in_minutes(number_of_layers: int) -> int:
    '''Calculate the total prep time based on the number of layers using the number of layers
     as an argument and the prep time constant
    '''
    return LAYER_PREP_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    '''Calculates the total time you have been cooking based on relevant constants and arguments.
    Note: this assumes you have finished prep. There is no way to track if you are mid-prep.
    '''
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
