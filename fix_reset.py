import re
with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

old_reset = r'''                            Text\("بازنشانی به پرتفوی اولیه نمونه", fontSize = 12\.sp, fontWeight = FontWeight\.Bold, color = colors\.primary\)
                            Text\("بازگردانی دارایی‌های نمونه پیش‌فرض اپلیکیشن شامل طلا، سهام و ارز\.", fontSize = 10\.sp, color = colors\.textSecondary\)'''

new_reset = """                            SettingTitleWithDescription("بازنشانی به پرتفوی اولیه نمونه", "بازگردانی دارایی‌های نمونه پیش‌فرض اپلیکیشن شامل طلا، سهام و ارز.")"""

content = re.sub(old_reset, new_reset, content)

# There's also one for "خام کردن کامل تمام اطلاعات مالی (صفر کردن)" around line 866.
# Let's fix that one too.
old_clear = r'''                            Text\("حذف و پاک‌سازی تمام اطلاعات", fontSize = 12\.sp, fontWeight = FontWeight\.Bold, color = colors\.loss\)
                            Text\("حذف و پاک‌سازی تمام دارایی‌ها، مبالغ و نودها جهت شروع یک پرتفوی کاملاً جدید و صفر\.", fontSize = 10\.sp, color = colors\.textSecondary\)'''

new_clear = """                            SettingTitleWithDescription("حذف و پاک‌سازی تمام اطلاعات", "حذف و پاک‌سازی تمام دارایی‌ها، مبالغ و نودها جهت شروع یک پرتفوی کاملاً جدید و صفر.")"""
content = re.sub(old_clear, new_clear, content)

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)
