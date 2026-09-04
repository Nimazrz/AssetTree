import re

with open("app/src/main/java/com/example/data/model/Models.kt", "r") as f:
    content = f.read()

# Remove AppThemePreset enum
content = re.sub(r"enum class AppThemePreset[\s\S]*?\}\n", "", content)

# Update DisplaySettings
content = content.replace("val themePreset: AppThemePreset = AppThemePreset.NAVY_CLASSIC,", "val customAppColor: Long = 0xFF005FB1,")

with open("app/src/main/java/com/example/data/model/Models.kt", "w") as f:
    f.write(content)

