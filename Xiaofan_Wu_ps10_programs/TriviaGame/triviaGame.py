#Xiaofan Wu
#CS 111 PS 10
# Trivia Game

import Tkinter as tk
import random

class QuestionsAndAnswers:
    def __init__(self, filename, startOfQuestionText, endOfQuestionText):
        self.startOfQuestionText = startOfQuestionText
        self.endOfQuestionText = endOfQuestionText
        lines = open(filename).readlines()
        self.QandA_list = []     # A list of question/answer tuples read in from file
        for line in lines:  # Populate list of questions/answers with data from file
            splitLine = line.strip().split('\t')  # Assumes tab-delimited file
            self.QandA_list.append((splitLine[0].strip(), splitLine[1].strip()))

    def get_random_QandA_number(self):
        '''Every question/answer has a number associated with it, i.e., the index
        it occurs in the list. Return the number associated with a randmoly
        chosen question/answer.'''
        return random.randint(0, len(self.QandA_list)-1)

    def getQuestion(self, number):
        '''Returns the question associated with the given number.'''
        return self.startOfQuestionText + self.QandA_list[number][0] + self.endOfQuestionText

    def getAnswer(self, number):
        '''Returns the answer associated with the given number.'''
        return self.QandA_list[number][1]


class TriviaGameApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self)
        self.QA = QuestionsAndAnswers('countries_capitals.txt', 'What is the capital city of ', '?')
        root.title('Trivia Game')
        self.grid()
        self.totalNumberOfQuestions = 10  # Total number of questions
        self.numberOfAnswers = 4          # Number of answer options
        self.currentQuestionNumber = 1    # Current question number (increments with after each question)
        self.numberAnsweredCorrectly = 0  # Number of questions answered correctly
        self.indexOfCurrentQuestion = self.QA.get_random_QandA_number()  # Number/index of current question
        self.awaitingUserToSubmitAnswer = True  # Are we waiting for the user to submit an answer to a question (True)? Or has the user already submitted an answer and we are waiting for the user to press the "Next" button (False)?
        self.createWidgets()

    def createWidgets(self):

        # Image and Title
        pic = tk.PhotoImage(file='map.gif')
        imageLabel = tk.Label(self, image=pic,borderwidth=0)
        imageLabel.pic = pic
        imageLabel.grid(row=0,column=0)
        titleLabel = tk.Label(self, text='World\nTrivia', bg='white', font='Verdana 24 bold')
        titleLabel.grid(row=0,column=1,sticky=tk.N+tk.E+tk.W+tk.S)

        # Question
        self.question = tk.StringVar()
        questionLabel = tk.Label(self, fg='blue', font='Times 14', textvariable=self.question)
        questionLabel.grid(rowspan=self.numberOfAnswers,column=0,sticky=tk.E)
        self.setQuestion()  # Set text of question

        # Answers
        self.answerIndex = tk.IntVar()  # Index of selected radiobutton
        self.answerTexts = []  # List of StringVars, one for each radiobutton. Each list element allows getting/setting the text of a radiobutton.
        for i in range(0, self.numberOfAnswers):
            self.answerTexts.append(tk.StringVar())
        self.rbs = []                           # a list of our radiobuttons
        for i in range(0, self.numberOfAnswers):  # Create radiobuttons
            rb = tk.Radiobutton(self, fg='red', textvariable=self.answerTexts[i], variable=self.answerIndex, value=i)
            rb.grid(row=1+i, column=1, sticky=tk.W)
            self.rbs.append(rb)
        self.setAnswers()  # Set text of radiobuttons


        # Status Label
        self.results = tk.StringVar()
        self.resultsLabel = tk.Label(self, fg='brown', font='Times 14 italic', textvariable=self.results)
        self.resultsLabel.grid(row=1+self.numberOfAnswers,column=0)

        # Submit Button
        self.submitButton = tk.Button(self, text='Submit', command=self.onSubmitButtonClick)
        self.submitButton.grid(row=1+self.numberOfAnswers,column=1)
        
        

        # Quit Button        
        quitButton = tk.Button(self, text='Quit', command=self.onQuitButtonClick)
        quitButton.grid(row=2+self.numberOfAnswers,column=0,sticky=tk.W)

    def setQuestion(self):
        self.question.set('Question ' + str(self.currentQuestionNumber) + ' out of ' + str(self.totalNumberOfQuestions) + '.\n' + self.QA.getQuestion(self.indexOfCurrentQuestion))


    def setAnswers(self):
        '''Populates the answer radiobuttons in a random order 
        with the correct answer as well as random answers.'''
        answers = []  # List of possible answers
        answers.append(self.QA.getAnswer(self.indexOfCurrentQuestion))  # Add correct answer to list
        while len(answers) != self.numberOfAnswers:  # Add random answers to list. Ensure each random answer is not already in list, i.e., no duplicates.
            index = self.QA.get_random_QandA_number()  # Get random number/index
            if self.QA.getAnswer(index) not in answers:  # Ensure random answer is not already in answer list
                answers.append(self.QA.getAnswer(index))  # Add random answer to list
        random.shuffle(answers)  # Randomly shuffle answer list
        for i in range(0, len(answers)):  # Populate text of radiobuttons
            self.answerTexts[i].set(answers[i])
            self.rbs[i].deselect()      # deselect the radiobuttons
            
    def onSubmitButtonClick(self):
        
        #First, we want to make sure that the question number is less or 
        #equal to 10. If it is greater than 10, we want to stop the game
        #and display the final result.
        
        if self.currentQuestionNumber<=10:
            #We want to use awaitingUsertoSubmitAnswer, so this way
            #we can distinguish the difference between waiting for the 
            #user to submit answe vs. user already submit answer, but waiting 
            #to click next. 
            if self.awaitingUserToSubmitAnswer==True:
                #We first check if the user input is same as what the correct
                #answer is.
                if self.answerTexts[self.answerIndex.get()].get()==self.QA.getAnswer(self.indexOfCurrentQuestion):
                    #If the answer is correct, display that the answer is correct.
                    self.results.set('correct! You are so smart!')
                    #add one to the current question number, so that there is a
                    #count up to 10 to stop the game when the number reach
                    #to 10. 
                    self.currentQuestionNumber+=1
                    #add 1 each time the answer is correct, so that in the 
                    #end, we can display the number of correctly answered. 
                    self.numberAnsweredCorrectly+=1
                    #change the button to next
                    self.submitButton.config(text='next')
                    #change the awaiting part to false, so that next time
                    #it goes through this loop, it will go to the phase
                    #when the computer is waiting for the user to hit next. 
                    self.awaitingUserToSubmitAnswer=False

                #if the answer that the user chose is incorrect 
                else:
                    #If the answer is incorrect,give the correct answer
                    self.results.set('Sorry :( Do better next time! The correct answer is '
                    + self.QA.getAnswer(self.indexOfCurrentQuestion))
                    #Add the current question number by 1
                    self.currentQuestionNumber+=1
                    #Still change the submit button to next
                    self.submitButton.config(text='next')
                    #change the awaiting part to false, so that next time
                    #it goes through this loop, it will go to the phase
                    #when the computer is waiting for the user to hit next. 
                    self.awaitingUserToSubmitAnswer=False
                #randomly generates the next quesiton   
                self.indexOfCurrentQuestion = self.QA.get_random_QandA_number()  

            else:
                    #reset the question and the correct answer when user click
                    #next and reset the text. Change awaiting to sumbit to true
                    #For next time the loop go through again. This way, next
                    #time the loop will ask the question again..
 
                    self.setQuestion()
                    self.setAnswers()
                    self.submitButton.config(text='submit')
                    self.results.set('')
                    self.awaitingUserToSubmitAnswer=True

        else:
            #once the number of question reach to 10, clicking next will display
            #the total question answered correctly and change the submit button
            #to next to display the final results. Then the button will change 
            #restart button and currentquestion answered will be set to 1 and
            #number of answered correctly will be 0 and the awaiting user to 
            #submit answer will be false, so this will the game can restart
            #the quesiton again and change the button to sumbit, once the 
            #restart button is clicked.
            #Also here, if the user answer more than 5 questions correctly,
            # I tell them they are smart. Otherwise, tell them to try harder
            #next time.
            if self.numberAnsweredCorrectly>5:
                self.submitButton.config(text='next')
                self.results.set('Game over: you answered ' + str(self.numberAnsweredCorrectly) 
                + ' out of ' + str(self.totalNumberOfQuestions) + ' correctly! You are so smart!')
            else:
                self.submitButton.config(text='next')
                self.results.set('Game over: you only answered ' + str(self.numberAnsweredCorrectly) 
                + ' out of ' + str(self.totalNumberOfQuestions) + ' correctly! Try harder next time!')

            self.submitButton.config(text='restart')
            self.awaitingUserToSubmitAnswer=False
            self.currentQuestionNumber=1
            self.numberAnsweredCorrectly=0
            
            
  
    def onQuitButtonClick(self):
        self.destroy()


root = tk.Tk()
app = TriviaGameApp(root)
app.mainloop()
