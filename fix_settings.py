import re

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

# Task 1: Rename "رنگ‌بندی تخصصی کلاس‌های دارایی در نمودارها" to "رنگ بندی نوع دارایی"
content = content.replace("رنگ‌بندی تخصصی کلاس‌های دارایی در نمودارها", "رنگ بندی نوع دارایی")

# Task 11: Backup section
content = content.replace("پشتیبان‌گیری و بازیابی داده‌ها (JSON)", "پشتیبان گیری و بازیابی اطلاعات")
content = content.replace('Text("بازیابی JSON"', 'Text("بازیابی"')

# Task 9: Remove items in Chart Order box. Keep only title and icon.
# The title is 'Text(\n                                        text = "ترتیب نمودارها",'
chart_order_pattern = r'val currentOrder = settings\.customViewOrder\.ifEmpty \{[\s\S]*?\}(?=\s*// 2\. Data Source & Root Options)'
content = re.sub(chart_order_pattern, '', content)

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)
