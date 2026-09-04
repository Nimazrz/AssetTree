import re

with open("app/src/main/java/com/example/data/repository/AssetRepository.kt", "r") as f:
    content = f.read()

# Add imports for json if not present
if "import org.json.JSONObject" not in content:
    content = content.replace("import kotlinx.coroutines.flow.asStateFlow", "import kotlinx.coroutines.flow.asStateFlow\nimport org.json.JSONObject\nimport org.json.JSONArray")

new_methods = """    fun saveCurrentSettingsAsDefault() {
        val settings = _displaySettings.value
        prefs.edit().apply {
            putBoolean("def_showPercentOfTotal", settings.showPercentOfTotal)
            putBoolean("def_showPercentOfGroup", settings.showPercentOfGroup)
            putBoolean("def_showTotalValue", settings.showTotalValue)
            putInt("def_decimalPlaces", settings.decimalPlaces)
            putBoolean("def_compactCurrency", settings.compactCurrency)
            putString("def_currencyUnit", settings.currencyUnit.name)
            putBoolean("def_usePersianDigits", settings.usePersianDigits)
            putString("def_themeMode", settings.themeMode.name)
            putBoolean("def_privacyMode", settings.privacyMode)
            putString("def_fontSize", settings.fontSize.name)
            putLong("def_customAppColor", settings.customAppColor)
            putString("def_customViewOrder", settings.customViewOrder.joinToString(",") { it.name })
            apply()
        }
    }

    fun restoreSettingsToDefault() {
        val showPT = prefs.getBoolean("def_showPercentOfTotal", true)
        val showPG = prefs.getBoolean("def_showPercentOfGroup", true)
        val showTV = prefs.getBoolean("def_showTotalValue", true)
        val dec = prefs.getInt("def_decimalPlaces", 1)
        val compact = prefs.getBoolean("def_compactCurrency", true)
        val cUnitStr = prefs.getString("def_currencyUnit", CurrencyUnit.TOMAN.name) ?: CurrencyUnit.TOMAN.name
        val cUnit = try { CurrencyUnit.valueOf(cUnitStr) } catch (e: Exception) { CurrencyUnit.TOMAN }
        val persianDigits = prefs.getBoolean("def_usePersianDigits", true)
        val themeModeStr = prefs.getString("def_themeMode", ThemeMode.SYSTEM.name) ?: ThemeMode.SYSTEM.name
        val themeMode = try { ThemeMode.valueOf(themeModeStr) } catch (e: Exception) { ThemeMode.SYSTEM }
        val privacy = prefs.getBoolean("def_privacyMode", false)
        val fontSizeStr = prefs.getString("def_fontSize", AppFontSize.STANDARD.name) ?: AppFontSize.STANDARD.name
        val fontSize = try { AppFontSize.valueOf(fontSizeStr) } catch (e: Exception) { AppFontSize.STANDARD }
        val customAppColor = prefs.getLong("def_customAppColor", 0xFF005FB1)
        val viewOrderStr = prefs.getString("def_customViewOrder", null)
        val customViewOrder = if (!viewOrderStr.isNullOrBlank()) {
            try {
                val parsed = viewOrderStr.split(",").mapNotNull { name ->
                    try { AppViewMode.valueOf(name.trim()) } catch (e: Exception) { null }
                }
                if (parsed.isNotEmpty()) parsed else DisplaySettings().customViewOrder
            } catch (e: Exception) {
                DisplaySettings().customViewOrder
            }
        } else {
            DisplaySettings().customViewOrder
        }

        val restored = DisplaySettings(
            showPercentOfTotal = showPT,
            showPercentOfGroup = showPG,
            showTotalValue = showTV,
            decimalPlaces = dec,
            compactCurrency = compact,
            currencyUnit = cUnit,
            usePersianDigits = persianDigits,
            themeMode = themeMode,
            privacyMode = privacy,
            fontSize = fontSize,
            customAppColor = customAppColor,
            customViewOrder = customViewOrder
        )
        updateDisplaySettings(restored)
    }

    fun updateDisplaySettings(settings: DisplaySettings) {"""

content = content.replace("    fun updateDisplaySettings(settings: DisplaySettings) {", new_methods)

with open("app/src/main/java/com/example/data/repository/AssetRepository.kt", "w") as f:
    f.write(content)
