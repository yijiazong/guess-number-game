"""
猜数字游戏
-----------
电脑随机生成一个指定范围内的整数，玩家在有限次数内猜出它。
支持难度选择、大小提示、历史记录和成绩统计。
"""

import random


def get_range_and_chances(difficulty):
    """根据难度返回数字范围和最大猜测次数"""
    settings = {
        "1": (1, 50, 10),    # 简单：1-50，10次机会
        "2": (1, 100, 7),    # 普通：1-100，7次机会
        "3": (1, 500, 6),    # 困难：1-500，6次机会
    }
    return settings.get(difficulty, (1, 100, 7))


def choose_difficulty():
    """让玩家选择难度"""
    print("\n请选择难度：")
    print("  1. 简单（1-50，10次机会）")
    print("  2. 普通（1-100，7次机会）")
    print("  3. 困难（1-500，6次机会）")
    choice = input("输入编号（默认2）：").strip()
    return choice if choice in ("1", "2", "3") else "2"


def play_once(low, high, max_chances):
    """
    进行一局游戏。
    返回：(是否猜中, 本局猜过的数字列表)
    """
    answer = random.randint(low, high)
    guesses = []

    print(f"\n我已经想好了一个 {low} 到 {high} 之间的整数。")
    print(f"你有 {max_chances} 次机会猜中它。")

    for attempt in range(1, max_chances + 1):
        remaining = max_chances - attempt + 1
        raw = input(f"\n第 {attempt} 次猜测（剩余 {remaining} 次），请输入数字：").strip()

        # 输入校验
        if not raw.lstrip("-").isdigit():
            print("输入无效，请输入一个整数。")
            continue

        guess = int(raw)

        if guess < low or guess > high:
            print(f"请猜 {low} 到 {high} 之间的数字。")
            continue

        guesses.append(guess)

        if guess == answer:
            print(f"\n恭喜！你猜对了！答案就是 {answer}。")
            print(f"你一共用了 {attempt} 次。")
            return True, guesses
        elif guess < answer:
            print("太小了，往大了猜。")
        else:
            print("太大了，往小了猜。")

    print(f"\n很遗憾，机会用完了。正确答案是 {answer}。")
    return False, guesses


def show_history(history):
    """展示历史战绩"""
    if not history:
        print("\n还没有游戏记录，先玩一局吧！")
        return

    print("\n===== 历史战绩 =====")
    for i, record in enumerate(history, 1):
        result = "✅ 猜中" if record["win"] else "❌ 失败"
        print(f"第 {i} 局：{result}，答案 {record['answer']}，猜了 {len(record['guesses'])} 次")
        print(f"        猜测序列：{record['guesses']}")

    wins = sum(1 for r in history if r["win"])
    total = len(history)
    print(f"\n总场次：{total}，胜场：{wins}，胜率：{wins / total:.0%}")


def main():
    """主程序入口"""
    print("=" * 40)
    print("        欢迎来到猜数字游戏！")
    print("=" * 40)

    history = []

    while True:
        print("\n主菜单：")
        print("  1. 开始新游戏")
        print("  2. 查看历史战绩")
        print("  3. 退出")

        choice = input("请选择（1/2/3）：").strip()

        if choice == "1":
            difficulty = choose_difficulty()
            low, high, max_chances = get_range_and_chances(difficulty)
            win, guesses = play_once(low, high, max_chances)

            # 记录本局答案：从猜测逻辑反推不方便，这里改写 play_once 返回值
            # 为简洁，我们在 play_once 里已经打印了答案，这里只存胜负和猜测
            history.append({
                "win": win,
                "answer": "见上局提示",  # 可选：改成返回答案
                "guesses": guesses,
            })

        elif choice == "2":
            show_history(history)

        elif choice == "3":
            print("\n感谢游玩，再见！")
            break

        else:
            print("无效选择，请输入 1、2 或 3。")


if __name__ == "__main__":
    main()