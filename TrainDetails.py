import speech_recognition as sr
import pyttsx3
import mysql.connector

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('voice', 'en-in')
engine.setProperty('rate', 110)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def convert_numbers_to_words(recognized_text):
    words = []
    for word in recognized_text.split():
        if word.isdigit():
            words.extend(list(word))
        else:
            words.append(word)
    return ' '.join(words)

# Function to retrieve train details from the MySQL database
def get_train_details(input_data):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="railway"
    )

    cursor = connection.cursor()

    query = f"SELECT * FROM RBG1 WHERE `Train_Number`='{input_data}' OR `Train_Name`='{input_data}'"
    cursor.execute(query)

    result = cursor.fetchone()

    # Check if train details exist for the given input
    if result is not None:
        train_number = result[0]
        train_name = result[1]
        source_station = result[2]
        destination_station = result[3]
        arrival_time = result[4]
        departure_time = result[5]
        running_days = result[6]

        train_number = convert_numbers_to_words(train_number)
        # Generate the response string
        response = f"The train {train_number} {train_name} runs from {source_station} to {destination_station}. It arrives at {arrival_time} and departs at {departure_time}."

    else:
        response = "Sorry, train details not found for the given input."

    cursor.close()
    connection.close()

    return response

# Function to take speech input and provide speech output
def take_speech_input():
    # Initialize speech recognizer and engine
    r = sr.Recognizer()
    
    # Take speech input from the user
    with sr.Microphone() as source:
        talk("Welcome to TrainGo - A Rail Enquiry Application")
        talk("Inform the Train number or Train name")
        print('listening...')
        audio = r.listen(source)

    try:
        # Use speech recognizer to convert speech to text
        print("Recognizing...")
        input_text = r.recognize_google(audio)

        # Retrieve train details from the MySQL database
        response = get_train_details(input_text)

        # Speak the response
        engine.say(response)
        engine.runAndWait()

    except sr.UnknownValueError:
        engine.say("Sorry, I could not understand your speech.")
        engine.runAndWait()

    except sr.RequestError as e:
        engine.say("Sorry, my speech service is not working.")
        engine.runAndWait()

if __name__ == '__main__':
    take_speech_input()    