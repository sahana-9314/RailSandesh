import mysql.connector
import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('voice', 'en-in')
engine.setProperty('rate', 110)

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="railway"
)

# Define a function to convert text to speech
def speak(text):
  engine.say(text)
  engine.runAndWait()

# Define a function to listen for speech input
def listen():
  with sr.Microphone() as source:
    print('listening...')
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
      speech = r.recognize_google(audio)
      return speech.lower()
    except sr.UnknownValueError:
      speak("Sorry, I didn't catch that. Please try again.")
      return listen()
    except sr.RequestError:
      speak("Sorry, my speech service is currently unavailable. Please try again later.")
      return None

def convert_date_format(date):
  date = date.replace(' ', '')
  return date

def convert_numbers_to_words(recognized_text):
    words = []
    for word in recognized_text.split():
        if word.isdigit():
            words.extend(list(word))
        else:
            words.append(word)
    return ' '.join(words)

# Define a function to check the availability of seats
def check_availability():
    speak("What is the train number?")
    train_no = listen()
    train_no = convert_numbers_to_words(train_no)
    speak(f"The train number is {train_no}. What is the date of travel? (in YYYY - MM - DD format)")
    date = listen()
    date = convert_date_format(date)
    print(date)
    speak("How many seats do you want to book?")
    num_seats = listen()
    num_seats = int(num_seats)
    cursor = mydb.cursor()

    # Query the database to get the number of available seats for the specified train and date
    cursor.execute("SELECT seats_available FROM trains WHERE train_no = %s AND date = %s", (train_no, date))
    result = cursor.fetchone()
    if not result:
      speak("Train not found for the specified date")
      return False
    seats_available = result[0]

    # Check if there are enough available seats for the booking
    if seats_available >= num_seats:
      speak("Seats available. Booking successful.")
      # Update the database with the new number of available seats
      new_seats_available = seats_available - num_seats
      cursor.execute("UPDATE trains SET seats_available = %s WHERE train_no = %s AND date = %s", (new_seats_available, train_no, date))
      mydb.commit()
      return True
    else:
      speak("Seats not available for the specified train and date")
      return False

# Define a function to check the PNR status
def check_pnr_status():
  speak("What is your PNR number?")
  pnr_number = listen()
  pnr = str(pnr_number)
  pnr.replace(" ","")
  pnr_len = len(pnr)
  if pnr_len != 10:
    speak("PNR Number must be of 10 digits only!! Please try again")
    return False
  cursor = mydb.cursor()

  # Query the database to get the PNR status for the specified PNR number
  cursor.execute("SELECT * FROM passengers WHERE pnr_number = %s ", (pnr_number,) )
  result = cursor.fetchone()
  if not result:
    speak("PNR number not found")
    return False
  else:
    speak(f"Corresponding PNR number {result[0]} is reserved for Train number {convert_numbers_to_words((str)(result[1]))} Train Name {result[2]} on date {result[3]} . Boarding is at {result[4]} and it is Reserved upto {result[5]} for class {result[6]}. Current Status is {result[7]}. Chart Status is {result[8]}. Coach Position is {result[9]}  ")
    return True

def main():
    while True:
        speak("How can I assist you?")
        command = listen()
        print(command)
        if "pnr status" in command:
            check_pnr_status()
            break
        if "seat availability"in command:
            check_availability()
            break
        if "Thank You" in command:
             speak("Thank You ! Have a nice day")
             break
        #else:
        speak("Sorry, I didn't understand. Please try again.")

if __name__ == '__main__':
    speak("Welcome to TrainGo - A Rail Enquiry Application")
    main()
