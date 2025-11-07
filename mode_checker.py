
def check_mood():
    mood = input("How are you feeling today? ").lower()

    if "happy" in mood or "good" in mood or "great" in mood or "joyful" in mood:
        print("That's wonderful to hear! Keep shining bright!")
    elif "sad" in mood or "down" in mood or "unhappy" in mood or "gloomy" in mood:
        print("I'm sorry to hear that. Remember, even the darkest clouds have a silver lining. Things will get better!")
    elif "anxious" in mood or "stressed" in mood or "worried" in mood:
        print("Take a deep breath. You're stronger than you think, and you'll get through this. One step at a time.")
    elif "bored" in mood:
        print("Time to find something exciting to do! What new adventure awaits you today?")
    elif "tired" in mood or "sleepy" in mood:
        print("It sounds like you could use some rest. Take care of yourself and recharge!")
    else:
        print("Every mood is valid. Remember to be kind to yourself today!")

if __name__ == "__main__":
    print("Welcome to Mode Checker!")
    check_mood()
