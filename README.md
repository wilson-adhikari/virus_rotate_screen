# Screen Rotator Script

This Python script demonstrates how to rotate your primary display programmatically using the `rotatescreen` library.  
It’s meant purely for **educational and experimental** purposes — to show how Python can control display orientation.

---

## ⚠️ WARNING — READ BEFORE RUNNING

This script will **continuously rotate your computer screen** several times in quick succession.  
Running it will cause your display to flip repeatedly, which may:
- Disrupt your current work.
- Confuse input orientation (especially with multiple monitors).
- Cause motion discomfort for some users.

**Do not** run this script on:
- A shared or production computer.
- A system connected to external displays used by others.
- Any device during presentations, recordings, or active tasks.

Run only on your **own machine** in a **safe, controlled environment**.  
If you lose control of the display orientation, press `Ctrl + Alt + Up Arrow` (on Windows) to reset manually.

---

## 🧠 What It Does

The script:
1. Gets your primary display using `rotatescreen`.
2. Rotates it through 90°, 180°, 270°, and 0° orientations.
3. Repeats this sequence four times, pausing briefly between each rotation.

---

## 🧩 Requirements

You’ll need Python 3 and the `rotatescreen` package.  
Install it via pip:

```bash
pip install rotatescreen
