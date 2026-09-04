import re
with open("app/src/main/java/com/example/ui/views/ClassicTreeView.kt", "r") as f:
    content = f.read()

# I will undo what `sed 's/^}$/}\n}/'` did.
# Every line that was just `}` became `}\n}`. So we can find `\n}\n}` where the first `}` is alone on a line?
# It's better to just write a simple script: if a line is `}` and the next line is `}`, and the second `}` has no indentation, remove the second one.
lines = content.split('\n')
new_lines = []
skip = False
for i, line in enumerate(lines):
    if skip:
        skip = False
        continue
    new_lines.append(line)
    if line == "}":
        if i + 1 < len(lines) and lines[i+1] == "}":
            skip = True

with open("app/src/main/java/com/example/ui/views/ClassicTreeView.kt", "w") as f:
    f.write('\n'.join(new_lines))
