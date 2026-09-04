with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

# Let's fix the extra closing brace at line 386!
# If line 386 is an extra brace, it closes the if early.
lines = content.split('\n')
print(lines[385])
print(lines[386])
