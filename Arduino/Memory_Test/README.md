# 🎮 Arduino Simon Says Game - Memory Challenge!

Have you ever played the classic **Simon Says** game? This is my attempt to bring that game to life using simple Arduino components. It’s a fun, interactive project that tests how good your memory is — with lights, buttons, and a buzzer!

## 🧠 What It Does

- Randomly lights up a sequence of LEDs.
- You have to repeat the exact same pattern using push buttons.
- If you're right: the game adds one more step and gets harder.
- If you're wrong: the buzzer buzzes and the game resets.
  
## 🔧 Hardware Used

- ✅ 1 x Arduino Uno 
- ✅ 4 x LEDs (any colors — I used Red, Green, Yellow, Blue)
- ✅ 4 x Push Buttons
- ✅ 1 x Buzzer
- ✅ Resistors for LEDs & Buttons (220Ω to 1kΩ)
- ✅ Breadboard & Jumper wires

## 🧾 How the Code Works

- `ledPin[]` and `buttonPin[]` arrays reduce repeated code.
- `for` loops are used to read buttons and control LEDs in sequence.
- `random()` helps in generating the game pattern.
- Buzzer gives feedback for correct and wrong attempts.

Want to see the full code? It's clean, short, and loop-based!  
👉 Check the https://github.com/Shwetha12608/embedded-projects/blob/main/Arduino/Memory_Test/code

## 👀 What You’ll Learn

- How to handle multiple inputs (buttons).
- Working with arrays in Arduino.
- Debouncing logic.
- Using buzzer and LEDs together.
- Basics of game logic using microcontrollers.

## 🛠 Future Ideas

- Add LCD for score display.
- Difficulty levels (faster LED blink).
- Use RGB LEDs to reduce wiring.
- Multiplayer version using serial communication!

## 📷 Preview

> *(Add video or gif here if available)*  
> A short clip showing button-LED sequence gameplay.
>[ https://github.com/Shwetha12608/embedded-projects/blob/main/Arduino/Memory_Test/demo_vedio.mp4](https://www.linkedin.com/posts/shwetha-k-c-67621734a_arduino-projectlearning-learningbydoing-activity-7353704937362518016-mBpe?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFc9u_oBkUnx0QzWfCCcFb2nVz2hC6ZN5Pc)

## 💡 Why I Made This

I wanted to test my understanding of digital inputs/outputs, and this game gave me the perfect way to practice arrays, loops, and timing — all in a fun way!
If you're learning Arduino — you should **definitely try building this.**

## 📬 Let’s Connect

If you're working on a similar project or just learning Arduino, feel free to reach out or fork this repo!
> Made with ❤️ using Arduino and Curiosity.
