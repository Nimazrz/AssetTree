import re
with open("app/src/main/java/com/example/ui/components/AppTopBar.kt", "r") as f:
    content = f.read()

content = content.replace("import com.example.data.model.AppThemePreset\n", "")
content = content.replace("    onSelectThemePreset: (AppThemePreset) -> Unit = {}\n", "")

with open("app/src/main/java/com/example/ui/components/AppTopBar.kt", "w") as f:
    f.write(content)
