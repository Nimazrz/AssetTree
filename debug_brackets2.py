with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    lines = f.readlines()

depth = 0
for i, line in enumerate(lines):
    for c in line:
        if c == '{': depth += 1
        elif c == '}': depth -= 1
    
    if i >= 140 and i <= 320:
        if '{' in line or '}' in line:
            print(f"{i+1:4}: Depth {depth} - {line.strip()}")
