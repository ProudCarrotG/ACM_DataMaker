import os


def walk_path(path: str) -> []:
    res = []
    for root, dirs, files in os.walk(path):
        for file in files:
            res.append(os.path.abspath(os.path.join(root, file)))

    return res

if __name__ == '__main__':
    tmp = walk_path('..\\std')
    print(tmp)