with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    lines = f.readlines()

depth = 0
for i, line in enumerate(lines):
    for c in line:
        if c == '{': depth += 1
        elif c == '}': depth -= 1
    if depth == 0 and '}' in line:
        print(f"Depth 0 at line {i+1}: {line.strip()}")
