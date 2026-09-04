import re

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

old_params = r"""    onImportBackupJson: \(String\) -> Unit,
    onResetAllData: \(\) -> Unit,
    onWipeFinancialData: \(\) -> Unit = \{\}
\) \{"""

new_params = """    onImportBackupJson: (String) -> Unit,
    onResetAllData: () -> Unit,
    onWipeFinancialData: () -> Unit = {},
    onSaveCurrentSettingsAsDefault: () -> Unit = {},
    onRestoreSettingsToDefault: () -> Unit = {}
) {"""

content = re.sub(old_params, new_params, content)

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)
