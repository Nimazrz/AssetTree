import re

with open("app/src/main/java/com/example/MainActivity.kt", "r") as f:
    content = f.read()

content = content.replace("preset = displaySettings.themePreset,", "primaryColorHex = displaySettings.customAppColor,")

with open("app/src/main/java/com/example/MainActivity.kt", "w") as f:
    f.write(content)
