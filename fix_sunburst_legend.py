import re

with open("app/src/main/java/com/example/ui/views/SunburstChartView.kt", "r") as f:
    content = f.read()

# Replace the legend
old_legend = r'// Horizontal Color Legend below the chart[\s\S]*?\}'

# The end of the block is the `}` of Surface.
# Wait, my regex might match too much. Let's be precise.
old_legend = """        // Horizontal Color Legend below the chart
        Surface(
            shape = RoundedCornerShape(10.dp),
            color = colors.surface.copy(alpha = 0.5f),
            border = androidx.compose.foundation.BorderStroke(1.dp, colors.border),
            modifier = Modifier.fillMaxWidth().padding(horizontal = 4.dp, vertical = 2.dp)
        ) {
            Row(
                modifier = Modifier.fillMaxWidth().padding(horizontal = 8.dp, vertical = 6.dp).horizontalScroll(rememberScrollState()),
                horizontalArrangement = Arrangement.spacedBy(12.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = "راهنمای رنگ:",
                    fontSize = 10.sp,
                    fontWeight = FontWeight.Bold,
                    color = colors.textPrimary
                )
                val legendItems = AssetColorUtils.MAIN_LEGEND_ITEMS
                legendItems.forEach { item ->
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.spacedBy(4.dp)
                    ) {
                        Box(
                            modifier = Modifier
                                .size(8.dp)
                                .clip(CircleShape)
                                .background(item.color)
                        )
                        Text(
                            text = item.title,
                            fontSize = 9.sp,
                            color = colors.textSecondary
                        )
                    }
                }
            }
        }"""

new_legend = "        com.example.ui.components.SharedAssetLegend(settings)"
content = content.replace(old_legend, new_legend)

with open("app/src/main/java/com/example/ui/views/SunburstChartView.kt", "w") as f:
    f.write(content)
