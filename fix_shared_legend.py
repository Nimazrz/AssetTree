with open("app/src/main/java/com/example/ui/components/SharedViewHeader.kt", "a") as f:
    f.write("""

@Composable
fun SharedAssetLegend(settings: com.example.data.model.DisplaySettings) {
    val colors = com.example.ui.theme.AppTheme.colors
    val assetColorCategories = listOf(
        Pair("مس و کاتد مس", androidx.compose.ui.graphics.Color(0xFFD32F2F)),
        Pair("نقره و شمش نقره", androidx.compose.ui.graphics.Color(0xFF90A4AE)),
        Pair("نقدینگی، ریال، دلار، سپرده و صندوق ثابت", androidx.compose.ui.graphics.Color(0xFF00897B)),
        Pair("املاک، مستغلات و ساختمان", androidx.compose.ui.graphics.Color(0xFF8D6E63)),
        Pair("خودرو و وسایل نقلیه", androidx.compose.ui.graphics.Color(0xFF8E24AA)),
        Pair("سهام و بورس", androidx.compose.ui.graphics.Color(0xFF1565C0)),
        Pair("سایر دارایی‌ها", androidx.compose.ui.graphics.Color(0xFFE65100))
    )

    androidx.compose.material3.Surface(
        shape = androidx.compose.foundation.shape.RoundedCornerShape(10.dp),
        color = colors.surface.copy(alpha = 0.5f),
        border = androidx.compose.foundation.BorderStroke(1.dp, colors.border),
        modifier = androidx.compose.ui.Modifier.fillMaxWidth().padding(horizontal = 4.dp, vertical = 2.dp)
    ) {
        androidx.compose.foundation.layout.Row(
            modifier = androidx.compose.ui.Modifier
                .fillMaxWidth()
                .padding(horizontal = 8.dp, vertical = 6.dp)
                .androidx.compose.foundation.horizontalScroll(androidx.compose.foundation.rememberScrollState()),
            horizontalArrangement = androidx.compose.foundation.layout.Arrangement.spacedBy(12.dp),
            verticalAlignment = androidx.compose.ui.Alignment.CenterVertically
        ) {
            androidx.compose.material3.Text(
                text = "راهنمای رنگ:",
                fontSize = 10.sp,
                fontWeight = androidx.compose.ui.text.font.FontWeight.Bold,
                color = colors.textPrimary
            )
            assetColorCategories.forEach { (title, defaultColor) ->
                val currentHex = settings.customAssetColors[title]
                val activeColor = if (currentHex != null) androidx.compose.ui.graphics.Color(currentHex) else defaultColor
                androidx.compose.foundation.layout.Row(
                    verticalAlignment = androidx.compose.ui.Alignment.CenterVertically,
                    horizontalArrangement = androidx.compose.foundation.layout.Arrangement.spacedBy(4.dp)
                ) {
                    androidx.compose.foundation.layout.Box(
                        modifier = androidx.compose.ui.Modifier
                            .size(8.dp)
                            .clip(androidx.compose.foundation.shape.CircleShape)
                            .background(activeColor)
                    )
                    androidx.compose.material3.Text(
                        text = title,
                        fontSize = 9.sp,
                        color = colors.textSecondary
                    )
                }
            }
        }
    }
}
""")
