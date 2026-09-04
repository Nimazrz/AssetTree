import re

with open("app/src/main/java/com/example/ui/views/PieChartView.kt", "r") as f:
    content = f.read()

old_logic = r"""                        val fontSize = \(percent \* 80f\)\.coerceIn\(6f, 36f\)\.sp
                        val percentFontSize = \(percent \* 100f\)\.coerceIn\(8f, 42f\)\.sp"""

new_logic = """                        val fontSize = (percent * 60f).coerceIn(4f, 32f).sp
                        val percentFontSize = (percent * 70f).coerceIn(4.5f, 38f).sp"""

content = re.sub(old_logic, new_logic, content)

with open("app/src/main/java/com/example/ui/views/PieChartView.kt", "w") as f:
    f.write(content)
