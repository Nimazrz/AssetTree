import re

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

# Task 1: Rename Chart Asset Colors Settings
content = content.replace('Text("رنگ‌بندی تخصصی کلاس‌های دارایی در نمودارها"', 'Text("رنگ بندی نوع دارایی"')

# Task 8: Currency unit in one row
currency_old = """                            Text("واحد پولی پیش‌فرض نمایش", fontSize = 12.sp, fontWeight = FontWeight.Bold, color = colors.textPrimary)
                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.spacedBy(8.dp)
                            ) {"""

currency_new = """                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.spacedBy(8.dp),
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Text("واحد پول:", fontSize = 12.sp, fontWeight = FontWeight.Bold, color = colors.textPrimary)"""
content = content.replace(currency_old, currency_new)

# Task 9: In chart order settings, keep only "ترتیب نمودارها" and the drag icon.
# Also remove the text button for default order and the descriptive text.
chart_order_regex = re.compile(
    r'(Text\(\s*text = "تنظیمات و شخصی‌سازی ترتیب نمودارها",\s*fontSize = 12\.5\.sp,\s*fontWeight = FontWeight\.Bold,\s*color = colors\.textPrimary\s*\)\s*\}\s*)val defaultOrder.*?Text\(\s*text = "ترتیب قرارگیری.*?colors\.textSecondary\s*\)\s*',
    re.DOTALL
)

def chart_order_replacer(match):
    return match.group(1).replace("تنظیمات و شخصی‌سازی ترتیب نمودارها", "ترتیب نمودارها")

content = chart_order_regex.sub(chart_order_replacer, content)

# Task 11: Backup text changes
content = content.replace('Text("مدیریت اطلاعات و پشتیبان‌گیری"', 'Text("پشتیبان گیری و بازیابی اطلاعات"')
content = content.replace('Text("خروجی JSON"', 'Text("پشتیبان گیری"')
content = content.replace('Text("ورود JSON"', 'Text("بازیابی"')

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)

with open("app/src/main/java/com/example/utils/PdfReportGenerator.kt", "r") as f:
    pdf_content = f.read()

pdf_content = pdf_content.replace('"نمودار دایره ای / خورشیدی"', '"خورشیدی"')
with open("app/src/main/java/com/example/utils/PdfReportGenerator.kt", "w") as f:
    f.write(pdf_content)

