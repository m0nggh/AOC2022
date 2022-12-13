class File:
    def __init__(self, filename, size):
        self.filename = filename
        self.size = size


class Directory:
    def __init__(self, dirname, files, subdirs, parentdir, size):
        self.dirname = dirname
        self.files = files
        self.subdirs = subdirs
        self.parentdir = parentdir
        self.size = size

    def __str__(self):
        return "Dirname: {}, size: {}".format(self.dirname, self.size)


def form_directory(file, root, line):
    line = file.readline()
    while line != '' and line[0] != "$":
        splitted = line.split()
        if splitted[0] == "dir":
            new_dir = Directory(splitted[1], [], [], root.dirname, 0)
            root.subdirs.append(new_dir)
        else:
            new_file_size = int(splitted[0])
            new_file = File(splitted[1], new_file_size)
            root.files.append(new_file)
            root.size += new_file_size  # update directory size
        line = file.readline()
    return line


def parse_input(file, root):
    line = file.readline()
    while line != '':
        splitted = line.split()
        # 3 commands: $ ls, $ cd folder, $ cd ..
        command = splitted[1]
        if command == "ls":
            # open and form sub directories
            line = form_directory(file, root, line)
        else:
            # confirm cd
            if splitted[2] == "..":
                # go back to parent dir and update the size
                dirsize = root.size
                root = root.parentdir
                root.size += dirsize
            else:
                subdir_name = splitted[2]
                # find and go into new subdir
                for subdir in root.subdirs:
                    if subdir_name == subdir.dirname:
                        # update parentdir
                        parentdir = root
                        root = subdir
                        root.parentdir = parentdir
                        break
            line = file.readline()
    return root


def part_one(root):
    # find subdirectories with size at most 100000
    def find_subdirs(root):
        total = 0
        for sub in root.subdirs:
            if sub.size < 100000:
                total += sub.size
            total += find_subdirs(sub)
        return total
    return find_subdirs(root)


def part_two(root):
    # obtain smallest subdirectory to remove to achieve target
    unused_space = 70000000 - root.size  # total space - dir size
    target = 30000000 - unused_space  # required size - unused size
    print("target size: " + str(target))
    smallest = float("inf")

    def find_smallest_subdir(root):
        nonlocal smallest
        for sub in root.subdirs:
            if sub.size >= target:
                smallest = min(smallest, sub.size)
            find_smallest_subdir(sub)
    find_smallest_subdir(root)
    return smallest


if __name__ == "__main__":
    file = open("inputs/day7.txt", "r")
    dummy = Directory("dummy", [], [], None, 0)
    root = Directory("/", [], [], dummy, 0)
    dummy.subdirs.append(root)
    dummy = parse_input(file, dummy)
    # update size by manually performing cd ..
    while dummy.dirname != "dummy":
        size = dummy.size
        dummy = dummy.parentdir
        dummy.size += size

    print(part_one(dummy.subdirs[0]))  # enter into the main directory
    print(part_two(dummy.subdirs[0]))  # enter into the main directory
