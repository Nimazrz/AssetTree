import re

with open("app/src/main/java/com/example/ui/theme/Theme.kt", "r") as f:
    content = f.read()

bad_lines = r"""val DarkAppColors = getAppColors\(0xFF005FB1, true\)
val LightAppColors = getAppColors\(0xFF005FB1, false\) = getAppColorsForPreset\(AppThemePreset\.NAVY_CLASSIC, true\)
val LightAppColors = getAppColorsForPreset\(AppThemePreset\.NAVY_CLASSIC, false\)"""

good_lines = """val DarkAppColors = getAppColors(0xFF005FB1, true)
val LightAppColors = getAppColors(0xFF005FB1, false)"""

content = re.sub(bad_lines, good_lines, content)
content = re.sub(r"import com.example.data.model.AppThemePreset\n", "", content)

with open("app/src/main/java/com/example/ui/theme/Theme.kt", "w") as f:
    f.write(content)
