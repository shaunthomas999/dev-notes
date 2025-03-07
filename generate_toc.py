import os

repo_url = 'https://github.com/shaunthomas999/dev-notes/blob/main'

def generate_toc(root_dir):
    toc_lines = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Filter out hidden directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        # Calculate the depth of the current directory
        depth = dirpath[len(root_dir):].count(os.sep)
        indent = '  ' * depth
        if depth == 0:
            toc_lines.append(f'# {os.path.basename(os.path.abspath(dirpath))}\n')
        else:
            toc_lines.append(f'{indent}- {os.path.basename(dirpath)}\n')
        subindent = '  ' * (depth + 1)
        for filename in sorted(filenames):
            if filename.endswith('.md'):
                filepath = os.path.join(dirpath, filename).replace('\\', '/')
                file_url = f'{filepath}'
                toc_lines.append(f'{subindent}- [{filename}](<{file_url}>)\n')
    return toc_lines

if __name__ == '__main__':
    toc = generate_toc('.')
    with open('TOC.md', 'w') as f:
        f.writelines(toc)
