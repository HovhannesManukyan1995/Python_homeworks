try:
    import speech_recognition as sr
except (Exception, TypeError, AttributeError) as e:
    print("You dont have 'speech_recognition' module:Install it")
    exit()
try:
    import os
except (Exception, TypeError, AttributeError) as e:
    print("You dont have 'os' module:Install it")
    exit()
try:
    from inputimeout import inputimeout
except (Exception, TypeError, AttributeError) as e:
    print("You dont have 'inputimeout' module:Install it")
    exit()

try:
    #Show how many command we can use: 
    md = {"firefox":"firefox" , 
          "make directory and dir.name" :"mkdir" ,
          "Where i am" : "pwd",
          "What we have" : "ls" ,
          "Create txt file"  : "touch and name.txt"}

    for i,j in md.items():
   	 print("Speak", i ,"Command ->" , j)

    print("\nClick Enter to countinue")
    time_over = inputimeout(timeout=10)
 
except Exception: 
  
    time_over = 'Okay Countinue'
    print(time_over) 

#implement your voice
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)
#check command and use
try:
    vci = r.recognize_google(audio)
    print("You say" + " " + vci)
    if "firefox" in vci.lower():
        os.system(vci.lower())

    elif "make directory" in vci.lower():
        split_one=vci.lower().split('make directory')
        create_one='mkdir'+' '+split_one[-1].strip()
        os.system(create_one)

    elif 'where i am' in vci.lower():
            os.system('pwd')

    elif 'what we have' in vci.lower():
            os.system('ls')

    elif 'create txt file' in vci.lower():
         split_one=vci.lower().split()
         create_file='touch'+' '+split_one[-1].strip()+'.txt'
         os.system(create_file)


except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
