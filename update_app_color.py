import re

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

old_theme_selector = r"""                            // Theme Palette Preset Selection\s*HorizontalDivider\(color = colors\.border\.copy\(alpha = 0\.5f\)\)\s*Text\(\s*text = "انتخاب تم و پالت رنگی برنامه:",\s*fontSize = 12\.sp,\s*fontWeight = FontWeight\.Bold,\s*color = colors\.textPrimary\s*\)\s*Column\(verticalArrangement = Arrangement\.spacedBy\(8\.dp\)\) \{\s*AppThemePreset\.values\(\)\.toList\(\)\.chunked\(6\)\.forEach \{ rowPresets ->\s*Row\(\s*modifier = Modifier\.fillMaxWidth\(\),\s*horizontalArrangement = Arrangement\.SpaceBetween\s*\) \{\s*rowPresets\.forEach \{ preset ->\s*val isSel = settings\.themePreset == preset\s*Box\(\s*modifier = Modifier\s*\.size\(36\.dp\)\s*\.clip\(RoundedCornerShape\(8\.dp\)\)\s*\.background\(Color\(preset\.primaryHex\)\)\s*\.border\(if \(isSel\) 3\.dp else 1\.dp, if \(isSel\) colors\.textPrimary else colors\.border, RoundedCornerShape\(8\.dp\)\)\s*\.clickable \{ onUpdateSettings\(settings\.copy\(themePreset = preset\)\) \},\s*contentAlignment = Alignment\.Center\s*\) \{\s*if \(isSel\) \{\s*Icon\(Icons\.Default\.Check, contentDescription = null, tint = Color\.White, modifier = Modifier\.size\(20\.dp\)\)\s*\}\s*\}\s*\}\s*\}\s*\}\s*\}"""

new_theme_selector = """                            // Theme Palette Custom Color Selection
                            HorizontalDivider(color = colors.border.copy(alpha = 0.5f))
                            SettingTitleWithDescription("انتخاب تم و پالت رنگی برنامه", "تنظیم رنگ اصلی (Primary Color) برای کل رابط کاربری اپلیکیشن.")
                            Surface(
                                shape = RoundedCornerShape(8.dp),
                                color = colors.surface,
                                border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f)),
                                modifier = Modifier.fillMaxWidth().clickable { selectedAssetForColor = "AppThemePrimaryColor" }
                            ) {
                                Row(
                                    modifier = Modifier.padding(horizontal = 10.dp, vertical = 10.dp),
                                    verticalAlignment = Alignment.CenterVertically,
                                    horizontalArrangement = Arrangement.SpaceBetween
                                ) {
                                    Text(
                                        text = "رنگ اصلی برنامه",
                                        fontSize = 11.5.sp,
                                        fontWeight = FontWeight.Bold,
                                        color = colors.textPrimary
                                    )
                                    Box(
                                        modifier = Modifier
                                            .size(24.dp)
                                            .clip(RoundedCornerShape(4.dp))
                                            .background(Color(settings.customAppColor))
                                            .border(1.dp, colors.border, RoundedCornerShape(4.dp))
                                    )
                                }
                            }"""

content = re.sub(old_theme_selector, new_theme_selector, content, flags=re.DOTALL)

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)
