import os

import mammoth

input_path = os.path.join('..', 'in.docx')
output_path = 'out.html'

def main():
    with open(input_path, 'rb') as f:
        result = mammoth.convert_to_html(f)

    html = result.value

    with open(output_path, 'w') as f:
        f.write(html)


if __name__ == '__main__':
    main()