import re
with open("app/src/main/java/com/example/ui/components/AppTopBar.kt", "r") as f:
    content = f.read()

# Remove the DropdownMenuItem for Palette
# Find "// Theme Colors & Mode Preset"
dropdown_item_pattern = r'// Theme Colors & Mode Preset.*?DropdownMenuItem\([\s\S]*?\}\s*\)\s*\}\s*\)'
content = re.sub(dropdown_item_pattern, '', content)

# Remove the Preset Dialog
dialog_pattern = r'if \(showPresetDialog\) \{.*?onDismissRequest\s*=\s*\{\s*showPresetDialog\s*=\s*false\s*\}[\s\S]*?\}\s*\}\s*\}'
content = re.sub(dialog_pattern, '', content)

# Remove showPresetDialog state
content = re.sub(r'var showPresetDialog by remember \{ mutableStateOf\(false\) \}\n?', '', content)

# Fix date/time background
date_time_surface = r'Surface\(\s*shape = RoundedCornerShape\(8\.dp\),\s*color = colors\.surface\.copy\(alpha = 0\.95f\),\s*border = androidx\.compose\.foundation\.BorderStroke\(1\.dp, colors\.border\.copy\(alpha = 0\.7f\)\)'
new_date_time = 'Surface(\n                                    shape = RoundedCornerShape(8.dp),\n                                    color = Color.Transparent'
content = re.sub(date_time_surface, new_date_time, content)

with open("app/src/main/java/com/example/ui/components/AppTopBar.kt", "w") as f:
    f.write(content)

