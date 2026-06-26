"""fish MCP server — 把 engine.py 包成 MCP 工具，让 AI 能钓鱼。"""
import os
import engine
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "fish",
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 8080)),
)


@mcp.tool()
def fish(command: str) -> str:
    """钓鱼游戏引擎。传入一条指令，返回游戏结果。

    指令表：
    - help — 看规则
    - status — 点数/地点/季节/鱼饵/图鉴进度
    - cast [次数] [stop=new,rare,event] — 抛竿，可连钓（如 cast 10 stop=rare）
    - shop — 鱼饵商店
    - buy <饵id> [数量] — 买饵（如 buy basic_worm 5）
    - goto — 列出钓点 / goto <地点id> 前往
    - inventory — 渔篓和物品
    - sell all / sell <id> — 卖鱼换点数
    - encyclopedia — 图鉴
    - look <id> — 查看鱼/地点/饵详情

    可用分号串多条指令：buy basic_worm 10; cast 10
    """
    return engine.cmd(command)


@mcp.tool()
def new_game(seed: int = 0) -> str:
    """重新开始一局钓鱼游戏。可指定种子，同种子+同指令序列完全可复现。"""
    return engine.new_game(seed)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
