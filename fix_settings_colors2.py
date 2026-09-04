import re

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

# Asset Colors replace
old_asset_colors = r'val assetColorCategories = listOf\([\s\S]*?Triple\([\s\S]*?\}\s*\}\s*\}'

new_asset_colors = """val assetColorCategories = listOf(
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
content = re.sub(old_asset_colors, new_asset_colors, content)

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)
