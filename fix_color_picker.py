with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    lines = f.readlines()

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
                            }
"""

# Replace lines 283 to 319
out_lines = lines[:282] + [new_theme_selector] + lines[319:]

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.writelines(out_lines)
