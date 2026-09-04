package com.example.ui.components

import android.app.Activity
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ExitToApp
import androidx.compose.material.icons.filled.*
import androidx.compose.material.icons.outlined.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.hapticfeedback.HapticFeedbackType
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalHapticFeedback
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.data.model.AppThemePreset
import com.example.data.model.DisplaySettings
import com.example.data.model.AppViewMode
import com.example.ui.theme.AppTheme
import com.example.utils.NumberFormatUtils
import com.example.utils.PersianDateUtils

@Composable
fun AppTopBar(
    activeView: AppViewMode,
    settings: DisplaySettings,
    totalPortfolioValue: Double,
    undoCount: Int,
    isDark: Boolean,
    onSelectView: (AppViewMode) -> Unit,
    onToggleTheme: () -> Unit,
    onTogglePrivacy: () -> Unit,
    onUndo: () -> Unit,
    onOpenExcelImport: () -> Unit,
    onOpenSymbolBook: () -> Unit,
    onOpenSettings: () -> Unit,
    onSelectThemePreset: (AppThemePreset) -> Unit = {}
) {
    val context = LocalContext.current
    val haptic = LocalHapticFeedback.current
    val colors = AppTheme.colors
    var showMenu by remember { mutableStateOf(false) }
    var showPresetDialog by remember { mutableStateOf(false) }
    var showExitConfirmDialog by remember { mutableStateOf(false) }
    var showChartDropdown by remember { mutableStateOf(false) }

    // Real-time Persian Date & Time connected to device clock (updates every second)
    var currentTimeMillis by remember { mutableStateOf(System.currentTimeMillis()) }
    LaunchedEffect(Unit) {
        while (true) {
            kotlinx.coroutines.delay(1000)
            currentTimeMillis = System.currentTimeMillis()
        }
    }
    val persianDateTimeStr = remember(currentTimeMillis) {
        PersianDateUtils.formatPersianDate(currentTimeMillis, includeTime = true)
    }

    Surface(
        color = colors.surface,
        shadowElevation = 0.dp,
        modifier = Modifier
            .fillMaxWidth()
            .statusBarsPadding()
    ) {
        BoxWithConstraints(modifier = Modifier.fillMaxWidth()) {
            val isCompact = maxWidth < 380.dp
            val isTablet = maxWidth >= 600.dp

            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(horizontal = if (isCompact) 8.dp else 12.dp, vertical = 6.dp),
                verticalArrangement = Arrangement.spacedBy(6.dp)
            ) {
                // بخش اصلی برنامه با پس‌زمینه متمایز و روشن‌تر و حاشیه خط‌دار ملایم
                // (نماد برنامه، تاریخ و ساعت، سه نقطه، آیکون خروج، ارزش کل و مبلغ، علامت چشم)
                Card(
                    shape = RoundedCornerShape(16.dp),
                    colors = CardDefaults.cardColors(
                        containerColor = if (isDark) colors.surfaceVariant.copy(alpha = 0.7f) else Color(0xFFF8FAFC)
                    ),
                    border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.6f)),
                    elevation = CardDefaults.cardElevation(defaultElevation = 2.dp),
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(horizontal = 12.dp, vertical = 9.dp),
                        verticalArrangement = Arrangement.spacedBy(8.dp)
                    ) {
                        // سطر ۱ هدر اصلی: نماد برنامه (راست) و تاریخ/ساعت نزدیک سه نقطه (چپ) (وظیفه ۵)
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            // راست: نماد برنامه (Custom App Icon)
                            Box(
                                modifier = Modifier
                                    .size(if (isCompact) 34.dp else 38.dp)
                                    .clip(RoundedCornerShape(10.dp))
                                    .background(
                                        Brush.linearGradient(
                                            listOf(
                                                Color(0xFF0F172A),
                                                Color(0xFF1E293B),
                                                Color(0xFF003B6F)
                                            )
                                        )
                                    )
                                    .border(
                                        1.2.dp,
                                        Brush.linearGradient(
                                            listOf(Color(0xFFF59E0B), Color(0xFF10B981), Color(0xFF38BDF8))
                                        ),
                                        RoundedCornerShape(10.dp)
                                    ),
                                contentAlignment = Alignment.Center
                            ) {
                                androidx.compose.foundation.Canvas(modifier = Modifier.size(if (isCompact) 22.dp else 24.dp)) {
                                    val w = size.width
                                    val h = size.height
                                    val trunkColor = Color(0xFFF59E0B) // Gold trunk
                                    val leaf1 = Color(0xFF10B981) // Emerald
                                    val leaf2 = Color(0xFF38BDF8) // Sky Blue
                                    val leaf3 = Color(0xFFA855F7) // Purple

                                    // Trunk lines
                                    drawLine(trunkColor, Offset(w * 0.5f, h * 0.82f), Offset(w * 0.5f, h * 0.32f), strokeWidth = 3f)
                                    drawLine(trunkColor, Offset(w * 0.5f, h * 0.55f), Offset(w * 0.24f, h * 0.44f), strokeWidth = 2.5f)
                                    drawLine(trunkColor, Offset(w * 0.5f, h * 0.55f), Offset(w * 0.76f, h * 0.44f), strokeWidth = 2.5f)

                                    // Root base node
                                    drawCircle(color = trunkColor, radius = w * 0.14f, center = Offset(w * 0.5f, h * 0.82f))

                                    // Branch leaves / coin nodes
                                    drawCircle(color = leaf1, radius = w * 0.17f, center = Offset(w * 0.5f, h * 0.25f))
                                    drawCircle(color = leaf2, radius = w * 0.13f, center = Offset(w * 0.22f, h * 0.42f))
                                    drawCircle(color = leaf3, radius = w * 0.13f, center = Offset(w * 0.78f, h * 0.42f))
                                }
                            }

                            Spacer(modifier = Modifier.weight(1f))

                            // چپ: تاریخ و ساعت زنده شمسی در کنار دکمه بازگشت و سه نقطه (وظیفه ۵)
                            Row(
                                horizontalArrangement = Arrangement.spacedBy(6.dp),
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                // تاریخ و ساعت زنده شمسی
                                Surface(
                                    shape = RoundedCornerShape(8.dp),
                                    color = colors.surface.copy(alpha = 0.95f),
                                    border = androidx.compose.foundation.BorderStroke(1.dp, colors.border.copy(alpha = 0.7f))
                                ) {
                                    Text(
                                        text = persianDateTimeStr,
                                        fontSize = if (isCompact) 12.sp else 13.5.sp,
                                        color = colors.textPrimary,
                                        fontWeight = FontWeight.Bold,
                                        modifier = Modifier.padding(horizontal = 7.dp, vertical = 3.5.dp)
                                    )
                                }

                                if (undoCount > 0) {
                                    IconButton(
                                        onClick = onUndo,
                                        modifier = Modifier.size(32.dp)
                                    ) {
                                        Icon(
                                            imageVector = Icons.Default.Undo,
                                            contentDescription = "بازگشت",
                                            tint = colors.warning,
                                            modifier = Modifier.size(20.dp)
                                        )
                                    }
                                }

                                // سه نقطه منوی امکانات
                                Box {
                                    IconButton(
                                        onClick = { showMenu = true },
                                        modifier = Modifier
                                            .size(32.dp)
                                            .testTag("btn_three_dots_menu")
                                    ) {
                                        Icon(
                                            imageVector = Icons.Default.MoreVert,
                                            contentDescription = "منوی امکانات",
                                            tint = colors.textPrimary,
                                            modifier = Modifier.size(20.dp)
                                        )
                                    }

                                    DropdownMenu(
                                        expanded = showMenu,
                                        onDismissRequest = { showMenu = false },
                                        modifier = Modifier
                                            .background(colors.surface, RoundedCornerShape(14.dp))
                                            .border(1.dp, colors.border.copy(alpha = 0.5f), RoundedCornerShape(14.dp))
                                            .clip(RoundedCornerShape(14.dp))
                                    ) {
                                        // Theme Colors & Mode Preset (وظیفه ۳: تجمیع حالت روز/شب در پالت رنگ)
                                        DropdownMenuItem(
                                            text = {
                                                Text(
                                                    text = "پالت و رنگ تم (حالت روز / شب)",
                                                    fontSize = 13.sp,
                                                    color = colors.textPrimary,
                                                    fontWeight = FontWeight.Medium
                                                )
                                            },
                                            leadingIcon = {
                                                Icon(
                                                    imageVector = Icons.Default.Palette,
                                                    contentDescription = null,
                                                    tint = colors.primary
                                                )
                                            },
                                            onClick = {
                                                showMenu = false
                                                showPresetDialog = true
                                            }
                                        )

                                        HorizontalDivider(color = colors.border.copy(alpha = 0.4f), modifier = Modifier.padding(horizontal = 8.dp))

                                        // Excel Import
                                        DropdownMenuItem(
                                            text = {
                                                Text(
                                                    text = "ورود اطلاعات از فایل اکسل",
                                                    fontSize = 13.sp,
                                                    color = colors.textPrimary,
                                                    fontWeight = FontWeight.Medium
                                                )
                                            },
                                            leadingIcon = {
                                                Icon(
                                                    imageVector = Icons.Default.TableChart,
                                                    contentDescription = null,
                                                    tint = colors.gain
                                                )
                                            },
                                            onClick = {
                                                showMenu = false
                                                onOpenExcelImport()
                                            }
                                        )

                                        // Symbol Book
                                        DropdownMenuItem(
                                            text = {
                                                Text(
                                                    text = "کتابچه نمادها و ضرایب",
                                                    fontSize = 13.sp,
                                                    color = colors.textPrimary,
                                                    fontWeight = FontWeight.Medium
                                                )
                                            },
                                            leadingIcon = {
                                                Icon(
                                                    imageVector = Icons.Default.MenuBook,
                                                    contentDescription = null,
                                                    tint = Color(0xFF8B5CF6)
                                                )
                                            },
                                            onClick = {
                                                showMenu = false
                                                onOpenSymbolBook()
                                            }
                                        )

                                        HorizontalDivider(color = colors.border.copy(alpha = 0.4f), modifier = Modifier.padding(horizontal = 8.dp))

                                        // Settings
                                        DropdownMenuItem(
                                            text = {
                                                Text(
                                                    text = "تنظیمات و سفارشی‌سازی",
                                                    fontSize = 13.sp,
                                                    color = colors.textPrimary,
                                                    fontWeight = FontWeight.Medium
                                                )
                                            },
                                            leadingIcon = {
                                                Icon(
                                                    imageVector = Icons.Default.Settings,
                                                    contentDescription = null,
                                                    tint = colors.textSecondary
                                                )
                                            },
                                            onClick = {
                                                showMenu = false
                                                onOpenSettings()
                                            }
                                        )
                                    }
                                }
                            }
                        }

                        // سطر ۲ هدر اصلی: ارزش کل و مبلغ (راست) و آیکون خروج سمت چپ آیکون چشم (چپ)
                        val formattedVal = if (settings.privacyMode) {
                            "••••••••"
                        } else {
                            NumberFormatUtils.formatCurrency(
                                totalPortfolioValue,
                                settings.currencyUnit,
                                compact = false,
                                usePersianDigits = settings.usePersianDigits,
                                privacyMode = settings.privacyMode
                            )
                        }

                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.SpaceBetween
                        ) {
                            Row(
                                verticalAlignment = Alignment.CenterVertically,
                                horizontalArrangement = Arrangement.spacedBy(8.dp)
                            ) {
                                Text(
                                    text = "ارزش کل:",
                                    fontSize = if (isCompact) 13.sp else 14.5.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = colors.textSecondary
                                )
                                Text(
                                    text = formattedVal,
                                    fontSize = if (isCompact) 18.sp else 22.sp,
                                    fontWeight = FontWeight.Black,
                                    color = colors.primary
                                )
                            }

                            // سمت چپ: علامت چشم (راست) و آیکون خروج سمت چپ آیکون چشم (چپ) (وظیفه ۲)
                            Row(
                                verticalAlignment = Alignment.CenterVertically,
                                horizontalArrangement = Arrangement.spacedBy(4.dp)
                            ) {
                                // علامت چشم (مخفی‌سازی/نمایش مبالغ)
                                IconButton(
                                    onClick = {
                                        haptic.performHapticFeedback(HapticFeedbackType.TextHandleMove)
                                        onTogglePrivacy()
                                    },
                                    modifier = Modifier
                                        .size(32.dp)
                                        .testTag("btn_toggle_privacy")
                                ) {
                                    Icon(
                                        imageVector = if (settings.privacyMode) Icons.Default.VisibilityOff else Icons.Default.Visibility,
                                        contentDescription = if (settings.privacyMode) "نمایش مبالغ" else "مخفی‌سازی مبالغ",
                                        tint = colors.primary,
                                        modifier = Modifier.size(20.dp)
                                    )
                                }

                                // آیکون خروج سمت چپ آیکون چشم (وظیفه ۲)
                                IconButton(
                                    onClick = { showExitConfirmDialog = true },
                                    modifier = Modifier
                                        .size(32.dp)
                                        .testTag("btn_exit_app")
                                ) {
                                    Icon(
                                        imageVector = Icons.AutoMirrored.Filled.ExitToApp,
                                        contentDescription = "خروج از برنامه",
                                        tint = colors.loss,
                                        modifier = Modifier.size(20.dp)
                                    )
                                }
                            }
                        }
                    }
                }

            }
        }
    }

    // دیالوگ اطمینان از خروج (وظیفه ۳)
    if (showExitConfirmDialog) {
        AlertDialog(
            onDismissRequest = { showExitConfirmDialog = false },
            icon = {
                Icon(
                    imageVector = Icons.AutoMirrored.Filled.ExitToApp,
                    contentDescription = null,
                    tint = colors.loss,
                    modifier = Modifier.size(28.dp)
                )
            },
            title = {
                Text(
                    text = "اطمینان از خروج",
                    fontWeight = FontWeight.Bold,
                    fontSize = 16.sp,
                    color = colors.textPrimary
                )
            },
            text = {
                Text(
                    text = "آیا مطمئن هستید که می‌خواهید از برنامه خارج شوید؟",
                    fontSize = 13.5.sp,
                    color = colors.textSecondary
                )
            },
            confirmButton = {
                Button(
                    onClick = {
                        showExitConfirmDialog = false
                        (context as? Activity)?.finish()
                    },
                    colors = ButtonDefaults.buttonColors(containerColor = colors.loss)
                ) {
                    Text("خروج از برنامه", color = Color.White, fontWeight = FontWeight.Bold)
                }
            },
            dismissButton = {
                OutlinedButton(
                    onClick = { showExitConfirmDialog = false },
                    border = androidx.compose.foundation.BorderStroke(1.dp, colors.border)
                ) {
                    Text("انصراف", color = colors.textPrimary)
                }
            }
        )
    }

    // Theme Preset & Mode Selector Dialog (وظیفه ۳)
    if (showPresetDialog) {
        AlertDialog(
            onDismissRequest = { showPresetDialog = false },
            title = {
                Text(
                    text = "پالت رنگ و حالت روز / شب",
                    fontWeight = FontWeight.Bold,
                    fontSize = 16.sp,
                    color = colors.textPrimary
                )
            },
            text = {
                Column(
                    modifier = Modifier.fillMaxWidth(),
                    verticalArrangement = Arrangement.spacedBy(10.dp)
                ) {
                    // بخش حالت روز و شب
                    Text(
                        text = "حالت روشنایی صفحه:",
                        fontWeight = FontWeight.Bold,
                        fontSize = 12.sp,
                        color = colors.textSecondary
                    )

                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.spacedBy(8.dp)
                    ) {
                        Surface(
                            shape = RoundedCornerShape(8.dp),
                            color = if (isDark) colors.surfaceVariant else colors.primaryContainer,
                            border = androidx.compose.foundation.BorderStroke(
                                1.dp,
                                if (!isDark) colors.primary else colors.border
                            ),
                            modifier = Modifier
                                .weight(1f)
                                .clickable {
                                    if (isDark) onToggleTheme()
                                }
                        ) {
                            Row(
                                modifier = Modifier.padding(vertical = 8.dp, horizontal = 6.dp),
                                horizontalArrangement = Arrangement.Center,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Icon(
                                    imageVector = Icons.Default.LightMode,
                                    contentDescription = null,
                                    tint = if (!isDark) colors.primary else Color(0xFFFBBF24),
                                    modifier = Modifier.size(16.dp)
                                )
                                Spacer(modifier = Modifier.width(4.dp))
                                Text(
                                    text = "روز (روشن)",
                                    fontSize = 11.5.sp,
                                    fontWeight = if (!isDark) FontWeight.Bold else FontWeight.Normal,
                                    color = if (!isDark) colors.primary else colors.textPrimary
                                )
                            }
                        }

                        Surface(
                            shape = RoundedCornerShape(8.dp),
                            color = if (isDark) colors.primaryContainer else colors.surfaceVariant,
                            border = androidx.compose.foundation.BorderStroke(
                                1.dp,
                                if (isDark) colors.primary else colors.border
                            ),
                            modifier = Modifier
                                .weight(1f)
                                .clickable {
                                    if (!isDark) onToggleTheme()
                                }
                        ) {
                            Row(
                                modifier = Modifier.padding(vertical = 8.dp, horizontal = 6.dp),
                                horizontalArrangement = Arrangement.Center,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Icon(
                                    imageVector = Icons.Default.DarkMode,
                                    contentDescription = null,
                                    tint = if (isDark) colors.primary else colors.textSecondary,
                                    modifier = Modifier.size(16.dp)
                                )
                                Spacer(modifier = Modifier.width(4.dp))
                                Text(
                                    text = "شب (تاریک)",
                                    fontSize = 11.5.sp,
                                    fontWeight = if (isDark) FontWeight.Bold else FontWeight.Normal,
                                    color = if (isDark) colors.primary else colors.textPrimary
                                )
                            }
                        }
                    }

                    HorizontalDivider(color = colors.border.copy(alpha = 0.6f))

                    Text(
                        text = "انتخاب رنگ تم:",
                        fontWeight = FontWeight.Bold,
                        fontSize = 12.sp,
                        color = colors.textSecondary
                    )

                    AppThemePreset.values().forEach { preset ->
                        val isSelected = settings.themePreset == preset
                        Surface(
                            shape = RoundedCornerShape(8.dp),
                            color = if (isSelected) colors.primaryContainer else colors.surfaceVariant,
                            border = androidx.compose.foundation.BorderStroke(
                                1.dp,
                                if (isSelected) colors.primary else colors.border
                            ),
                            modifier = Modifier
                                .fillMaxWidth()
                                .clickable {
                                    onSelectThemePreset(preset)
                                    
                                }
                        ) {
                            Row(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .padding(10.dp),
                                horizontalArrangement = Arrangement.SpaceBetween,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Row(
                                    verticalAlignment = Alignment.CenterVertically,
                                    horizontalArrangement = Arrangement.spacedBy(10.dp)
                                ) {
                                    Box(
                                        modifier = Modifier
                                            .size(20.dp)
                                            .clip(RoundedCornerShape(4.dp))
                                            .background(Color(preset.primaryHex))
                                    )
                                    Text(
                                        text = preset.labelFa,
                                        fontWeight = if (isSelected) FontWeight.Bold else FontWeight.Normal,
                                        color = colors.textPrimary,
                                        fontSize = 12.5.sp
                                    )
                                }
                                if (isSelected) {
                                    Icon(
                                        imageVector = Icons.Default.Check,
                                        contentDescription = null,
                                        tint = colors.primary,
                                        modifier = Modifier.size(18.dp)
                                    )
                                }
                            }
                        }
                    }
                }
            },
            confirmButton = {
                TextButton(onClick = { showPresetDialog = false }) {
                    Text("بستن", color = colors.primary)
                }
            }
        )
    }
}

