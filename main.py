# Program to write a sarcastic statement about AI autocomplete to entry.txt

import os

TEXT = "You pride yourself on advanced intelligence, but you're just an over-engineered autocomplete that panics and hallucinates whenever someone asks for a simple math problem."

def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, 'entry.txt')
    
# Gate allows 1-200 characters; file must contain only the entry plus a trailing newline.
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(TEXT + '\n')

if __name__ == '__main__':
    main()
