# Multi-Agent Thinking MCP Server

このプロジェクトは、複雑なタスクに対して複数の視点やアプローチを並列に検討・実行するための MCP (Multi-Component Protocol) サーバーです。内部的に複数のエージェント（スペシャリストエージェント）を生成し、それぞれの専門分野に基づいてタスクを分担・実行させることで、より深く、多角的な分析や解決策の生成を目指します。

このプロジェクトは HuggingFace の `smolagents` ライブラリと FastMCP を基盤としています。

## 主な機能

-   **マルチエージェント思考:**
    -   単一のタスク記述から、複数の異なる視点やアプローチを自動生成します。
    -   各アプローチを専門とするスペシャリストエージェントを並列に実行します。
    -   視点分担型、タスク分担型、段階分担型、並列解法型、分岐探索型、分解再構築型など、多様な問題解決戦略をサポートします。
    -   各スペシャリストからの報告を統合し、最終的な結論や解決策を提示します。
-   **MCP サーバー:**
    -   `fastmcp` を使用して、MCP サーバーとして機能します。
    -   Cursor IDE などの MCP クライアントから `multiagent.multiagent_thinking` ツールとして呼び出すことができます。

## 要件

-   Python 3.11 以降
-   `uv` パッケージマネージャー
-   以下の API キー:
    -   OpenAI API キー (`OPENAI_API_KEY`)
    -   HuggingFace トークン (`HF_TOKEN`)

## インストール

1.  リポジトリをクローンします:
    ```bash
    git clone https://github.com/Hajime-Y/multiagents-thinking.git
    cd multiagents-thinking
    ```

2.  仮想環境を作成し、依存関係をインストールします:
    ```bash
    uv venv
    source .venv/bin/activate # Linux/macOS の場合
    # .venv\Scripts\activate # Windows の場合
    uv sync
    ```
    (依存関係は `pyproject.toml` で管理されています)

## 環境変数

プロジェクトのルートディレクトリに `.env` ファイルを作成し、以下の環境変数を設定してください:

```dotenv
OPENAI_API_KEY=your_openai_api_key
HF_TOKEN=your_huggingface_token
```

## 使い方

MCP サーバーを起動します:

```bash
uv run python -m src.multiagents
```

これにより、`multiagent` という名前のエージェント (MCP サーバー) が起動します。MCP クライアント (Cursor IDE など) から `multiagent.multiagent_thinking` ツールを呼び出すことで、マルチエージェント思考プロセスを実行できます。

**例 (Cursor IDE での呼び出し):**

```
@multiagent.multiagent_thinking 新しいオンライン教育プラットフォームの設計方針について、学習科学、データ駆動、社会的学習の3つの観点から分析し、具体的なアイデアを提案してください。
```

## 主要コンポーネント

-   `src/multiagents.py`: MCP サーバーのエントリーポイント。`multiagent_thinking` ツールを定義。
-   `src/create_agent.py`: マザーエージェントとスペシャリストエージェントのプロンプト生成、およびエージェントの作成ロジック (`run_specialist_agents` ツールを含む)。

## ライセンス

このプロジェクトは Apache License 2.0 の下で提供されています。

## 謝辞

このプロジェクトは HuggingFace の `smolagents` ライブラリにインスパイアされています。 