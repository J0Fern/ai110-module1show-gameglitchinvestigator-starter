# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game ran but not without its flaws. I played the game and it gave me hints if I needed to guess higher or lower. When I lost or won I had to start a new game.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The hints were backwards, along with the game not being resettable after winning or losing. The difficulty settings also didn't reflect in the gameplay.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess to 60 | Too high hint | Too low hint | none. |
| Change difficulty to easy mode | Number range shrinks to 20 and attempts increase | Number range stays the same, and attempts decrease | none. |
| Change difficulty to hard mode | Number range increases to 100 and attemps decrease | Number range stays the same, and attempts decrease less than easy mode| none. |
| Winning / losing the game | Press the new game button to restart the game | The new game button doesn't fully reset the game. | none. |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used claude code in VS Code to help me with this project.

When fixing the hints for the guessed number, the AI pointed out that the fallback check existed for and executed on app.py, where the secret number on even attempts would be updated as a string causing the type error to run and check the guessed number against a string.
So far while doing this project I didn't have a time where I disagreed with the AI generated code.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided if a bug was fixed by re-running the code and testing it out manually, as well as asking the AI assistant if the code can handle edge cases.
After fixing the hints for the guessed number I tried the game again and found the hints to help drastically compared to before.
I also asked the AI assistant to write tests for me to test the hints and each of those tests specifically came back successful.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
It took me a while to find out but the reruns allow you to make changes and still have your code running, instead of stopping it and running it again to test out every change. Session state also helps with this making it so that your values are saved while you debug and change things, so that theres no need to constantly repeat setup steps to test if your changes work.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

A habit I will reuse is making new chats with the AI assistant to solve each bug, and also manually approving each change so I can have full awareness of what the AI assistant does.
What I would do differently is take time to look through parts of the code and use AI to help me understand the logic in key areas so that I can have a better idea of whats going on and how I can modify it.
This project help me see how AI is capable of going through logic and also finding other places where this logic could apply or cause error weather it be a couple lines away or in another file, its able to see the current problem and sometimes a future problem. It is also good to move / refactor code into another place or file.

