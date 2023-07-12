import speech_recognition as sr
import pyttsx3
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from transformers import pipeline
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer
import torch
import numpy as np


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('voice', 'en-in')
engine.setProperty('rate', 130)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'buddy' in command:
                command = command.replace('buddy', '')
        return command

    except Exception as err:
        print("Issue in read_command(): {}".format(err))
    
#Load pre-trained bert model
model=BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
tokenizer_for_bert=BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

talk("welcome to Rayabag station")
talk("how can i help you")
def run_alexa():
    command = take_command()
    print(command)
    #talk(command)
    #Testing function
    result = bert_question_answer(command,"Indian rail currently provides following ways to book tickets. Reservation at railway counters and Online reservation from https://irctc.co.in and Reservation through registered agents and agencies, A maximum of 6 passenger for general and upto 4 passenger for tatkal,No Bulk booking cannot be done on the internet,The rail ticket can not be transferred to a friend. Following Trains are scheduled from Raybag Station: RANI CHENNAMMA EXPRESS,HARIPRIYA EXPRESS,GOA EXPRESS,HOOBBALLI MEERAJ EXPRESS")

    print(result)
    talk(result)
    
def bert_question_answer(question, passage, max_len=5000):
    #Tokenize input question and passage
    #Add special tokens-[CLS] and [SEP]
    input_ids = tokenizer_for_bert.encode(question, passage, max_length=max_len, truncation=True)
    
    #Getting number of tokens in 1st sentence (question) and 2nd sentence (passage that contains answer)
    sep_index=input_ids.index(102)
    len_question = sep_index + 1   
    len_passage = len(input_ids)- len_question
   
    #Need to separate question and passage
    #Segment ids will be 0 for question and 1 for passage  
    segment_ids =  [0]*len_question + [1]*(len_passage)
   
    #Converting token ids to tokens
    tokens = tokenizer_for_bert.convert_ids_to_tokens(input_ids) 
    
    #Getting start and end scores for answer
    #Converting input arrays to torch tensors before passing to the model
    start_token_scores = model(torch.tensor([input_ids]), token_type_ids=torch.tensor([segment_ids]) )[0]
    end_token_scores = model(torch.tensor([input_ids]), token_type_ids=torch.tensor([segment_ids]) )[1]
    #Converting scores tensors to numpy arrays
    start_token_scores = start_token_scores.detach().numpy().flatten()
    end_token_scores = end_token_scores.detach().numpy().flatten()
   
    #Getting start and end index of answer based on highest scores
    answer_start_index = np.argmax(start_token_scores)
    answer_end_index = np.argmax(end_token_scores)
    #Getting scores for start and end token of the answer
    start_token_score = np.round(start_token_scores[answer_start_index], 2)
    end_token_score = np.round(end_token_scores[answer_end_index], 2)
   
    #Combining subwords starting with ## and get full words in output. 
    #It is because tokenizer breaks words which are not in its vocab.
        #Combining subwords starting with ## and get full words in output.
    #It is because tokenizer breaks words which are not in its vocab.
    answer = tokens[answer_start_index]
    for i in range(answer_start_index + 1, answer_end_index + 1):
        if tokens[i][0:2] == '##':
            answer += tokens[i][2:]
        else:
            answer += ' ' + tokens[i]
    
    return answer
while True:
    run_alexa()