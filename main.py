
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape_articles():
    data = request.get_json()
    keywords = data.get("keywords", [])

    # 假设根据关键词返回文章模拟数据
    results = []
    for kw in keywords:
        results.append({
            "keyword": kw,
            "url": f"https://www.zhichanli.com/search?q={kw}",
            "title": f"关于「{kw}」的热门文章",
            "content": f"{kw}相关的知识产权、专利、商标案例正在引发热议……"
        })

    return jsonify({"articles": results})

if __name__ == '__main__':
    app.run(debug=True)
