import re

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

old_click = """                                        onClick = { onSaveCurrentSettingsAsDefault() },"""
new_click = """                                        onClick = { 
                                            onSaveCurrentSettingsAsDefault()
                                            android.widget.Toast.makeText(context, "تنظیمات فعلی به عنوان پیش‌فرض ذخیره شد.", android.widget.Toast.LENGTH_SHORT).show()
                                        },"""

content = content.replace(old_click, new_click)

old_restore = """                                        onClick = { onRestoreSettingsToDefault() },"""
new_restore = """                                        onClick = { 
                                            onRestoreSettingsToDefault()
                                            android.widget.Toast.makeText(context, "تنظیمات به حالت پیش‌فرض بازگردانی شد.", android.widget.Toast.LENGTH_SHORT).show()
                                        },"""

content = content.replace(old_restore, new_restore)

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)
