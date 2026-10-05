# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The purpose of the game is to contain a secret number that you have to try to guess with limited attempts. Based on the games difficulty the number range could be between 1 and 20, 50, or 100, with the attempts decreasing as the difficulty increases. As you guess and submit the game will give you hints that are toggleable, suggesting you to guess higher or lower until you either guess the secret number, or run out of attempts, then you restart.

- [ ] Detail which bugs you found.
The bugs that I found was first the hints would tell you the opposite of what they were intended to mean, guessing too high caused the hints to tell you to guess higher and guessing too low caused the hints to tell you to go lower. The next bug was that after winning or losing the game, the new game button wouldn't reset the game state, it would instead just generate a new random secret number but only giving you 0 attempts to do so. Lastly the difficulties were improperly implemented, no matter which one you chose the number pool was always between 1-100 and the number of attempts didnt match the games difficulty, with normal giving you more tries than easy mode.

- [ ] Explain what fixes you applied.
I fixed the logic for the hints, making them steer you in the right direction while also removing the comparison for the string and an integer that happened as a result of the secret number becoming a string every even attempt at the game which I also fixed to just be an integer.
I fixed the logic for the difficulty selection, making it so that each difficulty matches whats chosen by changing the hard coded 1,100 range to be the low and high variables instead.
I fixed the game reset button by making the function reset the state of the game, specifically the attempt history and setting the status of the game to "playing".

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Run `python -m streamlit run app.py` and pick a difficulty in the sidebar. The sidebar shows the range and attempts allowed (Easy: 1-20 with 5 attempts, Normal: 1-50 with 6, Hard: 1-100 with 8).
2. Type a number into the "Enter your guess:" box and click **Submit Guess 🚀**. Empty or non-numeric input shows an error and still counts as an attempt.
3. Read the hint (with "Show hint" checked). A guess that is too high now says "📉 Go LOWER!" and one that is too low says "📈 Go HIGHER!". The "Attempts left" counter goes down after each guess.
4. Keep guessing until you find the secret number. Opening "Developer Debug Info" reveals the secret, attempts, score, and guess history if you want to verify the hints. A correct guess shows balloons, the final score, and ends the round.
5. If you run out of attempts, the game shows the secret and a "Game over" message. Click **New Game 🔁** to reset the attempts, history, and status, and get a fresh secret. Changing the difficulty also starts a new round.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================

============================================================================ test session starts =============================================================================
platform win32 -- Python 3.13.15, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\josef\Documents\VSCode Projects\Codepath AI110\Project1\ai110-module1show-gameglitchinvestigator-starter\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\josef\Documents\VSCode Projects\Codepath AI110\Project1\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 3 items                                                                                                                                                             

tests/test_game_logic.py::test_too_high_tells_player_to_go_lower PASSED                                                                                                 [ 33%]
tests/test_game_logic.py::test_too_low_tells_player_to_go_higher PASSED                                                                                                 [ 66%]
tests/test_game_logic.py::test_numeric_comparison_not_string_comparison PASSED                                                                                          [100%]

============================================================================= 3 passed in 0.04s ==============================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
