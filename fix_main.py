import re

with open("app/src/main/java/com/example/MainActivity.kt", "r") as f:
    content = f.read()

old_call = r"""        SettingsDialog\(
            settings = displaySettings,
            rootCalculated = root,
            onDismiss = \{ viewModel\.setSettingsOpen\(false\) \},
            onUpdateSettings = \{ viewModel\.onUpdateSettings\(it\) \},
            onExportBackupJson = \{ viewModel\.repository\.exportBackupJson\(\) \},
            onImportBackupJson = \{ viewModel\.onRestoreJsonBackup\(it\) \},
            onResetAllData = \{ viewModel\.onResetAllData\(\) \},
            onWipeFinancialData = \{ viewModel\.onWipeDatabaseToZero\(\) \}
        \)"""

new_call = """        SettingsDialog(
            settings = displaySettings,
            rootCalculated = root,
            onDismiss = { viewModel.setSettingsOpen(false) },
            onUpdateSettings = { viewModel.onUpdateSettings(it) },
            onExportBackupJson = { viewModel.repository.exportBackupJson() },
            onImportBackupJson = { viewModel.onRestoreJsonBackup(it) },
            onResetAllData = { viewModel.onResetAllData() },
            onWipeFinancialData = { viewModel.onWipeDatabaseToZero() },
            onSaveCurrentSettingsAsDefault = { viewModel.saveCurrentSettingsAsDefault() },
            onRestoreSettingsToDefault = { viewModel.restoreSettingsToDefault() }
        )"""

content = re.sub(old_call, new_call, content)

with open("app/src/main/java/com/example/MainActivity.kt", "w") as f:
    f.write(content)
