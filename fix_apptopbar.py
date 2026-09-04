import re
with open("app/src/main/java/com/example/ui/components/AppTopBar.kt", "r") as f:
    content = f.read()

bad_menu = r'''                                        // Theme Colors & Mode Preset.*?HorizontalDivider\(color = colors\.border\.copy\(alpha = 0\.4f\), modifier = Modifier\.padding\(horizontal = 8\.dp\)\)'''

content = re.sub(bad_menu, "", content, flags=re.DOTALL)

with open("app/src/main/java/com/example/ui/components/AppTopBar.kt", "w") as f:
    f.write(content)
