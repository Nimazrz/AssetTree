import re
with open("app/src/main/java/com/example/ui/components/AppTopBar.kt", "r") as f:
    content = f.read()

# I will just remove the if (showPresetDialog) block entirely
dialog_pattern = r'if \(showPresetDialog\).*?containerColor = colors\.surface\n\s*\)'
content = re.sub(dialog_pattern, '', content, flags=re.DOTALL)

# And replace `showPresetDialog = true` with nothing or just remove that dropdown item if it's still there
# It might be in the TopBar menu...
content = re.sub(r'showPresetDialog = true', '', content)
content = re.sub(r'showPresetDialog = false', '', content)

with open("app/src/main/java/com/example/ui/components/AppTopBar.kt", "w") as f:
    f.write(content)
