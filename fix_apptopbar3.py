with open("app/src/main/java/com/example/ui/components/AppTopBar.kt", "r") as f:
    content = f.read()

idx = content.find("if (showPresetDialog) {")
if idx != -1:
    end_idx = content.find("if (showExitConfirmDialog) {", idx)
    if end_idx != -1:
        content = content[:idx] + content[end_idx:]

with open("app/src/main/java/com/example/ui/components/AppTopBar.kt", "w") as f:
    f.write(content)
