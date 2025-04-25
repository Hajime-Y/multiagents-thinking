from typing import Any, List, Dict
import os
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import logging
import datetime

from create_agent import create_agent

# 環境変数を読み込む
load_dotenv()

# ロギングの設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("multiagent.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("multiagent")

# Initialize FastMCP server
mcp = FastMCP("multiagent")

# 環境変数の確認
if not os.environ.get("OPENAI_API_KEY"):
    logger.error("警告: OPENAI_API_KEY環境変数が設定されていません。")
elif not os.environ.get("HF_TOKEN"):
    logger.error("警告: HF_TOKEN環境変数が設定されていません。")

# ブラウザを操作するAgent
agent = create_agent(model_id="gpt-4.1")

@mcp.tool()
async def multiagent_thinking(task_description: str) -> str:
    """
    このツールは、複数の視点や分岐、条件を同時に検討する必要がある複雑なタスクを解決するために設計されています。
    内部的には複数のスペシャリストエージェントを並列に実行し、それぞれ異なる視点やアプローチで問題に取り組みます。
    
    最適な使用シーン:
    - 複数の観点からの分析が必要な複雑な意思決定
    - 多様な解決策のブレインストーミングと評価
    - 異なるカテゴリやレベルで対応策を検討する必要がある問題
    - 複数の条件分岐や「もし〜なら」シナリオの検討
    - 創造的な問題解決で多角的なアプローチが求められる場合
    
    このツールは以下の手法を組み合わせます:
    1. 問題の分解と制約の特定
    2. 複数の視点・方法論の並列探索
    3. タスク分担型または視点分担型の協調作業
    4. 結果の批判的評価と統合
    
    注意事項:
    - タスクの説明は明確かつ詳細であるほど良い結果が得られます
    - 特定の数の解決策やアイデアが必要な場合は、明示的に指定してください
    - 複雑すぎるタスクは複数のサブタスクに分割することを検討してください
    
    Args:
        task_description: 解決すべき問題やタスクの詳細な説明。制約条件や期待される成果物の形式も含めてください。
        
    Returns:
        複数の視点を統合した分析と解決策の提案。タスク要件に応じた形式で結果を返します。
    """
    # タスク詳細を記録
    logger.info(f"タスク詳細: {task_description}")
    
    try:
        # Open Deep Researchのエージェントによる調査の実行
        result = agent.run(task_description)
        
        # ログに回答を記録
        logger.info(f"タスク実行完了: {task_description}")
        
        return result
    
    except Exception as e:
        error_message = f"エラーが発生しました: {str(e)}"
        logger.error(error_message)
        return error_message

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
