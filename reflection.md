# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The game loaded fine, but it was effectively unwinnable: the hints pointed the wrong way, and every second guess was compared against a string version of the secret, so it gave wrong answers or could never match. New Game also left the old state in place and ignored the difficulty range. The bug table below lists five concrete bugs with inputs and results.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Secret 50, guess 60 (any attempt) | "Too High" with hint "Go LOWER!" | Hint says "Go HIGHER!" and the Too Low hint says "Go LOWER!" (hints are swapped) | None (silent logic bug) |
| Secret 50, guess 50 on an even-numbered attempt (2nd, 4th, ...) | "Win" | `app.py` converts the secret to a string on even attempts, so `check_guess` falls back to string comparison; 50 vs "50" never wins, and guess 9 vs "50" reports Too High because "9" > "50" as text | No exception; `TypeError` is swallowed by `except TypeError` in `check_guess` |
| Click "New Game" after a finished game, or switch difficulty | Fresh game: new secret in the selected range, score/history/status reset | Secret always drawn from 1-100, status stays "won"/"lost" so the game stays locked, score and history persist, attempts reset to 0 while a new session starts at 1 | None; "You already won. Start a new game" message keeps showing |
| Any game | "Attempts left" matches the limit shown in the sidebar | `attempts` starts at 1, so the banner shows one fewer attempt than allowed; banner text always says "1 and 100" even on Easy (1-20) | None |
| Wrong guess on Easy/Normal/Hard | Score drops by a fixed 5 for a wrong guess | "Too High" on an even attempt adds 5 points instead of subtracting; winning score uses `attempt_number + 1`, penalizing the player an extra attempt | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I treated a bug as fixed only when a test that failed before the fix passed after it, and then confirmed it in the running app. For example, `test_numeric_comparison_not_string` checks that guess 9 against secret 50 is "Too Low"; with the old string cast it was "Too High" because "9" > "50" as text. I also drove the Streamlit app with Streamlit's `AppTest` to play a short game and check hints, score, and New Game reset. The AI suggested which regression cases to write, and I checked each one against the bug it was meant to catch. The starter tests also expected `check_guess` to return a bare string even though its docstring says it returns a tuple, so I updated the tests to unpack `(outcome, message)`.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit re-runs the whole script from top to bottom every time you click a button or change an input, so ordinary variables are reset on every click. `st.session_state` is a dictionary that survives those reruns, so anything that must persist (the secret number, attempts, score) lives there and is only initialized when it is missing or when a new game starts.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
