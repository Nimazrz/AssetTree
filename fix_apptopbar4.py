with open("app/src/main/java/com/example/ui/components/AppTopBar.kt", "r") as f:
    content = f.read()

idx = content.find("if (showPresetDialog) {")
if idx != -1:
    last_brace = content.rfind("}")
    if last_brace != -1:
        # We need to keep the final closing brace of AppTopBar composable
        content = content[:idx] + "}\n"

with open("app/src/main/java/com/example/ui/components/AppTopBar.kt", "w") as f:
    f.write(content)
