import re

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

# Add the SettingTitle helper composable at the bottom of the file
setting_title_code = """
@Composable
fun SettingTitleWithDescription(title: String, description: String) {
    var expanded by remember { mutableStateOf(false) }
    val colors = AppTheme.colors
    Column(modifier = Modifier.fillMaxWidth().clickable { expanded = !expanded }) {
        Text(
            text = title,
            fontSize = 12.sp,
            fontWeight = FontWeight.Bold,
            color = colors.textPrimary,
            modifier = Modifier.padding(vertical = 4.dp)
        )
        androidx.compose.animation.AnimatedVisibility(visible = expanded) {
            Surface(
                shape = RoundedCornerShape(6.dp),
                color = colors.surfaceVariant,
                modifier = Modifier.fillMaxWidth().padding(top = 4.dp)
            ) {
                Text(
                    text = description,
                    fontSize = 10.sp,
                    color = colors.textSecondary,
                    modifier = Modifier.padding(8.dp)
                )
            }
        }
    }
}
"""

if "fun SettingTitleWithDescription" not in content:
    content = content + setting_title_code

# Now replace the hardcoded Text title/desc with SettingTitleWithDescription
# 1. Theme mode
t1_old = """                            Text(
                                text = "حالت تیره و روشن (تم برنامه)",
                                fontSize = 13.sp,
                                fontWeight = FontWeight.Bold,
                                color = colors.textPrimary
                            )
                            Text(
                                text = "حالت شبانه و روزانه برنامه را در اینجا مدیریت کنید. حالت سیستم به‌طور خودکار با گوشی شما هماهنگ می‌شود.",
                                fontSize = 10.5.sp,
                                color = colors.textSecondary
                            )"""
t1_new = '                            SettingTitleWithDescription("حالت تیره و روشن (تم برنامه)", "حالت شبانه و روزانه برنامه را در اینجا مدیریت کنید. حالت سیستم به‌طور خودکار با گوشی شما هماهنگ می‌شود.")'
content = content.replace(t1_old, t1_new)

# 2. Asset Colors
t2_old = """                                Text(
                                    text = "رنگ بندی نوع دارایی",
                                    fontSize = 13.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = colors.textPrimary
                                )
                            }

                            Text(
                                text = "راهنمای رنگ‌بندی ثابت و سایه‌دار دارایی‌ها در تمام نمودارها (نقشه درختی، خورشیدی، درختی مدرن و نوار انباشته):",
                                fontSize = 10.5.sp,
                                color = colors.textSecondary
                            )"""
t2_new = """                            }
                            SettingTitleWithDescription("رنگ بندی نوع دارایی", "راهنمای رنگ‌بندی ثابت و سایه‌دار دارایی‌ها در تمام نمودارها (نقشه درختی، خورشیدی، درختی مدرن و نوار انباشته):")"""
content = content.replace(t2_old, t2_new)

# 3. Node labels
t3_old = """                            Text("آیتم‌های نمایشی جلوی نام نودها", fontSize = 12.sp, fontWeight = FontWeight.Bold, color = colors.textPrimary)
                            Text("تنظیم نمایش یا عدم نمایش درصد از کل، درصد از هم‌گروه و مبلغ خلاصه شده جلوی هر دارایی", fontSize = 10.sp, color = colors.textSecondary)"""
t3_new = '                            SettingTitleWithDescription("آیتم‌های نمایشی جلوی نام نودها", "تنظیم نمایش یا عدم نمایش درصد از کل، درصد از هم‌گروه و مبلغ خلاصه شده جلوی هر دارایی")'
content = content.replace(t3_old, t3_new)

# 4. Persian Digits
t4_old = """                            Column(modifier = Modifier.weight(1f)) {
                                Text("اعداد و ارقام به خط فارسی", fontSize = 12.sp, fontWeight = FontWeight.Bold, color = colors.textPrimary)
                                Text("نمایش مبالغ و درصدها با ارقام فارسی (۱۲۳,۴۵۶)", fontSize = 10.sp, color = colors.textSecondary)
                            }"""
t4_new = """                            Column(modifier = Modifier.weight(1f)) {
                                SettingTitleWithDescription("اعداد و ارقام به خط فارسی", "نمایش مبالغ و درصدها با ارقام فارسی (۱۲۳,۴۵۶)")
                            }"""
content = content.replace(t4_old, t4_new)

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)
