import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data(file_path):
    """加载数据集并返回DataFrame"""
    try:
        df = pd.read_csv(file_path)
        print(f"数据加载成功，共{len(df)}条记录")
        return df
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在")
        return None
    except Exception as e:
        print(f"错误：加载数据时发生异常 - {e}")
        return None

def data_exploration(df):
    """数据探索与基本信息展示"""
    if df is None:
        return
        
    print("\n===== 数据前5行 =====")
    print(df.head())
    
    print("\n===== 数据基本信息 =====")
    print(df.info())
    
    print("\n===== 数值列统计信息 =====")
    print(df.describe())
    
    print("\n===== 数据集列名 =====")
    print(df.columns.tolist())

def plot_profit_and_revenue(df, profit_col='利润', revenue_col='收入', company_col='公司名称', top_n=30):
    """绘制利润和收入的对比图（取前top_n家公司）"""
    if df is None:
        return
    
    # 确保数据集中包含必要的列
    required_cols = [profit_col, revenue_col, company_col]
    missing_cols = [col for col in required_cols if col not in df.columns]
    
    if missing_cols:
        print(f"错误：数据集中缺少以下列: {', '.join(missing_cols)}")
        return
    
    # 将利润和收入列转换为数值类型
    try:
        df[profit_col] = pd.to_numeric(df[profit_col], errors='coerce')
        df[revenue_col] = pd.to_numeric(df[revenue_col], errors='coerce')
    except Exception as e:
        print(f"转换列时发生错误: {e}")
        return
    
    # 按收入排序并取前top_n家公司
    top_companies = df.sort_values(by=revenue_col, ascending=False).head(top_n)
    
    # 创建画布和双Y坐标轴
    fig, ax1 = plt.subplots(figsize=(14, 7))
    ax2 = ax1.twinx()
    
    # 设置X轴位置
    x = np.arange(len(top_companies))
    width = 0.35
    
    # 绘制利润柱状图（左Y轴）
    bars1 = ax1.bar(x - width/2, top_companies[profit_col], width, 
                    label=profit_col, color='skyblue')
    ax1.set_ylabel(f'{profit_col} (单位: 亿元)', color='skyblue', fontsize=12)
    ax1.tick_params(axis='y', labelcolor='skyblue')
    
    # 绘制收入柱状图（右Y轴）
    bars2 = ax2.bar(x + width/2, top_companies[revenue_col], width, 
                    label=revenue_col, color='salmon')
    ax2.set_ylabel(f'{revenue_col} (单位: 亿元)', color='salmon', fontsize=12)
    ax2.tick_params(axis='y', labelcolor='salmon')
    
    # 设置X轴标签为公司名称（旋转45度）
    ax1.set_xticks(x)
    ax1.set_xticklabels(top_companies[company_col], rotation=45, ha='right', fontsize=9)
    
    # 添加标题和图例
    plt.title(f'财富500强前{top_n}名公司的{profit_col}与{revenue_col}对比', fontsize=14)
    
    # 合并两个图例
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper left')
    
    # 调整布局，确保标签不被遮挡
    plt.tight_layout()
    
    # 保存图形
    plt.savefig('profit_revenue_comparison.png', dpi=300, bbox_inches='tight')
    print(f"\n已生成利润与收入对比图 'profit_revenue_comparison.png'")
    
    # 显示图形
    plt.show()

def main():
    # 请替换为实际数据文件路径
    file_path = 'C:\\Users\\Administrator\\Desktop\\android实验3\\fortune500.csv'
    
    # 请根据实际列名调整
    profit_column = 'Profit (in millions)'      # 利润列名
    revenue_column = 'Revenue (in millions)'    # 收入列名
    company_column = 'Company'  # 公司名列名（根据实际数据修改）
    
    # 加载数据
    df = load_data(file_path)
    
    # 数据探索（查看列名）
    data_exploration(df)
    
    # 绘制利润和收入对比图
    plot_profit_and_revenue(df, profit_column, revenue_column, company_column, top_n=30)

if __name__ == "__main__":
    main()