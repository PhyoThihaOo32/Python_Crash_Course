print("""
👽👾 Welcome to the Amazing Alien Shooter Game! 👾👽

🎯 Shoot as many aliens as you can to earn points:
    🟢 Green Alien   → 5 points
    🟡 Yellow Alien  → 3 points
    🔴 Red Alien     → 10 points

Type 'exit' anytime to end the game... if you dare. 😈
""")

score = 0

while True:
    color = input("What color of alien did you shoot down? ").strip().lower()

    if color == 'exit':
        print("\n🛑 Game Over! The aliens will remember you... You can run, but you can't hide! 👀")
        break
    elif color == 'green':
        print("🟢 You shot down the Green Alien! 👽 [ +5 points ]")
        score += 5
    elif color == 'yellow':
        print("🟡 You shot down the Yellow Alien! 👽 [ +3 points ]")
        score += 3
    elif color == 'red':
        print("🔴 You shot down the Red Alien! 👽 [ +10 points ]")
        score += 10
    else:
        print("💥 You missed the target! No points for you... LOL 😅")

    print(f"🎯 Current Score: {score}\n")

print(f"""
🏆 Final Score: {score} points!
🎁 Don’t forget to exchange your points for intergalactic rewards!

Thanks for playing – Star_Trooper! 🌌
""")


