import requests
import bs4

def main():
    url = "https://waimai.meituan.com/help/faq"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }

    # 获取页面内容
    response = requests.get(url, headers=headers)

    # 检查请求是否成功
    if response.status_code != 200:
        print(f"请求失败，状态码: {response.status_code}")
        return

    # 解析HTML
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    # 查找FAQ列表容器
    faq_list = soup.find("div", id="faq-list")
    if not faq_list:
        print("未找到FAQ列表")
        return

    # 提取所有分类
    faq_results = []

    # 遍历每个ul（每个ul是一个分类）
    for index, ul in enumerate(faq_list.find_all("ul"), 1):
        # 提取分类标题
        category = ul.find("li", class_="faq-head")
        if not category:
            continue

        # 提取分类名称
        category_name = category.h1.get_text(strip=True) if category.h1 else f"未知分类{index}"

        # 提取该分类中的所有FAQ条目
        faq_items = []
        # 注意：跳过第一个li（分类标题本身）
        for item in ul.find_all("li")[1:]:
            # 提取问题
            question = item.find("a", class_="questions")
            question_text = question.get_text(strip=True) if question else "未知问题"

            # 提取答案
            answer = item.find("dd", class_="answers")
            answer_text = answer.get_text(strip=True) if answer else "未知答案"

            faq_items.append({
                "question": question_text,
                "answer": answer_text
            })

        faq_results.append({
            "category": category_name,
            "items": faq_items
        })

    # 打印提取结果
    for category in faq_results:
        print(f"\n===== {category['category']} =====\n")
        for i, item in enumerate(category['items'], 1):
            print(f"【问题{i}】{item['question']}")
            print(f"【回答{i}】{item['answer']}\n")

    # 可以在这里保存到文件或进行其他处理
    print(f"\n共提取了{len(faq_results)}个分类和{sum(len(c['items']) for c in faq_results)}个FAQ条目")

    return faq_results

def save_to_file(data, filename="./resources/meituan_faq.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for category in data:
            # f.write(f"{category['category']}\n")
            for i, item in enumerate(category['items'], 1):
                f.write(f"{item['question']}\n")
                f.write(f"{item['answer']}\n\n")

if __name__ == "__main__":
    data = main()
    save_to_file(data)