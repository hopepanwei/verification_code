import os
import uuid
import random
import json
import base64
import string


train_dir = "/Users/dashuai/Desktop/program/spider_project/jiyan/train_file/nine"
names = json.loads(open('/Users/dashuai/Documents/git_huaiyukeji/verification_code/nine/data/labels2.json', 'r').read()).keys()

def get_labels_file():
    labels = json.loads(open('/Users/dashuai/Documents/git_huaiyukeji/verification_code/nine/data/labels2.json', 'r').read())
    for v in labels.keys():
        with open("/Users/dashuai/Documents/git_huaiyukeji/verification_code/nine/data/nine.labels", 'a+') as f:
            f.write(str(v) + "\n")
    f.close()


def ranstr(num):
    salt = ''.join(random.sample(string.ascii_letters, num))
    return salt


def parse_labels():
    labels = names
    labels_json = {}
    for index, label in enumerate(labels):
        labels_json[label] = index
    with open('/Users/dashuai/Documents/git_huaiyukeji/verification_code/nine/data/labels2.json', 'a+') as f:
        f.write(json.dumps(labels_json, ensure_ascii=False, indent=4))
        f.close()


def parse_file():
    files = os.listdir(train_dir)
    print(f"total files {len(files)}")
    for i in files:
        file_name = i.split("_")[0]
        if not file_name in names:
            os.remove(os.path.join(train_dir, i))
        if not "_" in i:
            os.remove(os.path.join(train_dir, i))


def file_rename7():
    count = 0
    for file in os.listdir(train_dir):
        file_name = file.split("_")[0]
        file_path = os.path.join(train_dir, file)
        if '锅' == file_name:
            new_name = file.replace('锅', '饭锅')
            os.rename(file_path, os.path.join(train_dir, new_name))
            print(f"{count}-{file}-{new_name}")
            count += 1


def file_rename6():
    count = 0
    for file in os.listdir(train_dir):
        file_path = os.path.join(train_dir, file)
        flag = file.split("-")[-1].split("_")[0]
        new_name = ranstr(32) + f"_{flag}.jpg"
        os.rename(file_path, os.path.join(train_dir, new_name))
        print(f"{count}-{file}-{new_name}")
        count += 1



def file_rename5():
    count = 0
    labels = json.loads(open('/Users/dashuai/Documents/git_huaiyukeji/verification_code/nine/data/labels2.json', 'r').read())
    for file in os.listdir(train_dir):
        file_path = os.path.join(train_dir, file)
        flag = file.split("_")[-1].split(".")[0]
        new_name = ranstr(32) + f"-{flag}_{labels[flag]}.jpg"
        os.rename(file_path, os.path.join(train_dir, new_name))
        print(f"{count}-{file}-{new_name}")
        count += 1


def file_rename4():
    count = 0
    for file in os.listdir(train_dir):
        if "_" in file:
            file_path = os.path.join(train_dir, file)
            new_name = str(int(random.random()*10000000000000000)) + "_" + file.split("_")[1]
            os.rename(file_path, os.path.join(train_dir, new_name))
            print(f"{count}-{file}-{new_name}")
            count += 1
        else:
            delpath = os.path.join(train_dir, file)
            os.remove(delpath)
            print(f"remove {delpath}")


def file_rename3():
    count = 0
    for file in os.listdir(train_dir):
        file_path = os.path.join(train_dir, file)
        new_name = str(int(random.random()*10000000000000000)) + "_" + file.split("_")[1]
        os.rename(file_path, os.path.join(train_dir, new_name))
        print(f"{count}-{file}-{new_name}")
        count += 1


def file_rename2():
    count = 0
    for file in os.listdir(train_dir):
        file_path = os.path.join(train_dir, file)
        new_name = file.replace("\\u", "")
        os.rename(file_path, os.path.join(train_dir, new_name))
        print(f"{count}-{file}-{new_name}")
        count += 1


def file_rename():
    count = 0
    for file in os.listdir(train_dir):
        file_path = os.path.join(train_dir, file)
        flag = file.split("_")[0]
        flag_unicode = flag.encode('unicode_escape').decode()
        new_name = uuid.uuid1().hex + flag + f"_{flag_unicode}.jpg"
        os.rename(file_path, os.path.join(train_dir, new_name))
        print(f"{count}-{file}-{new_name}")
        count += 1


if __name__ == '__main__':
    file_rename6()