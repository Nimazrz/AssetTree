import re

with open("app/src/main/java/com/example/ui/components/SharedViewHeader.kt", "r") as f:
    content = f.read()

# I will replace the messy SharedAssetLegend with a clean one
old_legend = r'@Composable\nfun SharedAssetLegend\([\s\S]*?\}\n\}\n'
new_legend = """@Composable
fun SharedAssetLegend(settings: com.example.data.model.DisplaySettings) {
    val colors = AppTheme.colors
    val assetColorCategories = listOf(
        Pair("مس و کاتد مس", Color(0xFFD32F2F)),
        Pair("نقره و شمش نقره", Color(0xFF90A4AE)),
        Pair("نقدینگی، ریال، دلار، سپرده و صندوق ثابت", Color(0xFF00897B)),
        Pair("املاک، مستغلات و ساختمان", Color(0xFF8D6E63)),
        Pair("خودرو و وسایل نقلیه", Color(0xFF8E24AA)),
        Pair("سهام و بورس", Color(0xFF1565C0)),
        Pair("سایر دارایی‌ها", Color(0xFFE65100))
    )

    Surface(
        shape = RoundedCornerShape(10.dp),
        color = colors.surface.copy(alpha = 0.5f),
        border = androidx.compose.foundation.BorderStroke(1.dp, colors.border),
        modifier = Modifier.fillMaxWidth().padding(horizontal = 4.dp, vertical = 2.dp)
    ) {
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = 8.dp, vertical = 6.dp)
                .horizontalScroll(rememberScrollState()),
            horizontalArrangement = Arrangement.spacedBy(12.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            Text(
                text = "راهنمای رنگ:",
                fontSize = 10.sp,
                fontWeight = FontWeight.Bold,
                color = colors.textPrimary
            )
            assetColorCategories.forEach { (title, defaultColor) ->
                val currentHex = settings.customAssetColors[title]
                val activeColor = if (currentHex != null) Color(currentHex) else defaultColor
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(4.dp)
                ) {
                    Box(
                        modifier = Modifier
                            .size(8.dp)
                            .clip(androidx.compose.foundation.shape.CircleShape)
                            .background(activeColor)
                    )
                    Text(
                        text = title,
                        fontSize = 9.sp,
                        color = colors.textSecondary
                    )
                }
            }
        }
    }
}
"""
content = re.sub(old_legend, new_legend, content)

with open("app/src/main/java/com/example/ui/components/SharedViewHeader.kt", "w") as f:
    f.write(content)
