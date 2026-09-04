import re

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

# Find the end of the day/night Row
row_end = r"""                                \}
                            \}

                        \}
                    \}

                    // 1.2 Chart Asset Colors Card"""

replacement = """                                }
                            }
                            
                            HorizontalDivider(color = colors.border.copy(alpha = 0.5f))
                            
                            Surface(
                                shape = RoundedCornerShape(10.dp),
                                color = colors.surface,
                                border = androidx.compose.foundation.BorderStroke(1.dp, colors.border),
                                modifier = Modifier.fillMaxWidth().clickable { selectedAssetForColor = "AppThemePrimaryColor" }
                            ) {
                                Row(
                                    modifier = Modifier.padding(horizontal = 12.dp, vertical = 12.dp),
                                    verticalAlignment = Alignment.CenterVertically,
                                    horizontalArrangement = Arrangement.SpaceBetween
                                ) {
                                    Text(
                                        text = "رنگ تم برنامه",
                                        fontSize = 13.sp,
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

                        }
                    }

                    // 1.2 Chart Asset Colors Card"""

content = re.sub(row_end, replacement, content)

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)
