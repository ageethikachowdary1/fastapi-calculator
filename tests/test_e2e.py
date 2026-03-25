def test_calculator_e2e(page):
    page.goto("http://127.0.0.1:8000/")

    page.fill('input[name="a"]', "12")
    page.fill('input[name="b"]', "3")
    page.select_option('select[name="operation"]', "divide")
    page.click('button[type="submit"]')

    page.wait_for_selector("h2")
    content = page.locator("h2").text_content()
    assert "Result: 4" in content
