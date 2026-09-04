import re
with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

old_backup = r'''                            Text\("پشتیبان گیری و بازیابی اطلاعات", fontSize = 12\.sp, fontWeight = FontWeight\.Bold, color = colors\.textPrimary\)
                            Text\("تهیه نسخه پشتیبان از کل ساختار درخت دارایی و تنظیمات جهت انتقال به دستگاه دیگر\.", fontSize = 10\.sp, color = colors\.textSecondary\)

                            Row\(
                                modifier = Modifier\.fillMaxWidth\(\),
                                horizontalArrangement = Arrangement\.spacedBy\(8\.dp\)
                            \) \{
                                Button\(
                                    onClick = \{
                                        coroutineScope\.launch \{
                                            backupJsonContent = onExportBackupJson\(\)
                                            showJsonBackupModal = true
                                        \}
                                    \},
                                    colors = ButtonDefaults\.buttonColors\(containerColor = colors\.primary\),
                                    modifier = Modifier\.weight\(1f\)
                                \) \{
                                    Icon\(Icons\.Default\.Backup, contentDescription = null, modifier = Modifier\.size\(14\.dp\), tint = Color\.White\)
                                    Spacer\(modifier = Modifier\.width\(4\.dp\)\)
                                    Text\("پشتیبان گیری", fontSize = 11\.sp\)
                                \}

                                OutlinedButton\(
                                    onClick = \{ showRestoreDialog = true \},
                                    colors = ButtonDefaults\.outlinedButtonColors\(contentColor = colors\.textPrimary\),
                                    border = androidx\.compose\.foundation\.BorderStroke\(1\.dp, colors\.border\),
                                    modifier = Modifier\.weight\(1f\)
                                \) \{
                                    Icon\(Icons\.Default\.Restore, contentDescription = null, modifier = Modifier\.size\(14\.dp\), tint = colors\.textPrimary\)
                                    Spacer\(modifier = Modifier\.width\(4\.dp\)\)
                                    Text\("بازیابی", fontSize = 11\.sp, color = colors\.textPrimary\)
                                \}
                            \}'''

new_backup = """                            SettingTitleWithDescription("کلید پشتیبان تنظیمات و دارایی ها", "تهیه نسخه پشتیبان از کل ساختار درخت دارایی و تنظیمات جهت انتقال به دستگاه دیگر.")

                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.spacedBy(8.dp)
                            ) {
                                Button(
                                    onClick = {
                                        coroutineScope.launch {
                                            backupJsonContent = onExportBackupJson()
                                            showJsonBackupModal = true
                                        }
                                    },
                                    colors = ButtonDefaults.buttonColors(containerColor = colors.primary),
                                    modifier = Modifier.weight(1f)
                                ) {
                                    Icon(Icons.Default.Backup, contentDescription = null, modifier = Modifier.size(14.dp), tint = Color.White)
                                    Spacer(modifier = Modifier.width(4.dp))
                                    Text("تولید کلید پشتیبان", fontSize = 11.sp, maxLines = 1)
                                }

                                OutlinedButton(
                                    onClick = { showRestoreDialog = true },
                                    colors = ButtonDefaults.outlinedButtonColors(contentColor = colors.textPrimary),
                                    border = androidx.compose.foundation.BorderStroke(1.dp, colors.border),
                                    modifier = Modifier.weight(1f)
                                ) {
                                    Icon(Icons.Default.Restore, contentDescription = null, modifier = Modifier.size(14.dp), tint = colors.textPrimary)
                                    Spacer(modifier = Modifier.width(4.dp))
                                    Text("اعمال کلید پشتیبان", fontSize = 11.sp, color = colors.textPrimary, maxLines = 1)
                                }
                            }"""

content = re.sub(old_backup, new_backup, content, flags=re.DOTALL)
with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)
