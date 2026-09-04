import re

with open("app/src/main/java/com/example/ui/AssetTreeViewModel.kt", "r") as f:
    content = f.read()

new_methods = """    fun onUpdateSettings(settings: DisplaySettings) {
        repository.updateDisplaySettings(settings)
    }

    fun saveCurrentSettingsAsDefault() {
        repository.saveCurrentSettingsAsDefault()
    }

    fun restoreSettingsToDefault() {
        repository.restoreSettingsToDefault()
    }"""

content = content.replace("    fun onUpdateSettings(settings: DisplaySettings) {\n        repository.updateDisplaySettings(settings)\n    }", new_methods)

with open("app/src/main/java/com/example/ui/AssetTreeViewModel.kt", "w") as f:
    f.write(content)
