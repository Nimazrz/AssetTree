import re

with open("app/src/main/java/com/example/ui/views/PieChartView.kt", "r") as f:
    content = f.read()

# Add imports
imports = """import androidx.compose.ui.text.drawText
import androidx.compose.ui.text.rememberTextMeasurer
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.style.TextAlign
import kotlin.math.PI"""

content = content.replace("import kotlin.math.sin", imports + "\nimport kotlin.math.sin")

# Inside PieChartView, add textMeasurer
content = content.replace("    val colors = AppTheme.colors", "    val colors = AppTheme.colors\n    val textMeasurer = rememberTextMeasurer()")

# Add drawText in Canvas
draw_arc_code = """                    drawArc(
                        color = slice.color,
                        startAngle = slice.startAngle,
                        sweepAngle = slice.sweepAngle,
                        useCenter = true,
                        topLeft = Offset(center.x - radius, center.y - radius),
                        size = Size(radius * 2, radius * 2)
                    )"""

draw_arc_with_text = """                    drawArc(
                        color = slice.color,
                        startAngle = slice.startAngle,
                        sweepAngle = slice.sweepAngle,
                        useCenter = true,
                        topLeft = Offset(center.x - radius, center.y - radius),
                        size = Size(radius * 2, radius * 2)
                    )
                    
                    if (slice.sweepAngle > 5f) {
                        val angleInRadians = (slice.startAngle + slice.sweepAngle / 2) * (PI / 180f)
                        val textRadius = radius * 0.65f
                        val textX = center.x + textRadius * cos(angleInRadians).toFloat()
                        val textY = center.y + textRadius * sin(angleInRadians).toFloat()
                        
                        val percent = slice.sweepAngle / 360f
                        // Scale font based on slice percentage
                        val fontSize = (percent * 80f).coerceIn(6f, 36f).sp
                        val percentFontSize = (percent * 100f).coerceIn(8f, 42f).sp
                        
                        val nameText = slice.node.name
                        val percentText = NumberFormatUtils.formatPercentage(slice.node.percentOfTotal, 1, settings.usePersianDigits)
                        
                        val nameLayout = textMeasurer.measure(
                            text = nameText,
                            style = TextStyle(fontSize = fontSize, fontWeight = FontWeight.Bold, color = Color.White, textAlign = TextAlign.Center)
                        )
                        val percentLayout = textMeasurer.measure(
                            text = percentText,
                            style = TextStyle(fontSize = percentFontSize, fontWeight = FontWeight.Bold, color = Color.White, textAlign = TextAlign.Center)
                        )
                        
                        drawText(
                            textLayoutResult = nameLayout,
                            topLeft = Offset(textX - nameLayout.size.width / 2f, textY - nameLayout.size.height)
                        )
                        drawText(
                            textLayoutResult = percentLayout,
                            topLeft = Offset(textX - percentLayout.size.width / 2f, textY + 2f)
                        )
                    }"""

content = content.replace(draw_arc_code, draw_arc_with_text)

with open("app/src/main/java/com/example/ui/views/PieChartView.kt", "w") as f:
    f.write(content)
