# Transformer Encoder（Transformer 编码器）

## 题目概述

以渐进方式实现 Transformer Encoder，并在整个过程中明确记录张量形状与组件边界。

## 输入与输出

在选定正式题目描述后定义。

## 约束

在开始实现前定义。

## 算法与学习计划

下一阶段将按顺序学习和实现以下组件：

1. Q / K / V 投影
2. 缩放点积注意力（Scaled Dot-Product Attention）
3. 自注意力（Self-Attention）
4. 多头注意力（Multi-Head Attention）
5. 张量形状追踪
6. 前馈网络（Feed-Forward Network，FFN）
7. 残差连接（Residual Connection）
8. 层归一化（LayerNorm）
9. 编码器层（Encoder Layer）
10. 多层编码器（Multi-Layer Encoder）

仓库初始化阶段不包含完整的 Transformer 实现。

## 复杂度

在输入张量约定与实现范围确定后推导。

## 关键模式

- 张量形状约定
- 投影与多头形状重排
- Attention 的缩放与 Mask
- 残差连接与归一化的执行顺序
- 重复编码器层的组合

## 当前状态

- 状态：`not_started`
- 训练方向：`ai_coding`
- 下一步：定义张量约定，然后实现并测试 Q / K / V 投影
