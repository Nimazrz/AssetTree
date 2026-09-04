package com.example.ui.dialogs

import android.content.ClipData
import android.content.ClipboardManager
import android.content.Context
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.material3.TabRow
import androidx.compose.material3.Tab
import androidx.compose.material3.TabRowDefaults
import androidx.compose.material3.TabRowDefaults.tabIndicatorOffset
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Dialog
import androidx.compose.ui.window.DialogProperties
import com.example.data.model.AppThemePreset
import com.example.data.model.CalculatedNode
import com.example.data.model.CurrencyUnit
import com.example.data.model.DisplaySettings
import com.example.data.model.ThemeMode
import com.example.ui.theme.*
import com.example.utils.PdfChartType
import com.example.utils.PdfReportGenerator
import kotlinx.coroutines.launch

@Composable
fun SettingsDialog(
    settings: DisplaySettings,
    rootCalculated: CalculatedNode? = null,
    onDismiss: () -> Unit,
    onUpdateSettings: (DisplaySettings) -> Unit,
    onExportBackupJson: suspend () -> String,
    onImportBackupJson: (String) -> Unit,
    onResetAllData: () -> Unit,
    onWipeFinancialData: () -> Unit = {}
) {
    val context = LocalContext.current
    val coroutineScope = rememberCoroutineScope()
    val colors = AppTheme.colors

    var selectedPdfChartType by remember { mutableStateOf(PdfChartType.TREEMAP) }
    var showJsonBackupModal by remember { mutableStateOf(false) }
    var backupJsonContent by remember { mutableStateOf("") }
    var restoreJsonInput by remember { mutableStateOf("") }
    var showResetConfirm by remember { mutableStateOf(false) }
    var showWipeConfirm by remember { mutableStateOf(false) }

    Dialog(
        onDismissRequest = onDismiss,
        properties = DialogProperties(usePlatformDefaultWidth = false)
    ) {
        Card(
            shape = RoundedCornerShape(20.dp),
            colors = CardDefaults.cardColors(containerColor = colors.surface),
            border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f)),
            modifier = Modifier
                .fillMaxWidth(0.95f)
                .widthIn(max = 680.dp)
                .fillMaxHeight(0.88f)
                .padding(8.dp)
        ) {
            Column(modifier = Modifier.fillMaxSize()) {
                // Header
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .background(colors.surfaceVariant)
                        .padding(horizontal = 16.dp, vertical = 12.dp),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.spacedBy(8.dp)
                    ) {
                        Icon(Icons.Default.Tune, contentDescription = null, tint = colors.primary)
                        Text(
                            text = "تنظیمات تم، نمایش و داده‌ها",
                            fontSize = 14.sp,
                            fontWeight = FontWeight.Black,
                            color = colors.textPrimary
                        )
                    }
                    IconButton(onClick = onDismiss) {
                        Icon(Icons.Default.Close, contentDescription = "بستن", tint = colors.textSecondary)
                    }
                }


                var selectedTabIndex by remember { mutableStateOf(0) }
                val tabs = listOf("پوسته و ظاهر", "تنظیمات نمایش", "داده و بک‌آپ")

                TabRow(
                    selectedTabIndex = selectedTabIndex,
                    containerColor = colors.surfaceVariant,
                    contentColor = colors.primary,
                    indicator = { tabPositions ->
                        TabRowDefaults.Indicator(
                            Modifier.tabIndicatorOffset(tabPositions[selectedTabIndex]),
                            color = colors.primary
                        )
                    }
                ) {
                    tabs.forEachIndexed { index, title ->
                        Tab(
                            selected = selectedTabIndex == index,
                            onClick = { selectedTabIndex = index },
                            text = { Text(title, fontSize = 13.sp, fontWeight = if (selectedTabIndex == index) FontWeight.Bold else FontWeight.Normal) },
                            selectedContentColor = colors.primary,
                            unselectedContentColor = colors.textSecondary
                        )
                    }
                }

                // Body
                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .weight(1f)
                        .padding(16.dp)
                        .verticalScroll(rememberScrollState()),
                    verticalArrangement = Arrangement.spacedBy(14.dp)
                ) {
                    if (selectedTabIndex == 0) {
                    // 1. Theme & Color Palette Card (وظیفه ۴ و ۵: تجمیع حالت روز/شب با پالت و تم برنامه)
                    Card(
                        shape = RoundedCornerShape(20.dp),
                        colors = CardDefaults.cardColors(containerColor = colors.surfaceVariant.copy(alpha = 0.5f)),
                        border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f))
                    ) {
                        Column(modifier = Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                            Row(
                                verticalAlignment = Alignment.CenterVertically,
                                horizontalArrangement = Arrangement.spacedBy(6.dp)
                            ) {
                                Icon(
                                    imageVector = Icons.Default.Palette,
                                    contentDescription = null,
                                    tint = colors.primary,
                                    modifier = Modifier.size(18.dp)
                                )
                                Text(
                                    text = "پالت رنگ و تم اپلیکیشن",
                                    fontSize = 13.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = colors.textPrimary
                                )
                            }

                            Text(
                                text = "حالت تیره/روشن و پالت رنگی سازمانی برنامه را از این بخش انتخاب کنید.",
                                fontSize = 11.sp,
                                color = colors.textSecondary
                            )

                            // سطر حالت روز و شب (وظیفه ۵)
                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.spacedBy(8.dp)
                            ) {
                                // System Mode Option
                                val isSys = settings.themeMode == ThemeMode.SYSTEM
                                Surface(
                                    shape = RoundedCornerShape(10.dp),
                                    color = if (isSys) colors.primary else colors.surface,
                                    border = androidx.compose.foundation.BorderStroke(1.dp, if (isSys) colors.primary else colors.border),
                                    modifier = Modifier
                                        .weight(1f)
                                        .clickable { onUpdateSettings(settings.copy(themeMode = ThemeMode.SYSTEM)) }
                                ) {
                                    Column(
                                        modifier = Modifier.padding(vertical = 10.dp, horizontal = 4.dp),
                                        horizontalAlignment = Alignment.CenterHorizontally,
                                        verticalArrangement = Arrangement.spacedBy(4.dp)
                                    ) {
                                        Icon(
                                            imageVector = Icons.Default.BrightnessAuto,
                                            contentDescription = null,
                                            tint = if (isSys) Color.White else colors.textPrimary,
                                            modifier = Modifier.size(20.dp)
                                        )
                                        Text(
                                            text = "سیستم گوشی",
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 11.sp,
                                            color = if (isSys) Color.White else colors.textPrimary
                                        )
                                        Text(
                                            text = "اتوماتیک",
                                            fontSize = 9.sp,
                                            color = if (isSys) Color.White.copy(alpha = 0.8f) else colors.textSecondary
                                        )
                                    }
                                }

                                // Dark Mode Option
                                val isDark = settings.themeMode == ThemeMode.DARK
                                Surface(
                                    shape = RoundedCornerShape(10.dp),
                                    color = if (isDark) colors.primary else colors.surface,
                                    border = androidx.compose.foundation.BorderStroke(1.dp, if (isDark) colors.primary else colors.border),
                                    modifier = Modifier
                                        .weight(1f)
                                        .clickable { onUpdateSettings(settings.copy(themeMode = ThemeMode.DARK)) }
                                ) {
                                    Column(
                                        modifier = Modifier.padding(vertical = 10.dp, horizontal = 4.dp),
                                        horizontalAlignment = Alignment.CenterHorizontally,
                                        verticalArrangement = Arrangement.spacedBy(4.dp)
                                    ) {
                                        Icon(
                                            imageVector = Icons.Default.DarkMode,
                                            contentDescription = null,
                                            tint = if (isDark) Color.White else colors.textPrimary,
                                            modifier = Modifier.size(20.dp)
                                        )
                                        Text(
                                            text = "حالت شب",
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 11.sp,
                                            color = if (isDark) Color.White else colors.textPrimary
                                        )
                                        Text(
                                            text = "تیره (Dark)",
                                            fontSize = 9.sp,
                                            color = if (isDark) Color.White.copy(alpha = 0.8f) else colors.textSecondary
                                        )
                                    }
                                }

                                // Light Mode Option
                                val isLight = settings.themeMode == ThemeMode.LIGHT
                                Surface(
                                    shape = RoundedCornerShape(10.dp),
                                    color = if (isLight) colors.primary else colors.surface,
                                    border = androidx.compose.foundation.BorderStroke(1.dp, if (isLight) colors.primary else colors.border),
                                    modifier = Modifier
                                        .weight(1f)
                                        .clickable { onUpdateSettings(settings.copy(themeMode = ThemeMode.LIGHT)) }
                                ) {
                                    Column(
                                        modifier = Modifier.padding(vertical = 10.dp, horizontal = 4.dp),
                                        horizontalAlignment = Alignment.CenterHorizontally,
                                        verticalArrangement = Arrangement.spacedBy(4.dp)
                                    ) {
                                        Icon(
                                            imageVector = Icons.Default.LightMode,
                                            contentDescription = null,
                                            tint = if (isLight) Color.White else colors.textPrimary,
                                            modifier = Modifier.size(20.dp)
                                        )
                                        Text(
                                            text = "حالت روز",
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 11.sp,
                                            color = if (isLight) Color.White else colors.textPrimary
                                        )
                                        Text(
                                            text = "روشن (Light)",
                                            fontSize = 9.sp,
                                            color = if (isLight) Color.White.copy(alpha = 0.8f) else colors.textSecondary
                                        )
                                    }
                                }
                            }

                            // Theme Palette Preset Selection
                            HorizontalDivider(color = colors.border.copy(alpha = 0.5f))
                            Text(
                                text = "انتخاب تم و پالت رنگی برنامه:",
                                fontSize = 12.sp,
                                fontWeight = FontWeight.Bold,
                                color = colors.textPrimary
                            )

                            Column(verticalArrangement = Arrangement.spacedBy(6.dp)) {
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
                            }
                        }
                    }

                    // 1.2 Chart Asset Colors Card (وظیفه ۴: تفکیک رنگ‌بندی نمودارها از پالت و تم برنامه)
                    Card(
                        shape = RoundedCornerShape(20.dp),
                        colors = CardDefaults.cardColors(containerColor = colors.surfaceVariant.copy(alpha = 0.5f)),
                        border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f))
                    ) {
                        Column(modifier = Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                            Row(
                                verticalAlignment = Alignment.CenterVertically,
                                horizontalArrangement = Arrangement.spacedBy(6.dp)
                            ) {
                                Icon(
                                    imageVector = Icons.Default.AutoGraph,
                                    contentDescription = null,
                                    tint = colors.primary,
                                    modifier = Modifier.size(18.dp)
                                )
                                Text(
                                    text = "رنگ‌بندی تخصصی کلاس‌های دارایی در نمودارها",
                                    fontSize = 13.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = colors.textPrimary
                                )
                            }

                            Text(
                                text = "راهنمای رنگ‌بندی ثابت و سایه‌دار دارایی‌ها در تمام نمودارها (نقشه درختی، خورشیدی، درختی مدرن و نوار انباشته):",
                                fontSize = 10.5.sp,
                                color = colors.textSecondary
                            )

                            val assetColorCategories = listOf(
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
                                                Text(
                                                    text = title,
                                                    fontSize = 11.sp,
                                                    fontWeight = FontWeight.Bold,
                                                    color = colors.textPrimary
                                                )
                                            }
                                            Text(
                                                text = desc,
                                                fontSize = 9.5.sp,
                                                color = colors.textSecondary
                                            )
                                        }
                                    }
                                }
                            }
                        }
                    }

                    // 1.5 Text & Icon Size Selector
                    Card(
                        shape = RoundedCornerShape(20.dp),
                        colors = CardDefaults.cardColors(containerColor = colors.surfaceVariant.copy(alpha = 0.5f)),
                        border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f))
                    ) {
                        Column(modifier = Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
                            Text("اندازه نوشته‌ها و آیکون‌ها", fontSize = 12.sp, fontWeight = FontWeight.Bold, color = colors.textPrimary)
                            
                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.spacedBy(8.dp)
                            ) {
                                com.example.data.model.AppFontSize.values().forEach { fs ->
                                    val isSel = settings.fontSize == fs
                                    Surface(
                                        shape = RoundedCornerShape(8.dp),
                                        color = if (isSel) colors.primary else colors.surface,
                                        border = androidx.compose.foundation.BorderStroke(1.dp, if (isSel) colors.primary else colors.border),
                                        modifier = Modifier
                                            .weight(1f)
                                            .clickable { onUpdateSettings(settings.copy(fontSize = fs)) }
                                    ) {
                                        Text(
                                            text = fs.labelFa,
                                            fontSize = 11.sp,
                                            fontWeight = if (isSel) FontWeight.Bold else FontWeight.Normal,
                                            color = if (isSel) Color.White else colors.textPrimary,
                                            modifier = Modifier.padding(vertical = 8.dp),
                                            textAlign = androidx.compose.ui.text.style.TextAlign.Center
                                        )
                                    }
                                }
                            }
                        }
                    }

                    }
                    if (selectedTabIndex == 1) {
                    // 1.8 Customization of Chart & View Tabs Order (شخصی‌سازی ترتیب نمودارها)
                    Card(
                        shape = RoundedCornerShape(20.dp),
                        colors = CardDefaults.cardColors(containerColor = colors.surfaceVariant.copy(alpha = 0.5f)),
                        border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f))
                    ) {
                        Column(modifier = Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                            Row(
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

                                val currentOrder = settings.customViewOrder.ifEmpty {
                                listOf(
                                    com.example.data.model.AppViewMode.TREEMAP,
                                    com.example.data.model.AppViewMode.CLASSIC_TREE,
                                    com.example.data.model.AppViewMode.TREE,
                                    com.example.data.model.AppViewMode.CHART,
                                    com.example.data.model.AppViewMode.BAR_CHART,
                                    com.example.data.model.AppViewMode.ANALYTICS
                                )
                            }

                            Column(verticalArrangement = Arrangement.spacedBy(6.dp)) {
                                currentOrder.forEachIndexed { index, mode ->
                                    val icon = when (mode) {
                                        com.example.data.model.AppViewMode.TREEMAP -> Icons.Default.Dashboard
                                        com.example.data.model.AppViewMode.CLASSIC_TREE -> Icons.Default.FormatListBulleted
                                        com.example.data.model.AppViewMode.TREE -> Icons.Default.AccountTree
                                        com.example.data.model.AppViewMode.CHART -> Icons.Default.PieChart
                                        com.example.data.model.AppViewMode.BAR_CHART -> Icons.Default.BarChart
                                        com.example.data.model.AppViewMode.ANALYTICS -> Icons.Default.Analytics
                                    }

                                    Surface(
                                        shape = RoundedCornerShape(8.dp),
                                        color = colors.surface,
                                        border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f)),
                                        modifier = Modifier.fillMaxWidth()
                                    ) {
                                        Row(
                                            modifier = Modifier
                                                .fillMaxWidth()
                                                .padding(horizontal = 10.dp, vertical = 6.dp),
                                            verticalAlignment = Alignment.CenterVertically,
                                            horizontalArrangement = Arrangement.SpaceBetween
                                        ) {
                                            Row(
                                                verticalAlignment = Alignment.CenterVertically,
                                                horizontalArrangement = Arrangement.spacedBy(8.dp)
                                            ) {
                                                Surface(
                                                    shape = RoundedCornerShape(4.dp),
                                                    color = colors.surfaceVariant
                                                ) {
                                                    val numDisplay = if (settings.usePersianDigits) {
                                                        com.example.utils.NumberFormatUtils.toPersianDigits((index + 1).toString())
                                                    } else {
                                                        (index + 1).toString()
                                                    }
                                                    Text(
                                                        text = numDisplay,
                                                        fontSize = 11.sp,
                                                        fontWeight = FontWeight.Bold,
                                                        color = colors.primary,
                                                        modifier = Modifier.padding(horizontal = 6.dp, vertical = 2.dp)
                                                    )
                                                }

                                                Icon(
                                                    imageVector = icon,
                                                    contentDescription = null,
                                                    tint = colors.primary,
                                                    modifier = Modifier.size(16.dp)
                                                )

                                                Text(
                                                    text = mode.titleFa,
                                                    fontSize = 12.sp,
                                                    fontWeight = FontWeight.Medium,
                                                    color = colors.textPrimary
                                                )
                                            }

                                            Row(horizontalArrangement = Arrangement.spacedBy(4.dp)) {
                                                // Move Up Button
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
                                                    enabled = index > 0,
                                                    modifier = Modifier.size(28.dp)
                                                ) {
                                                    Icon(
                                                        imageVector = Icons.Default.ArrowUpward,
                                                        contentDescription = "انتقال به بالا",
                                                        tint = if (index > 0) colors.primary else colors.textSecondary.copy(alpha = 0.3f),
                                                        modifier = Modifier.size(16.dp)
                                                    )
                                                }

                                                // Move Down Button
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
                                                    enabled = index < currentOrder.size - 1,
                                                    modifier = Modifier.size(28.dp)
                                                ) {
                                                    Icon(
                                                        imageVector = Icons.Default.ArrowDownward,
                                                        contentDescription = "انتقال به پایین",
                                                        tint = if (index < currentOrder.size - 1) colors.primary else colors.textSecondary.copy(alpha = 0.3f),
                                                        modifier = Modifier.size(16.dp)
                                                    )
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }

                    // 2. Display Metrics Toggles (Percent of Total, Percent of Group, Total Value)
                    Card(
                        shape = RoundedCornerShape(20.dp),
                        colors = CardDefaults.cardColors(containerColor = colors.surfaceVariant.copy(alpha = 0.5f)),
                        border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f))
                    ) {
                        Column(modifier = Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
                            Text("آیتم‌های نمایشی جلوی نام نودها", fontSize = 12.sp, fontWeight = FontWeight.Bold, color = colors.textPrimary)
                            Text("تنظیم نمایش یا عدم نمایش درصد از کل، درصد از هم‌گروه و مبلغ خلاصه شده جلوی هر دارایی", fontSize = 10.sp, color = colors.textSecondary)

                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.SpaceBetween,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Text("نمایش درصد از کل سبد دارایی (%)", fontSize = 11.sp, color = colors.textPrimary)
                                Switch(
                                    checked = settings.showPercentOfTotal,
                                    onCheckedChange = { onUpdateSettings(settings.copy(showPercentOfTotal = it)) }
                                )
                            }

                            HorizontalDivider(color = colors.border.copy(alpha = 0.5f))

                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.SpaceBetween,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Text("نمایش درصد از هم‌گروه / هم‌گروه (%)", fontSize = 11.sp, color = colors.textPrimary)
                                Switch(
                                    checked = settings.showPercentOfGroup,
                                    onCheckedChange = { onUpdateSettings(settings.copy(showPercentOfGroup = it)) }
                                )
                            }

                            HorizontalDivider(color = colors.border.copy(alpha = 0.5f))

                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.SpaceBetween,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Text("نمایش مبلغ خلاصه شده (میلیون/میلیارد)", fontSize = 11.sp, color = colors.textPrimary)
                                Switch(
                                    checked = settings.showTotalValue,
                                    onCheckedChange = { onUpdateSettings(settings.copy(showTotalValue = it)) }
                                )
                            }
                        }
                    }

                    // 3. Currency Unit Selection
                    Card(
                        shape = RoundedCornerShape(20.dp),
                        colors = CardDefaults.cardColors(containerColor = colors.surfaceVariant.copy(alpha = 0.5f)),
                        border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f))
                    ) {
                        Column(modifier = Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.spacedBy(8.dp),
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Text("واحد پول:", fontSize = 12.sp, fontWeight = FontWeight.Bold, color = colors.textPrimary)
                                Surface(
                                    shape = RoundedCornerShape(8.dp),
                                    color = if (settings.currencyUnit == CurrencyUnit.TOMAN) colors.primary else colors.surface,
                                    border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f)),
                                    modifier = Modifier
                                        .weight(1f)
                                        .clickable { onUpdateSettings(settings.copy(currencyUnit = CurrencyUnit.TOMAN)) }
                                ) {
                                    Column(
                                        modifier = Modifier.padding(10.dp),
                                        horizontalAlignment = Alignment.CenterHorizontally
                                    ) {
                                        Text(
                                            "تومان",
                                            fontWeight = FontWeight.Bold,
                                            color = if (settings.currencyUnit == CurrencyUnit.TOMAN) Color.White else colors.textPrimary
                                        )
                                        Text(
                                            "(۱۰ ریال)",
                                            fontSize = 10.sp,
                                            color = if (settings.currencyUnit == CurrencyUnit.TOMAN) Color.White.copy(alpha = 0.8f) else colors.textSecondary
                                        )
                                    }
                                }

                                Surface(
                                    shape = RoundedCornerShape(8.dp),
                                    color = if (settings.currencyUnit == CurrencyUnit.RIAL) colors.primary else colors.surface,
                                    border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f)),
                                    modifier = Modifier
                                        .weight(1f)
                                        .clickable { onUpdateSettings(settings.copy(currencyUnit = CurrencyUnit.RIAL)) }
                                ) {
                                    Column(
                                        modifier = Modifier.padding(10.dp),
                                        horizontalAlignment = Alignment.CenterHorizontally
                                    ) {
                                        Text(
                                            "ریال",
                                            fontWeight = FontWeight.Bold,
                                            color = if (settings.currencyUnit == CurrencyUnit.RIAL) Color.White else colors.textPrimary
                                        )
                                        Text(
                                            "(واحد پایه)",
                                            fontSize = 10.sp,
                                            color = if (settings.currencyUnit == CurrencyUnit.RIAL) Color.White.copy(alpha = 0.8f) else colors.textSecondary
                                        )
                                    }
                                }
                            }
                        }
                    }

                    // 3. Persian Digits Toggle
                    Card(
                        shape = RoundedCornerShape(20.dp),
                        colors = CardDefaults.cardColors(containerColor = colors.surfaceVariant.copy(alpha = 0.5f)),
                        border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f))
                    ) {
                        Row(
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(14.dp),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Column(modifier = Modifier.weight(1f)) {
                                Text("اعداد و ارقام به خط فارسی", fontSize = 12.sp, fontWeight = FontWeight.Bold, color = colors.textPrimary)
                                Text("نمایش مبالغ و درصدها با ارقام فارسی (۱۲۳,۴۵۶)", fontSize = 10.sp, color = colors.textSecondary)
                            }
                            Switch(
                                checked = settings.usePersianDigits,
                                onCheckedChange = { onUpdateSettings(settings.copy(usePersianDigits = it)) }
                            )
                        }
                    }

                    // 4. Decimal Places
                    Card(
                        shape = RoundedCornerShape(20.dp),
                        colors = CardDefaults.cardColors(containerColor = colors.surfaceVariant.copy(alpha = 0.5f)),
                        border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f))
                    ) {
                        Column(modifier = Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(6.dp)) {
                            Text("تعداد رقم اعشار در درصدها", fontSize = 12.sp, fontWeight = FontWeight.Bold, color = colors.textPrimary)
                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.spacedBy(8.dp)
                            ) {
                                listOf(0, 1, 2, 3).forEach { dec ->
                                    val isSel = settings.decimalPlaces == dec
                                    Surface(
                                        shape = RoundedCornerShape(8.dp),
                                        color = if (isSel) colors.primary else colors.surface,
                                        border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f)),
                                        modifier = Modifier
                                            .weight(1f)
                                            .clickable { onUpdateSettings(settings.copy(decimalPlaces = dec)) }
                                    ) {
                                        Box(
                                            modifier = Modifier.padding(vertical = 8.dp),
                                            contentAlignment = Alignment.Center
                                        ) {
                                            Text(
                                                text = "$dec رقم",
                                                fontSize = 11.sp,
                                                fontWeight = FontWeight.Bold,
                                                color = if (isSel) Color.White else colors.textPrimary
                                            )
                                        }
                                    }
                                }
                            }
                        }
                    }

                    }
                    if (selectedTabIndex == 2) {
                    // 5. Data Backup & Restore
                    Card(
                        shape = RoundedCornerShape(20.dp),
                        colors = CardDefaults.cardColors(containerColor = colors.surfaceVariant.copy(alpha = 0.5f)),
                        border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f))
                    ) {
                        Column(modifier = Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
                            Text("پشتیبان‌گیری و بازیابی داده‌ها (JSON)", fontSize = 12.sp, fontWeight = FontWeight.Bold, color = colors.textPrimary)
                            Text("تهیه نسخه پشتیبان از کل ساختار درخت دارایی و تنظیمات جهت انتقال به دستگاه دیگر.", fontSize = 10.sp, color = colors.textSecondary)

                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.spacedBy(8.dp)
                            ) {
                                Button(
                                    onClick = {
                                        coroutineScope.launch {
                                            backupJsonContent = onExportBackupJson()
                                            showJsonBackupModal = true
                                        }
                                    },
                                    colors = ButtonDefaults.buttonColors(containerColor = colors.primary),
                                    modifier = Modifier.weight(1f)
                                ) {
                                    Icon(Icons.Default.Download, contentDescription = null, modifier = Modifier.size(16.dp))
                                    Spacer(modifier = Modifier.width(4.dp))
                                    Text("پشتیبان گیری", fontSize = 11.sp)
                                }

                                OutlinedButton(
                                    onClick = {
                                        showJsonBackupModal = true
                                    },
                                    modifier = Modifier.weight(1f)
                                ) {
                                    Icon(Icons.Default.Upload, contentDescription = null, modifier = Modifier.size(16.dp))
                                    Spacer(modifier = Modifier.width(4.dp))
                                    Text("بازیابی JSON", fontSize = 11.sp, color = colors.textPrimary)
                                }
                            }
                        }
                    }

                    // 6. Reset Database
                    Card(
                        shape = RoundedCornerShape(20.dp),
                        colors = CardDefaults.cardColors(containerColor = colors.surfaceVariant),
                        border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f))
                    ) {
                        Column(modifier = Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(6.dp)) {
                            Text("بازنشانی به پرتفوی اولیه نمونه", fontSize = 12.sp, fontWeight = FontWeight.Bold, color = colors.primary)
                            Text("بازگردانی دارایی‌های نمونه پیش‌فرض اپلیکیشن شامل طلا، سهام و ارز.", fontSize = 10.sp, color = colors.textSecondary)

                            OutlinedButton(
                                onClick = { showResetConfirm = true },
                                modifier = Modifier.fillMaxWidth()
                            ) {
                                Icon(Icons.Default.RestartAlt, contentDescription = null)
                                Spacer(modifier = Modifier.width(6.dp))
                                Text("بازنشانی به پرتفوی پیش‌فرض", fontSize = 11.sp, fontWeight = FontWeight.Bold)
                            }
                        }
                    }

                    // 6.5 Wipe All Financial Data (وظیفه ۶: منوی خام کردن کامل اطلاعات مالی با منوی اخطار)
                    Card(
                        shape = RoundedCornerShape(20.dp),
                        colors = CardDefaults.cardColors(containerColor = colors.lossContainer.copy(alpha = 0.35f)),
                        border = androidx.compose.foundation.BorderStroke(1.2.dp, colors.loss.copy(alpha = 0.5f))
                    ) {
                        Column(modifier = Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
                            Row(
                                verticalAlignment = Alignment.CenterVertically,
                                horizontalArrangement = Arrangement.spacedBy(6.dp)
                            ) {
                                Icon(
                                    imageVector = Icons.Default.DeleteForever,
                                    contentDescription = null,
                                    tint = colors.loss,
                                    modifier = Modifier.size(20.dp)
                                )
                                Text(
                                    text = "خام کردن کامل اطلاعات مالی",
                                    fontSize = 12.5.sp,
                                    fontWeight = FontWeight.Black,
                                    color = colors.loss
                                )
                            }
                            Text(
                                text = "حذف و پاک‌سازی تمام دارایی‌ها، مبالغ و نودها جهت شروع یک پرتفوی کاملاً جدید و صفر.",
                                fontSize = 10.5.sp,
                                color = colors.textSecondary
                            )

                            Button(
                                onClick = { showWipeConfirm = true },
                                colors = ButtonDefaults.buttonColors(containerColor = colors.loss, contentColor = Color.White),
                                modifier = Modifier.fillMaxWidth()
                            ) {
                                Icon(Icons.Default.DeleteSweep, contentDescription = null)
                                Spacer(modifier = Modifier.width(6.dp))
                                Text("خام کردن کامل تمام اطلاعات مالی (صفر کردن)", fontSize = 11.5.sp, fontWeight = FontWeight.Bold)
                            }
                        }
                    }

                    // 7. PDF Report Generation (گزارش‌گیری)
                    Card(
                        shape = RoundedCornerShape(20.dp),
                        colors = CardDefaults.cardColors(containerColor = colors.surfaceVariant),
                        border = androidx.compose.foundation.BorderStroke(1.2.dp, colors.primary.copy(alpha = 0.5f))
                    ) {
                        Column(modifier = Modifier.padding(14.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
                            Row(
                                verticalAlignment = Alignment.CenterVertically,
                                horizontalArrangement = Arrangement.spacedBy(6.dp)
                            ) {
                                Icon(
                                    imageVector = Icons.Default.PictureAsPdf,
                                    contentDescription = null,
                                    tint = colors.primary,
                                    modifier = Modifier.size(20.dp)
                                )
                                Text(
                                    text = "گزارش‌گیری و خروجی اینفوگرافیک PDF",
                                    fontSize = 13.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = colors.textPrimary
                                )
                            }

                            Text(
                                text = "تولید فایل اینفوگرافیک PDF بر اساس نمودار انتخابی شما همراه با راهنمای رنگی و جدول متنی درصدها و ارزش دارایی‌ها.",
                                fontSize = 10.5.sp,
                                color = colors.textSecondary
                            )

                            // Chart Type Selector
                            Text(
                                text = "نوع نمودار در گزارش اینفوگرافیک:",
                                fontSize = 11.sp,
                                fontWeight = FontWeight.Medium,
                                color = colors.textPrimary
                            )

                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.spacedBy(6.dp)
                            ) {
                                PdfChartType.values().forEach { chartType ->
                                    val isSelected = selectedPdfChartType == chartType
                                    Surface(
                                        shape = RoundedCornerShape(8.dp),
                                        color = if (isSelected) colors.primaryContainer else colors.surface,
                                        border = androidx.compose.foundation.BorderStroke(
                                            1.dp,
                                            if (isSelected) colors.primary else colors.border
                                        ),
                                        modifier = Modifier
                                            .weight(1f)
                                            .clickable { selectedPdfChartType = chartType }
                                    ) {
                                        Column(
                                            modifier = Modifier.padding(vertical = 8.dp, horizontal = 4.dp),
                                            horizontalAlignment = Alignment.CenterHorizontally,
                                            verticalArrangement = Arrangement.spacedBy(4.dp)
                                        ) {
                                            Icon(
                                                imageVector = when (chartType) {
                                                    PdfChartType.TREEMAP -> Icons.Default.Dashboard
                                                    PdfChartType.DONUT_SUNBURST -> Icons.Default.PieChart
                                                    PdfChartType.STACKED_BAR -> Icons.Default.BarChart
                                                },
                                                contentDescription = null,
                                                tint = if (isSelected) colors.primary else colors.textSecondary,
                                                modifier = Modifier.size(18.dp)
                                            )
                                            Text(
                                                text = chartType.title,
                                                fontSize = 9.5.sp,
                                                fontWeight = if (isSelected) FontWeight.Bold else FontWeight.Normal,
                                                color = if (isSelected) colors.primary else colors.textPrimary,
                                                textAlign = androidx.compose.ui.text.style.TextAlign.Center
                                            )
                                        }
                                    }
                                }
                            }

                            Button(
                                onClick = {
                                    rootCalculated?.let { root ->
                                        PdfReportGenerator.generateAndSharePdf(
                                            context = context,
                                            rootCalculated = root,
                                            settings = settings,
                                            chartType = selectedPdfChartType
                                        )
                                    }
                                },
                                colors = ButtonDefaults.buttonColors(containerColor = colors.primary),
                                modifier = Modifier.fillMaxWidth()
                            ) {
                                Icon(Icons.Default.Download, contentDescription = null, modifier = Modifier.size(18.dp))
                                Spacer(modifier = Modifier.width(6.dp))
                                Text("تولید و دریافت گزارش اینفوگرافیک PDF", fontSize = 12.sp, fontWeight = FontWeight.Bold)
                            }
                        }
                    }
                }
            }
                    }
        }
    }

    if (showResetConfirm) {
        AlertDialog(
            onDismissRequest = { showResetConfirm = false },
            title = { Text("تأیید بازنشانی به داده‌های نمونه اولیه", fontWeight = FontWeight.Bold, color = colors.textPrimary) },
            text = { Text("آیا مطمئن هستید؟ تمام تغییرات و دارایی‌های شخصی شما پاک شده و با پرتفوی اولیه پیش‌فرض جایگزین خواهند شد.", color = colors.textSecondary) },
            containerColor = colors.surface,
            confirmButton = {
                Button(
                    onClick = {
                        showResetConfirm = false
                        onResetAllData()
                    },
                    colors = ButtonDefaults.buttonColors(containerColor = colors.primary)
                ) {
                    Text("بله، بازنشانی به پیش‌فرض")
                }
            },
            dismissButton = {
                OutlinedButton(onClick = { showResetConfirm = false }) {
                    Text("انصراف", color = colors.textPrimary)
                }
            }
        )
    }

    // وظیفه ۶: منوی اخطار خام کردن کامل اطلاعات مالی
    if (showWipeConfirm) {
        AlertDialog(
            onDismissRequest = { showWipeConfirm = false },
            title = {
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(6.dp)
                ) {
                    Icon(Icons.Default.Warning, contentDescription = null, tint = colors.loss)
                    Text(
                        text = "هشدار مهم: خام کردن کامل اطلاعات مالی",
                        fontWeight = FontWeight.Black,
                        color = colors.loss
                    )
                }
            },
            text = {
                Text(
                    text = "آیا از خام کردن تمام اطلاعات مالی اطمینان کامل دارید؟\n\nکلیه دارایی‌ها، نودها، مبالغ، تعداد سهام و اطلاعات آماری به طور کامل پاک شده و پایگاه داده به حالت خام و صفر ریال درمی‌آید.\n\nاین عملیات غیرقابل بازگشت است مگر اینکه نسخه پشتیبان JSON داشته باشید.",
                    color = colors.textPrimary,
                    fontSize = 12.sp,
                    lineHeight = 18.sp
                )
            },
            containerColor = colors.surface,
            confirmButton = {
                Button(
                    onClick = {
                        showWipeConfirm = false
                        onWipeFinancialData()
                    },
                    colors = ButtonDefaults.buttonColors(containerColor = colors.loss, contentColor = Color.White)
                ) {
                    Text("بله، تمام اطلاعات را خام کن", fontWeight = FontWeight.Bold)
                }
            },
            dismissButton = {
                OutlinedButton(onClick = { showWipeConfirm = false }) {
                    Text("انصراف و بازگشت", color = colors.textPrimary)
                }
            }
        )
    }

    if (showJsonBackupModal) {
        Dialog(onDismissRequest = { showJsonBackupModal = false }) {
            Card(
                shape = RoundedCornerShape(16.dp),
                colors = CardDefaults.cardColors(containerColor = colors.surface),
                border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f)),
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(12.dp)
            ) {
                Column(
                    modifier = Modifier.padding(16.dp),
                    verticalArrangement = Arrangement.spacedBy(10.dp)
                ) {
                    Text("پشتیبان‌گیری / بازیابی JSON", fontWeight = FontWeight.Bold, fontSize = 14.sp, color = colors.textPrimary)

                    OutlinedTextField(
                        value = if (backupJsonContent.isNotEmpty()) backupJsonContent else restoreJsonInput,
                        onValueChange = { restoreJsonInput = it },
                        label = { Text("محتوای JSON نسخه پشتیبان", color = colors.textSecondary) },
                        textStyle = LocalTextStyle.current.copy(color = colors.inputText),
                        colors = OutlinedTextFieldDefaults.colors(
                            focusedTextColor = colors.inputText,
                            unfocusedTextColor = colors.inputText,
                            focusedContainerColor = colors.inputBackground,
                            unfocusedContainerColor = colors.inputBackground,
                            focusedBorderColor = colors.primary,
                            unfocusedBorderColor = colors.border,
                            cursorColor = colors.inputText
                        ),
                        modifier = Modifier
                            .fillMaxWidth()
                            .height(180.dp)
                    )

                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.spacedBy(8.dp)
                    ) {
                        if (backupJsonContent.isNotEmpty()) {
                            Button(
                                onClick = {
                                    val clipboard = context.getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager
                                    val clip = ClipData.newPlainText("AssetTree Backup", backupJsonContent)
                                    clipboard.setPrimaryClip(clip)
                                },
                                colors = ButtonDefaults.buttonColors(containerColor = colors.primary),
                                modifier = Modifier.weight(1f)
                            ) {
                                Text("کپی متن JSON", fontSize = 11.sp)
                            }
                        } else {
                            Button(
                                onClick = {
                                    if (restoreJsonInput.isNotBlank()) {
                                        onImportBackupJson(restoreJsonInput)
                                        showJsonBackupModal = false
                                    }
                                },
                                colors = ButtonDefaults.buttonColors(containerColor = colors.primary),
                                modifier = Modifier.weight(1f)
                            ) {
                                Text("اعمال و بازیابی", fontSize = 11.sp)
                            }
                        }

                        OutlinedButton(
                            onClick = {
                                showJsonBackupModal = false
                                backupJsonContent = ""
                                restoreJsonInput = ""
                            },
                            modifier = Modifier.weight(1f)
                        ) {
                            Text("بستن", fontSize = 11.sp, color = colors.textPrimary)
                        }
                    }
                }
            }
        }
    }
}
}
