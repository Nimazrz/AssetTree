import re

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

# 1. Currency unit captions
content = re.sub(
    r"""                                        Text\(\s*"\(۱۰ ریال\)",\s*fontSize = 10\.sp,\s*color = if \(settings\.currencyUnit == CurrencyUnit\.TOMAN\) Color\.White\.copy\(alpha = 0\.8f\) else colors\.textSecondary\s*\)""",
    "",
    content
)

content = re.sub(
    r"""                                        Text\(\s*"\(واحد پایه\)",\s*fontSize = 10\.sp,\s*color = if \(settings\.currencyUnit == CurrencyUnit\.RIAL\) Color\.White\.copy\(alpha = 0\.8f\) else colors\.textSecondary\s*\)""",
    "",
    content
)

# 2. Theme mode captions
content = re.sub(
    r"""                                        Text\(\s*"اتوماتیک",\s*fontSize = 9\.sp,\s*color = if \(isSys\) Color\.White\.copy\(alpha = 0\.8f\) else colors\.textSecondary\s*\)""",
    "",
    content
)
content = re.sub(
    r"""                                        Text\(\s*"تیره \(Dark\)",\s*fontSize = 9\.sp,\s*color = if \(isDark\) Color\.White\.copy\(alpha = 0\.8f\) else colors\.textSecondary\s*\)""",
    "",
    content
)
content = re.sub(
    r"""                                        Text\(\s*"روشن \(Light\)",\s*fontSize = 9\.sp,\s*color = if \(isLight\) Color\.White\.copy\(alpha = 0\.8f\) else colors\.textSecondary\s*\)""",
    "",
    content
)

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)

