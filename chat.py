logfile = "chat.txt"

# Returns a list of dictionaries. Each dictionary in the list
# is a message that has been sent in our chat server
def get_chat():
  full_chat = []
  with open(logfile) as file:
    for line in file:
      line = line.rstrip("\n\r")
      rec = {"message" :  line }
      full_chat.append(rec)
  return full_chat

# Adds the message text to our file containing all the messages
def add_message(message):
  with open(logfile, "a") as file:
    file.write(message + "\n")
  # This return is not needed, but helps ensure replit shows the updated
  # file when it is selected from the file browser
  return None