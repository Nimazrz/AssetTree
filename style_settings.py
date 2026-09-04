with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "r") as f:
    content = f.read()

# Replace Card(shape = RoundedCornerShape(14.dp), colors = CardDefaults.cardColors(containerColor = colors.background) with softer styles.
content = content.replace("containerColor = colors.background", "containerColor = colors.surfaceVariant.copy(alpha = 0.5f)")
content = content.replace("RoundedCornerShape(14.dp)", "RoundedCornerShape(20.dp)")
content = content.replace("border = androidx.compose.foundation.BorderStroke(1.dp, colors.border)", "border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f))")

with open("app/src/main/java/com/example/ui/dialogs/SettingsDialog.kt", "w") as f:
    f.write(content)
print("Styled")
