with open("app/src/main/java/com/example/ui/views/ClassicTreeView.kt", "r") as f:
    text = f.read()

count = 0
for i, line in enumerate(text.split('\n')):
    for char in line:
        if char == '{': count += 1
        elif char == '}': count -= 1
    if count == 0 and 'fun ' in line:
        print(f"Function started on line {i+1} with count 0!")
    if count < 0:
        print(f"Negative count on line {i+1}!")
print(f"Final count: {count}")
