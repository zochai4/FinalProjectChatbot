import random

GREET_INPUTS = ('hi', 'hello') 
GREET_RESPONSES = ('hi', 'hey', 'hope you are well' , 'glad you found your way here') 

def greet(sentence): 
    """Greets the user
    
    Parameters
    __________
    sentence : str
        user inputs a greeting
    
    Returns
    _______
    output : str
        greeting back to user
    """
    for word in sentence.split(): 
        if word.lower() in GREET_INPUTS: 
            output = random.choice(GREET_RESPONSES)
            return output
        
        
def BMI_index(weight, height): 
    """function to compute the BMI based on inputted height and weight
    
    Parameters
    __________
    weight : int
        user inputs weight
    height : int
        user inputs height
    
    Returns
    _______
    answer : str
        BMI calculated using input
    """
    answer = (int(weight) / (int(height)**2))
    return str(answer)


def have_a_medical_chat():
    """Main function to run our chatbot
    
    Returns
    _______
    output : str
        talking back to the user
    """
    
    chat = True
    """while the chat is true the function continues"""
    
    while chat:
        msg_greet = input('Say hello / hi to start')
        print(greet(msg_greet))
        """continuously chat checks if the chat is ongoing after every loop"""    
        msg_name = input('What is your name? :\t')
        """when they input their name it gets assigned to the function msg_name"""
        msg_sex = input('What is your sex? (M or F) :\t')
        out_msg = None
        
        gender = True
        if (msg_sex  == "F"):
            sex = True
        elif (msg_sex  == "M"):
            sex = False
        else:
            print('You did not enter in a proper input')
            """checks that user inputs a gender, if user doesnt input M or F output message error"""     
        
        msg_age = input('How old are you? :\t')
        age = 0
        if (int(msg_age) < 18): 
            print('You will be sent to a pediactric floor')
            out_msg = 'quit'
            break
            """This loop asks receives an int input and determines if the age is under 18 breaks out of loop"""     
        
        
        msg_height = input('What height are you in inches? :\t')
        msg_weight = input('What weight are you in pounds? :\t')
    
        print('Your BMI is :' + BMI_index(msg_weight, msg_height))
        """prints the BMI function with the inputs"""
        
        # we are going to diagnose the patient
        
        msg_cause = input('Please enter a number for psychiatric (1), trauma (2), or other (3) :\t')
        
        if (int(msg_cause) == 1):
            print('You will be receieved by the psych ward shortly')
        elif (int(msg_cause) == 2):
            msg_cause_trauma = input('Is a skin tear (Y/N) :\t')
            if (msg_cause_trauma == 'Y' or msg_cause_trauma == 'Yes'):
                print('You will be sent to plastics')
            else:
                print('will be sent to dermatology')
        else:
            print('you will be sent to urgent care')
            """if user inputs a certain int it breaks out of loop and prints a specifc message"""
        out_msg = 'quit'

        print('OUTPUT:', out_msg)
        break
        
        
def end_chat(input_list): 
    """Function to end chat
    
    Parameters
    __________
    input_list : list
        data of all of user inputs
    
    Returns
    _______
    output : bool
        BMI calculated using input
    """
    if 'quit' in input_list: 
        output = True 
    else: 
        output = False 
    return output 
