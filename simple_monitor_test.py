"""
Weave Monitor 簡単なテストスクリプト
Simple test script for Weave Monitor feature

このスクリプトは、Weave Monitorが正しく動作するかをテストします。
This script tests if Weave Monitor is working correctly.

使い方 / Usage:
1. Weave UIでこの関数のMonitorを作成してください
   Create a Monitor for this function in Weave UI
   
2. Monitorの設定 / Monitor Configuration:
   - Operations: generate_summary
   - Scoring prompt で使用できる変数 / Available variables in scoring prompt:
     {text}     - 入力テキスト / Input text
     {文字数}   - 指定された文字数 / Target character count
     {output}   - 生成された要約 / Generated summary
   
3. このスクリプトを実行 / Run this script:
   python simple_monitor_test.py
   
4. Weave UIで結果を確認 / Check results in Weave UI:
   - Traces ページで呼び出しを確認
   - Monitors ページで評価結果を確認
"""

import weave

# Weave プロジェクトの初期化 / Initialize Weave project
# 注意: "your-entity/your-project" を実際のプロジェクト名に変更してください
# Note: Change "your-entity/your-project" to your actual project name
weave.init("wandb/monitor-test-simple")


@weave.op()
def generate_summary(text: str, 文字数: int = 100) -> str:
    """
    テキストの簡単な要約を生成する関数
    Simple function that generates a summary of the given text
    
    Parameters:
    -----------
    text : str
        要約したいテキスト / Text to summarize
    文字数 : int
        指定された文字数 / Target character count (default: 100)
        
    Returns:
    --------
    str
        生成された要約 / Generated summary
    """
    # 実際のアプリケーションでは、ここでLLMを呼び出します
    # In a real application, you would call an LLM here
    
    # テストのため、簡単な要約を返します
    # For testing, return a simple summary
    word_count = len(text.split())
    return f"この文章は{word_count}語で構成されています。{文字数}文字での要約：{text[:50]}..."


def main():
    print("=" * 60)
    print("Weave Monitor テスト / Weave Monitor Test")
    print("=" * 60)
    
    # テストケース / Test cases
    test_texts = [
        "人工知能は現代社会において重要な役割を果たしています。機械学習やディープラーニングの発展により、様々な分野で革新が起きています。",
        "気候変動は地球規模の課題です。持続可能な社会を実現するために、再生可能エネルギーへの移行が必要です。",
        "健康的な生活を送るためには、バランスの取れた食事と適度な運動が重要です。十分な睡眠も欠かせません。"
    ]
    
    print("\n実行中... / Running...")
    print("-" * 60)
    
    for i, text in enumerate(test_texts, 1):
        print(f"\nテスト {i} / Test {i}:")
        print(f"入力 / Input: {text[:50]}...")
        
        # 関数を呼び出す / Call the function
        # 文字数を指定して呼び出し（100, 200, 300と変えてみる）
        char_count = i * 100
        summary = generate_summary(text, 文字数=char_count)
        
        print(f"出力 / Output: {summary}")
    
    print("\n" + "=" * 60)
    print("✅ 完了！ / Completed!")
    print("=" * 60)
    print("\n次のステップ / Next steps:")
    print("1. Weave UIのTracesページを開いてください")
    print("   Open the Traces page in Weave UI")
    print("2. 'generate_summary'の呼び出しを確認してください")
    print("   Check the 'generate_summary' calls")
    print("3. MonitorページでCalls数が増えているか確認してください")
    print("   Check if the Calls count increased in Monitors page")
    print("4. 評価スコアを確認してください")
    print("   Check the evaluation scores")
    print("\nWeave UI: https://wandb.ai/wandb/monitor-test-simple/weave")


if __name__ == "__main__":
    main()


