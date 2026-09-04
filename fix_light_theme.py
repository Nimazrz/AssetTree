import re
with open("app/src/main/java/com/example/ui/theme/Theme.kt", "r") as f:
    content = f.read()

content = content.replace("surface = Color(0xFFF7F9FC)", "surface = Color(0xFFF2F4F7)")
content = content.replace("surfaceVariant = Color(0xFFEAEFF5)", "surfaceVariant = Color(0xFFE5E7EB)")
content = content.replace("background = bg", "background = bg.copy(alpha=0.9f)") # or just leave bg since I set it in presets
content = content.replace("inputBackground = Color(0xFFF8FAFC)", "inputBackground = Color(0xFFF3F4F6)")
with open("app/src/main/java/com/example/ui/theme/Theme.kt", "w") as f:
    f.write(content)
