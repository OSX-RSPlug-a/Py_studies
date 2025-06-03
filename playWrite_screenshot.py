from playwright.sync_api import sync_playwright

def take_screenshoot(url):
    
    with sync_playwright() as playwright:
        
        webkit = playwright.webkit
        browser = webkit.launch()
        browser_context = browser.new_context()
        
        page = browser_context.new_page()
        page.goto(url)
        
        element = page.locator("body")
        
        screenshot_bytes = element.screenshot()
        
        browser.close()
        with open ("screenshot.png", mode="wb") as img:
            img.write(screenshot_bytes)
        
        
if __name__ == "__main__":
    take_screenshoot("https:theverge.com")
    print("Screenshot taken and saved as screenshot.png")