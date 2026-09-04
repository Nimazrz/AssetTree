package com.example.ui.theme

import android.os.Build
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Typography
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.dynamicDarkColorScheme
import androidx.compose.material3.dynamicLightColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.runtime.remember
import androidx.compose.runtime.staticCompositionLocalOf
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext

import com.example.data.model.AppThemePreset
import androidx.compose.material3.Shapes
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.ui.unit.dp

data class AppThemeColors(
    val isDark: Boolean,
    val background: Color,
    val surface: Color,
    val surfaceVariant: Color,
    val border: Color,
    val textPrimary: Color,
    val textSecondary: Color,
    val textMuted: Color,
    val primary: Color,
    val primaryContainer: Color,
    val onPrimaryContainer: Color,
    val gain: Color,
    val gainContainer: Color,
    val onGainContainer: Color,
    val loss: Color,
    val lossContainer: Color,
    val onLossContainer: Color,
    val warning: Color,
    val warningContainer: Color,
    val onWarningContainer: Color,
    val inputBackground: Color,
    val inputBorder: Color,
    val inputText: Color,
    val inputPlaceholder: Color,
    val cardHighlight: Color
)

fun getAppColorsForPreset(preset: AppThemePreset, isDark: Boolean): AppThemeColors {
    val primaryColor = Color(preset.primaryHex)
    return if (isDark) {
        val bg = Color(preset.darkBgHex)
        val surf = Color(preset.darkBgHex).copy(alpha = 1f)
        val surfColor = Color(0xFF141620)
        AppThemeColors(
            isDark = true,
            background = bg,
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
        val bg = Color(preset.lightBgHex)
        AppThemeColors(
            isDark = false,
            background = bg,
            surface = Color(0xFFFFFFFF),
            surfaceVariant = Color(0xFFEEF1F8),
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
            inputBackground = Color(0xFFF8FAFC),
            inputBorder = Color(0xFFCBD5E1),
            inputText = Color(0xFF0F172A),
            inputPlaceholder = Color(0xFF94A3B8),
            cardHighlight = Color(0xFFF1F5F9)
        )
    }
}

val DarkAppColors = getAppColorsForPreset(AppThemePreset.NAVY_CLASSIC, true)
val LightAppColors = getAppColorsForPreset(AppThemePreset.NAVY_CLASSIC, false)

val LocalAppThemeColors = staticCompositionLocalOf { LightAppColors }

object AppTheme {
    val colors: AppThemeColors
        @Composable
        get() = LocalAppThemeColors.current
    
    @Composable
    fun getDepthColor(depth: Int, isSelected: Boolean): Color {
        if (isSelected) return colors.primary
        
        val isDark = colors.isDark
        return when (depth) {
            0 -> colors.textPrimary // Root (White in dark mode, Black in light mode)
            1 -> if (isDark) Color(0xFF4ADE80) else Color(0xFF16A34A) // Level 1 (Green)
            2 -> if (isDark) Color(0xFFFBBF24) else Color(0xFFD97706) // Level 2 (Yellow/Orange)
            3 -> if (isDark) Color(0xFF60A5FA) else Color(0xFF2563EB) // Level 3 (Blue)
            4 -> if (isDark) Color(0xFFF472B6) else Color(0xFFDB2777) // Level 4 (Pink)
            5 -> if (isDark) Color(0xFFC084FC) else Color(0xFF9333EA) // Level 5 (Purple)
            else -> if (isDark) Color(0xFF9CA3AF) else Color(0xFF4B5563) // Level 6+ (Gray)
        }
    }

    val typography: Typography
        @Composable
        get() = MaterialTheme.typography
}

val ModernShapes = Shapes(
    extraSmall = RoundedCornerShape(12.dp),
    small = RoundedCornerShape(16.dp),
    medium = RoundedCornerShape(20.dp),
    large = RoundedCornerShape(24.dp),
    extraLarge = RoundedCornerShape(32.dp)
)

// Super AMOLED Pitch-Black Dark Theme (Custom-optimized for Galaxy A52s 120Hz OLED screen)
private val DarkColorScheme =
  darkColorScheme(
    primary = DarkAppColors.primary,
    onPrimary = Color.White,
    primaryContainer = DarkAppColors.primaryContainer,
    onPrimaryContainer = DarkAppColors.onPrimaryContainer,
    secondary = HighDensitySecondary,
    onSecondary = Color.White,
    secondaryContainer = HighDensitySecondaryContainer,
    onSecondaryContainer = HighDensityOnSecondaryContainer,
    tertiary = DarkAppColors.gain,
    background = DarkAppColors.background,
    surface = DarkAppColors.surface,
    surfaceVariant = DarkAppColors.surfaceVariant,
    outline = DarkAppColors.border,
    onBackground = DarkAppColors.textPrimary,
    onSurface = DarkAppColors.textPrimary
  )

private val LightColorScheme =
  lightColorScheme(
    primary = LightAppColors.primary,
    onPrimary = Color.White,
    primaryContainer = LightAppColors.primaryContainer,
    onPrimaryContainer = LightAppColors.onPrimaryContainer,
    secondary = HighDensitySecondary,
    onSecondary = Color.White,
    secondaryContainer = HighDensitySecondaryContainer,
    onSecondaryContainer = HighDensityOnSecondaryContainer,
    tertiary = LightAppColors.gain,
    background = LightAppColors.background,
    surface = LightAppColors.surface,
    surfaceVariant = LightAppColors.surfaceVariant,
    outline = LightAppColors.border,
    onBackground = LightAppColors.textPrimary,
    onSurface = LightAppColors.textPrimary,
  )

@Composable
fun MyApplicationTheme(
  darkTheme: Boolean = isSystemInDarkTheme(),
  dynamicColor: Boolean = false,
  preset: AppThemePreset = AppThemePreset.NAVY_CLASSIC,
  fontScale: Float = 1.0f,
  content: @Composable () -> Unit,
) {
  val context = LocalContext.current
  val appColors = remember(preset, darkTheme) { getAppColorsForPreset(preset, darkTheme) }

  val colorScheme = remember(preset, darkTheme, dynamicColor) {
    if (dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
      if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
    } else if (darkTheme) {
      darkColorScheme(
        primary = appColors.primary,
        onPrimary = Color.White,
        primaryContainer = appColors.primaryContainer,
        onPrimaryContainer = appColors.onPrimaryContainer,
        secondary = HighDensitySecondary,
        onSecondary = Color.White,
        secondaryContainer = HighDensitySecondaryContainer,
        onSecondaryContainer = HighDensityOnSecondaryContainer,
        tertiary = appColors.gain,
        background = appColors.background,
        surface = appColors.surface,
        surfaceVariant = appColors.surfaceVariant,
        outline = appColors.border,
        onBackground = appColors.textPrimary,
        onSurface = appColors.textPrimary
      )
    } else {
      lightColorScheme(
        primary = appColors.primary,
        onPrimary = Color.White,
        primaryContainer = appColors.primaryContainer,
        onPrimaryContainer = appColors.onPrimaryContainer,
        secondary = HighDensitySecondary,
        onSecondary = Color.White,
        secondaryContainer = HighDensitySecondaryContainer,
        onSecondaryContainer = HighDensityOnSecondaryContainer,
        tertiary = appColors.gain,
        background = appColors.background,
        surface = appColors.surface,
        surfaceVariant = appColors.surfaceVariant,
        outline = appColors.border,
        onBackground = appColors.textPrimary,
        onSurface = appColors.textPrimary
      )
    }
  }

  val currentDensity = androidx.compose.ui.platform.LocalDensity.current
  val customDensity = remember(currentDensity, fontScale) {
      androidx.compose.ui.unit.Density(currentDensity.density * fontScale, currentDensity.fontScale * fontScale)
  }

  CompositionLocalProvider(
      LocalAppThemeColors provides appColors,
      androidx.compose.ui.platform.LocalDensity provides customDensity
  ) {
    MaterialTheme(colorScheme = colorScheme, typography = Typography, shapes = ModernShapes, content = content)
  }
}

