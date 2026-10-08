import os
import re

dir_path = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-form-dang-ky-nguoi-dung"

for html_file in ['register_basic.html', 'index.html']:
    with open(os.path.join(dir_path, html_file), 'r', encoding='utf-8') as f:
        content = f.read()
    assert 'method="POST"' in content, f'{html_file} missing method="POST"'
    assert 'http://demo.codegym.vn/6/registration_form/register.php' in content, f'{html_file} missing action URL'
    assert re.search(r'name=["\']name["\']', content), f'{html_file} missing name="name"'
    assert re.search(r'name=["\']email["\']', content), f'{html_file} missing name="email"'
    assert re.search(r'name=["\']phone["\']', content), f'{html_file} missing name="phone"'
    assert re.search(r'name=["\']gender["\']', content), f'{html_file} missing name="gender"'
    print(f"PASS: {html_file} satisfies all HTML form criteria.")

pdf_path = os.path.join(dir_path, "Bao_Cao_Bai_Tap_Form_Dang_Ky_Nguoi_Dung.pdf")
pdf_size = os.path.getsize(pdf_path)
assert pdf_size <= 2 * 1024 * 1024, f"PDF size {pdf_size} exceeds 2 MB"
print(f"PASS: PDF size {pdf_size} bytes ({pdf_size/1024:.1f} KB) is under 2 MB.")
print("\nALL VERIFICATIONS PASSED!")
