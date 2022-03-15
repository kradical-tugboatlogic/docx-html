import os

from pydocx import PyDocX

input_path = os.path.join('..', 'in.docx')
output_path = 'out.html'

def main():
    html = PyDocX.to_html(input_path)

    with open(output_path, 'w') as f:
        f.write(html)


if __name__ == '__main__':
    main()