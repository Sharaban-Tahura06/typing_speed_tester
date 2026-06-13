import time
import random
from sentences import sentences


def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()

    correct = sum(1 for a, b in zip(original_words, typed_words) if a == b)
    accuracy = (correct / len(original_words)) * 100
    return round(accuracy, 2)
def calculate_wpm(typed_text, elapsed_time):
    words = len(typed_text.split())
    minutes = elapsed_time / 60
    wpm = words / minutes
    return round(wpm, 2)


def run_test():
    sentence = random.choice(sentences)

    print("\n" + "=" * 55)
    print("        🎯 TYPING SPEED TESTER")
    print("=" * 55)
    print("\n📝 Type the following sentence:\n")
    print(f"  {sentence}\n")
    input("Press ENTER when ready to start...")

    print("\nStart typing now! ⬇️\n")

    start_time = time.time()
    user_input = input("> ")
    end_time = time.time()

    elapsed_time = end_time - start_time

    wpm = calculate_wpm(user_input, elapsed_time)
    accuracy = calculate_accuracy(sentence, user_input)

    print("\n" + "=" * 55)
    print("              📊 YOUR RESULTS")
    print("=" * 55)
    print(f"  ⏱️  Time Taken  : {round(elapsed_time, 2)} seconds")
    print(f"  🚀 WPM         : {wpm}")
    print(f"  🎯 Accuracy    : {accuracy}%")

    if accuracy == 100:
        print("  🏆 Perfect accuracy! Amazing!")
    elif accuracy >= 80:
        print("  ✅ Great job! Keep practicing!")
    else:
        print("  ⚠️  Try to focus more on accuracy!")

    print("=" * 55)


import json
import os


def save_score(wpm, accuracy):
    scores = []

    if os.path.exists("scores.json"):
        with open("scores.json", "r") as f:
            scores = json.load(f)

    scores.append({"wpm": wpm, "accuracy": accuracy})

    with open("scores.json", "w") as f:
        json.dump(scores, f, indent=4)

    print("\n  💾 Score saved!")


def show_leaderboard():
    if not os.path.exists("scores.json"):
        print("\n  No scores yet!")
        return

    with open("scores.json", "r") as f:
        scores = json.load(f)

    sorted_scores = sorted(scores, key=lambda x: x["wpm"], reverse=True)

    print("\n" + "=" * 55)
    print("           🏆 TOP SCORES")
    print("=" * 55)
    for i, score in enumerate(sorted_scores[:5], 1):
        print(f"  #{i}  WPM: {score['wpm']}   Accuracy: {score['accuracy']}%")
    print("=" * 55)


def main():
    print("\nWelcome to Typing Speed Tester! 🎮")

    while True:
        print("\nWhat would you like to do?")
        print("  1. Start Typing Test")
        print("  2. View Leaderboard")
        print("  3. Quit")

        choice = input("\nEnter choice (1/2/3): ").strip()

        if choice == "1":
            run_test()
            save_score(wpm, accuracy)  # pass results from run_test
        elif choice == "2":
            show_leaderboard()
        elif choice == "3":
            print("\n👋 Thanks for practicing! Goodbye!\n")
            break
        else:
            print("Invalid choice. Try again.")



if __name__ == "__main__":
    main()