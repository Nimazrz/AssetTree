import re

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

chart_order_content = """                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.SpaceBetween,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Row(
                                    verticalAlignment = Alignment.CenterVertically,
                                    horizontalArrangement = Arrangement.spacedBy(6.dp)
                                ) {
                                    Icon(
                                        imageVector = Icons.Default.Reorder,
                                        contentDescription = null,
                                        tint = colors.primary,
                                        modifier = Modifier.size(18.dp)
                                    )
                                    Text(
                                        text = "ترتیب نمودارها",
                                        fontSize = 12.5.sp,
                                        fontWeight = FontWeight.Bold,
                                        color = colors.textPrimary
                                    )
                                }
                            }
                            
                            val currentOrder = settings.customViewOrder.ifEmpty { AppViewMode.values().toList() }
                            Column(verticalArrangement = Arrangement.spacedBy(4.dp)) {
                                currentOrder.forEachIndexed { index, mode ->
                                    Row(
                                        modifier = Modifier.fillMaxWidth().background(colors.surface, RoundedCornerShape(8.dp)).border(1.dp, colors.border, RoundedCornerShape(8.dp)).padding(horizontal = 8.dp, vertical = 6.dp),
                                        horizontalArrangement = Arrangement.SpaceBetween,
                                        verticalAlignment = Alignment.CenterVertically
                                    ) {
                                        Text(mode.titleFa, fontSize = 12.sp, color = colors.textPrimary)
                                        Row(horizontalArrangement = Arrangement.spacedBy(4.dp)) {
                                            IconButton(
                                                onClick = {
                                                    if (index > 0) {
                                                        val mutable = currentOrder.toMutableList()
                                                        val temp = mutable[index]
                                                        mutable[index] = mutable[index - 1]
                                                        mutable[index - 1] = temp
                                                        onUpdateSettings(settings.copy(customViewOrder = mutable))
                                                    }
                                                },
                                                modifier = Modifier.size(28.dp)
                                            ) {
                                                Icon(Icons.Default.ArrowUpward, contentDescription = "بالا", tint = if (index > 0) colors.primary else colors.textSecondary)
                                            }
                                            IconButton(
                                                onClick = {
                                                    if (index < currentOrder.size - 1) {
                                                        val mutable = currentOrder.toMutableList()
                                                        val temp = mutable[index]
                                                        mutable[index] = mutable[index + 1]
                                                        mutable[index + 1] = temp
                                                        onUpdateSettings(settings.copy(customViewOrder = mutable))
                                                    }
                                                },
                                                modifier = Modifier.size(28.dp)
                                            ) {
                                                Icon(Icons.Default.ArrowDownward, contentDescription = "پایین", tint = if (index < currentOrder.size - 1) colors.primary else colors.textSecondary)
                                            }
                                        }
                                    }
                                }
                            }"""

# Find the Row block exactly as it is in the file and replace it with the new content
old_row = r"""                            Row\(
                                modifier = Modifier\.fillMaxWidth\(\),
                                horizontalArrangement = Arrangement\.SpaceBetween,
                                verticalAlignment = Alignment\.CenterVertically
                            \) \{
                                Row\(
                                    verticalAlignment = Alignment\.CenterVertically,
                                    horizontalArrangement = Arrangement\.spacedBy\(6\.dp\)
                                \) \{
                                    Icon\(
                                        imageVector = Icons\.Default\.Reorder,
                                        contentDescription = null,
                                        tint = colors\.primary,
                                        modifier = Modifier\.size\(18\.dp\)
                                    \)
                                    Text\(
                                        text = "ترتیب نمودارها",
                                        fontSize = 12\.5\.sp,
                                        fontWeight = FontWeight\.Bold,
                                        color = colors\.textPrimary
                                    \)
                                \}
                            \}"""

content = re.sub(old_row, chart_order_content, content, count=1)

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)

