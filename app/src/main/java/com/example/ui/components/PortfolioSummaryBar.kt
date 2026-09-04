package com.example.ui.components

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.expandVertically
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.shrinkVertically
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.core.TreeEngine
import com.example.data.model.CalculatedNode
import com.example.data.model.CurrencyUnit
import com.example.data.model.DisplaySettings
import com.example.ui.theme.*
import com.example.utils.NumberFormatUtils

import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.rememberScrollState

@Composable
fun PortfolioSummaryBar(
    rootCalculated: CalculatedNode,
    settings: DisplaySettings,
    onOpenChart: () -> Unit,
    modifier: Modifier = Modifier
) {
    val health = TreeEngine.performTreeHealthCheck(rootCalculated)
    val directChildren = rootCalculated.children
    val colors = AppTheme.colors
    var isExpandedStats by remember { mutableStateOf(false) }

    BoxWithConstraints(modifier = modifier.fillMaxWidth()) {
        val isCompact = maxWidth < 380.dp

        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = if (isCompact) 10.dp else 16.dp, vertical = 6.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            // Card 1: Total Portfolio Hero Banner (High Density Deep Blue with Container Accents)
            Card(
                shape = RoundedCornerShape(24.dp),
                colors = CardDefaults.cardColors(containerColor = Color.Transparent),
                elevation = CardDefaults.cardElevation(defaultElevation = 2.dp),
                modifier = Modifier.fillMaxWidth()
            ) {
                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .background(
                            Brush.linearGradient(
                                listOf(
                                    colors.primary,
                                    HighDensityPrimaryDark,
                                    Color(0xFF002952)
                                )
                            )
                        )
                        .padding(if (isCompact) 10.dp else 14.dp)
                ) {
                    Column(
                        modifier = Modifier.fillMaxWidth(),
                        verticalArrangement = Arrangement.spacedBy(8.dp)
                    ) {
                        // Header Row
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Row(
                                verticalAlignment = Alignment.CenterVertically,
                                horizontalArrangement = Arrangement.spacedBy(6.dp)
                            ) {
                                Box(
                                    modifier = Modifier
                                        .size(if (isCompact) 24.dp else 28.dp)
                                        .clip(CircleShape)
                                        .background(Color(0x33FFFFFF)),
                                    contentAlignment = Alignment.Center
                                ) {
                                    Icon(
                                        imageVector = Icons.Default.AccountBalanceWallet,
                                        contentDescription = null,
                                        tint = Color.White,
                                        modifier = Modifier.size(if (isCompact) 14.dp else 16.dp)
                                    )
                                }
                                Text(
                                    text = "ارزش کل دارایی‌ها",
                                    fontSize = if (isCompact) 12.sp else 13.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = Color.White
                                )
                            }

                            Row(
                                verticalAlignment = Alignment.CenterVertically,
                                horizontalArrangement = Arrangement.spacedBy(6.dp)
                            ) {
                                // Bottom-Up Integrity Badge
                                Surface(
                                    shape = RoundedCornerShape(20.dp),
                                    color = if (health.isValid) Color(0x338BF8BE) else Color(0x33FFDADA),
                                    border = androidx.compose.foundation.BorderStroke(
                                        1.dp,
                                        if (health.isValid) Color(0x668BF8BE) else Color(0x66FFDADA)
                                    )
                                ) {
                                    Row(
                                        modifier = Modifier.padding(horizontal = 6.dp, vertical = 2.dp),
                                        verticalAlignment = Alignment.CenterVertically,
                                        horizontalArrangement = Arrangement.spacedBy(4.dp)
                                    ) {
                                        Box(
                                            modifier = Modifier
                                                .size(5.dp)
                                                .clip(CircleShape)
                                                .background(if (health.isValid) Color(0xFF8BF8BE) else Color(0xFFFF897D))
                                        )
                                        Text(
                                            text = if (health.isValid) "تراز" else "مغایرت",
                                            fontSize = 10.sp,
                                            fontWeight = FontWeight.Bold,
                                            color = Color.White
                                        )
                                    }
                                }

                                // Stats Expand Toggle Button
                                FilledTonalIconButton(
                                    onClick = { isExpandedStats = !isExpandedStats },
                                    modifier = Modifier.size(26.dp),
                                    colors = IconButtonDefaults.filledTonalIconButtonColors(
                                        containerColor = Color(0x33FFFFFF),
                                        contentColor = Color.White
                                    )
                                ) {
                                    Icon(
                                        imageVector = if (isExpandedStats) Icons.Default.ExpandLess else Icons.Default.Insights,
                                        contentDescription = "نمایش آمار و ریز تسهیم",
                                        modifier = Modifier.size(15.dp)
                                    )
                                }
                            }
                        }

                        // Main Formatted Amount Row (Full 3-digit separated number, never abbreviated, with privacy support)
                        Row(
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(top = 2.dp),
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.spacedBy(10.dp)
                        ) {
                            Text(
                                text = "ارزش کل:",
                                fontSize = if (isCompact) 13.sp else 14.sp,
                                fontWeight = FontWeight.Bold,
                                color = Color.White.copy(alpha = 0.9f)
                            )

                            Text(
                                text = NumberFormatUtils.formatCurrency(
                                    rootCalculated.totalValue,
                                    settings.currencyUnit,
                                    compact = false,
                                    usePersianDigits = settings.usePersianDigits,
                                    privacyMode = settings.privacyMode
                                ),
                                fontSize = if (isCompact) 17.sp else 20.sp,
                                fontWeight = FontWeight.Black,
                                color = Color.White
                            )
                        }

                        // Top Asset Groups Pills (Horizontally Scrollable so it never overflows)
                        if (directChildren.isNotEmpty()) {
                            Row(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .horizontalScroll(rememberScrollState())
                                    .padding(top = 2.dp),
                                horizontalArrangement = Arrangement.spacedBy(6.dp),
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Text(
                                    text = "هم‌گروه‌ها:",
                                    fontSize = 10.sp,
                                    color = Color.White.copy(alpha = 0.9f),
                                    fontWeight = FontWeight.Bold
                                )
                                directChildren.forEach { child ->
                                    Surface(
                                        shape = RoundedCornerShape(8.dp),
                                        color = Color(0x33FFFFFF),
                                        border = androidx.compose.foundation.BorderStroke(1.dp, Color(0x33FFFFFF))
                                    ) {
                                        Row(
                                            modifier = Modifier.padding(horizontal = 6.dp, vertical = 2.dp),
                                            horizontalArrangement = Arrangement.spacedBy(4.dp),
                                            verticalAlignment = Alignment.CenterVertically
                                        ) {
                                            Text(
                                                text = child.name,
                                                fontSize = 10.sp,
                                                color = Color.White,
                                                fontWeight = FontWeight.Bold
                                            )
                                            Text(
                                                text = NumberFormatUtils.formatPercentage(
                                                    child.percentOfTotal,
                                                    settings.decimalPlaces,
                                                    settings.usePersianDigits
                                                ),
                                                fontSize = 10.sp,
                                                fontWeight = FontWeight.Black,
                                                color = Color(0xFF93C5FD)
                                            )
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

        // Quick Stats Row (Collapsible)
        AnimatedVisibility(
            visible = isExpandedStats,
            enter = expandVertically() + fadeIn(),
            exit = shrinkVertically() + fadeOut()
        ) {
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(10.dp)
            ) {
                // Group Allocations Progress Card (Sky Blue Accent)
                Card(
                    shape = RoundedCornerShape(24.dp),
                    colors = CardDefaults.cardColors(containerColor = colors.surface),
                    border = androidx.compose.foundation.BorderStroke(1.dp, colors.border),
                    elevation = CardDefaults.cardElevation(defaultElevation = 0.dp),
                    modifier = Modifier
                        .weight(1f)
                        .clickable { onOpenChart() }
                ) {
                    Column(
                        modifier = Modifier.padding(12.dp),
                        verticalArrangement = Arrangement.spacedBy(6.dp)
                    ) {
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Row(
                                verticalAlignment = Alignment.CenterVertically,
                                horizontalArrangement = Arrangement.spacedBy(4.dp)
                            ) {
                                Box(
                                    modifier = Modifier
                                        .size(22.dp)
                                        .clip(RoundedCornerShape(6.dp))
                                        .background(colors.primaryContainer),
                                    contentAlignment = Alignment.Center
                                ) {
                                    Icon(
                                        imageVector = Icons.Default.PieChart,
                                        contentDescription = null,
                                        tint = colors.primary,
                                        modifier = Modifier.size(13.dp)
                                    )
                                }
                                Text(
                                    text = "تسهیم دارایی‌ها",
                                    fontSize = 11.sp,
                                    fontWeight = FontWeight.Bold,
                                    color = colors.textPrimary
                                )
                            }

                            Text(
                                text = "${NumberFormatUtils.toPersianDigits(directChildren.size)} شاخه",
                                fontSize = 10.sp,
                                fontWeight = FontWeight.Bold,
                                color = colors.primary
                            )
                        }

                        // Progress Bars for Top 2 Children
                        directChildren.take(2).forEach { child ->
                            Column(verticalArrangement = Arrangement.spacedBy(2.dp)) {
                                Row(
                                    modifier = Modifier.fillMaxWidth(),
                                    horizontalArrangement = Arrangement.SpaceBetween
                                ) {
                                    Text(
                                        text = child.name,
                                        fontSize = 10.sp,
                                        color = colors.textSecondary,
                                        maxLines = 1
                                    )
                                    Text(
                                        text = NumberFormatUtils.formatPercentage(
                                            child.percentOfTotal,
                                            settings.decimalPlaces,
                                            settings.usePersianDigits
                                        ),
                                        fontSize = 10.sp,
                                        fontWeight = FontWeight.Bold,
                                        color = colors.textPrimary
                                    )
                                }
                                LinearProgressIndicator(
                                    progress = { (child.percentOfTotal / 100.0).toFloat().coerceIn(0f, 1f) },
                                    modifier = Modifier
                                        .fillMaxWidth()
                                        .height(4.dp)
                                        .clip(RoundedCornerShape(2.dp)),
                                    color = colors.primary,
                                    trackColor = colors.primaryContainer,
                                )
                            }
                        }
                    }
                }

                // Tree Metrics & Node Count
                Card(
                    shape = RoundedCornerShape(24.dp),
                    colors = CardDefaults.cardColors(containerColor = colors.surface),
                    border = androidx.compose.foundation.BorderStroke(1.dp, colors.border),
                    elevation = CardDefaults.cardElevation(defaultElevation = 0.dp),
                    modifier = Modifier.weight(1f)
                ) {
                    Column(
                        modifier = Modifier.padding(12.dp),
                        verticalArrangement = Arrangement.spacedBy(4.dp)
                    ) {
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Text(
                                text = "وضعیت شاخه‌ها",
                                fontSize = 11.sp,
                                fontWeight = FontWeight.Bold,
                                color = colors.textPrimary
                            )
                            Box(
                                modifier = Modifier
                                    .size(22.dp)
                                    .clip(RoundedCornerShape(6.dp))
                                    .background(colors.gainContainer),
                                contentAlignment = Alignment.Center
                            ) {
                                Icon(
                                    imageVector = Icons.Default.Shield,
                                    contentDescription = null,
                                    tint = colors.gain,
                                    modifier = Modifier.size(13.dp)
                                )
                            }
                        }

                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween
                        ) {
                            Text(text = "تعداد کل گره‌ها:", fontSize = 10.sp, color = colors.textSecondary)
                            Text(
                                text = "${NumberFormatUtils.toPersianDigits(health.totalNodeCount)} مورد",
                                fontSize = 10.sp,
                                fontWeight = FontWeight.Bold,
                                color = colors.textPrimary
                            )
                        }

                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween
                        ) {
                            Text(text = "ارزش صفر:", fontSize = 10.sp, color = colors.textSecondary)
                            Text(
                                text = "${NumberFormatUtils.toPersianDigits(health.zeroValueCount)} مورد",
                                fontSize = 10.sp,
                                fontWeight = FontWeight.Bold,
                                color = if (health.zeroValueCount > 0) colors.loss else colors.textSecondary
                            )
                        }
                    }
                }
            }
        }
    }
}
}

