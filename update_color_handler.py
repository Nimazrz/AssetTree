import re

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

old_click = r"""                                        \.clickable \{
                                            val newColors = settings\.customAssetColors\.toMutableMap\(\)
                                            newColors\[selectedAssetForColor!!\] = hex
                                            onUpdateSettings\(settings\.copy\(customAssetColors = newColors\)\)
                                            selectedAssetForColor = null
                                        \}"""

new_click = """                                        .clickable {
                                            if (selectedAssetForColor == "AppThemePrimaryColor") {
                                                onUpdateSettings(settings.copy(customAppColor = hex))
                                            } else {
                                                val newColors = settings.customAssetColors.toMutableMap()
                                                newColors[selectedAssetForColor!!] = hex
                                                onUpdateSettings(settings.copy(customAssetColors = newColors))
                                            }
                                            selectedAssetForColor = null
                                        }"""

content = re.sub(old_click, new_click, content)

old_title = r"""title = \{ Text\("انتخاب رنگ برای \$selectedAssetForColor", fontSize = 14\.sp, fontWeight = FontWeight\.Bold, color = colors\.textPrimary\) \},"""
new_title = """title = { Text(if (selectedAssetForColor == "AppThemePrimaryColor") "انتخاب رنگ اصلی برنامه" else "انتخاب رنگ برای $selectedAssetForColor", fontSize = 14.sp, fontWeight = FontWeight.Bold, color = colors.textPrimary) },"""
content = content.replace(old_title, new_title)

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)

