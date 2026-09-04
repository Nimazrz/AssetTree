import re

with open("app/src/main/java/com/example/ui/theme/Theme.kt", "r") as f:
    content = f.read()

# Replace getAppColorsForPreset with getAppColors
old_func = r"fun getAppColorsForPreset\(preset: AppThemePreset, isDark: Boolean\): AppThemeColors \{(.*?)\}\n\nval DarkAppColors"
new_func = """fun getAppColors(primaryHex: Long, isDark: Boolean): AppThemeColors {
    val primaryColor = Color(primaryHex)
    return if (isDark) {
        val bg = Color(0xFF090A0E)
        val surfColor = Color(0xFF141620)
        AppThemeColors(
            isDark = true,
            background = bg.copy(alpha=0.9f),
            surface = surfColor,
            surfaceVariant = Color(0xFF1B1E2B),
            border = Color(0xFF282D3E),
            textPrimary = Color(0xFFF3F4F8),
            textSecondary = Color(0xFF9EA6BB),
            textMuted = Color(0xFF687085),
            primary = primaryColor,
            primaryContainer = primaryColor.copy(alpha = 0.25f),
            onPrimaryContainer = Color(0xFFCEE3FF),
            gain = Color(0xFF10B981),
            gainContainer = Color(0xFF0E382A),
            onGainContainer = Color(0xFFA7F3D0),
            loss = Color(0xFFF43F5E),
            lossContainer = Color(0xFF45111E),
            onLossContainer = Color(0xFFFECDD3),
            warning = Color(0xFFF59E0B),
            warningContainer = Color(0xFF422806),
            onWarningContainer = Color(0xFFFDE68A),
            inputBackground = Color(0xFF171A25),
            inputBorder = Color(0xFF31364A),
            inputText = Color(0xFFF3F4F8),
            inputPlaceholder = Color(0xFF70778D),
            cardHighlight = Color(0xFF202434)
        )
    } else {
        val bg = Color(0xFFFAFAFA)
        AppThemeColors(
            isDark = false,
            background = bg.copy(alpha=0.9f),
            surface = Color(0xFFF2F4F7),
            surfaceVariant = Color(0xFFE5E7EB),
            border = Color(0xFFDDE2EE),
            textPrimary = Color(0xFF0F172A),
            textSecondary = Color(0xFF475569),
            textMuted = Color(0xFF94A3B8),
            primary = primaryColor,
            primaryContainer = primaryColor.copy(alpha = 0.15f),
            onPrimaryContainer = primaryColor,
            gain = Color(0xFF00875A),
            gainContainer = Color(0xFFD4F6E5),
            onGainContainer = Color(0xFF003822),
            loss = Color(0xFFDC2626),
            lossContainer = Color(0xFFFFE4E6),
            onLossContainer = Color(0xFF5B000C),
            warning = Color(0xFFD97706),
            warningContainer = Color(0xFFFEF3C7),
            onWarningContainer = Color(0xFF451A03),
            inputBackground = Color(0xFFF3F4F6),
            inputBorder = Color(0xFFCBD5E1),
            inputText = Color(0xFF0F172A),
            inputPlaceholder = Color(0xFF94A3B8),
            cardHighlight = Color(0xFFF1F5F9)
        )
    }
}

val DarkAppColors = getAppColors(0xFF005FB1, true)
val LightAppColors = getAppColors(0xFF005FB1, false)"""
content = re.sub(old_func, new_func, content, flags=re.DOTALL)

old_theme_func = r"fun MyApplicationTheme\(\s*darkTheme: Boolean = isSystemInDarkTheme\(\),\s*dynamicColor: Boolean = false,\s*preset: AppThemePreset = AppThemePreset.NAVY_CLASSIC,\s*fontScale: Float = 1.0f,\s*content: @Composable \(\) -> Unit,\n\) \{"
new_theme_func = """fun MyApplicationTheme(
  darkTheme: Boolean = isSystemInDarkTheme(),
  dynamicColor: Boolean = false,
  primaryColorHex: Long = 0xFF005FB1,
  fontScale: Float = 1.0f,
  content: @Composable () -> Unit,
) {"""
content = re.sub(old_theme_func, new_theme_func, content)

content = content.replace("val appColors = remember(preset, darkTheme) { getAppColorsForPreset(preset, darkTheme) }", "val appColors = remember(primaryColorHex, darkTheme) { getAppColors(primaryColorHex, darkTheme) }")
content = content.replace("val colorScheme = remember(preset, darkTheme, dynamicColor) {", "val colorScheme = remember(primaryColorHex, darkTheme, dynamicColor) {")

with open("app/src/main/java/com/example/ui/theme/Theme.kt", "w") as f:
    f.write(content)
