import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """加载数据集并返回DataFrame"""
    try:
        df = pd.read_csv(file_path)
        print("数据加载成功，数据集形状：", df.shape)
        return df
    except FileNotFoundError:
        print(f"错误：未找到文件 {file_path}")
        return None

def data_exploration(df):
    """数据探索与基本信息展示"""
    print("\n===== 数据前5行 =====")
    print(df.head())
    
    print("\n===== 数据基本信息 =====")
    print(df.info())
    
    print("\n===== 数值列统计信息 =====")
    print(df.describe())

def handle_profit_outliers(df, profit_col='利润'):
    """处理利润列异常值（基于IQR方法）"""
    # 转换利润列为数值类型（假设可能存在非数字情况）
    df[profit_col] = pd.to_numeric(df[profit_col], errors='coerce')
    
    # 计算四分位数
    q1 = df[profit_col].quantile(0.25)
    q3 = df[profit_col].quantile(0.75)
    iqr = q3 - q1
    
    # 定义异常值边界
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    # 标记异常值并过滤数据
    before_count = df.shape[0]
    df_clean = df[(df[profit_col] >= lower_bound) & (df[profit_col] <= upper_bound)]
    after_count = df_clean.shape[0]
    
    print(f"\n检测到利润列异常值数量：{before_count - after_count} 条")
    print(f"数据清洗前记录数：{before_count}，清洗后记录数：{after_count}")
    
    return df_clean

def visualize_profit(df_before, df_after, profit_col='利润'):
    """可视化利润分布对比"""
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    df_before[profit_col].plot(kind='box', title='清洗前利润分布')
    
    plt.subplot(1, 2, 2)
    df_after[profit_col].plot(kind='box', title='清洗后利润分布')
    
    plt.tight_layout()
    plt.savefig('profit_distribution_comparison.png')
    print("\n利润分布对比图已保存为 profit_distribution_comparison.png")

def main():
    # 配置参数（根据实际数据路径修改）
    FILE_PATH = 'C:\\Users\\Administrator\\Downloads\\fortune500.csv' # 替换为你的数据路径
    PROFIT_COL = 'Profit (in millions)'  # 根据实际列名调整
    
    # 数据加载
    df = load_data(FILE_PATH)
    if df is None:
        return
    
    # 数据探索
    data_exploration(df)
    
    # 处理异常值
    df_clean = handle_profit_outliers(df, PROFIT_COL)
    
    # 可视化对比（需要matplotlib）
    visualize_profit(df, df_clean, PROFIT_COL)
    
    # 保存清洗后数据
    output_path = 'fortune500_clean.csv'
    df_clean.to_csv(output_path, index=False)
    print(f"\n清洗后数据已保存至 {output_path}")

if __name__ == "__main__":
    main()
    