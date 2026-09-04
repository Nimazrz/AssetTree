with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    lines = f.readlines()

depth = 0
for i, line in enumerate(lines):
    for c in line:
        if c == '{': depth += 1
        elif c == '}': depth -= 1
    
    if "when (selectedTab)" in line or "Card(" in line or "1.2 Chart Asset Colors Card" in line or "1.5 Text & Icon Size Selector" in line or "ترتیب نمودارها" in line:
        print(f"Line {i+1}: Depth {depth} - {line.strip()}")
