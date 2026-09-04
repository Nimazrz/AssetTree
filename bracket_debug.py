with open("app/src/main/java/com/example/ui/views/ClassicTreeView.kt", "r") as f:
    text = f.read()

count = 0
for i, line in enumerate(text.split('\n')):
    if i >= 250 and i <= 265:
        print(f"L{i+1} Start: {count} | {line}")
    for char in line:
        if char == '{': count += 1
        elif char == '}': count -= 1
    if i >= 250 and i <= 265:
        print(f"L{i+1} End  : {count}")
