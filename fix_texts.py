import re

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

# 1. Change title to "تم"
content = content.replace(
    'SettingTitleWithDescription("انتخاب تم و پالت رنگی برنامه"',
    'SettingTitleWithDescription("تم"'
)

# 2. Fix theme mode texts
content = re.sub(
    r'Text\(\s*text = "حالت شب",',
    'Text(\n                                            text = "شب",',
    content
)
content = re.sub(
    r'Text\(\s*text = "حالت روز",',
    'Text(\n                                            text = "روز",',
    content
)

# Remove subtitles
content = re.sub(r'Text\(\s*text = "اتوماتیک",\s*fontSize = 9\.sp,\s*color = if \(isSys\) Color\.White\.copy\(alpha = 0\.8f\) else colors\.textSecondary\s*\)', '', content)
content = re.sub(r'Text\(\s*text = "تیره \(Dark\)",\s*fontSize = 9\.sp,\s*color = if \(isDark\) Color\.White\.copy\(alpha = 0\.8f\) else colors\.textSecondary\s*\)', '', content)
content = re.sub(r'Text\(\s*text = "روشن \(Light\)",\s*fontSize = 9\.sp,\s*color = if \(isLight\) Color\.White\.copy\(alpha = 0\.8f\) else colors\.textSecondary\s*\)', '', content)

# 3. Remove the icon row above "رنگ بندی نوع دارایی"
icon_row = r"""                            Row\(
                                verticalAlignment = Alignment\.CenterVertically,
                                horizontalArrangement = Arrangement\.spacedBy\(6\.dp\)
                            \) \{
                                Icon\(
                                    imageVector = Icons\.Default\.AutoGraph,
                                    contentDescription = null,
                                    tint = colors\.primary,
                                    modifier = Modifier\.size\(18\.dp\)
                                \)
                            \}"""
content = re.sub(icon_row, '', content)

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)

