import re

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

# 1. Remove the header "پالت رنگ و تم اپلیکیشن" and its description text
old_header = r"""                            Row\(
                                verticalAlignment = Alignment\.CenterVertically,
                                horizontalArrangement = Arrangement\.spacedBy\(6\.dp\)
                            \) \{
                                Icon\(
                                    imageVector = Icons\.Default\.Palette,
                                    contentDescription = null,
                                    tint = colors\.primary,
                                    modifier = Modifier\.size\(18\.dp\)
                                \)
                                Text\(
                                    text = "پالت رنگ و تم اپلیکیشن",
                                    fontSize = 13\.sp,
                                    fontWeight = FontWeight\.Bold,
                                    color = colors\.textPrimary
                                \)
                            \}

                            Text\(
                                text = "حالت تیره/روشن و پالت رنگی سازمانی برنامه را از این بخش انتخاب کنید\.",
                                fontSize = 11\.sp,
                                color = colors\.textSecondary
                            \)"""
content = re.sub(old_header, '', content)

# 2. Remove the "تم" section (Primary Color Selection)
old_custom_theme = r"""                            // Theme Palette Custom Color Selection
                            HorizontalDivider\(color = colors\.border\.copy\(alpha = 0\.5f\)\)
                            SettingTitleWithDescription\("تم", "تنظیم رنگ اصلی \(Primary Color\) برای کل رابط کاربری اپلیکیشن\."\)
                            Surface\(
                                shape = RoundedCornerShape\(8\.dp\),
                                color = colors\.surface,
                                border = androidx\.compose\.foundation\.BorderStroke\(1\.dp, colors\.border\.copy\(alpha = 0\.6f\)\),
                                modifier = Modifier\.fillMaxWidth\(\)\.clickable \{ selectedAssetForColor = "AppThemePrimaryColor" \}
                            \) \{
                                Row\(
                                    modifier = Modifier\.padding\(horizontal = 10\.dp, vertical = 10\.dp\),
                                    verticalAlignment = Alignment\.CenterVertically,
                                    horizontalArrangement = Arrangement\.SpaceBetween
                                \) \{
                                    Text\(
                                        text = "رنگ اصلی برنامه",
                                        fontSize = 11\.5\.sp,
                                        fontWeight = FontWeight\.Bold,
                                        color = colors\.textPrimary
                                    \)
                                    Box\(
                                        modifier = Modifier
                                            \.size\(24\.dp\)
                                            \.clip\(RoundedCornerShape\(4\.dp\)\)
                                            \.background\(Color\(settings\.customAppColor\)\)
                                            \.border\(1\.dp, colors\.border, RoundedCornerShape\(4\.dp\)\)
                                    \)
                                \}
                            \}"""
content = re.sub(old_custom_theme, '', content)

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)
