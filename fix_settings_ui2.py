import re

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

new_card = """                    }
                    
                    if (selectedTabIndex == 0 || selectedTabIndex == 1) {
                        // Default Settings Card
                        Card(
                            shape = RoundedCornerShape(20.dp),
                            colors = CardDefaults.cardColors(containerColor = colors.surfaceVariant.copy(alpha = 0.5f)),
                            border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f))
                        ) {
                            Column(modifier = Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                                SettingTitleWithDescription("تنظیمات پیش‌فرض", "ذخیره تنظیمات فعلی (شامل تم، منوها، واحد پول و...) به عنوان پیش‌فرض، یا بازنشانی به حالت پیش‌فرض.")
                                
                                Row(
                                    modifier = Modifier.fillMaxWidth(),
                                    horizontalArrangement = Arrangement.spacedBy(8.dp)
                                ) {
                                    Button(
                                        onClick = { onSaveCurrentSettingsAsDefault() },
                                        modifier = Modifier.weight(1f),
                                        colors = ButtonDefaults.buttonColors(containerColor = colors.primary, contentColor = Color.White),
                                        shape = RoundedCornerShape(10.dp)
                                    ) {
                                        Text("ذخیره به عنوان پیش‌فرض", fontSize = 10.5.sp, fontWeight = FontWeight.Bold, textAlign = androidx.compose.ui.text.style.TextAlign.Center)
                                    }
                                    
                                    OutlinedButton(
                                        onClick = { onRestoreSettingsToDefault() },
                                        modifier = Modifier.weight(1f),
                                        colors = ButtonDefaults.outlinedButtonColors(contentColor = colors.textPrimary),
                                        border = androidx.compose.foundation.BorderStroke(1.dp, colors.primary),
                                        shape = RoundedCornerShape(10.dp)
                                    ) {
                                        Text("بازگشت به پیش‌فرض", fontSize = 10.5.sp, fontWeight = FontWeight.Bold, textAlign = androidx.compose.ui.text.style.TextAlign.Center)
                                    }
                                }
                            }
                        }
                    }"""

# Insert before "if (selectedTabIndex == 2)"
content = content.replace("                    }\n                    if (selectedTabIndex == 2) {", new_card + "\n                    if (selectedTabIndex == 2) {")

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)
