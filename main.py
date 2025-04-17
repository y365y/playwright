import os
from playwright.sync_api import sync_playwright

def handle_page(page):
    # 从环境变量中获取Cookie信息
    cookie_value = os.getenv('ck')
    url = os.getenv('url')    
    if not cookie_value:
        raise ValueError("环境变量 'ck' 未设置，请确保已正确配置。")

    # 定义Cookie
    cookie = {
        'name': 'm_session_id',  # 替换为实际的Cookie名
        'value': cookie_value,       # 使用环境变量中的值
        'domain': '.modelscope.cn',  # 确保域名正确
        'path': '/',
    }

    # 导航到目标页面前添加Cookie
    page.context.add_cookies([cookie])
    
    # 访问目标网页
    page.goto(url)
    print(f"网页标题: {page.title()}")
    
    # 抓取类名为.chinese_name_title的文字内容
    elements = page.query_selector_all('.acss-zddqpb, .chinese_name_title')
    for element in elements:
        print(element.text_content())

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # 若不需要GUI界面，可将headless设置为True
        page = browser.new_page()
        try:
            handle_page(page)
        finally:
            browser.close()

if __name__ == '__main__':
    main()
