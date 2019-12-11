#finds which drink option had the most responses-figures out final result
def find_drink (answer_list):
    '''originally used find_max function from A3 assignment as a refrence, 
    but reworked it so that it would work for this chatbot'''
    highest_tally = 0
    for item in answer_list:
        if len(item) > highest_tally:
            highest_tally = len(item)
    return highest_tally

#check if user wants to end the quiz
def check_end_quiz (input_string):
    end_quiz=['quit', 'Quit', 'bye', 'Bye', 'quit ', 'Quit ', 'bye ', 
              'Bye ', 'exit', 'Exit', 'exit ', 'Exit ']
    if input_string in end_quiz:
        return True
    else:
        return False

#check if input means yes
def check_yes (input_string):
    answer_yes = ['yes', 'Yes', 'ya', 'Ya', 'Yeah', 'yeah','yes!', 'Yes!', 
                  'ya!', 'Ya!', 'Yeah!', 'yeah!', 'ye', 'Ye'] 
    if input_string in answer_yes:
        return True
    else:
        return False

#check if input means no
def check_no (input_string):
    answer_no = ['no', 'No']
    if input_string in answer_no:
        return True
    else:
        return False

#check if user wants to start quiz over again
def check_replay (input_string):
    answer_replay = ['again', 'Again', 'restart', 'Restart']
    if input_string in answer_replay:
        return True
    else:
        return False

#check for the answer to the questions
def check_answer_a (input_string):
    choice_a =['a', 'A', 'a ', 'A ', ' a', ' A', ' a ', ' A ']
    if input_string in choice_a:
        return True
    else:
        return False
def check_answer_b (input_string):
    choice_b =['b', 'B', ' b', ' B', ' b ', ' B ', 'b ', 'B ']
    if input_string in choice_b:
        return True
    else:
        return False
def check_answer_c (input_string):
    choice_c =['c', 'C', ' c', ' C', ' c ', ' C ', 'c ', 'C ']
    if input_string in choice_c:
        return True
    else:
        return False
def check_answer_d (input_string):
    choice_d =['d', 'D', ' d', ' D', ' d ', ' D ', 'd ', 'D ']
    if input_string in choice_d:
        return True
    else:
        return False
    
def holiday_drink_quiz():
    '''function for main chatbot'''
    
    #instructions, introduction, and invalid response output
    instructions = 'Let\'s get started. I\'m going to ask you some simple \
questions, and all I need is for you to respond with \'A\', \'B\', \'C\', \
or \'D\'. You can stop the game at any time by typing \'quit\'. Or start \
from the beggining by typing \'restart\'. Type \'ready\' to continue.'
    intro = "Hello! Do you want to take a quiz to see what kind of holiday \
drink matches your personality? Type \'yes\' to continue."
    invalid_answer = 'Invalid response. Please respond with \'A\', \'B\', \
\'C\', or \'D\'. Try again or type \'restart\' to restart the quiz'
    
    #Questions and their options
    question_1 ='Question 1: What is your favorite part of the holidays? \
\t \n A) Spending time with loved ones!\t \n B) No more school! \t \n C) \
Presents! \t \n D) Wearing ugly sweaters!'
    question_2 = 'Question 2: When do you start listening to holiday music?\
\t \n A) November 1st (Thanksgiving who?) \t \n B) December 1st \t \n C) \
A week before Christmas \t \n D) Never'
    question_3 ='Question 3: What is perfect holiday weather? \t \n A) \
Snowy \t \n B) Rainy \t \n C) Cold but dry \t \n D) Sunny'
    question_4 = 'Question 4: What is your favorite winter activity? \t \
\n A) Driving around to look at the Christmas lights \t \n B) Ice skating \t\
\n C) Skiing or snowboarding \t \n D) Baking holiday treats'
    question_5 = 'Question 5: What is your favorite holiday dessert? \t\
\n A) Gingerbread cookies \t \n B) Peppermint bark \t \n C) Assorted \
chocolates\t \n D) Fruit cake'
    
    #final result options-which drink they got
    hot_coco= 'You got Hot Chocolate! Your sweet personality is always \
comforting to those around you, and your kindness makes people feel warm \
inside. Type \'again\' to play again! Or \'quit\' to end the quiz.'
    pepp_mocha = 'You got Peppermint Mocha Latte! You\'re full of energy and \
and love just the right amount of holiday spirit! Type \'again\' to play \
again! Or \'quit\' to end the quiz.'
    spiced_cider = 'You got Spiced Cider! A spicy classic! You\'re always up \
for an adventure, and your mature personality always gets along well with \
everyone. Type \'again\' to play again! Or \'quit\' to end the quiz.'
    eggnog= 'You got Eggnog! You\'re an acquired taste. Although you might \
not love the holidays as much as others, you\'re bold, full of flavor, and \
great to have around! Type \'again\' to play again! Or \'quit\' to end the \
quiz.'
    
    counter = 0
  
    print(intro)
    
    quiz = True
    while quiz:
        # Get a message from the user
        msg = input('Answer: ')

        # Check for an end message 
        if check_end_quiz(msg):
            print ('Bye! See you later!')
            quiz = False
        
        #check for restarting quiz
        elif check_replay(msg):
            counter = 0 
            print(intro)
            
        #give instructions and ask if they are ready 
        elif counter == 0:
            answer_a = []
            answer_b = []
            answer_c = []
            answer_d = []
            if check_yes(msg):
                print(instructions)
                counter = 1
            elif check_no(msg):
                print('Whoops you must be at the wrong place then! Respond \
with \'yes\' if you changed your mind and want to take the quiz!')
            else:
                print('Oops that\'s an invalid response. Type \'yes\' if \
you want to take the quiz.')
    
        #check that they're ready and ask Q1
        elif counter == 1:
            if msg == 'ready':
                print(question_1)
                counter = 2
            else: 
                print ('Type \'ready\' to continue on to the quiz.')
    
        #Q1 answer input and ask Q2
        elif counter == 2:
            if check_answer_a(msg):
                answer_a.append(msg)
                counter = 3
                print(question_2)
            elif check_answer_b(msg):
                answer_b.append(msg)
                counter = 3
                print(question_2)
            elif check_answer_c(msg):
                answer_c.append(msg)
                counter = 3
                print(question_2)
            elif check_answer_d(msg):
                answer_d.append(msg)
                counter = 3
                print(question_2)
            else:
                print (invalid_answer)
    
        #Q2 answer input and ask Q3
        elif counter == 3:
            if check_answer_a(msg):
                answer_a.append(msg)
                counter = 4
                print(question_3)
            elif check_answer_b(msg):
                answer_b.append(msg)
                counter = 4
                print(question_3)
            elif check_answer_c(msg):
                answer_c.append(msg)
                counter = 4
                print(question_3)
            elif check_answer_d(msg):
                answer_d.append(msg)
                counter = 4
                print(question_3)
            else:
                print (invalid_answer)
    
     
    #Q3 answer input and ask Q4
        elif counter == 4:
            if check_answer_a(msg):
                answer_a.append(msg)
                counter = 5
                print(question_4)
            elif check_answer_b(msg):
                answer_b.append(msg)
                counter = 5
                print(question_4)
            elif check_answer_c(msg):
                answer_c.append(msg)
                counter = 5
                print(question_4)
            elif check_answer_d(msg):
                answer_d.append(msg)
                counter = 5
                print(question_4)
            else:
                print (invalid_answer)
    
    #Q4 answer input and ask Q5
        elif counter == 5:
            if check_answer_a(msg):
                answer_a.append(msg)
                counter = 6
                print(question_5)
            elif check_answer_b(msg):
                answer_b.append(msg)
                counter = 6
                print(question_5)
            elif check_answer_c(msg):
                answer_c.append(msg)
                counter = 6
                print(question_5)
            elif check_answer_d(msg):
                answer_d.append(msg)
                counter = 6
                print(question_5)
            else:
                print (invalid_answer)
    

    #Q5 answer input and tell them it's the last question 
        elif counter == 6:
            if check_answer_a(msg):
                answer_a.append(msg)
                counter = 7
                print('That\'s the last question! Are you excited to find\
out what Holiday Drink you are!?')
            elif check_answer_b(msg):
                answer_b.append(msg)
                counter = 7
                print('That\'s the last question! Are you excited to find\
out what Holiday Drink you are!?')
            elif check_answer_c(msg):
                answer_c.append(msg)
                counter = 7
                print('That\'s the last question! Are you excited to find\
out what Holiday Drink you are!?')
            elif check_answer_d(msg):
                answer_d.append(msg)
                counter = 7
                print('That\'s the last question! Are you excited to find\
out what Holiday Drink you are!?')
            else:
                print (invalid_answer)
           
    #calculate result and return it to the user, option to play again
        elif counter == 7:
            if check_yes(msg):
                all_answer_scores = [answer_a, answer_b, answer_c, answer_d]
                if len(answer_a) == find_drink(all_answer_scores):
                    print(hot_coco)
                elif len(answer_b) == find_drink(all_answer_scores):
                    print(pepp_mocha)
                elif len(answer_c) == find_drink(all_answer_scores):
                    print(spiced_cider)
                elif len(answer_d) == find_drink(all_answer_scores):
                    print(eggnog)
            else: 
                print ('Oops! Type \'yes\' to find out what holiday drink \
you are!')
