import re

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

# Add a state for color picker at the top of SettingsDialog
if "var selectedAssetForColor" not in content:
    content = content.replace("var showResetConfirm by remember { mutableStateOf(false) }", 
                              "var showResetConfirm by remember { mutableStateOf(false) }\n    var selectedAssetForColor by remember { mutableStateOf<String?>(null) }")

# Theme Preset replace
old_theme_preset = """                            Column(verticalArrangement = Arrangement.spacedBy(6.dp)) {
                                AppThemePreset.values().toList().chunked(2).forEach { pair ->
                                    Row(
                                        modifier = Modifier.fillMaxWidth(),
                                        horizontalArrangement = Arrangement.spacedBy(8.dp)
                                    ) {
                                        pair.forEach { preset ->
                                            val isSel = settings.themePreset == preset
                                            Surface(
                                                shape = RoundedCornerShape(10.dp),
                                                color = if (isSel) Color(preset.primaryHex).copy(alpha = 0.15f) else colors.surface,
                                                border = androidx.compose.foundation.BorderStroke(
                                                    if (isSel) 2.dp else 1.dp,
                                                    if (isSel) Color(preset.primaryHex) else colors.border
                                                ),
                                                modifier = Modifier
                                                    .weight(1f)
                                                    .clickable { onUpdateSettings(settings.copy(themePreset = preset)) }
                                            ) {
                                                Row(
                                                    modifier = Modifier.padding(horizontal = 8.dp, vertical = 8.dp),
                                                    verticalAlignment = Alignment.CenterVertically,
                                                    horizontalArrangement = Arrangement.spacedBy(8.dp)
                                                ) {
                                                    Box(
                                                        modifier = Modifier
                                                            .size(18.dp)
                                                            .clip(RoundedCornerShape(4.dp))
                                                            .background(Color(preset.primaryHex))
                                                    )
                                                    Text(
                                                        text = preset.labelFa,
                                                        fontSize = 11.sp,
                                                        fontWeight = if (isSel) FontWeight.Bold else FontWeight.Normal,
                                                        color = if (isSel) Color(preset.primaryHex) else colors.textPrimary
                                                    )
                                                }
                                            }
                                        }
                                        if (pair.size == 1) {
                                            Spacer(modifier = Modifier.weight(1f))
                                        }
                                    }
                                }
                            }"""

new_theme_preset = """                            Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                                AppThemePreset.values().toList().chunked(6).forEach { rowPresets ->
                                    Row(
                                        modifier = Modifier.fillMaxWidth(),
                                        horizontalArrangement = Arrangement.SpaceBetween
                                    ) {
                                        rowPresets.forEach { preset ->
                                            val isSel = settings.themePreset == preset
                                            Box(
                                                modifier = Modifier
                                                    .size(36.dp)
                                                    .clip(RoundedCornerShape(8.dp))
                                                    .background(Color(preset.primaryHex))
                                                    .border(if (isSel) 3.dp else 1.dp, if (isSel) colors.textPrimary else colors.border, RoundedCornerShape(8.dp))
                                                    .clickable { onUpdateSettings(settings.copy(themePreset = preset)) },
                                                contentAlignment = Alignment.Center
                                            ) {
                                                if (isSel) {
                                                    Icon(Icons.Default.Check, contentDescription = null, tint = Color.White, modifier = Modifier.size(20.dp))
                                                }
                                            }
                                        }
                                        // Fill empty spaces
                                        repeat(6 - rowPresets.size) {
                                            Spacer(modifier = Modifier.size(36.dp))
                                        }
                                    }
                                }
                            }"""
content = content.replace(old_theme_preset, new_theme_preset)

# Asset Colors replace
old_asset_colors = """                            val assetColorCategories = listOf(
                                Triple("مس و کاتد مس", "انواع قرمز اکسیدی و شاداب", Color(0xFFD32F2F)),
                                Triple("نقره و شمش نقره", "رنگ نقره‌ای و طوسی متالیک", Color(0xFF90A4AE)),
                                Triple("نقدینگی، ریال، دلار، سپرده و صندوق ثابت", "انواع سبز زمردی و نعنایی", Color(0xFF00897B)),
                                Triple("املاک، مستغلات و ساختمان", "انواع قهوه‌ای و خاکی", Color(0xFF8D6E63)),
                                Triple("خودرو و وسایل نقلیه", "رنگ بنفش", Color(0xFF8E24AA)),
                                Triple("سهام و بورس", "رنگ آبی سلطنتی", Color(0xFF1565C0)),
                                Triple("سایر دارایی‌ها", "رنگ‌های مکمل و متمایز", Color(0xFFE65100))
                            )

                            Column(verticalArrangement = Arrangement.spacedBy(6.dp)) {
                                assetColorCategories.forEach { (title, desc, badgeColor) ->
                                    Surface(
                                        shape = RoundedCornerShape(8.dp),
                                        color = colors.surface,
                                        border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f)),
                                        modifier = Modifier.fillMaxWidth()
                                    ) {
                                        Row(
                                            modifier = Modifier.padding(horizontal = 10.dp, vertical = 6.dp),
                                            verticalAlignment = Alignment.CenterVertically,
                                            horizontalArrangement = Arrangement.SpaceBetween
                                        ) {
                                            Row(
                                                verticalAlignment = Alignment.CenterVertically,
                                                horizontalArrangement = Arrangement.spacedBy(8.dp)
                                            ) {
                                                Box(
                                                    modifier = Modifier
                                                        .size(16.dp)
                                                        .clip(RoundedCornerShape(4.dp))
                                                        .background(badgeColor)
                                                )
                                                Column {
                                                    Text(
                                                        text = title,
                                                        fontSize = 11.5.sp,
                                                        fontWeight = FontWeight.Bold,
                                                        color = colors.textPrimary
                                                    )
                                                    Text(
                                                        text = desc,
                                                        fontSize = 10.sp,
                                                        color = colors.textSecondary
                                                    )
                                                }
                                            }
                                        }
                                    }
                                }
                            }"""

new_asset_colors = """                            val assetColorCategories = listOf(
                                Pair("مس و کاتد مس", Color(0xFFD32F2F)),
                                Pair("نقره و شمش نقره", Color(0xFF90A4AE)),
                                Pair("نقدینگی، ریال، دلار، سپرده و صندوق ثابت", Color(0xFF00897B)),
                                Pair("املاک، مستغلات و ساختمان", Color(0xFF8D6E63)),
                                Pair("خودرو و وسایل نقلیه", Color(0xFF8E24AA)),
                                Pair("سهام و بورس", Color(0xFF1565C0)),
                                Pair("سایر دارایی‌ها", Color(0xFFE65100))
                            )

                            Column(verticalArrangement = Arrangement.spacedBy(6.dp)) {
                                assetColorCategories.forEach { (title, defaultColor) ->
                                    val currentHex = settings.customAssetColors[title]
                                    val activeColor = if (currentHex != null) Color(currentHex) else defaultColor
                                    Surface(
                                        shape = RoundedCornerShape(8.dp),
                                        color = colors.surface,
                                        border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f)),
                                        modifier = Modifier.fillMaxWidth().clickable { selectedAssetForColor = title }
                                    ) {
                                        Row(
                                            modifier = Modifier.padding(horizontal = 10.dp, vertical = 10.dp),
                                            verticalAlignment = Alignment.CenterVertically,
                                            horizontalArrangement = Arrangement.SpaceBetween
                                        ) {
                                            Text(
                                                text = title,
                                                fontSize = 11.5.sp,
                                                fontWeight = FontWeight.Bold,
                                                color = colors.textPrimary
                                            )
                                            Box(
                                                modifier = Modifier
                                                    .size(24.dp)
                                                    .clip(RoundedCornerShape(4.dp))
                                                    .background(activeColor)
                                                    .border(1.dp, colors.border, RoundedCornerShape(4.dp))
                                            )
                                        }
                                    }
                                }
                            }"""
content = content.replace(old_asset_colors, new_asset_colors)

# Add the dialog at the bottom
color_dialog = """
    if (selectedAssetForColor != null) {
        val colorPalette = listOf(
            0xFFD32F2F, 0xFFC2185B, 0xFF7B1FA2, 0xFF512DA8, 0xFF303F9F, 0xFF1976D2, 0xFF0288D1,
            0xFF0097A7, 0xFF00796B, 0xFF388E3C, 0xFF689F38, 0xFFAFB42B, 0xFFFBC02D, 0xFFFFA000,
            0xFFF57C00, 0xFFE64A19, 0xFF5D4037, 0xFF616161, 0xFF455A64, 0xFF90A4AE, 0xFF9E9E9E,
            0xFFBDBDBD, 0xFFE0E0E0, 0xFFFFFFFF
        )
        AlertDialog(
            onDismissRequest = { selectedAssetForColor = null },
            title = { Text("انتخاب رنگ برای $selectedAssetForColor", fontSize = 14.sp, fontWeight = FontWeight.Bold, color = colors.textPrimary) },
            text = {
                Column(verticalArrangement = Arrangement.spacedBy(12.dp)) {
                    colorPalette.chunked(6).forEach { rowColors ->
                        Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
                            rowColors.forEach { hex ->
                                Box(
                                    modifier = Modifier
                                        .size(36.dp)
                                        .clip(RoundedCornerShape(8.dp))
                                        .background(Color(hex))
                                        .border(1.dp, Color.Gray, RoundedCornerShape(8.dp))
                                        .clickable {
                                            val newColors = settings.customAssetColors.toMutableMap()
                                            newColors[selectedAssetForColor!!] = hex
                                            onUpdateSettings(settings.copy(customAssetColors = newColors))
                                            selectedAssetForColor = null
                                        }
                                )
                            }
                            repeat(6 - rowColors.size) { Spacer(modifier = Modifier.size(36.dp)) }
                        }
                    }
                }
            },
            confirmButton = {
                TextButton(onClick = { selectedAssetForColor = null }) {
                    Text("بستن")
                }
            },
            containerColor = colors.surface
        )
    }
"""

content = content.replace("    if (showResetConfirm) {", color_dialog + "\n    if (showResetConfirm) {")

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)
