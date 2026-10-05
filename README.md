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

**Purpose.** A Streamlit number-guessing game: pick a difficulty, guess the secret number within a limited number of attempts, get Higher/Lower hints, and earn a score (more points for winning in fewer attempts).

**Bugs found** (full reproduction table in `reflection.md`):
- Hints were swapped ("Go HIGHER!" for a guess that was too high).
- On even-numbered attempts the secret was cast to a string, so comparisons were text-based and the game could not be won.
- "New Game" ignored the difficulty range and left status, score, and history untouched, so a finished game stayed locked.
- Attempts started at 1, so "Attempts left" was off by one; the banner always said 1-100.
- Scoring was inconsistent (Too High added 5 points on even attempts; wins used `attempt + 1`).
- Hard (1-50) was easier than Normal (1-100).

**Fixes applied.**
- Moved `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` into `logic_utils.py`; `app.py` now only handles the UI.
- Corrected hint messages, removed the string-cast and the `TypeError` fallback, and made every wrong guess cost 5 points.
- Added a `reset_game()` helper used by New Game and by difficulty changes; Hard is now 1-200; attempts start at 0.
- Added pytest regression tests in `tests/test_game_logic.py`.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

## Demo Walkthrough (Normal difficulty, secret = 50)
1. Player enters a guess of 40; the game returns "Too Low" with the hint "Go HIGHER!" and the score drops to -5.
2. Player enters 70; the game returns "Too High" with the hint "Go LOWER!" and the score drops to -10 (this is an even attempt, which used to break the comparison).
3. Player enters 50 on the third attempt; the game shows balloons and "You won!", with a final score of 60 (-10 + 70).
4. The sidebar shows the attempt limit and range; "Attempts left" counts down correctly from 8.
5. Clicking "New Game" resets score, history, attempts, and status, and draws a new secret from the selected difficulty's range.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
..........                                                               [100%]
10 passed in 0.04s
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
